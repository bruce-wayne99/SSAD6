from golive.utils.utils import *
from golive.active_users.based_on_moneyspent.transaction import *

threshold_amount = int(sys.argv[1])

activeUsers = []

data = findDataFromApplication('./golive/data/transaction.json', "Data")

data = modifyUnixTime(data)

usersdata = findDataOfEachUser(data)

usersdata = sortDataBasedOnSessionTime(usersdata)

for i in usersdata:
    isActive = processDataOfUser(usersdata[i], threshold_amount)
    if(isActive):
        activeUsers.append(i)

outputListOfActiveUsers(activeUsers,threshold_amount)
