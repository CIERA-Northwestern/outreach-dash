import csv
from datetime import date
from datetime import datetime
import os

# helper function to either update value of person's attendance in a dicitonary or adds that person
def update_or_add(dictionary, key):
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1


def update_or_add_events(dictionary, key, val):
    if key in dictionary:
        dictionary[key] += val
    else:
        dictionary[key] = val


# Initial values for beginning and end dates
beginning_date = "5/1"
end_date = "4/30"

def set_dates(new_beginning_date, new_end_date):
    global beginning_date, end_date
    beginning_date = new_beginning_date
    end_date = new_end_date


#print(end_date, beginning_date)

# this is for fy25 data
# list of people who attended events
grads_lis_25 = []
postd_lis_25 = []
fac_lis_25 = []
staf_lis_25 = []

# this is for fy24 data
# list of people who attended events
grads_lis_24 = []
postd_lis_24 = []
fac_lis_24 = []
staf_lis_24 = []

# this is for fy23 data
# list of people who attended events
grads_lis_23 = []
postd_lis_23 = []
fac_lis_23 = []
staf_lis_23 = []


# this is for fy22 data
# list of people who attended events
grads_lis_22 = []
postd_lis_22 = []
fac_lis_22 = []
staf_lis_22 = []


# this is for fy21 data
# list of people who attended events
grads_lis_21 = []
postd_lis_21 = []
fac_lis_21= []
staf_lis_21 = []


# this is for fy20 data
# list of people who attended events
grads_lis_20 = []
postd_lis_20 = []
fac_lis_20 = []
staf_lis_20 = []

# this is for fy19 data
# list of people who attended events
grads_lis_19 = []
postd_lis_19 = []
fac_lis_19 = []
staf_lis_19 = []

# this is for fy18 data
# list of people who attended events
grads_lis_18 = []
postd_lis_18 = []
fac_lis_18 = []
staf_lis_18 = []

# this is for fy17 data
# list of people who attended events
grads_lis_17 = []
postd_lis_17 = []
fac_lis_17 = []
staf_lis_17 = []

# this is for fy16 data
# list of people who attended events
grads_lis_16 = []
postd_lis_16 = []
fac_lis_16 = []
staf_lis_16 = []


# attendees year over year
attendees_16 = 0
attendees_17 = 0
attendees_18 = 0
attendees_19 = 0
attendees_20 = 0
attendees_21 = 0
attendees_22 = 0
attendees_23 = 0
attendees_24 = 0
attendees_25 = 0


# this is for audience types
audience_16 = []
audience_17 = []
audience_18 = []
audience_19 = []
audience_20 = []
audience_21 = []
audience_22 = []
audience_23 = []
audience_24 = []
audience_25 = []


# this is for event types
event_16 = []
event_17 = []
event_18 = []
event_19 = []
event_20 = []
event_21 = []
event_22 = []
event_23 = []
event_24 = []
event_25 = []


# event type and audience attendance

event_audience_pop_25 = {}
event_audience_pop_24 = {}
event_audience_pop_23 = {}
event_audience_pop_22 = {}
event_audience_pop_21 = {}
event_audience_pop_20 = {}
event_audience_pop_19 = {}
event_audience_pop_18 = {}
event_audience_pop_17 = {}
event_audience_pop_16 = {}

# event type and audience attendance

type_audience_pop_25 = {}
type_audience_pop_24 = {}
type_audience_pop_23 = {}
type_audience_pop_22 = {}
type_audience_pop_21 = {}
type_audience_pop_20 = {}
type_audience_pop_19 = {}
type_audience_pop_18 = {}
type_audience_pop_17 = {}
type_audience_pop_16 = {}

csv_file_path = os.path.join(os.path.dirname(__file__), 'data.csv')


