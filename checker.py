import requests

while(True):
    try:
        url = input("Enter a URL: ")
        response = requests.get(url, timeout = 5 )
        print(response.status_code)
        # 200 means the request was successful
    except requests.exceptions.Timeout:
        print("Request timed out. The cause is not yet known.")
    except requests.exceptions.MissingSchema:
        print("Please include https:// or http:// in the URL.") 
    except requests.exceptions.ConnectionError as error:
        print("Could not establish a connection.")
        print(error)