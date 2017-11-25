##Task : Find the list of players have played the game atleast n consecutive days in a row.

# Sample JSON Object
{
      "eventTime": 1498349760,
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "end_time": "1498329960"
}

# Used Parameters from the JSON Object
- "event_time" implies the time in unix format when the session has started. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "end_time" is the time in unix format which implies when the session has ended.

# How to Run?
- To execute the file, run the command for the executable file located in the src folder.
"python run_based_on_days.py <consecutive days>"
ex: "python based_on_days.py days_data.json 7" 

# Output
- A new file "ListOfActiveUsers.json" and "ListOfActiveUsers.txt" is created in the output directory inside active_users where you can see the output.