with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:

        date = line[4]

        try:
            date_cell = datetime.strptime(date, "%m/%d/%Y")
        except:
            date_cell = datetime.strptime(date, '%d %b %Y')



        # start and end for fy25
        start_25 = datetime.strptime(beginning_date+"/2025", "%m/%d/%Y")
        end_25 = datetime.strptime(end_date+"/2026", "%m/%d/%Y")

        # start and end for fy24
        start_24 = datetime.strptime(beginning_date+"/2024", "%m/%d/%Y")
        end_24 = datetime.strptime(end_date+"/2025", "%m/%d/%Y")

        # start and end for fy23
        start_23 = datetime.strptime(beginning_date+"/2023", "%m/%d/%Y")
        end_23 = datetime.strptime(end_date+"/2024", "%m/%d/%Y")

        # start and end for fy22
        start_22 = datetime.strptime(beginning_date+"/2022", "%m/%d/%Y")
        end_22 = datetime.strptime(end_date+"/2023", "%m/%d/%Y")

        # start and end for fy21
        start_21 = datetime.strptime(beginning_date+"/2021", "%m/%d/%Y")
        end_21 = datetime.strptime(end_date+"/2022", "%m/%d/%Y")

        # start and end for fy20
        start_20 = datetime.strptime(beginning_date+"/2020", "%m/%d/%Y")
        end_20 = datetime.strptime(end_date+"/2021", "%m/%d/%Y")

        # start and end for fy19
        start_19 = datetime.strptime(beginning_date+"/2019", "%m/%d/%Y")
        end_19 = datetime.strptime(end_date+"/2020", "%m/%d/%Y")

        # start and end for fy18
        start_18 = datetime.strptime(beginning_date+"/2018", "%m/%d/%Y")
        end_18 = datetime.strptime(end_date+"/2019", "%m/%d/%Y")

        # start and end for fy17
        start_17 = datetime.strptime(beginning_date+"/2017", "%m/%d/%Y")
        end_17 = datetime.strptime(end_date+"/2018", "%m/%d/%Y")
        
        # start and end for fy16
        start_16 = datetime.strptime(beginning_date+"/2016", "%m/%d/%Y")
        end_16 = datetime.strptime(end_date+"/2017", "%m/%d/%Y")
            
            
        if start_25 <= date_cell <= end_25:
            # add to global lists
            grads_lis_25.append(line[7])
            postd_lis_25.append(line[8])
            fac_lis_25.append(line[9])
            staf_lis_25.append(line[10])
            audience_25.append(line[11])
            event_25.append(line[2])
            try:
                attendees_25 += int(line[13])
                update_or_add_events(event_audience_pop_25, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_25, line[11], int(line[13]))
            except:
                None
        elif start_24 <= date_cell <= end_24:
            # add to global lists
            grads_lis_24.append(line[7])
            postd_lis_24.append(line[8])
            fac_lis_24.append(line[9])
            staf_lis_24.append(line[10])
            audience_24.append(line[11])
            event_24.append(line[2])
            try:
                attendees_24 += int(line[13])
                update_or_add_events(event_audience_pop_24, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_24, line[11], int(line[13]))
            except:
                None
        elif start_23 <= date_cell <= end_23:
            # add to global lists
            grads_lis_23.append(line[7])
            postd_lis_23.append(line[8])
            fac_lis_23.append(line[9])
            staf_lis_23.append(line[10])
            audience_23.append(line[11])
            event_23.append(line[2])
            try:
                attendees_23 += int(line[13])
                update_or_add_events(event_audience_pop_23, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_23, line[11], int(line[13]))
            except:
                None
        elif start_22 <= date_cell <= end_22:
            # add to global lists
            grads_lis_22.append(line[7])
            postd_lis_22.append(line[8])
            fac_lis_22.append(line[9])
            staf_lis_22.append(line[10])
            audience_22.append(line[11])
            event_22.append(line[2])
            try:
                attendees_22 += int(line[13])
                update_or_add_events(event_audience_pop_22, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_22, line[11], int(line[13]))
            except:
                None
        elif start_21 <= date_cell <= end_21:
            # add to global lists
            grads_lis_21.append(line[7])
            postd_lis_21.append(line[8])
            fac_lis_21.append(line[9])
            staf_lis_21.append(line[10])
            audience_21.append(line[11])
            event_21.append(line[2])
            try:
                attendees_21 += int(line[13])
                #print(line[13])
                update_or_add_events(event_audience_pop_21, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_21, line[11], int(line[13]))
            except:
                None
        elif start_20 <= date_cell <= end_20:
            # add to global lists
            grads_lis_20.append(line[7])
            postd_lis_20.append(line[8])
            fac_lis_20.append(line[9])
            staf_lis_20.append(line[10])
            audience_20.append(line[11])
            event_20.append(line[2])
            try:
                attendees_20 += int(line[13])
                update_or_add_events(event_audience_pop_20, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_20, line[11], int(line[13]))
            except:
                None
        elif start_19 <= date_cell <= end_19:
            # add to global lists
            grads_lis_19.append(line[7])
            postd_lis_19.append(line[8])
            fac_lis_19.append(line[9])
            staf_lis_19.append(line[10])
            audience_19.append(line[11])
            event_19.append(line[2])
            try:
                attendees_19 += int(line[13])
                update_or_add_events(event_audience_pop_19, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_19, line[11], int(line[13]))
            except:
                None
        elif start_18 <= date_cell <= end_18:
            # add to global lists
            grads_lis_18.append(line[7])
            postd_lis_18.append(line[8])
            fac_lis_18.append(line[9])
            staf_lis_18.append(line[10])
            audience_18.append(line[11])
            event_18.append(line[2])
            try:
                attendees_18 += int(line[13])
                update_or_add_events(event_audience_pop_18, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_18, line[11], int(line[13]))
            except:
                None
        elif start_17 <= date_cell <= end_17:
            # add to global lists
            grads_lis_17.append(line[7])
            postd_lis_17.append(line[8])
            fac_lis_17.append(line[9])
            staf_lis_17.append(line[10])
            audience_17.append(line[11])
            event_17.append(line[2])
            try:
                attendees_17 += int(line[13])
                update_or_add_events(event_audience_pop_17, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_17, line[11], int(line[13]))
            except:
                None
        elif start_16 <= date_cell <= end_16:
            # add to global lists
            grads_lis_16.append(line[7])
            postd_lis_16.append(line[8])
            fac_lis_16.append(line[9])
            staf_lis_16.append(line[10])
            audience_16.append(line[11])
            event_16.append(line[2])
            try:
                attendees_16 += int(line[13])
                update_or_add_events(event_audience_pop_16, line[2], int(line[13]))
                if "," not in line[11]:
                    update_or_add_events(type_audience_pop_16, line[11], int(line[13]))
            except:
                None


