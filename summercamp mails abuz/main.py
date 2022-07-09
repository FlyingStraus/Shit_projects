import requests
#from requests import requests



with open('mails.txt') as f:
    Lines = f.readlines()
count=0
print(" BIGGEST DICK  - https://t.me/Straus_loveYou - BIGGEST DICK ")
for line in Lines:
    count += 1
    mail = line.strip()
    url = f'https://solana.us17.list-manage.com/subscribe/post-json?u=dc5b8a6eb6dc3d737579c03c9&id=a43a9eb2ad&EMAIL={mail}&c=__jp2'
    responce = requests.get(url)
    ans = "completed"
    print("Mail{}: {} - {}".format(count, mail, ans))
    