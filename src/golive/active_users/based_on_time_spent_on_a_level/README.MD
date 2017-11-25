## Task : Find the list of players who have spent more than "x" time units on a particular level "y".

# Sample JSON Object:
{
      "startTime": 1498349760,
	  "endTime" : 1498349987
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "event_name": "Level 7 attempt"
}

# Used Parameters from the JSON Object
- "start_time" implies the time in unix format when the level has started. 
- "end_time" implies the time in unix format when the level has ended. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "event_name" describes which level the user has attempted when he plays the game in a session.

# How to Run?
- To execute the file, run the command for the executable file located in the src folder.
- "python run_based_on_time_spent.py <level> <time units>"
- ex: "python run_based_on_time_spent.py  7 400"

# Output
- A new file "TimeSpentOnLevel.json" and "TimeSpentOnLevel.txt" is created in the output directory inside active_users where you can see the output.
