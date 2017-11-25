import sys
import datetime
import json
from collections import defaultdict

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def empty(self):
        self.items = []

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


def checkOnTheSameDay(stack, sessions, iterator):
    time1 = stack.peek()["eventTime"]
    time2 = sessions[iterator]["eventTime"]
    hours = findDifferenceInHours(time2, time1)
    if hours <= 24:
        return True
    else:
        return False


def checkOnTheNextDay(stack, sessions, iterator):
    time1 = stack.peek()["eventTime"]
    time2 = sessions[iterator]["eventTime"]
    hours = findDifferenceInHours(time2, time1)
    if hours > 24 and hours <= 48:
        return True
    else:
        return False


def isSameDay(sessions, iterator, BaseSession, stack, session_gap):
    # consider the latest appearance if he comes on the same day.
    time1 = BaseSession["eventTime"]
    time2 = sessions[iterator]["eventTime"]
    days = findDifferenceInDays(time2, time1)
    if days == stack.size() - 1:
        stack.pop()
        stack.push(sessions[iterator])
    elif days == stack.size():
        hours = findDifferenceInHours(time2, time1)
        if hours >= session_gap:
            stack.push(sessions[iterator])

    return stack


def onTheSameDay(
        sessions,
        iterator,
        session_gap,
        consec_days,
        BaseSession,
        stack):
    if isSameDay(sessions, iterator, BaseSession, stack, session_gap):
        stack.pop()
        stack.push(sessions[iterator])

    elif isNextDay(sessions, iterator, BaseSession, stack, session_gap):
        if isSessionGap(sessions, iterator, stack, session_gap):
            stack.push(sessions[iterator])

    return stack


def processDataOfUser(sessions, session_gap, consec_days):
    stack = Stack()
    iterator = 0
    BaseSession = None

    while iterator < len(sessions):
        if stack.size() == consec_days:
            return True
        if stack.size() == 0:
            stack.push(sessions[iterator])
            BaseSession = sessions[iterator]
        elif checkOnTheSameDay(stack, sessions, iterator):
            stack = onTheSameDay(
                sessions,
                iterator,
                session_gap,
                consec_days,
                BaseSession,
                stack)
        elif checkOnTheNextDay(stack, sessions, iterator):
            stack.push(sessions[iterator])
        else:
            stack.empty()
            stack.push(sessions[iterator])
            BaseSession = sessions[iterator]
        iterator += 1

    if stack.size() == consec_days:
        return True
    else:
        return False

def outputListOfActiveUsers(activeUsers,consec_days):
    json_data = defaultdict(list)
    data = ""
    data = data + "There are " + str(len(activeUsers)) + " Users who played the game atleast " + str(consec_days) + " consecutive days in a row." + '\n'
    for i in range(len(activeUsers)):
        data = data + str(i+1) + " : " +  str(activeUsers[i]) + '\n'
        json_data["consective_days_users"].append(activeUsers[i])
    output_file = open("golive/output/active_users/text_file/ListOfActiveUsers.txt", "w")
    output_file.write(data)
    output_file.close()
    with open("golive/output/active_users/json/ListofActiveUsers.json","w") as outfile:
        json.dump(json_data, outfile, indent = 4)
    return
