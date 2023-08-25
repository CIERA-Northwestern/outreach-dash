'''Main dashboard class.
'''
import importlib
import os
import types
import yaml

import pandas as pd
import streamlit as st

from . import user_utils as default_user_utils
from . import settings, interface, data_handler, aggregator, data_viewer

# We need to reload all the individual pieces if we want changes in them to propagate
for module in [ settings, interface, data_handler, aggregator, data_viewer ]:
    importlib.reload(module)

class DashBuilder:
    '''Main class for constructing dashboards.

    Args:
        config_fp: Path to the config file.
        user_utils: User-customized module for data loading
            and preprocessing.
    '''

    def __init__(
        self,
        config_fp: str,
        user_utils: types.ModuleType = None,
    ):

        if user_utils is None:
            user_utils = default_user_utils

        self.config = self.load_config(config_fp)
        self.settings = settings.Settings(self.config)
        self.interface = interface.Interface(self.config, self.settings)
        self.data_handler = data_handler.DataHandler(self.config, user_utils)
        self.agg = aggregator.Aggregator(self.config)
        self.data_viewer = data_viewer.DataViewer(self.config, self.settings, self.data_handler)

    @property
    def data(self):
        '''Convenience property for accessing the dataframes.

        Returns:
            data (dict): The dataframes.
        '''
        return self.data_handler.data

    def load_config(self, config_fp: str) -> dict:
        '''Get the config. This is done once per session.
        The config directory is set as the working directory.

        Args:
            config_fp: Filepath for the config file.

        Returns:
            config: The config dictionary.
        '''

        config_dir, config_fn = os.path.split(config_fp)

        # Check if we're in the directory the script is in,
        # which should also be the directory the config is in.
        # If not, move into that directory
        if os.getcwd() != config_dir:
            os.chdir(config_dir)

        with open(config_fn, "r", encoding='UTF-8') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        return config

    @st.cache_resource
    def prep_data(_self, config: dict) -> pd.DataFrame:
        '''Load, clean, and preprocess the data.

        This is the one time that the config can be altered during execution,
        chosen as such to allow the user to modify the config on the fly,
        as these two functions are user defined.

        For this and other functions wrapped by a streamlit caching function,
        "self" must be replaced be preceeded by "_" to avoid streamlit
        trying to cache self.

        Args:
            config: The config dict.

        Returns:
            preprocessed_df: The preprocessed data.
            config: The config file. This will also be stored at self.config
        
        Side Effects:
            self.data_handler.data: Updates data stored.
            self.config: Possible updates to the stored config file.
        '''

        print('Doing data prep...')

        raw_df, _self.config = _self.data_handler.load_data(config)
        cleaned_df, _self.config = _self.data_handler.clean_data(raw_df, _self.config)
        preprocessed_df, _self.config = _self.data_handler.preprocess_data(cleaned_df, _self.config)

        return _self.data_handler
 
    @st.cache_data
    def recategorize_data(
            _self,
            preprocessed_df: pd.DataFrame,
            new_categories: dict = None,
            recategorize: bool = True,
            combine_single_categories: bool = False,
        ) -> pd.DataFrame:
        '''Recategorize the data, i.e. combine existing categories into new ones.
        The end result is one category per article, so no articles are double-counted.
        However, if the new categories are ill-defined they can contradict one another
        and lead to inconsistencies.

        This is a wrapper for the same function in the data handler.
        Part of the motivation for being a wrapper is to limit data caching to the builder.

        Args:
            preprocessed_df: The dataframe containing the original data.
            new_categories: The new categories to use.
            recategorize: Whether to recategorize the data. Included for caching.
            combine_single_categories: If True, instead of leaving
                undefined singly-tagged entries alone,
                group them all into an "Other" category.

        Returns:
            recategorized: The dataframe containing the recategorized data.
                One entry per article.
        '''

        print( 'Recategorizing data...' )

        return _self.data_handler.recategorize_data(
            preprocessed_df=preprocessed_df,
            new_categories=new_categories,
            recategorize=recategorize,
            combine_single_categories=combine_single_categories,
        )
