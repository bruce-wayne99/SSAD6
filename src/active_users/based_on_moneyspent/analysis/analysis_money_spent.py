import sys
sys.path.append('../../..')
from utils import *
import matplotlib.pyplot as plt


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

graph1 = []
graph2 = []

for i in range(0,50):
    print(i)
    data = findDataFromApplication()
    data = modifyUnixTime(data)
    usersdata = findDataOfEachUser(data)
    usersdata = sortDataBasedOnSessionTime(usersdata)
    count = 0
    for j in usersdata:
        isActive = processDataOfUser(usersdata[j], i)
        if(isActive):
            count+=1
    graph1.append(i)
    graph2.append(count)


plt.xlabel('Money')
plt.ylabel('No of Users who spent more than threshold units')
plt.title('Classifaction based on money spent')
plt.plot(graph1, graph2, 'r--')
plt.axis([0, 50, 0, 15000])
plt.show()
