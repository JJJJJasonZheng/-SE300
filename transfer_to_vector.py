f = open("C.txt","r+")
worddict = {}
for line in f.readlines():
    line  = line.replace('\n','')
    line = line.split('\t')
    worddict[line[0]]=int(line[1])
f.close()
worddict[' ']=0
worddict['\n']=111
worddict['\t']=112
print(worddict)
print()
#f = open("closeHashTable.cpp", 'r', True)
atrlist = {'\n':1, ' ':1, '{':1, '}':1, '(':1, ')':1, '[':1, ']':1, ';':1, '#':1, ',':1,
          '+':2, '-':2, '*':2, '/':2, '=':2, '>':2, '<':2, '!':2, '^':2, '&':2, '%':2,          
          }

f = open('test.txt', 'r', True)
wordlist = []
#first character
ch = f.read(1)
if ch not in atrlist:
    atr0 = 3
else:
    atr0 = atrlist[ch]
word = ch
atr = 0;
vector = []
length = 112

while True:
    ch = f.read(1)
    #赋值attribute
    if (ch == ''):
        break
    if ch not in atrlist:
        atr = 3
    else:
        atr = atrlist[ch]
    #判断是否为必须独立出现的字符
    if (atr == 1): 
        wordlist.append(word)
        if word in worddict:
            vector.append(worddict[word])
        else:
            length = length + 1
            worddict[word] = length
            vector.append(worddict[word])
            #vector.append(111)
        atr0 = atr
        word = ch
        continue
    #判断是否与前一个字符attribute相同
    if (atr == atr0):
        word = word + ch
        atr0 = atr
        continue
    if (atr != atr0):
        wordlist.append(word)
        if word in worddict:
            vector.append(worddict[word])
        else:
            length = length + 1
            worddict[word] = length
            vector.append(worddict[word])
            #vector.append(111)
        atr0 = atr
        word = ch
#print(len(vector))
print(vector)
print()
#print(len(wordlist))
print(wordlist)
print()
#print(len(worddict))
print(worddict)
print()
f.close()