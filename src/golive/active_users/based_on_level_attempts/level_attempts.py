import sys
from collections import defaultdict
import json

def outputListOfLevelStuckUsers(level_stuck_users,attempts_lowerbound,attempts_upperbound,level):
    json_data = defaultdict(list)
    data = ""
    data = data + "There are " + str(len(level_stuck_users)) + " Users who made between " + str(attempts_lowerbound) + "-" + str(attempts_upperbound) + " attempts to clear the level " + str(level) +  '\n'
    for i in range(len(level_stuck_users)):
        data = data + str(i+1) + " : " +  str(level_stuck_users[i]) + '\n'
        json_data["level_attempts_users"].append(level_stuck_users[i])
    output_file = open("golive/output/active_users/text_file/ListOfUsersStuckAtALevel.txt", "w")
    output_file.write(data)
    output_file.close()
    with open("golive/output/active_users/json/ListOfUsersStuckAtALevel.json","w") as outfile:
        json.dump(json_data, outfile, indent = 4)
    return

def filter_level(data,level):
	filtered_data = []
	for i in range(len(data)):
		check_level = data[i]["event_name"].split(' ')
		if int(check_level[1]) == level and check_level[2]=='Failed':
			filtered_data.append(data[i])
	return filtered_data
