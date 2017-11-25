## Task : Find the list of players who have spent more than a threshold amount in a period of time.

# Sample JSON Object
{
      "eventTime": 1498349760,
      "user_id": "3622beb0bcc4d0eb9fcff3c95931f631d998e8a8",
      "key": "Transaction",
      "transaction_amount": 10
}

# Used Parameters from the JSON Object
- "event_time" implies the time in unix format when the event has occured. 
- "user_id" is the unique "id" of the user who is playing in this session.
- "transaction_amount" is the amount the user has spent to buy an offer.

# How to Run?
- To execute the file, run the command for the executable file located in the src folder.
- "python run_transaction.py <threshold amount>"

ex: "python transaction.py 12"

# Output
- A new file "ListOfMoneySpenders.json" and "ListOfMoneySpenders.txt" is created in the output directory inside active_users where you can see the output.

