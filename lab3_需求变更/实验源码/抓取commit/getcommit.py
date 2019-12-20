import requests
import time
import json
import re
import codecs
false = False
null = 0

f = codecs.open("D:\coding\soft_req_lab3\git1.txt", "a+", "utf-8")

class getcommit:
    reconnect=0
    ids = []
    def __init__(self):
        self.reconnect=0

    def getIndex(self, filename):
        fp = open(filename, "r")
        fp.readline()
        for line in fp:
            line=line.replace("\n","")
            self.ids.append(line)

    def judge(self, str):
        for a in re.findall(r"#\d+", str):
            a=a.replace("#", "")
            if a in self.ids: return a
        return ""

    def compare_time(self, t1, t2):
        tl1 = re.findall("\d+", t1)
        tl2 = re.findall("\d+", t2)
        for i in range(0, 6):
            if tl1[i]>tl2[i]:return 1
            elif tl1[i]<tl2[i]:return -1
        return 0

    def insert_issue(self, author, date, num, title):
        f = open("D:\coding\soft_req_lab3\open_change\issue"+num+".txt", "a+")
        f.write("\nCommenter:"+author+" Time:"+date+"\n")
        f.write("Commit Context:"+title+"\n")

    def getStackData(self,urlpath:str,present_num:int):
        head = {
            'Authorization': 'token a8127eae009a6361a0e4648a8a551febc4349797',
        }
        for i in range(1,9):
            #print("https://api.github.com/repos/"+urlpath+"commits?page="+str(present_num))
            r = requests.get("https://api.github.com/repos/"+urlpath+"commits?page="+str(present_num),headers=head)
            #print(r.status_code)
            if r.status_code==200:
                break
            else:
                print("%d页获取失败，错误码%d，正在进行第%d次重连，请稍后"%(present_num,r.status_code,i))
                d=2**i
                time.sleep(10*d)
        json_response=r.content.decode()
        dict_json=json.loads(json_response)
        if dict_json:
            print("len",len(dict_json))
            for i in range(1, len(dict_json)+1):
                title = dict_json[i-1]["commit"]["message"]
                if "key" not in title and "ssh" not in title and "password" not in title: continue
                print("find: "+title)
                if "login" in dict_json[i-1]["author"].keys():
                    author = dict_json[i-1]["author"]["login"]
                elif "name" in dict_json[i-1]["author"].keys():
                    author = dict_json[i-1]["author"]["name"]
                date = dict_json[i-1]["commit"]["committer"]["date"]

                for j in range(1, 9):
                    r1 = requests.get(dict_json[i-1]["url"], headers = head)
                    if r1.status_code == 200:
                        break
                    else:
                        print("%d页获取失败，错误码%d，正在进行第%d次重连，请稍后" % (i - 1, r1.status_code, i))
                        d = 2 ** j
                        time.sleep(10 * d)
                json_response1 = r1.content.decode()
                dict_json1 = json.loads(json_response1)
                files = dict_json1["files"]
                for k in range(1, len(files)+1):
                    print("page %d, commit %d, file %d"%(present_num, i, k))
                    if "patch" not in files[k-1].keys() or "filename" not in files[k-1].keys():continue
                    code = files[k-1]["patch"]
                    file_name = files[k-1]["filename"]
                    f.write("author:"+author)
                    f.write("\n")
                    f.write("date:"+date)
                    f.write("\n")
                    f.write("title:"+title)
                    f.write("\n")
                    f.write("filename:"+file_name)
                    f.write("\n")
                    f.write("code:\n")
                    f.write(code)
                    f.write("\n")
                    f.write("\n")
            return True
        else:
            return False 
        