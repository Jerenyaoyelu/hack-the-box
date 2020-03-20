import requests
import hashlib

URI = "http://docker.hackthebox.eu:32321"
PROXIES = {}

password = 'leonardo'

session = requests.Session()
req = session.get(URI, proxies=PROXIES)
data = password.encode('utf-8')
req = session.post(URI, data={"password": data}, proxies=PROXIES)
print(req.text)