#modify the IR

f=open('StaticCode.txt')
script=f.readlines()
result=''
#print(script)
for i in range(0,len(script)):
	line=script[i][:-1]
	#print(line)
	#line=script.readline()
	if line.isspace() or line=='':
		continue
	if line.find('log.')>=0:
		continue
	if line.find('//')>=0:
		continue
	line=line.replace('public ','def ')
	line=line.replace('private ','def ')
	line=line.replace('this.','')
	line=line.replace('java.lang.Object ','')

	if line.find('subscribe')>=0 :
		if line.count(',')==2:
			if line.count('.')>0:
				val1=line[line.find('(')+1:line.find(',')]+'.'+line[line.find(',')+1:line.find('.')]
				val2=line[line.find('.')+1:line.rfind(',')]
				val3=line[line.rfind(',')+2:line.rfind(')')]+'(evt)'
				line='if('+val1+'=='+val2+') \n    '+val3
			else:
				val1=line[line.find('(')+1:line.find(',')]
				val2=line[line.find(',')+1:line.rfind(',')]
				val3=line[line.rfind(',')+2:line.rfind(')')]+'(evt)'
				line='if('+val1+'=='+val2+') \n    '+val3
		else :
			if line.count(',')==1:
				val1=line[line.find('(')+1:line.find(',')]
				val2=line[line.rfind(',')+2:line.rfind(')')]
				line=line+'\n'+'if('+val1+'=='+val2+')\n     '+val2+'()'


	if line.find('?')>0 and line.find(':')>0:
		condition=line[line.find('=')+2:line.find('?')-1]
		#print(condition)
		val1=line[line.find('?')+2:line.find(':')-1]
		val2=line[line.find(':')+2:]
		val=(line[:line.find('=')-1]).replace(' ','')
		line='    if ('+condition+') \n        '+val+' = '+val1+'\n    else \n        '+val+' = '+val2+'\n'
		#print(line)
	if line.find('[')>0 and line.find(':')>0:
		value=line[line.find(':')+2:line.find(']')-1]
		#print(value)
		pre=line[:line.find('[')]
		#print(pre)
		back=line[line.find(']')+1:]
		line=pre+' '+value+' '+back


	result=result+line+'\n'

	#print(line)
f.close()
print(result)