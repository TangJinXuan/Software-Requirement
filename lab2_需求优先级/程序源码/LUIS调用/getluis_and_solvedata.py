#coding = utf-8
import requests
import time

global null
null = ''

if __name__ == "__main__":
    f = open("result01.txt", "r")
    res = {"highest":[],"high":[],"medium":[],"low":[],"lowest":[],"None":[]}
    #url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/04faf27d-f667-4bbd-8d69-1c055d1f7a46?verbose=true&timezoneOffset=0&subscription-key=64dd9a79db3d494bb140dcc25da364f5&q="
    for line in f:
        pr = line.split()
        my = pr[1]
        del pr[0]
        del pr[0]
        ce = " ".join(pr)
        res[str(my)].append(ce)
        """
        se = " ".join(pr)
        stri = url + se
        print(unicode(bugg +" "+ se,encoding = "utf-8"))
        req = requests.get(url = stri)
        if req.text == '': break
        dic = eval(req.text)
        if "topScoringIntent" not in dic.keys(): break;
        type = dic["topScoringIntent"]['intent']
        print(unicode(type,encoding = "utf-8"))
        time.sleep(1)
        
       
        f2 = open("result01.txt","ab")
        f2.write(bugg+" "+type + " " + se)
        f2.write('\n')
        f1.close()
        f2.close()
        """
    f.close()
    f1 = open("result1.txt", "w")
    for key in res:
        f1.write(key + ":")
        f1.write(str(len(res[key])))
        f1.write('\n')
        for i in res[key]:
            f1.write(i)
            f1.write("\n")
    f1.close()
    #print("result:"+str(x))
    #for key in res:
        #print(key, ":" , len(res[key]))
