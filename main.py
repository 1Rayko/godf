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
while 1:
    url = genurl()
    r = requests.get(url)
    if r.status_code == 404:# бляха-муха какой код (200 в любом случае возвращается)
        print("\033[33m"+url)
    #  else:
    #      print("Невалид "+ url  )
