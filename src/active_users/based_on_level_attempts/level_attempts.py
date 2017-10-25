import sys
sys.path.append('../..')
from utils import *

def outputListOfLevelStuckUsers(level_stuck_users,attempts,level):
	data = ""
	data = data + "There are " + str(len(level_stuck_users)) + " Users who made atleast " + str(attempts) + " attempts to clear the level " + str(level) +  '\n'
	for i in range(len(level_stuck_users)):
		data = data + str(i+1) + " : " +  str(level_stuck_users[i]) + '\n'

	output_file = open("ListOfUsersStuckAtALevel.txt", "w")
	output_file.write(data)
	output_file.close()
	return

def filter_level(data,level):
	filtered_data = []
	for i in range(len(data)):
		check_level = data[i]["event_name"].split(' ')
		if int(check_level[1]) == level and check_level[2]=='Failed':
			filtered_data.append(data[i])
	return filtered_data

level = int(sys.argv[2])
attempts = int(sys.argv[3])
level_stuck_users = []

data = findDataFromApplication()

data = modifyUnixTime(data)

data = filter_level(data,level)

usersdata = findDataOfEachUser(data)

for i in usersdata:
	if(len(usersdata[i])>=attempts):
		level_stuck_users.append(i)


outputListOfLevelStuckUsers(level_stuck_users,attempts,level)
