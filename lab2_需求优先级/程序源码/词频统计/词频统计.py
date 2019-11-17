import json
import re

if __name__ == "__main__":
    f = open("data1.txt", "r", encoding="ISO-8859-1")
    wc1 = {}
    wc2 = {}
    wc3 = {}
    wc4 = {}
    wc5 = {}
    maxword = 20
    count = 0
    nowords = ("in", "on", "for", "to", "", "to", "is", "the", "a", "if", "not", "when", "and", "from", "only", "dont","before","after","with", "of", "be", "are", "cannot", "does", "down", "an", "as", "no", "out", "could", "should", "shall", "very", "will", "would", "about", "its", "first", "too", "also", "do", "some", "below", "at", "by", "this", "that", "it", "can", "doesnt", "during", "all", "or", "into", "have", "has", "had", "via")
    for line in f:
        count += 1
        for ch in line:
            if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
                line = line.replace(ch, "")
        k = line.split(" ", 2)
        words = k[2].split()
        for word in words:
            word = word.lower()
            if word.isdigit(): continue
            if word not in nowords:
                if k[1] == "blocker" or k[1] == "critical":
                    if word in wc1:
                        wc1[word] += 1
                    else:
                        wc1[word] = 1
                elif k[1] == "major":
                    if word in wc2:
                        wc2[word] += 1
                    else:
                        wc2[word] = 1
                elif k[1] == "normal":
                    if word in wc3:
                        wc3[word] += 1
                    else:
                        wc3[word] = 1
                elif k[1] == "minor":
                    if word in wc4:
                        wc4[word] += 1
                    else:
                        wc4[word] = 1
                elif k[1] == "trivial" or k[1] == "enhancement":
                    if word in wc5:
                        wc5[word] += 1
                    else:
                        wc5[word] = 1
    pre_items1 = list(wc1.items())
    items1 = [[x, y] for (y, x) in pre_items1]
    items1 = [(x, y) for (x, y) in items1 if x > 10]
    items1.sort(reverse = 1)
    pre_items2 = list(wc2.items())
    items2 = [[x, y] for (y, x) in pre_items2]
    items2 = [(x, y) for (x, y) in items2 if x > 10]
    items2.sort(reverse = 1)
    pre_items3 = list(wc3.items())
    items3 = [[x, y] for (y, x) in pre_items3]
    items3 = [(x, y) for (x, y) in items3 if x > 10]
    items3.sort(reverse = 1)
    pre_items4 = list(wc4.items())
    items4 = [[x, y] for (y, x) in pre_items4]
    items4 = [(x, y) for (x, y) in items4 if x > 10]
    items4.sort(reverse = 1)
    pre_items5 = list(wc5.items())
    items5 = [[x, y] for (y, x) in pre_items5]
    items5 = [(x, y) for (x, y) in items5 if x > 10]
    items5.sort(reverse = 1)
    f1 = open("result.txt", "w")
    f1.write("count:" + str(count) + "\n")
    f1.write("\n")
    f1.write("highest" + "\n")
    for key, value in items1:
        f1.write(str(key) + ":" + str(value) + "\n")
    f1.write("\n")
    f1.write("high" + "\n")
    for key, value in items2:
        f1.write(str(key) + ":" + str(value) + "\n")
    f1.write("\n")
    f1.write("medium" + "\n")
    for key, value in items3:
        f1.write(str(key) + ":" + str(value) + "\n")
    f1.write("\n")
    f1.write("low" + "\n")
    for key, value in items4:
        f1.write(str(key) + ":" + str(value) + "\n")
    f1.write("\n")
    f1.write("lowest" + "\n")
    for key, value in items5:
        f1.write(str(key) + ":" + str(value) + "\n")
