from urllib import response
import requests
import json
from bs4 import BeautifulSoup
from pyuseragents import random as random_useragent
from random import randint
from time import time, ctime
#from requests import requests

session = requests.Session()

def Convert(string):
    li = list(string.split(" "))
    return li



count=0
print(" BIGGEST DICK  - https://t.me/Straus_loveYou - BIGGEST DICK ")
ref_code = input("Enter your ref code - ")
ref_amount = input("Enter request amount of refferalls - ")

def get_new_mails():
    url = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    responce = session.get(url)
    mails = responce.text
    mails = Convert(mails)



    url = f"https://www.1secmail.com/api/v1/?action=getDomainList"
    responce = session.get(url)
    domains = responce.text
    
    return mails, domains

def send_response(url,mail):
    
    """print(type(mail))
    user = f'{"email":{mail}}'
    params = f'{"event":"registration","user":{user}}'
    post_ans = f'{"apiToken":"OB9kRs4qNUVSuncX4S80G93tp5s","params":{params}}'"""
    mail = mail[2:]
    i = len(mail) - 2
    mail = mail[:i]
    #post_ans = {"apiToken":"OB9kRs4qNUVSuncX4S80G93tp5s","params":{"event":"registration","user":{"email":mail},"referrer":{"referralCode":ref_code},"refSource":"copy"}}
    post_ans = {"apiToken":"OB9kRs4qNUVSuncX4S80G93tp5s","params":{"event":"registration","user":{"email":mail},"referrer":{"referralCode":ref_code},"refSource":"copy"}}
    #post_ans = {'apiToken':'OB9kRs4qNUVSuncX4S80G93tp5s','params':{'event':'registration','user':{'email':'zh9jpe@esiix.com'},'referrer':{'referralCode':'cun6ztl'},'refSource':'copy'}}
    print(post_ans)
    
    #print(session.options("https://app.viral-loops.com/api/v2/events").json)

    responce = session.post(url, json=post_ans)
    #print("Cookie is - ", session.cookies)
    #print(responce)
    return responce

def get_message_info(mail):
    mail=str(mail)
    mail = mail.split('"')[1]

    domain = mail.split('@')[-1]

    login = mail.split('@')[0]

    print(mail)
    #print(login)
    #print(domain)
    url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={str(login)}&domain={str(domain)}'
    #print(url)

    responce = session.get(url)
    messages = json.loads(responce.text)
    print("Waiting for email message")
    while True:
        try:
            message_id = messages[-1] 
            break
        except:
            responce = session.get(url)
            messages = json.loads(responce.text)
        

    #print(messages)
       
    print("Recieved the message")
    #print(message_id)
    message_id = message_id["id"]
    
    url = f'https://www.1secmail.com/api/v1/?action=readMessage&login={str(login)}&domain={str(domain)}&id={int(float(message_id))}'
    #print(url)
    responce = session.get(url)
    message_text = responce.text
    json_data = json.loads(message_text)
    message_text = json_data["body"]


    soup = BeautifulSoup(message_text, "lxml")

    message_link = soup.find('a', href=True)
    message_link = message_link['href']
    print(message_link)

    t = time()
    time_now = ctime(t)
    new_line = f"{time_now} - {message_link}"
    

    filename = 'recheck.json'
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        #print(type(file_data))
        file_data["links"].append(new_line)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)




    return message_link
    #message_text = message_text["a"]




def main():
    count=0
    mails, domains = get_new_mails()
    

    url = "https://app.viral-loops.com/api/v2/events"

    #print(mails)
    #print(domains)

    for i in range(len(mails)):

        #print(i)

        #proxy_auth = str(randint(1, 0x7fffffff)) + ':' + str(randint(1, 0x7fffffff))
        #proxies = {'http': 'socks5://{}@localhost:9150'.format(proxy_auth), 'https': 'socks5://{}@localhost:9150'.format(proxy_auth)}

        #session.proxies.update(proxies)
        session.headers.update({'user-agent': random_useragent(), 'Accept': '*/*', 'Accept-Language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7', 'Origin': 'https://https://ultimate.money/', 'Referer': 'https://https://ultimate.money/'})


        mail = mails[i]
        #print("mail is here")
        #print(mails[i])
        #print("mail is here")
        response = send_response(url,mail)
        #print("every this is OK")
        json_data = json.loads(response.text)

        #print(json_data)
        #print(type(json_data))
        #print(json_data["dt"])
        
        try:
            json_data["email"]
            trust = 1
            
        except:
            #print("we are losers")
            trust=0 
            main()
        
        if trust == 1:

            
            
            #printlogin = len(mail)-len(domain)-1
            #login = mail[:login]

            link = get_message_info(mail)

            
            responce = session.get(link)
            

            count += 1  
            #print(f"account - {count} - completed")

            i=i+1
            

        ##print("Mail{}: {} - {}".format(count, mail, ans))


def extra_main():
    for i in range(int(ref_amount)):
        
        main()
        
    print("COMPLETED")


if __name__ == "__main__":
    extra_main()


    

