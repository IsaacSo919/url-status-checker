import requests


        
def describe_status_code(status_code):
    if status_code == 200:
        return "OK: The request was successful."
    elif status_code == 404:
        return "Not Found: The requested resource could not be found."
    elif status_code == 500:
        return "Internal Server Error: The server encountered an error."
    else:
        return f"Status code {status_code}: No description available."
    
def main():
    try:
        url = input("Enter a URL: ")
        response = requests.get(url, timeout = 5 )
        print(f"Final URL: {response.url}")
        print(f"Redirect count: {len(response.history)}")
        print (f"Status Code: {response.status_code}")
        print (f"Description: {describe_status_code(response.status_code)}")
    except requests.exceptions.Timeout:
        print("Request timed out. The cause is not yet known.")
    except requests.exceptions.MissingSchema:
        print("Please include https:// or http:// in the URL.") 
    except requests.exceptions.ConnectionError as error:
        print("Could not establish a connection.")
        print(error)
    except requests.exceptions.InvalidURL:
        print("Invalid URL. Enter a complete URL, such as https://example.com.")

if __name__ == "__main__":
    main()
        
