Task : Find the list of players have played the game atleast n consecutive days in a row.

Sample JSON object:
{
      "eventTime": 1498349760,
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "end_time": "1498329960"
}

- "event_time" implies the time in unix format when the session has started. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "end_time" is the time in unix format which implies when the session has ended.

To run the file run the command
"python based_on_days.py <session_data_file> <consecutive days>"
ex: "python based_on_days.py session_data.json 7" 


A new file "ListOfActiveUsers.txt" is created in the same directory which gives the list of users who have played the game atleast "n" consecutive days in a row.
