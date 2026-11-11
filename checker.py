import requests

try:
    url = input("Enter a URL: ")
    response = requests.get(url, timeout = 5 )
    print(response.status_code)
    # 200 means the request was successful
except requests.exceptions.Timeout:
    print("Request timed out. The cause is not yet known.")