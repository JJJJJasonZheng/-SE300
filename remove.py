import os

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.py':  
                L.append(os.path.join(root, file))  
    return L  

names = file_name("C:\\Users\\FENG ZI YAO\\Desktop\\software")
s=''
a=0
for filename in names:
    for l in open(filename).readlines():
        if '#'in l:
            l=l.split('#')[0]+'\n'
            if(l!='\n'):
                s+=l
        elif '"""' in l:
            a+=1
        elif(a==1 or a==2):
            if(a==2):
                a=0
            continue
        else:
            s += l
    
f = open(filename,'w')
f.write(s)
f.close()
