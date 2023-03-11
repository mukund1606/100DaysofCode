"""
# API Endpoint
eg: api.coinbase.com

# API Request -> request we make to the API
eg: What are the current prices of Bitcoin and Ethereum?
    This is a GET request

# API Response -> response we get from the API
eg: Bitcoin is $10,000 and Ethereum is $500
    This is a JSON response

    
# API Parameters -> Data we can send to the API to customize the response
eg: What are the current prices of Bitcoin and Ethereum in Euros?
    This is a GET request with a parameter

## Working with Responses

# Response Code -> Tells us if the request was successful
# 1XX -> Informational Response
# 2XX -> Successful
# 3XX -> Go somewhere else
# 4XX -> You messed up
# 5XX -> Server messed up



# Make a GET request to the API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# if response.status_code == 404:
#     raise Exception("The resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to make this request.")

# Instead of checking the status code, we can use the raise_for_status() method

# response.raise_for_status()


# data = response.json()


# print(data["iss_position"])
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)
"""
