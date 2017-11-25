import sys
import datetime
import json
from collections import defaultdict

def processDataOfUser(user_data, coins_threshold):
    coins = 0
    for i in user_data:
        coins += int(i["attributes"]["NoOfCoins"])
    if coins >= coins_threshold:
        return True
    return False

def outputListOfActiveUsers(activeUsers, coins_threshold):
    json_data = defaultdict(list)
    data = ""
    data = data + "There are " + str(len(activeUsers)) + " Users who made spent more than " + str(coins_threshold) + " coins" + '\n'
    for i in range(len(activeUsers)):
        data = data + str(i+1) + " : " +  str(activeUsers[i]) + '\n'
        json_data["app_in_users"].append(activeUsers[i])
    output_file = open("golive/output/active_users/text_file/ListOfAppInPurchasers.txt", "w")
    output_file.write(data)
    output_file.close()
    with open("golive/output/active_users/json/ListOfAppInPurchasers.json","w") as outfile:
        json.dump(json_data, outfile, indent = 4)
    return
