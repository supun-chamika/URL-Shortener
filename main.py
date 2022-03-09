import requests

# enter the API key got from Cuttly
API_key = "insert your API key here"

# get the URL you want to shorten
URL = input('Enter The URL: ')

# preferred name in the URL
API_URL = f"https://cutt.ly/api/api.php?key={API_key}&short={URL}"

# make the request
data = requests.get(API_URL).json()["url"]

if data["status"] == 7:
    short_URL = data["shortLink"]
    print("Short URL: ", short_URL)
else:
    print('[!] error shortening URL:', data)
