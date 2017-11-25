## Task : Find the list of players who played exactly 'x' sessions.

# Sample JSON Object
{
            "rtime": 1509493384, 
            "eventTime": 1509518566, 
            "user_id": "1914ded8960b7ab9bf6baad20aabd9eaeb63aff0", 
            "did": "5bb06264-7fa3-4b88-942e-f33c92e5b961", 
            "mtimestamp": 1509493366495, 
            "key": "Session_Start", 
            "sid": "f2c1cc83-355d-49d9-897c-ef4a9c92deea", 
            "createdAt": 1509493384, 
            "utime": "1509493367"
}

# Used Parameters from the JSON Object
- "event_time" implies the time in unix format when the session has started. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "end_time" is the time in unix format which implies when the session has ended.

# How to Run?
- To execute the file, run the command for the executable file located in the src folder.
- "python run_based_on_sessions.py <threshold sessions>"

ex: "python transaction.py 12"

# Output
- A new file "ListOfMoneySpenders.json" and "ListOfMoneySpenders.txt" is created in the output directory inside active_users where you can see the output.

