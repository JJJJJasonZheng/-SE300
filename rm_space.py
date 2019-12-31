import os
import random
path = r"C:\Users\FENG ZI YAO\Documents\WeChat Files\feng5539990\FileStorage\File\2019-12\dataset\dataset1"
names = os.listdir(path)

s=''

a=0
word = [" ","\n"]
for filename in names:
    print(filename)
    s=''
    for l in open(path + "\\" +filename).readlines():
        b = 0  #random.randint(0,99)
        c = random.randint(0,1)
        if(a!=b):
            s+=l
        else:
            l = l.replace(word[c],'')
            s+=l
    f = open(path + "\\" +filename,'w')
    f.write(s)
    f.close()
    
