import sys
import datetime
import json
from collections import defaultdict

def outputListOfActiveUsers(activeUsers,sessions):
    json_data = defaultdict(list)
    data = ""
    data = data + "There are " + str(len(activeUsers)) + " Users who played for exactly " + str(sessions) + ' sessions\n'
    for i in range(len(activeUsers)):
        data = data + str(i+1) + " : " +  str(activeUsers[i]) + '\n'
        json_data["num_sessions"].append(activeUsers[i])
    output_file = open("./golive/output/active_users/text_file/ListOfNumSessionUsers.txt", "w")
    output_file.write(data)
    output_file.close()
    with open("./golive/output/active_users/json/ListofNumSessionUsers.json","w") as outfile:
        json.dump(json_data, outfile, indent = 4)
    return

def processDataOfUser(user_data, sessions):
    if len(user_data) == sessions:
        return True
    else:
        return False
