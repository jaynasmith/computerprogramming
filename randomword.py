import random
words = []
with open('sowpods.txt','r') as f:
    line = f.readline()
    words.append(line)
    while line:
        line = f.readline()
        words.append(line)
print(random.choice(words))