# list for total attendees
attendees_list = [attendees_16, attendees_17, attendees_18, attendees_19, attendees_20, attendees_21, attendees_22, attendees_23, attendees_24, attendees_25]
# dictionary so we can keep track of how many times each person has volunteered for each year
# fy25
gradstudents_list_25 = {}
postdocs_list_25 = {}
faculty_list_25 = {}
staff_list_25 = {}

# fy24
gradstudents_list_24 = {}
postdocs_list_24 = {}
faculty_list_24 = {}
staff_list_24 = {}

# fy23
gradstudents_list_23 = {}
postdocs_list_23 = {}
faculty_list_23 = {}
staff_list_23 = {}


# fy22
gradstudents_list_22 = {}
postdocs_list_22 = {}
faculty_list_22 = {}
staff_list_22 = {}

# fy21
gradstudents_list_21 = {}
postdocs_list_21 = {}
faculty_list_21 = {}
staff_list_21 = {}

# fy20
gradstudents_list_20 = {}
postdocs_list_20 = {}
faculty_list_20 = {}
staff_list_20 = {}

# fy19
gradstudents_list_19 = {}
postdocs_list_19 = {}
faculty_list_19 = {}
staff_list_19 = {}

# fy18
gradstudents_list_18 = {}
postdocs_list_18 = {}
faculty_list_18 = {}
staff_list_18 = {}

# fy17
gradstudents_list_17 = {}
postdocs_list_17 = {}
faculty_list_17 = {}
staff_list_17 = {}

# fy16
gradstudents_list_16 = {}
postdocs_list_16 = {}
faculty_list_16 = {}
staff_list_16 = {}


# audience type dictionaries
audience_type_list_16 = {}
audience_type_list_17 = {}
audience_type_list_18 = {}
audience_type_list_19 = {}
audience_type_list_20 = {}
audience_type_list_21 = {}
audience_type_list_22 = {}
audience_type_list_23 = {}
audience_type_list_24 = {}
audience_type_list_25 = {}


# event type dictionaries
event_type_list_16 = {}
event_type_list_17 = {}
event_type_list_18 = {}
event_type_list_19 = {}
event_type_list_20 = {}
event_type_list_21 = {}
event_type_list_22 = {}
event_type_list_23 = {}
event_type_list_24 = {}
event_type_list_25 = {}


