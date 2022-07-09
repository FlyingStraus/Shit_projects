from urllib import response
import requests
import json
from bs4 import BeautifulSoup
from pyuseragents import random as random_useragent
from random import randint


session = requests.Session()
proxy_auth = str(randint(1, 0x7fffffff)) + ':' + str(randint(1, 0x7fffffff))
proxies = {'http': 'socks5://{}@localhost:9150'.format(proxy_auth), 'https': 'socks5://{}@localhost:9150'.format(proxy_auth)}

session.proxies.update(proxies)
session.headers.update({'user-agent': random_useragent(), 'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7', 'Origin': 'https://https://ultimate.money/', 'Referer': 'https://https://ultimate.money/'})



url = 'https://www.1secmail.com/api/v1/?action=readMessage&login=qlsh42t9y&domain=bheps.com&id=234589161'
print(url)
responce = session.get(url)
message_text = responce.text
json_data = json.loads(message_text)
message_text = json_data["body"]


soup = BeautifulSoup(message_text, "lxml")

print(soup.find('a', href=True)):
    print("Found the URL:", a['href'])
#print(soup.find_all("a"))

#print(message_link['href'])







"""mail = ["bjqz7c@vddaz.com"]
#domain = mail.split('@')[-1]
domain = mail[2:]
#login = mail.split('@')[0]
login = mail[:-2]
print(mail.replace('["', ''))
print(mail[2:])
url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={str(login)}&domain={str(domain)}'
print(url)
responce = session.get(url)
messages = json.loads(responce.text)
print(messages)
message_id = messages[-1]  
message_id = message_id["i"""


"""#print(session.headers)
url = "https://app.viral-loops.com/api/v2/events"
#post_ans = {"apiToken":"OB9kRs4qNUVSuncX4S80G93tp5s","params":{"event":"registration","user":{"email":{"zh9jpe@esiix.com"}},"referrer":{"referralCode":{"cun6ztl"}},"refSource":"copy"}}
post_ans = {"apiToken":"OB9kRs4qNUVSuncX4S80G93tp5s","params":{"event":"registration","user":{"email":"alamarqw1e@gmail.com"},"referrer":{"referralCode":"cun6ztl"}}}
#print(post_ans)

#rint(session.options("https://app.viral-loops.com/api/v2/events").json)

responce = session.post(url, json=post_ans)
print(responce.text)
"""






