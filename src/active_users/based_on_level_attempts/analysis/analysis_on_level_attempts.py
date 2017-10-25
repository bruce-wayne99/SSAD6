import sys
sys.path.append('../../..')
from utils import *
import matplotlib.pyplot as plt


def filter_level(data,level):
	filtered_data = []
	for i in range(len(data)):
		check_level = data[i]["event_name"].split(' ')
		if int(check_level[1]) == level and check_level[2]=='Failed':
			filtered_data.append(data[i])
	return filtered_data

attempts = int(sys.argv[2])

graph1 = []
graph2 = []

for i in range(1,8):
	print(i)
	level = i
	data = findDataFromApplication()
	data = modifyUnixTime(data)
	data = filter_level(data,level)
	usersdata = findDataOfEachUser(data)
	graph1.append(i)
	count = 0
	for j in usersdata:
		if(len(usersdata[j])>=attempts):
			count+=1
	graph2.append(count)



plt.xlabel('Level')
plt.ylabel('No of Users who made more than threshold attempts')
plt.title('Classifaction based on number of attempts on a level')
plt.plot(graph1, graph2, 'r--')
plt.axis([1, 8, 0, 2000])
plt.show()
