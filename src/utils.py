import sys
import datetime
import json
from collections import defaultdict

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

def sortDataBasedOnSessionTime(usersdata):
    for i in usersdata:
        usersdata[i].sort(key=lambda x: x["SessionTime"])
    return usersdata

def modifyUnixTime(data):
    for i in data:
        unixTime = i["eventTime"]
        time = converTime(unixTime)
        i["SessionTime"] = unixTime
        i["eventTime"] = time
    return data
