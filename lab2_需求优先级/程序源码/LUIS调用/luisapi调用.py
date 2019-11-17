import requests
import time

global null
null = ''
headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
NETWORK_STATUS = True

def req_get(target):
    try:
        a = requests.get(url=target, headers = headers)
        if a.status_code == 200: return a
    except requests.exceptions.Timeout:
        global NETWORK_STATUS
        NETWORK_STATUS = False
        if NETWORK_STATUS == False:
            while 1:
                response = requests.get(url = target, headers = headers)
                if response.status_code == 200:
                    return response

if __name__ == "__main__":
    f = open("data02.txt", "r", encoding="UTF-8")
    f2 = open("result2.txt", "a")
    all_test = 867
    right_test = 355
    url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/c0589fc7-63b7-4636-851c-8c2751a05a47?verbose=true&timezoneOffset=0&subscription-key=68bb9abef95d4211a3f2265455ca550b&q="
    for line in f:
        l = line.split(" ", 2)
        stri = url + l[2]
        print(l[2])
        req = req_get(stri)
        if req.text == '': break
        dic = eval(req.text)
        if "topScoringIntent" not in dic.keys(): break;
        type = dic["topScoringIntent"]['intent']
        print(type)
        all_test = all_test + 1
        if type == "highest" and (l[1] == "blocker" or l[1] == "critical"): right_test = right_test + 1
        elif type == "high" and l[1] == "major": right_test += 1
        elif type == "medium" and l[1] == "normal": right_test += 1
        elif type == "low" and l[1] == "minor": right_test += 1
        elif type == "lowest" and (l[1] == "enhancement" or l[1] == "trivial"): right_test += 1

        f2.write(type + " " + l[2])

        print(all_test, right_test)

        time.sleep(1)
    print("result:")
    f1 = open("result3.txt", "w")
    for key in res:
        print(key, ":" , len(res[key]))
        f1.write(key + ":")
        f1.write(str(len(res[key])))
        f1.write('\n')
        for i in res[key]:f1.write(i)
        f1.write("\n")
