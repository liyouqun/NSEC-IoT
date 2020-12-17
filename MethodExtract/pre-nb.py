
file = open('C:/Users/51442/Desktop/PPG/MethodExtract/method.txt','r',encoding='UTF-8') 
script=file.readlines()
for line in script:
	print('nb.train("", "'+line.replace('\n','')+'")')

file.close()