import os
import os.path
import codecs
import re

list=[]
words={}

def read_file(path,list):
    file_list=os.listdir(path)
    for file_name in file_list:
        path2=os.path.join(path,file_name)
        if os.path.isdir(path2):
            read_file(path2,list)
        else:
            f = codecs.open(path2, 'r', encoding='Latin1')
            # with open(path2,'r',encoding='utf-8',errors='ignore') as f:
            file_data=f.read()
            list.append(file_data)
            f.close()

# def count(txt):
#      for line in txt:
#          line = re.sub(r"[0-9]+", " ", line)
#          word1 = re.sub(r"([^A-Za-z\s])+", "", line.strip()).split()
#      for word in word1:
#          word = word.lower()
#          if word in words:
#              words[word] += 1
#          words.setdefault(word, 1)



path='D:\\lab1-feature-selection\\20news-bydate'
read_file(path,list)
list='\n'.join(list)
length=len(list.splitlines())
print(list)
print(length)

with open("test.txt", "w",encoding='utf-8') as f:
    f.write(list) #Merge all files into one txt file called text.txt
# with open("test.txt", "r",encoding='utf-8') as f:
#     count(f)
# print(words)