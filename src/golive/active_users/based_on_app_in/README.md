##Task : Find the list of players who have spent more than "x" coins in character unlocks.

# Sample JSON Object
{
            "rtime": 1509516199, 
            "eventTime": 1509535994, 
            "user_id": "28c2ec07bfd8c543fcce53925ab0994f6ebeaa0d", 
            "did": "d7c67cd7-abc1-48a5-8301-b82dbfd1196c", 
            "mtimestamp": 1509516194454, 
            "key": "CharacterUnlockCount", 
            "sid": "4f355d8a-4d9d-437b-a094-1d76323f46be", 
            "attributes": {
                "PlayerId": "c1d6e4f3bda088ea167e357b6d7d2174", 
                "NoOfCoins": "210", 
                "Level": "1", 
                "characterID": "bala", 
                "TimeOfEvent": "11_01_2017 11:33:14"
            }, 
            "segment": {
                "PlayerId": "c1d6e4f3bda088ea167e357b6d7d2174", 
                "NoOfCoins": "210", 
                "Level": "1", 
                "characterID": "Bala", 
                "TimeOfEvent": "11_01_2017 11:33:14"
            }, 
            "createdAt": 1509516199, 
            "utime": "1509516194"
}

# Used Parameters from the JSON Object.
- "user_id" describes the id of the user.
- "NoOfCoins" describes the coins spent on inapp purchases.

# How to Run?
- To execute the file, run the command for the executable file located in the src folder.
- "python run_based_on_app_in_purchases.py <no of coins>"
- ex: "python run_based_on_app_in_purchases.py 400"

# Output
- A new file "ListOfAppInPurchasers.json" and "ListOfAppInPurchasers.txt" is created in the output directory inside active_users where you can see the output.