import sys
import datetime
import json
from collections import defaultdict

def findDataFromApplication(datafile_path, title):
    with open(datafile_path) as data_file:
        data = json.load(data_file)
    data = data[title]
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

def findCommonUsers(offer, object1, object2, object3):
    common_users = []
    json_data = {}
    for ele in object1:
        if (ele in object2) and (ele in object3):
            common_users.append(ele)
    json_data["classified_users"] = common_users
    json_data["offer"] = offer
    dest = "classification_" + str(offer["offer_id"]) + ".json"

    with open("golive/output/classified_users/" + dest, "w") as outfile:
        json.dump(json_data, outfile,  indent = 4)
    return