def extract_names(list, dictionary):
    for k in list:
        if k != "+" and k != "none" and k != "None" and k != " " and k != "" and k != None:
            names = k.split(', ')
            for h in names:
                if h != "":
                    # add each name to the list after splitting by comma (same for each)
                    update_or_add(dictionary, h)


# gradstudents
extract_names(grads_lis_25, gradstudents_list_25)
extract_names(grads_lis_24, gradstudents_list_24)
extract_names(grads_lis_23, gradstudents_list_23)
extract_names(grads_lis_22, gradstudents_list_22)
extract_names(grads_lis_21, gradstudents_list_21)
extract_names(grads_lis_20, gradstudents_list_20)
extract_names(grads_lis_19, gradstudents_list_19)
extract_names(grads_lis_18, gradstudents_list_18)
extract_names(grads_lis_17, gradstudents_list_17)
extract_names(grads_lis_16, gradstudents_list_16)

# postdocs
extract_names(postd_lis_25, postdocs_list_25)
extract_names(postd_lis_24, postdocs_list_24)
extract_names(postd_lis_23, postdocs_list_23)
extract_names(postd_lis_22, postdocs_list_22)
extract_names(postd_lis_21, postdocs_list_21)
extract_names(postd_lis_20, postdocs_list_20)
extract_names(postd_lis_19, postdocs_list_19)
extract_names(postd_lis_18, postdocs_list_18)
extract_names(postd_lis_17, postdocs_list_17)
extract_names(postd_lis_16, postdocs_list_16)

# faculty
extract_names(fac_lis_25, faculty_list_25)
extract_names(fac_lis_24, faculty_list_24)
extract_names(fac_lis_23, faculty_list_23)
extract_names(fac_lis_22, faculty_list_22)
extract_names(fac_lis_21, faculty_list_21)
extract_names(fac_lis_20, faculty_list_20)
extract_names(fac_lis_19, faculty_list_19)
extract_names(fac_lis_18, faculty_list_18)
extract_names(fac_lis_17, faculty_list_17)
extract_names(fac_lis_16, faculty_list_16)

# staff
extract_names(staf_lis_25, staff_list_25)
extract_names(staf_lis_24, staff_list_24)
extract_names(staf_lis_23, staff_list_23)
extract_names(staf_lis_22, staff_list_22)
extract_names(staf_lis_21, staff_list_21)
extract_names(staf_lis_20, staff_list_20)
extract_names(staf_lis_19, staff_list_19)
extract_names(staf_lis_18, staff_list_18)
extract_names(staf_lis_17, staff_list_17)
extract_names(staf_lis_16, staff_list_16)


# audience type
extract_names(audience_16, audience_type_list_16)
extract_names(audience_17, audience_type_list_17)
extract_names(audience_18, audience_type_list_18)
extract_names(audience_19, audience_type_list_19)
extract_names(audience_20, audience_type_list_20)
extract_names(audience_21, audience_type_list_21)
extract_names(audience_22, audience_type_list_22)
extract_names(audience_23, audience_type_list_23)
extract_names(audience_24, audience_type_list_24)
extract_names(audience_25, audience_type_list_25)


# event type
extract_names(event_16, event_type_list_16)
extract_names(event_17, event_type_list_17)
extract_names(event_18, event_type_list_18)
extract_names(event_19, event_type_list_19)
extract_names(event_20, event_type_list_20)
extract_names(event_21, event_type_list_21)
extract_names(event_22, event_type_list_22)
extract_names(event_23, event_type_list_23)
extract_names(event_24, event_type_list_24)
extract_names(event_25, event_type_list_25)



#print(gradstudents_list_21)

#update with number of volunteers

#fy25
grad_len_25 = len(gradstudents_list_25.keys())
postdoc_len_25 = len(postdocs_list_25.keys())
faculty_len_25 = len(faculty_list_25.keys())
staff_len_25 = len(staff_list_25.keys())

#fy24
grad_len_24 = len(gradstudents_list_24.keys())
postdoc_len_24 = len(postdocs_list_24.keys())
faculty_len_24 = len(faculty_list_24.keys())
staff_len_24 = len(staff_list_24.keys())

#fy23
grad_len_23 = len(gradstudents_list_23.keys())
postdoc_len_23 = len(postdocs_list_23.keys())
faculty_len_23 = len(faculty_list_23.keys())
staff_len_23 = len(staff_list_23.keys())

