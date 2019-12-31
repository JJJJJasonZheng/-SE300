import os
import subprocess
import random

path = './dataset'
filename = os.listdir(path)
for file in filename:
	line = random.randint(20,40)
	#print(str(line))
	cmd = 'split -l ' + str(line) + ' ' + path + '/' + file + ' ' + path + '/' + file +'_temp'
	#print(cmd)
	subprocess.call(cmd, shell = True)