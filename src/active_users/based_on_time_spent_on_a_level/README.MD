Task : Find the list of players who have spent more than "x" time units on a particular level "y".

Sample JSON object:
{
      "startTime": 1498349760,
	  "endTime" : 1498349987
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "event_name": "Level 7 attempt"
}

- "start_time" implies the time in unix format when the level has started. 
- "end_time" implies the time in unix format when the level has ended. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "event_name" describes which level the user has attempted when he plays the game in a session.

To execute the file, run the command
"python time_spent_level.py <session_data> <level> <time units>"
ex: "python time_spent_level.py dummy.json 7 400"


A new file "ListOfActiveUsers.txt" is created in the same directory which gives the list of users who have spent more than 400 time units on Level 7.

