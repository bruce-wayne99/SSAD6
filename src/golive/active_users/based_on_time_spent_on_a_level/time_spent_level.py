import datetime
import json
from collections import defaultdict
import sys

def findDifferenceInDays(time2, time1):
    start = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    diff = start - end
    return diff.days

def findDifferenceInHours(time2, time1):
    start = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    diff = start - end
    return diff.days * 24 + diff.seconds / 3600.0

def outputListOfActiveUsers(activeUsers, level, threshold_amount):
    json_data = defaultdict(list)
    data = ""
    data = data + "There are " + str(len(activeUsers)) + " users who have spent more than or equal to " + str(threshold_amount) + " time units on Level " + str(level)  + '\n'
    for i in range(len(activeUsers)):
        data = data + str(i+1) + " : " +  str(activeUsers[i]) + '\n'
        json_data["time_spent_users"].append(activeUsers[i])
    output_file = open("golive/output/active_users/text_file/TimeSpentOnLevel.txt", "w")
    output_file.write(data)
    output_file.close()
    with open("golive/output/active_users/json/TimeSpentOnLevel.json","w") as outfile:
        json.dump(json_data, outfile, indent = 4)
    return

def processDataOfUser(userdata, level, threshold_time):
	iterator = 0
	total_time = 0
	while iterator < len(userdata):
		total_time += int(userdata[iterator]["endTime"])-int(userdata[iterator]["startTime"])
		iterator += 1

	if total_time>= threshold_time:
		return True
	return False

def filter_level(data, level):
	filtered_data = []
	for i in range(len(data)):
		check_level = data[i]["event_name"].split(' ')
		if int(check_level[1]) == level:
			filtered_data.append(data[i])
	return filtered_data
