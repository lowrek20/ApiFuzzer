import requests
import sys

def loop():
    for word in sys.stdin:
        word = word.strip()  # Remove any surrounding whitespace/newlines
        url = f"enter your url here!"
        
        try:
            res = requests.get(url)
            res.raise_for_status()  # Raise an error for bad status codes
            
            # Try to parse JSON data
            try:
                data = res.json()
                print(data)
            except ValueError:
                print(f"Response is not in JSON format: {res.text}")
        
        except requests.exceptions.HTTPError as http_err:
            if res.status_code == 404:
                print(f"Resource not found: {url}")
                continue  # Skip to the next word
            else:
                print(f"HTTP error occurred: {http_err}")
        
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")

loop()
