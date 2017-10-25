Task : Find the list of players who have failed a level "m" more than "n" times.

Sample JSON object:
{
      "eventTime": 1498349760,
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "event_name": "Level 7 Failed"
}

- "event_time" implies the time in unix format when the event has occured. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "event_name" describes whether the user has failed or cleared a particular level when he plays a game in a session.

To execute the file, run the command
"python level_attempts.py <data_file> <level> <threshold attempts>"
ex: "python level_attempts.py dummy.json 7 2"


A new file "ListOfUsersStuckAtALevel.txt" is created in the same directory which gives the list of users who have failed the level 7 more than 2 times.

