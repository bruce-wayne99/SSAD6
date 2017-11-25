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

def outputListOfActiveUsers(activeUsers,threshold_amount):
    json_data = defaultdict(list)
    data = ""
    data = data + "There are " + str(len(activeUsers)) + " users who have spent more than or equal to " + str(threshold_amount) + " units" + '\n'
    for i in range(len(activeUsers)):
        data = data + str(i+1) + " : " +  str(activeUsers[i]) + '\n'
        json_data["transaction_users"].append(activeUsers[i])
    output_file = open("golive/output/active_users/text_file/ListOfMoneySpenders.txt", "w")
    output_file.write(data)
    output_file.close()
    with open("golive/output/active_users/json/ListOfMoneySpenders.json","w") as outfile:
        json.dump(json_data, outfile, indent = 4)
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
