import os
import csv
import json
import pickle
from django.conf import settings


########## colleges.pickle ##########
path_to_colleges = os.path.join(settings.STATIC_ROOT, 'colleges.json')

json_data = []
#need encoding to prevent error on live server
with open(path_to_colleges, encoding='utf-8') as json_file:
    json_data = json.load(json_file)

onlyCollegeList = []
for piece in json_data:
    this_ip = piece['institution']
    onlyCollegeList.append(this_ip)

#sorted and deletes duplicates from onlyCollegeList
onlyCollegeList = sorted(set(onlyCollegeList))
onlyCollegeList.insert(0, 'Other')
onlyCollegeList.insert(0, 'NA')
#puts onlyCollegeList into a tupled list of choices for forms
tupled_list_colleges = list(zip(onlyCollegeList, onlyCollegeList))

with open('static/colleges.pickle', 'wb') as handle:
    pickle.dump(tupled_list_colleges, handle, protocol=pickle.HIGHEST_PROTOCOL)


########## majors.pickle ##########
path_to_majors = os.path.join(settings.STATIC_ROOT, 'major_list.csv')

with open(path_to_majors, 'r') as f:
    reader = csv.reader(f)
    complete_majors_list = list(reader)

only_majors_list = [a[1] for a in complete_majors_list]
#delete first index of major list because it is not a major(it's a header)
only_majors_list.pop(0)
only_majors_list = sorted(only_majors_list)
majors_lower = [x.lower() for x in only_majors_list]
for x in range(len(majors_lower)):
    majors_lower[x] = majors_lower[x].title()
    x = x + 1

majors_lower.insert(0, 'Other')
majors_lower.insert(0, 'NA')
tupled_list_majors = list(zip(majors_lower, majors_lower))

with open('static/majors.pickle', 'wb') as handle:
    pickle.dump(tupled_list_majors, handle, protocol=pickle.HIGHEST_PROTOCOL)


########## states.pickle ##########
path_to_states = os.path.join(settings.STATIC_ROOT, 'states.csv')

with open(path_to_states, 'r', encoding='utf-8') as file:
    states = csv.reader(file)
    states_list = list(states)

states_list = [a[0] for a in states_list]
states_list.pop(0)
states_list.insert(0, 'NA')
tupled_list_states = list(zip(states_list,states_list))

with open('static/states.pickle', 'wb') as handle:
    pickle.dump(tupled_list_states, handle, protocol=pickle.HIGHEST_PROTOCOL)
