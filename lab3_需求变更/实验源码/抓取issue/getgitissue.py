#coding=UTF-8
import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
import io
import sys
import openpyxl
import time
 
record=[]
head = {
         'Authorization': 'token 4c4c0896206a479d54cc115958cc52ac47778bbf'
}
x = 1
def gettitle(page):
	try:
		global record
		#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8')
		url="https://github.com/microsoft/vscode/issues?page="+str(page)+"&q=is%3Aissue+is%3Aclosed+label%3Agit"
		req = urllib2.Request(url=url,headers = head)
		response = urllib2.urlopen(req)
		data = response.read()
		z_data = data.decode('UTF-8')
		soup = BeautifulSoup(z_data, 'lxml')
		a = soup.select('a.link-gray-dark.v-align-middle')
		b = soup.select('span.opened-by')
		c = soup.select('relative-time')
		test = soup.select('div.float-left.col-8.lh-condensed.p-2')
		#hostsfile = open('record.txt', 'w', newline='',encoding='UTF-8')
		for i in range(1,len(b)+1):
			temp=[]
			#sn=b[i].get_text().replace(" ","").split('\n')[1].replace("#","").replace("\n","")
			m = re.search(r'\d+',b[i - 1].get_text())
			temp.append(m.group(0)+" "+a[i - 1].get_text())
			temp.append(c[i - 1].attrs['datetime'])
			getdata(temp,m.group(0))
			record.append(temp)
			with open(str(x-1)+".json",'ab+') as fp:
				json.dump(record,fp=fp,ensure_ascii = True,indent = 4,sort_keys = False)
			record =[]
		time.sleep(1)
		#print(u'hosts刷新成功:',len(a))
	except Exception as err:
		print(err)

def getdata(record,sn):
	try:
		url="https://github.com/microsoft/vscode/issues/"+str(sn)
		req = urllib2.Request(url=url,headers = head)
		response = urllib2.urlopen(req)
		data = response.read()
		#data = urllib2.urlopen(url).read()
		z_data = data.decode('UTF-8')
		soup = BeautifulSoup(z_data, 'lxml')
		a = soup.select('table > tbody > tr > td')
		b = soup.select('div > h3 > strong')
		c = soup.select('h3 > a > relative-time')
		#hostsfile = open('record.txt', 'w', newline='')
		for i in range(1,len(a)+1):
			record.append(b[i-1].get_text()+" "+c[i-1].attrs['datetime'])
			record.append(a[i-1].get_text())
			#hostsfile.write(value)
		#hostsfile.close()
		#print('hosts刷新成功:',len(a))
	except Exception as err:
		print(str(err))
	global x
	print(u"第"+str(x)+u"条抓取完成")
	x += 1

if __name__=="__main__":
    for i in range(1,65):
        gettitle(i)
        print(u"第"+str(i)+u"页抓取完成")