#fy22
grad_len_22 = len(gradstudents_list_22.keys())
postdoc_len_22 = len(postdocs_list_22.keys())
faculty_len_22 = len(faculty_list_22.keys())
staff_len_22 = len(staff_list_22.keys())

#fy21
grad_len_21 = len(gradstudents_list_21.keys())
postdoc_len_21 = len(postdocs_list_21.keys())
faculty_len_21 = len(faculty_list_21.keys())
staff_len_21 = len(staff_list_21.keys())

#fy20
grad_len_20 = len(gradstudents_list_20.keys())
postdoc_len_20 = len(postdocs_list_20.keys())
faculty_len_20 = len(faculty_list_20.keys())
staff_len_20 = len(staff_list_20.keys())

#fy19
grad_len_19 = len(gradstudents_list_19.keys())
postdoc_len_19 = len(postdocs_list_19.keys())
faculty_len_19 = len(faculty_list_19.keys())
staff_len_19 = len(staff_list_19.keys())

#fy18
grad_len_18 = len(gradstudents_list_18.keys())
postdoc_len_18 = len(postdocs_list_18.keys())
faculty_len_18 = len(faculty_list_18.keys())
staff_len_18 = len(staff_list_18.keys())

#fy17
grad_len_17 = len(gradstudents_list_17.keys())
postdoc_len_17 = len(postdocs_list_17.keys())
faculty_len_17 = len(faculty_list_17.keys())
staff_len_17 = len(staff_list_17.keys())

#fy16
grad_len_16 = len(gradstudents_list_16.keys())
postdoc_len_16 = len(postdocs_list_16.keys())
faculty_len_16 = len(faculty_list_16.keys())
staff_len_16 = len(staff_list_16.keys())




volunteers_grads = [grad_len_16, grad_len_17, grad_len_18, grad_len_19, grad_len_20, grad_len_21, grad_len_22, grad_len_23, grad_len_24, grad_len_25]
volunteers_postdoc = [postdoc_len_16, postdoc_len_17, postdoc_len_18, postdoc_len_19, postdoc_len_20, postdoc_len_21, postdoc_len_22, postdoc_len_23, postdoc_len_24, postdoc_len_25]
volunteers_faculty = [faculty_len_16, faculty_len_17, faculty_len_18, faculty_len_19, faculty_len_20, faculty_len_21, faculty_len_22, faculty_len_23, faculty_len_24, faculty_len_25]
volunteers_staff = [staff_list_16, staff_list_17, staff_list_18, staff_list_19, staff_list_20, staff_list_21, staff_list_22, staff_list_23, staff_list_24, staff_list_25]
# print(volunteers_grads)
# print(volunteers_postdoc)
# print(volunteers_faculty)
#print(volunteers_staff)


# Initialize an empty dictionary to accumulate the sums

def dictionary_counts(dictionary):
    counter = 0
    # Loop through each dictionary in the list
    for _,count in dictionary.items():
        # Loop through each key-value pair in the dictionary
        #for _, count in i.items():
            # Add the value to the corresponding key in the new dictionary
            # If the key does not exist, it adds the key with its value
        counter += count
    return counter




#fy25
grad_total_25 = dictionary_counts(gradstudents_list_25)
postdoc_total_25 = dictionary_counts(postdocs_list_25)
faculty_total_25 = dictionary_counts(faculty_list_25)
staff_total_25 = dictionary_counts(staff_list_25)

#fy24
grad_total_24 = dictionary_counts(gradstudents_list_24)
postdoc_total_24 = dictionary_counts(postdocs_list_24)
faculty_total_24 = dictionary_counts(faculty_list_24)
staff_total_24 = dictionary_counts(staff_list_24)

#fy23
grad_total_23 = dictionary_counts(gradstudents_list_23)
postdoc_total_23 = dictionary_counts(postdocs_list_23)
faculty_total_23 = dictionary_counts(faculty_list_23)
staff_total_23 = dictionary_counts(staff_list_23)

#fy22
grad_total_22 = dictionary_counts(gradstudents_list_22)
postdoc_total_22 = dictionary_counts(postdocs_list_22)
faculty_total_22 = dictionary_counts(faculty_list_22)
staff_total_22 = dictionary_counts(staff_list_22)

