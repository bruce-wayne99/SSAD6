## Task : Find the list of players who have failed a level "m" more than "n" times.

# Sample JSON Object
{
      "eventTime": 1498349760,
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "event_name": "Level 7 Failed"
}

# Used Parameters from the JSON Object
- "event_time" implies the time in unix format when the event has occured. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "event_name" describes whether the user has failed or cleared a particular level when he plays a game in a session.

# How to Run?
- To execute the file, run the command for the executable file located in the src folder.
"python run_level_attempts.py <threshold lower_bound_attempts> <threshold upper_bound_attempts>"
ex: "python level_attempts.py 7 2 5"

# Output
- A new file "ListOfUsersStuckAtALevel.json" and "ListOfUsersStuckAtALevel.txt" is created in the output directory inside active_users where you can see the output.

