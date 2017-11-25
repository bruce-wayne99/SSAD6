from golive.utils.utils import *
import golive.active_users.based_on_days.based_on_days as based_on_days_mod
import golive.active_users.based_on_level_attempts.level_attempts as level_attempts_mod
import golive.active_users.based_on_moneyspent.transaction as transaction_mod
import golive.active_users.based_on_time_spent_on_a_level.time_spent_level as time_spent_level_mod
import golive.active_users.based_on_sessions.based_on_sessions as based_on_sessions_mod
import golive.active_users.based_on_app_in.based_on_app_in_purchases as based_on_app_in_purchases_mod

offer_classifications = findDataFromApplication('./golive/data/offer_classification.json', "Offers")

MAX_LEVEL = 20

for offer in offer_classifications:

    '''
        consecutive days
    '''
    consec_days = offer["consecutive_days"]
    session_gap = 2
    activeUsers = []
    activeUsers_consecutive = defaultdict(int)
    data = findDataFromApplication('./golive/data/session_data.json', "Data")

    data = modifyUnixTime(data)

    usersdata = findDataOfEachUser(data)

    usersdata = sortDataBasedOnSessionTime(usersdata)

    for i in usersdata:
        isActive = based_on_days_mod.processDataOfUser(usersdata[i], session_gap, consec_days)
        if(isActive):
            activeUsers.append(i)
            activeUsers_consecutive[i] = 1
    based_on_days_mod.outputListOfActiveUsers(activeUsers, consec_days)

    '''
        based on time spent
    '''
    level_min = offer["level_lowerbound"]
    threshold_time = offer["time_spent"]
    activeUsers = []
    activeUsers_timespent = defaultdict(int)
    
    data = findDataFromApplication('./golive/data/time_spent.json', "Data")
    data = modifyUnixTime(data)
    
    total_data = findDataOfEachUser(data)
    total_data = sortDataBasedOnSessionTime(total_data)
    
    for level in range(level_min, MAX_LEVEL + 1):
    
        data_for_level = time_spent_level_mod.filter_level(data, level)
        usersdata = findDataOfEachUser(data_for_level)
        usersdata = sortDataBasedOnSessionTime(usersdata)
    
        for i in usersdata:
            current_level = total_data[i][-1]["event_name"].split(' ')
            current_level = int(current_level[1])
            if current_level == level:
                isSpend = time_spent_level_mod.processDataOfUser(usersdata[i], level, threshold_time)
                if(isSpend):
                    activeUsers.append(i)
                    activeUsers_timespent[i] = 1
    time_spent_level_mod.outputListOfActiveUsers(activeUsers, level, threshold_time)
    
    '''
        based on transaction
    '''
    threshold_amount = offer["amount_spent"]
    
    activeUsers = []
    activeUsers_transaction = defaultdict(int)
    data = findDataFromApplication('./golive/data/transaction.json', "Data")
    
    data = modifyUnixTime(data)
    
    usersdata = findDataOfEachUser(data)
    
    usersdata = sortDataBasedOnSessionTime(usersdata)
    
    for i in usersdata:
        isActive = transaction_mod.processDataOfUser(usersdata[i], threshold_amount)
        if(isActive):
            activeUsers.append(i)
            activeUsers_transaction[i] = 1
    transaction_mod.outputListOfActiveUsers(activeUsers, threshold_amount)
    
    '''
        based on level attempts
    '''
    
    level_min = offer["level_lowerbound"]
    attempts_lowerbound = offer["attempts_lowerbound"]
    attempts_upperbound = offer["attempts_upperbound"]
    level_stuck_users = []
    level_stuck_users_level_attempts = defaultdict(int)
    
    data = findDataFromApplication('./golive/data/level_attempts.json', "Data")
    data = modifyUnixTime(data)
    
    total_data = findDataOfEachUser(data)
    total_data = sortDataBasedOnSessionTime(total_data)
    
    for level in range(level_min, MAX_LEVEL + 1):
    
        data_for_level = level_attempts_mod.filter_level(data, level)
        usersdata = findDataOfEachUser(data_for_level)
        for i in usersdata:
            current_level = total_data[i][-1]["event_name"].split(' ')
            current_level = int(current_level[1])
            if current_level == level:
            	if(len(usersdata[i]) >= attempts_lowerbound and len(usersdata[i]) <= attempts_upperbound):
                    level_stuck_users.append(i)
                    level_stuck_users_level_attempts[i] = 1
    
    level_attempts_mod.outputListOfLevelStuckUsers(level_stuck_users, attempts_lowerbound, attempts_upperbound, level)

    '''
        based on sessions
    '''

    sessions_min = offer["no_sessions_lowerbound"]
    sessions_max = offer["no_sessions_upperbound"]
    data = findDataFromApplication('./golive/data/session_data.json', "Data")
    usersdata = findDataOfEachUser(data)
    activeUsers = []
    activeUsers_sessions = defaultdict(int)
    for sessions in range(sessions_min, sessions_max + 1):
        for i in usersdata:
            isNumSessions = based_on_sessions_mod.processDataOfUser(usersdata[i], sessions)
            if(isNumSessions):
                activeUsers.append(i)
                activeUsers_sessions[i] = 1
    # outputListOfActiveUsers(activeUsers,sessions_min,sessions_max):
    '''
        based on app-in purchases
    '''

    coins = offer["no_of_coins"]
    activeUsers_purchase = defaultdict(int)
    data = findDataFromApplication('./golive/data/app_in.json', "Data")
    usersdata = findDataOfEachUser(data)
    activeUsers = []
    for i in usersdata:
    	isCoins = based_on_app_in_purchases_mod.processDataOfUser(usersdata[i], coins)
        if(isCoins):
            activeUsers.append(i)
            activeUsers_purchase[i] = 1

    findCommonUsers(offer, activeUsers_consecutive, activeUsers_sessions, activeUsers_purchase)
