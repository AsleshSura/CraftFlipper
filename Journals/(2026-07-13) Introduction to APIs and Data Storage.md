Hey y'all, Welcome to my first Journal Entry!

The Journal folder is where I'll try to keep track of all the work and changes I've implemented during the day and update whatever I've learned from my work today.

# Learning
1. APIs: I learned how to query GET requests to the Hypixel Skyblock API through Python's requests package and understood how API calls work, types of responses, and how to traverse and identity necessary data (such as timestamps)

2. Data Storage: I learned how to work with Python's os module to create and store data collected from the API requests within custom folders and files.

# Features and Updates
I mainly worked on setting up the repo and [BazaarRequests.py](..\BazaarRequests.py) today.

1. The BazaarRequest() function within [BazaarRequests.py](..\BazaarRequests.py) executes an API request to the [Bazaar Endpoint](https://api.hypixel.net/v2/skyblock/bazaar) to capture a snapshot of the entire Hypixel Skyblock Bazaar as stored in the Hypixel's cache. This response is then converted and returned it the user in json format. This function takes about .8 ± .1 second to compute.

2. The DataStorage(data) function within [BazaarRequests.py](..\BazaarRequests.py) accepts data from BazaarRequest() to store collected data in an orderly fashion. Using the "lastUpdated" field of the data, the function creates a brand new folder for each day under the Data folder; the date folder is formatted as YYYY-MM-DD. Within this folder, the function stores the data in individual files for each instance; the files are labelled based on the time of data collection in a HH-MM-SS format. This function takes about .8 ± .02 second to compute.

3. The ClearStorage() function within [BazaarRequests.py](..\BazaarRequests.py) completely wipes the Data folder, ensuring no date folders exist. This function aids in removing all captured data after our work is complete.