#fy21
grad_total_21 = dictionary_counts(gradstudents_list_21)
postdoc_total_21 = dictionary_counts(postdocs_list_21)
faculty_total_21 = dictionary_counts(faculty_list_21)
staff_total_21 = dictionary_counts(staff_list_21)

#fy20
grad_total_20 = dictionary_counts(gradstudents_list_20)
postdoc_total_20 = dictionary_counts(postdocs_list_20)
faculty_total_20 = dictionary_counts(faculty_list_20)
staff_total_20 = dictionary_counts(staff_list_20)

#fy19
grad_total_19 = dictionary_counts(gradstudents_list_19)
postdoc_total_19 = dictionary_counts(postdocs_list_19)
faculty_total_19 = dictionary_counts(faculty_list_19)
staff_total_19 = dictionary_counts(staff_list_19)

#fy18
grad_total_18 = dictionary_counts(gradstudents_list_18)
postdoc_total_18 = dictionary_counts(postdocs_list_18)
faculty_total_18 = dictionary_counts(faculty_list_18)
staff_total_18 = dictionary_counts(staff_list_18)

#fy17
grad_total_17 = dictionary_counts(gradstudents_list_17)
postdoc_total_17 = dictionary_counts(postdocs_list_17)
faculty_total_17 = dictionary_counts(faculty_list_17)
staff_total_17 = dictionary_counts(staff_list_17)

#fy16
grad_total_16 = dictionary_counts(gradstudents_list_16)
postdoc_total_16 = dictionary_counts(postdocs_list_16)
faculty_total_16 = dictionary_counts(faculty_list_16)
staff_total_16 = dictionary_counts(staff_list_16)

# grads_by_year = {'2016': gradstudents_list_16,
#                 '2017': gradstudents_list_17,
#                 '2018': gradstudents_list_18,
#                 '2019': gradstudents_list_19,
#                 '2020': gradstudents_list_20,
#                 '2021': gradstudents_list_21,
#                 '2022': gradstudents_list_22,
#                 '2023': gradstudents_list_23,
#                 '2024': gradstudents_list_24,
#                 '2025': gradstudents_list_25}


# # Specify the output CSV file
# csv_file = 'aggregated_data.csv'

# # Open the CSV file and write the data
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     # Write the header
#     writer.writerow(['Name', 'Count', 'Year', 'Category'])
    
#     # Write the data for each year
#     for year, data in grads_by_year.items():
#         for name, count in data.items():
#             writer.writerow([name, count, year, 'grads'])


# Data structure for each category from 2016 to 2025
# Data structure for each category from 2016 to 2025
data_by_year = {
    '2016': {
        'grads': gradstudents_list_16,
        'postdocs': postdocs_list_16,
        'faculty': faculty_list_16,
        'staff': staff_list_16
    },
    '2017': {
        'grads': gradstudents_list_17,
        'postdocs': postdocs_list_17,
        'faculty': faculty_list_17,
        'staff': staff_list_17
    },
    '2018': {
        'grads': gradstudents_list_18,
        'postdocs': postdocs_list_18,
        'faculty': faculty_list_18,
        'staff': staff_list_18
    },
    '2019': {
        'grads': gradstudents_list_19,
        'postdocs': postdocs_list_19,
        'faculty': faculty_list_19,
        'staff': staff_list_19
    },
    '2020': {
        'grads': gradstudents_list_20,
        'postdocs': postdocs_list_20,
        'faculty': faculty_list_20,
        'staff': staff_list_20
    },
    '2021': {
        'grads': gradstudents_list_21,
        'postdocs': postdocs_list_21,
        'faculty': faculty_list_21,
        'staff': staff_list_21
    },
    '2022': {
        'grads': gradstudents_list_22,
        'postdocs': postdocs_list_22,
        'faculty': faculty_list_22,
        'staff': staff_list_22
    },
    '2023': {
        'grads': gradstudents_list_23,
        'postdocs': postdocs_list_23,
        'faculty': faculty_list_23,
        'staff': staff_list_23
    },
    '2024': {
        'grads': gradstudents_list_24,
        'postdocs': postdocs_list_24,
        'faculty': faculty_list_24,
        'staff': staff_list_24
    },
    '2025': {
        'grads': gradstudents_list_25,
        'postdocs': postdocs_list_25,
        'faculty': faculty_list_25,
        'staff': staff_list_25
    }
}

