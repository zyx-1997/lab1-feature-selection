from nltk.stem.porter import *
import re

words = []
# r = re.compile(r"[,!\*\.]")

with open("test.txt", "r", encoding='utf-8') as f:
    # for line in f:
    #     for word in r.sub("",line.strip()).split(" "):
    #         if word in words:
    #             words[word] += 1
    #         words.setdefault(word,1)
    for line in f:
        line = re.sub(r"[0-9]+", " ", line)
        word1 = re.sub(r"([^A-Za-z\s])+", "", line.strip()).split()
        for word in word1:
            word = word.lower()
            words.append(word)
            # if word in words:
            #     words[word] += 1
            # words.setdefault(word, 1)

stopwords = open(r"stopwords.txt", 'r')
s = set()
for stopword in stopwords:
    stopword = stopword.replace('\n', '')
    s.add(stopword)

# for key in list(words.keys()):
#     if set(key).issubset(stopword):
#            del words[key]


# TOO SLOW TO RUN THE PROGRAM
# for key in words:#Remove the stopwords
#     key=key.split()
#     if set(key).issubset(s):
#         key=''.join(key)
#         words.remove(key)

# x=-1
# Words=words
# for m in words:
#     x+=1
#     if m in s:
#         Words.pop(x)
#         x-=1
#
# words=Words
stopwords.close()

# print(words)
# print(len(words))

# stemmer = PorterStemmer()#remove the word suffix
# singles = [stemmer.stem(plural) for plural in words]
# print(singles)


word_count = {}  # word count
for word2 in words:
    if word2 in word_count:
        word_count[word2] += 1
    word_count.setdefault(word2, 1)

# for word2,count in word_count.items():
#     print(word2,count)

index = []#to rmove the low-frequency words
for key, value in word_count.items():
    if value < 5:
        index.append(key)

for key1 in index:
    del word_count[key1]

for word2, count in word_count.items():
    print(word2, count)
