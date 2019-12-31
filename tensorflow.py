import os

names = os.listdir("C:\\Users\\FENG ZI YAO\\Desktop\\software\\DAC2017_Training-master\\DAC2017_Training-master")
path = "C:\\Users\\FENG ZI YAO\\Desktop\\software\\DAC2017_Training-master\\DAC2017_Training-master"
s=''
a=0
b=0
for filename in names:
    s=''
    for l in open(path + "\\" +filename).readlines():
        if '//' in l:
            if(l.startswith("//")):
                continue
            l=l.split('//')[0]+'\n'
            if(l!='\n'):
                s += l
        elif '/*' in l:
            a+=1
        elif '*/' in l:
            b+=1
        elif(a==1 or b==1):
            if(a==1 and b ==1):
                a=b=0
            continue
        else:
            s += l
    f = open(path + "\\" +filename,'w')
    f.write(s)
    f.close()
    