categories_data = {
        'Grads': [grad_total_16, grad_total_17, grad_total_18, grad_total_19, grad_total_20, grad_total_21, grad_total_22, grad_total_23, grad_total_24, grad_total_25],
        'Postdoc': [postdoc_total_16, postdoc_total_17, postdoc_total_18, postdoc_total_19, postdoc_total_20, postdoc_total_21, postdoc_total_22, postdoc_total_23, postdoc_total_24, postdoc_total_25],
        'Faculty': [faculty_total_16, faculty_total_17, faculty_total_18, faculty_total_19, faculty_total_20, faculty_total_21, faculty_total_22, faculty_total_23, faculty_total_24, faculty_total_25],
        'Staff': [staff_total_16, staff_total_17, staff_total_18, staff_total_19, staff_total_20, staff_total_21, staff_total_22, staff_total_23, staff_total_24, staff_total_25]
    }

event_attendance_data = {
    '2025': event_audience_pop_25,
    '2024': event_audience_pop_24,
    '2023': event_audience_pop_23,
    '2022': event_audience_pop_22,
    '2021': event_audience_pop_21,
    '2020': event_audience_pop_20,
    '2019': event_audience_pop_19,
    '2018': event_audience_pop_18,
    '2017': event_audience_pop_17,
    '2016': event_audience_pop_16,
}

def find_folder(folder_name):
    # Get the current directory of the script
    root_dir = os.getcwd()
    
    # Walk through the directory tree to find the folder
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if folder_name in dirnames:
            return os.path.join(dirpath, folder_name)
    
    return None

# Search for the 'aggregate' folder
folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'processed_data')

if folder_path:
    print("Folder found at:", folder_path)
    
    # Path to the CSV file in the aggregate folder
    csv_file_path_volunteers = os.path.join(folder_path, "aggregate_volunteers.csv")
    csv_file_path_volunteer_categories = os.path.join(folder_path, "aggregate_volunteer_category.csv")
    csv_file_path_attendees_count = os.path.join(folder_path, "aggregate_attendees_count.csv")
    csv_file_event_type = os.path.join(folder_path, "aggreagate_event_type.csv")
    
    # Check if the file already exists
    if not os.path.exists(csv_file_path_volunteers):
        # File does not exist, create and write to the file
        with open(csv_file_path_volunteers, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write the header
            writer.writerow(['Name', 'Count', 'Year', 'Category'])
            
            # Write the data for each year and category (example structure)
            for year, categories in data_by_year.items():
                for category, data in categories.items():
                    if isinstance(data, dict):  # Ensure the data is in dictionary format
                        for name, count in data.items():
                            writer.writerow([name, count, year, category])
                    else:
                        print(f"Data for year {year}, category {category} is not in dictionary format.")
    else:
        print(f"The file 'aggregate_volunteers.csv' already exists at: {csv_file_path_volunteers}")
    
    years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
     # Check if the file already exists
    with open(csv_file_path_volunteer_categories, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header: Year and Categories
        header = ['Year'] + list(categories_data.keys())
        writer.writerow(header)
        
        # Write the data rows for each year
        for i, year in enumerate(years):
            row = [year]  # Start with the year
            for category in categories_data:
                row.append(categories_data[category][i])  # Add the total for each category in that year
            writer.writerow(row)

    with open(csv_file_path_attendees_count, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header: Year and Categories
        header = ['Year'] + ['Count']
        writer.writerow(header)
        
        # Write the data rows for each year
        for i, year in enumerate(years):
            row = [year]  # Start with the year
            row.append(attendees_list[i])
            writer.writerow(row)
    
    # Create and write to the CSV file
    with open(csv_file_event_type, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        header = ['Year', 'Event', 'Attendance']
        writer.writerow(header)
        
        # Write the event attendance data
        for year, events in event_attendance_data.items():
            if isinstance(events, dict):  # Ensure that the events are in dictionary format
                for event, attendance in events.items():
                    writer.writerow([year, event, attendance])
            else:
                print(f"Data for year {year} is not in the expected dictionary format.")

else:
    print("Folder not found.")


# need csv with audience type and year and attendance (like general public, k-12, etc.)
# then data event type with year and attendance (like Astronomy on Tap)