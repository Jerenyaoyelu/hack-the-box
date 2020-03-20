import requests
import hashlib
from bs4 import BeautifulSoup

URI = "http://docker.hackthebox.eu:32273"
PROXIES = {}

def get_and_hash(ret):
    soup = BeautifulSoup(ret, 'html.parser')
    string = soup.h3.string.encode('utf-8')
    digest = hashlib.md5(string).hexdigest()
    return digest

session = requests.Session()
req = session.get(URI, proxies=PROXIES)
md5 = get_and_hash(req.text)
req = session.post(URI, data={"hash":md5}, proxies=PROXIES)
print(req.text)