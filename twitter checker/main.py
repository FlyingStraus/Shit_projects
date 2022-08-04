import requests
from bs4 import BeautifulSoup as bs



base_url = "https://coinsguru.io/twitter/"


input_file = open('twitters.txt', "r")
output_file = open("ans.txt","w")

twitters_list = input_file.readlines()



print("Best proger is - @Straus_fm\n")
print("By the way he has a channel :)")
print("https://t.me/Straus_loveYou\n")
print("Working...")
for twitter in twitters_list:
    
    twitter = str(twitter).split("https://twitter.com/")
    twitter = str(twitter[1])
    twitter = twitter.strip('\n')
    print(f"Checking - {twitter}")

    url = str(base_url) + str(twitter) + "/"

    responce = requests.get(url)  

    if responce.status_code == 200:

        soup = bs(responce.text, 'html.parser')

        score = soup.find_all("div", {"class": "progress"})
        score = score[0]['data-target']

        info = f"{twitter} - {score}\n"

        output_file.writelines(info)
    
    else:
        print("Something wrong with score checker website")
        print(responce)
        print(url)

print("My work was done")

