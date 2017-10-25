import datetime
import json
from collections import defaultdict
import sys

def findDataFromApplication():
    with open(sys.argv[1]) as data_file:
        data = json.load(data_file)
    data = data["Data"]
    return data


def converTime(unix_time):
    time = datetime.datetime.fromtimestamp(
        int(unix_time)
    ).strftime('%Y-%m-%d %H:%M:%S')
    return time


def findDataOfEachUser(data):
    usersdata = defaultdict(list)
    iterator = 0
    while(iterator < len(data)):
        user_id = data[iterator]["user_id"]
        usersdata[user_id].append(data[iterator])
        iterator += 1
    return usersdata


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

def modifyUnixTime(data):
    for i in data:
        unixTime = i["eventTime"]
        time = converTime(unixTime)
        i["SessionTime"] = unixTime
        i["eventTime"] = time
    return data


def sortDataBasedOnSessionTime(usersdata):
    for i in usersdata:
        usersdata[i].sort(key=lambda x: x["SessionTime"])
    return usersdata

def outputListOfActiveUsers(activeUsers, level, threshold_amount):
	data = ""
	data = data + "There are " + str(len(activeUsers)) + " users who have spent more than or equal to " + str(threshold_amount) + " time units on Level " + str(level)  + '\n'
	for i in range(len(activeUsers)):
		data = data + str(i+1) + " : " +  str(activeUsers[i]) + '\n'

	output_file = open("ListOfActiveUsers.txt", "w")
	output_file.write(data)
	output_file.close()
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

def filter_level(data,level):
	filtered_data = []
	for i in range(len(data)):
		check_level = data[i]["event_name"].split(' ')
		if int(check_level[1]) == level:
			filtered_data.append(data[i])
	return filtered_data

level = int(sys.argv[2])
threshold_time = int(sys.argv[3])
activeUsers = []
data = findDataFromApplication()

data = modifyUnixTime(data)

data = filter_level(data,level)

usersdata = findDataOfEachUser(data)

usersdata = sortDataBasedOnSessionTime(usersdata)
#print(usersdata[0])

for i in usersdata:
    isSpend = processDataOfUser(usersdata[i], level,threshold_time)
    if(isSpend):
        activeUsers.append(i)
outputListOfActiveUsers(activeUsers,level,threshold_time)
