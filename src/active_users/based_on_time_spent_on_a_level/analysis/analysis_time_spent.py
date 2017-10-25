import sys
sys.path.append('../../..')
from utils import *
import matplotlib.pyplot as plt



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

threshold_time = int(sys.argv[2])
graph2 = []
graph1 = []


for i in range(1,8):
	print(i)
	level = i
	data = findDataFromApplication()
	data = modifyUnixTime(data)
	data = filter_level(data,level)
	usersdata = findDataOfEachUser(data)
	usersdata = sortDataBasedOnSessionTime(usersdata)
	count = 0
	for j in usersdata:
		isSpend = processDataOfUser(usersdata[j], level,threshold_time)
		if(isSpend):
			count+=1
	graph1.append(i)
	graph2.append(count)

plt.xlabel('Level')
plt.ylabel('No of Users who spent more than threshold time units')
plt.title('Classifaction based on time spent on a level')
plt.plot(graph1, graph2, 'r--')
plt.axis([1, 8, 0, 1000])
plt.show()
