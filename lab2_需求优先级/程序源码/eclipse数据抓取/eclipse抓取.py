import requests
from bs4 import BeautifulSoup
import time
import random

NETWORK_STATUS = True

proxy = [
    {
        'http': 'http://61.135.217.7:80',
        'https': 'http://61.135.217.7:80',
    },
{
        'http': 'http://118.114.77.47:8080',
        'https': 'http://118.114.77.47:8080',
    },
{
        'http': 'http://112.114.31.177:808',
        'https': 'http://112.114.31.177:808',
    },
{
        'http': 'http://183.159.92.117:18118',
        'https': 'http://183.159.92.117:18118',
    },
{
        'http': 'http://110.73.10.186:8123',
        'https': 'http://110.73.10.186:8123',
    },
]

useragents = [
    r'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; PE-TL20 Build/HuaweiPE-TL20) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.3 Mobile Safari/537.36',
    r'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
    r'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'
]

def req_get(target):
    try:
        a = requests.get(url=target,timeout=5)
        if a.status_code == 200: return a
    except requests.exceptions.Timeout:
        global NETWORK_STATUS
        NETWORK_STATUS = False
        if NETWORK_STATUS == False:
            while 1:
                response = requests.get(url = target, timeout=5)
                if response.status_code == 200:
                    return response



if __name__ == "__main__":
    url = "https://bugs.eclipse.org/bugs/show_bug.cgi?id="
    id = 500000
    fp = open("data1.txt", "a", encoding='utf-8')
    for id in range(512768, 515000):#change id range
        target = url + str(id)
        p = req_get(target)
        bf = BeautifulSoup(p.text, "html.parser")
        #get website info
        wa = bf.find_all('div', class_ =  "throw_error")
        if(len(wa) != 0):
            print(id, "false")
            continue
        #ensure true id
        title = bf.find_all(['div', 'span'], id = 'short_desc_nonedit_display')
        er = title[0].text
        #get request
        judge = bf.find('tr').find_all('td')
        imp = judge[11].text.replace(" ", "")
        imp = imp.replace("\n", " ")
        #get class of request
        fp.write(imp.split()[0]+" "+imp.split()[1]+" "+er+"\n")
        print(id)
        time.sleep(1)