import requests


r = requests.get("http://www.apple.com")
print(r.status_code)
