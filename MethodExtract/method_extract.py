import os
import re
#所在文件路径

method=[]
counter=[]
i=0

file_path = os.listdir('C:/Users/51442/Desktop/PPG/results/SourceCode/Official')
for files in file_path:
	file = open('C:/Users/51442/Desktop/PPG/results/SourceCode/Official/' + files,'r',encoding='UTF-8') 
	script=file.readlines()
	for line in script:
		if line[0:4]=='def ' and line.find('(')>0:
			name=line[line.find(' ')+1:line.find('(')]
			if name!='':
				if name not in method:
					method.append(name)
					counter.insert(i,1)
					i=i+1
				else:
					counter[method.index(name)]+=1
	file.close()

file_path = os.listdir('C:/Users/51442/Desktop/PPG/results/SourceCode/ThirdParty')
for files in file_path:
	file = open('C:/Users/51442/Desktop/PPG/results/SourceCode/ThirdParty/' + files,'r',encoding='UTF-8') 
	script=file.readlines()
	for line in script:
		if line[0:4]=='def ' and line.find('(')>0:
			name=line[line.find(' ')+1:line.find('(')]
			if name!='':
				if name not in method:
					method.append(name)
					counter.insert(i,1)
					i=i+1
				else:
					counter[method.index(name)]+=1
	file.close()

for k in range(0,i):
	print(method[k],counter[k])
