from gensim.models import word2vec
# 用 word2vec 进行训练
sentences=word2vec.Text8Corpus(u'traindata2.txt')
# 第一个参数是训练语料，第二个参数是小于该数的单词会被剔除，默认值为5, 第三个参数是神经网络的隐藏层单元数，默认为100
model=word2vec.Word2Vec(sentences,min_count=1, size=50, window=5, workers=4)
file =open("traindata2.txt","r");
# wt=open("changed_code_open.txt","w");
text=file.read();
res=[];
count=0;
title=0;
code=0;
record=0;
maxchange=0;
frequency = {}
for word in text.split():
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1
#print(frequency)
for ti in range (1,100):
    temp=0;
    test=open("D:/Mashiro's works/大三上/Software-Requirement/lab3_需求变更/open_res/"+str(ti)+".txt","r")
    #test=open("D:/Mashiro's works/大三上/Software-Requirement/lab3_需求变更/open_res/99.txt","r")
    line = test.readline()             # 调用文件的 readline()方法
#    print(ti)
    count=0;
    for word in line.split():
        if count!=0:
            if word in frequency:
                title = title + model.similarity(word, u'Git')
            else:
                title = title + 0.5
        else:
            code = int(word)
        count=count+1
    count=count-1
    title = title / count
    # print(title)
    line = test.readline()
    line = test.readline()
    changed=0
    print("wenjian:"+str(ti))
    while line:
        #print("hang:"+str(temp))
        temp=temp+1
        #print(line)                 # 后面跟 ',' 将忽略换行符
        # print(line, end = '')　　　# 在 Python 3中使用
        line=test.readline()
        count=0
        point=0;
        for word in line.split():
            if word in frequency:
                point=point+model.similarity(word,u'Git')
            # else:
            #     point=point+0.5
            count=count+1
        if(count!=0):
            point=point/count
        else:
            point=title;
      #  print(point)
        #catag=max(point,key=point.get())
        line = test.readline()
        if (point-title)>0.3:
            changed=changed+1
        else:
            if (point-title)<-0.3:
                changed=changed+1
        # print(point-title)
        # print(changed)
    if changed>5:
        print(code)
        if(changed>maxchange):
            maxchange=changed
            record=ti
        # wt.write(str(code)+'\n')
        wt1=open("D:/Mashiro's works/大三上/Software-Requirement/lab3_需求变更/open_change/issue"+str(code)+".txt","w");
        temp=0;
        wt1.write("issue:")
        test.seek(0)
        line=test.readline()
        #print(line)
        wt1.write(line)
        line=test.readline()
        #print(line)
        wt1.write("Time:"+line+"\n")
        while line:
            line = test.readline()
            count = 0
            for word in line.split():
                if count==0:
                    wt1.write("Commenter:"+word+" ")
                else:
                    wt1.write("Time:"+word+"\n")
                # else:
                #     point=point+0.5
                count = count + 1
            # catag=max(point,key=point.get())
            line = test.readline()
            for word in line.split():
                if word in frequency:
                    point = point + model.similarity(word, u'Git')
                # else:
                #     point=point+0.5
                count = count + 1
            if (count != 0):
                point = point / count
            else:
                point = title;
            #  print(point)
            # catag=max(point,key=point.get())
            if (point - title) > 0.3:
                wt1.write("Requirement changed context\n")
            else:
                if (point - title) < -0.3:
                    wt1.write("Requirement changed context\n")
            wt1.write("Comment Context:"+line+"\n")
        wt1.close()
# wt.close()
print(record)
    #print(result)