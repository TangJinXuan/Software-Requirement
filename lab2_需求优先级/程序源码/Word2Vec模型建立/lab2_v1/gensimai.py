from gensim.models import word2vec
# 用 word2vec 进行训练
sentences=word2vec.Text8Corpus(u'traindata1.txt')
# 第一个参数是训练语料，第二个参数是小于该数的单词会被剔除，默认值为5, 第三个参数是神经网络的隐藏层单元数，默认为100
model=word2vec.Word2Vec(sentences,min_count=1, size=50, window=5, workers=4)
file =open("traindata1.txt","r");
text=file.read();
fn=open('normal.txt','w')
fb=open('blocker.txt','w')
fma=open('major.txt','w')
fmi=open('minor.txt','w')
fe=open('enhancement.txt','w')
res=[];
frequency = {}
for word in text.split():
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1
#print(frequency)
test=open("traindata1.txt","r")
line = test.readline()             # 调用文件的 readline()方法
correct={'normal':0, 'major':0,'blocker':0,'minor':0,'enhancement':0};
all={'normal':0, 'major':0,'blocker':0,'minor':0,'enhancement':0};
while line:
    #print(line)                 # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    point={'normal':0, 'major':0,'blocker':0,'minor':0,'enhancement':0};
    for word in line.split():
        if word in frequency:
            if word!="ctrl":
                point['normal']=point['normal']+model.similarity(word,u'normal')
                point['major']=point['major']+model.similarity(word,u'major')
                point['blocker']=point['blocker']+model.similarity(word,u'blocker')
                point['minor']=point['minor']+model.similarity(word,u'minor')
                point['enhancement']=point['enhancement']+model.similarity(word,u'enhancement')

    for key, value in point.items():
        if (value == max(point.values())):
            print(key)

            if(line.startswith("normal")):
                all['normal']=all['normal']+1
                if key=="normal":
                    correct['normal']=correct['normal']+1
            else:
                if(line.startswith("major")):
                    all['major']=all['major']+1
                    if key=="major":
                        correct['major']=correct['major']+1
                else:
                    if (line.startswith("blocker")):
                        all['blocker']=all['blocker']+1
                        if key == "blocker":
                            correct['blocker'] = correct['blocker'] + 1
                    else:
                        if (line.startswith("minor")):
                            all['minor'] = all['minor'] + 1
                            if key == "minor":
                                correct['minor'] = correct['minor'] + 1
                        else:
                            if (line.startswith("enhancement")):
                                all['enhancement'] = all['enhancement'] + 1
                                if key == "enhancement":
                                    correct['enhancement'] = correct['enhancement'] + 1

            if key == "normal":
                fn.write(line+'\n')
            else:
                if key == "major":
                    fma.write(line+'\n')
                else:
                    if key == "blocker":
                        fb.write(line+'\n')
                    else:
                        if key == "minor":
                            fmi.write(line+'\n')
                        else:
                            if key == "enhancement":
                                fe.write(line+'\n')
            break
    #catag=max(point,key=point.get())
    line = test.readline()
#print(result)
print(correct)
print(all)
fn.write("all:"+str(all['normal'])+"  correct:"+str(correct['normal']))
fb.write("all:"+str(all['blocker'])+"  correct:"+str(correct['blocker']))
fe.write("all:"+str(all['enhancement'])+"  correct:"+str(correct['enhancement']))
fma.write("all:"+str(all['major'])+"  correct:"+str(correct['major']))
fmi.write("all:"+str(all['minor'])+"  correct:"+str(correct['minor']))
fn.close()
fb.close()
fe.close()
fmi.close()
fma.close()