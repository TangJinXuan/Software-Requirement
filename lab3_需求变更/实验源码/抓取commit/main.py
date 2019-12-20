from getcommit import *
from saveFile import  *
import time
import io
import sys

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
stackcap=getcommit()
present_num = 790
urlpath="microsoft/vscode/"
while True:
    judge=stackcap.getStackData(urlpath,present_num)
    #dict2json("./","res_"+str(present_num)+"_data.json",data)
    if judge:
        present_num=present_num+1
        print("page",present_num)
    else:
        break;
