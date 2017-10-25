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

def outputListOfActiveUsers(activeUsers,threshold_amount):
	data = ""
	data = data + "There are " + str(len(activeUsers)) + " users who have spent more than or equal to " + str(threshold_amount) + " units" + '\n'
	for i in range(len(activeUsers)):
		data = data + str(i+1) + " : " +  str(activeUsers[i]) + '\n'

	output_file = open("ListOfActiveUsers.txt", "w")
	output_file.write(data)
	output_file.close()
	return

def processDataOfUser(sessions, threshold_amount):

    iterator = 0
    BaseSession = None
    total_amount = 0
    avg_amount = 0
    while iterator < len(sessions):
        total_amount += sessions[iterator]["transaction_amount"]
        iterator += 1
    if total_amount >= threshold_amount:
        return True
    else:
        return False

threshold_amount = int(sys.argv[2])

activeUsers = []

data = findDataFromApplication()

data = modifyUnixTime(data)

usersdata = findDataOfEachUser(data)

usersdata = sortDataBasedOnSessionTime(usersdata)

for i in usersdata:
    isActive = processDataOfUser(usersdata[i], threshold_amount)
    if(isActive):
        activeUsers.append(i)

outputListOfActiveUsers(activeUsers,threshold_amount)
