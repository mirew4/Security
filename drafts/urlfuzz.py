# URL FUZZING TOOL
# usage: 'cat $wordlist | python3 urlfuzz.py'
import requests
import sys

# REPLACE WITH YOUR IP
ip = "10.10.10.10"
port = "80"

# Check for response
response = requests.get(url=f"http://{ip}:{port}")
# Check for 200 status code:
if response.status_code != 200:
    print("URL NOT FOUND")
    # exit program with a code of 1
    sys.exit(1)

def fuzzloop():
    print("[*] BEGIN URL FUZZING")
    for word in sys.stdin:
        response = requests.get(f"http://{ip}:{port}/{word}")
        if response.status_code == 404:
           continue
        else:
            print(f"[+] URL FOUND: /{word}")
            print(f"JSON: " + response.json())
            print("STATUS CODE: " + response.status_code)

fuzzloop()