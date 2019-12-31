

def getWordDict():
    f = open("C.txt","r+")
    wordDict = {}
    for line in f.readlines():
        line  = line.replace('\n','')
        line = line.split('\t')
        wordDict[line[0]]=int(line[1])
    f.close()
    wordDict[' ']=0
    wordDict['\n']=111
    wordDict['\t']=112

    wordDict = {k:(v+4) for k,v in wordDict.items()}
    wordDict["<PAD>"] = 0
    wordDict["<START>"] = 1
    wordDict["<UNK>"] = 2  # unknown
    wordDict["<UNUSED>"] = 3

    return wordDict

def code2Vect(path, wordDict, atrlist):
    f = open(path , 'r', True)

    wordlist = []
    #first character
    ch = f.read(1)
    if ch not in atrlist:
        atr0 = 3
    else:
        atr0 = atrlist[ch]
    word = ch
    atr = 0
    vector = []
    length = 116

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
            if word in wordDict:
                vector.append(wordDict[word])
            else:
                length = length + 1
                wordDict[word] = length
                vector.append(wordDict[word])
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
            if word in wordDict:
                vector.append(wordDict[word])
            else:
                length = length + 1
                wordDict[word] = length
                vector.append(wordDict[word])
                #vector.append(111)
            atr0 = atr
            word = ch

    f.close()

    return vector

