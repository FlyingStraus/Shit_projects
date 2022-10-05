import requests
from bs4 import BeautifulSoup as bs
import time




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

        #Getting score

        soup = bs(responce.text, 'html.parser')

        score = soup.find_all("div", {"class": "progress"})
        score = score[0]['data-target']

        #Getting followers
        #getting ID
        btn = soup.find_all("button", {"id": "nav-friends-list-tab"})
        
        code = btn[0]['onclick']
        code = code.split("'")
        code = code[1]

        

        #Getting list of followers
        page_start_poz = 0
        project_name = twitter
        project_id = code
        url = "https://coinsguru.io/followedByList/ajax/?"
        data = f"draw=1&columns%5B0%5D%5Bdata%5D=&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=description&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=project_score&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=4&order%5B0%5D%5Bdir%5D=desc&start={page_start_poz}&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false&slug={project_name}&username={project_name}&twitter_id={project_id}&categoryName=All&tagName=All&_={time.time()}"
        url = url+data
        list_followers= []
        try:
            responce = requests.get(url)
            responce = responce.json()


            followers = responce['data']
            
            for item in followers[:10]:
                list_followers.append(f' {item["profile_username"]} - {item["project_score"]}')
        except:
            list_followers = "No top guys followed"

        

        info = f"{twitter} - {score} - {list_followers}\n"
        output_file.writelines(info)


    else:
        info = f"{twitter} - Not found\n"
        output_file.writelines(info)
    

print("My work was done")
