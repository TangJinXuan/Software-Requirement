import requests
import time

global null
null = ''

if __name__ == "__main__":
    f = open("data2.txt", "r")
    res = {"编译功能": [], "文件管理": [], "编辑功能": [], "扩展功能": [], "界面设计": [], "软件稳定性": [], "None": []}
    url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/94061432-57a3-4b87-a324-b28ee89c70b7?verbose=true&timezoneOffset=0&subscription-key=ca809b20854840d5b54119abf235177a&q="
    for line in f:
        stri = url + line
        print(line)
        req = requests.get(url = stri)
        print(req)
        if req.text == '': break
        dic = eval(req.text)
        if "topScoringIntent" not in dic.keys(): break;
        type = dic["topScoringIntent"]['intent']
        print(type)
        res[type].append(line)
        time.sleep(1)
    print("result:")
    f1 = open("result2.txt", "w")
    for key in res:
        print(key, ":" , len(res[key]))
        f1.write(key + ":")
        f1.write(str(len(res[key])))
        f1.write('\n')
        for i in res[key]:f1.write(i)
        f1.write("\n")
