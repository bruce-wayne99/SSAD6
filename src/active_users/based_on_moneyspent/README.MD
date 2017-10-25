Task : Find the list of players who have spent more than a threshold amount in a period of time.

Sample JSON object:
{
      "eventTime": 1498349760,
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "key": "Transaction",
      "transaction_amount": 10
}

- "event_time" implies the time in unix format when the event has occured. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "transaaction_amount" is the amount the user has spent to buy an offer.

To execute the file,run the command
"python transaction.py <data_file> <threshold amount>"

ex: "python transaction.py dummy.json 12"


A new file "ListOfActiveUsers.txt" is created in the same directory which gives the list of users who have spent atleast "n" units of money.

