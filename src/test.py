import requests
import random
import string
import json

def randomStringOfLenN(n):
    return ''.join(random.choice(string.lowercase) for x in range(n))

url = "http://127.0.0.1:8000/test.php"
url = "http://127.0.0.1:8084/test.php"

payload = randomStringOfLenN(20000)

response = requests.request("POST", url, data=payload)

print(response.text)

responseParsed = json.loads(response.text)

print("{}, expected: {}, real: {}".format(
        responseParsed['success'],
        responseParsed['expectedContentLength'],
        responseParsed['realContentLength']
))
