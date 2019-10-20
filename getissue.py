
import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
import io
import sys
import openpyxl
 
record=[]
x = 4226

def gettitle(page):
	try:
		global record
		#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='UTF-8')
		url="https://github.com/microsoft/vscode/issues?page="+str(page)+"&q=is%3Aissue+is%3Aopen"
		data = urllib2.urlopen(url).read()
		z_data = data.decode('UTF-8')
		soup = BeautifulSoup(z_data, 'lxml')
		a = soup.select('a.link-gray-dark.v-align-middle')
		b = soup.select('span.opened-by')
		c = soup.select('relative-time')
		test = soup.select('div.float-left.col-8.lh-condensed.p-2')
		#hostsfile = open('record.txt', 'w', newline='',encoding='UTF-8')
		for i in range(1,len(b)):
			temp=[]
			temp.append(a[i - 1].get_text())
			temp.append("opened")
			temp.append(c[i].attrs['datetime'])
			z=""
			for j in test[i - 1].select('a.d-inline-block.IssueLabel.v-align-text-top'):
				z+=j.get_text()+'/'
			temp.append(z)
			#sn=b[i].get_text().replace(" ","").split('\n')[1].replace("#","").replace("\n","")
			m = re.search('\d+',b[i].get_text())
			temp.append(getdata(m.group(0)))
			record.append(temp)
		#hostsfile.close()
		print(u'hosts刷新成功:',len(a))
		with open("issue.json",'ab+') as fp:
		    json.dump(record,fp=fp,ensure_ascii = True,indent = 4,sort_keys = False)
		record =[]
	except Exception as err:
		print(err)

def getdata(sn):
	value=""
	try:
		url="https://github.com/microsoft/vscode/issues/"+str(sn)
		data = urllib2.urlopen(url).read()
		z_data = data.decode('UTF-8')
		soup = BeautifulSoup(z_data, 'lxml')
		a = soup.select('table > tbody > tr > td')
		#hostsfile = open('record.txt', 'w', newline='')
		for i in a:
			value=value+i.get_text()+ "\n\r"
			#hostsfile.write(value)
		#hostsfile.close()
		#print('hosts刷新成功:',len(a))
	except Exception as err:
		print(str(err))
	global x
	print(u"第"+str(x)+u"条抓取完成")
	x += 1
	return value

if __name__=="__main__":
		gettitle(175)
		print(u"第"+str(i)+u"页抓取完成")
