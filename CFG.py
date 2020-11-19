#coding:utf-8

f = open('D:/project/browser/PreCFG.txt','r',encoding = 'utf-8')
script=f.readlines()
#print(script)
#fo=open('cap.txt','w')
nodes=[]
MethodNode=[]
BlockFirstLine=[]
MethodNodeName=[]
MethodCall=[]
IfStatement=[]
IfStatementBlock=[]
Block=[]
Path=[]
nodelist=[]
hasline=0


def num_set_list():
    sort_list = []
    for i in sorted(set(BlockFirstLine)):
        sort_list.append(i)
    return sort_list

def AddMethodCallToBlock():
	for i in range(0,len(MethodCall)):
		lev=nodes[MethodCall[i]]['level']
		j=MethodCall[i]+1
		flag=0
		thisnum=nodes[MethodCall[i]]
		while nodes[j]['level']>lev:
			if nodes[j]['name']=='Constant':
				start=nodes[j]['value'].find('-')+1
				end=nodes[j]['value'].find(':')-1
				CallName=nodes[j]['value'][start:end]
				#print(CallName)
				if CallName in MethodNodeName:
					thisnum=MethodCall[i]
					callname=CallName
					returnnum=-1
					methodnode={'thisnum':thisnum,'callname':callname,'returnnum':returnnum}
					MethodNode.append(methodnode)
					BlockFirstLine.append(MethodCall[i])
					flag=1
					break
				else:
					nodes[MethodCall[i]]['name']='APICall'
					break
			j=j+1
		if flag:
			while nodes[j]['level']>lev:
				j=j+1
			if nodes[j]['name']=='RightChild' or nodes[j]['name']=='EmptyStatement':
				k=j+1
				while nodes[k]['level']>=nodes[j]['level']:
					k=k+1
				if nodes[k]['level']>3:
					MethodNode[len(MethodNode)-1]['returnnum']=k

					BlockFirstLine.append(k)
			else:
				if nodes[j]['level']>3:
					MethodNode[len(MethodNode)-1]['returnnum']=j

					BlockFirstLine.append(j)
	return

def AddIfStatementToBlock():
	for i in range(0,len(IfStatement)):
		lev=nodes[IfStatement[i]]['level']
		j=IfStatement[i]+1
		flag=0
		for k in range(0,len(IfStatementBlock)):
			if nodes[IfStatement[k]]['num']==nodes[IfStatement[i]]['num']:
				order=k
				break
		while flag<=4:
			if j>=len(nodes)-1:
				IfStatementBlock[order]['end']=j
				if nodes[j]['level']>3:
					BlockFirstLine.append(j)
				break
			if nodes[j]['level']==lev+1:
				flag=flag+1
				if flag==2:
					BlockFirstLine.append(j)
					nodes[j]['name']='LeftChild'
					IfStatementBlock[order]['left']=j
				if flag==3 and nodes[j]['name']!='EmptyStatement':
					BlockFirstLine.append(j)
					nodes[j]['name']='RightChild'
					IfStatementBlock[order]['right']=j
			if nodes[j]['level']<=lev:
				flag=flag+1
				IfStatementBlock[order]['end']=j-1
				if nodes[j]['level']>3:
					BlockFirstLine.append(j)
			j=j+1

	return

def BuildTheBlock():
	num=0
	#print(BlockFirstLine)
	for i in range(0,len(BlockFirstLine)-1):
		block_start=BlockFirstLine[i]
		block_end=BlockFirstLine[i+1]-1
		block={'num':num,'start':block_start,'end':block_end}
		Block.append(block)
		#print(block)
		num=num+1
	block_start=BlockFirstLine[len(BlockFirstLine)-1]
	block_end=len(nodes)-1
	block={'num':num,'start':block_start,'end':block_end}
	Block.append(block)
	return

#通过行数确定在哪个block
def FindBlockByNum(num):
	for i in Block:
		if i['start']<=num and i['end']>=num:
			return i['num']
	return 0

def FindBlockByName(name):
	for i in Block:
		if nodes[i['start']]['value']==name:
			return i['start']
	return 0

def FindReturn(num):
	returnlist=[]
	i=num+1
	flag=0
	while nodes[i]['level']>3 and i<(len(nodes)-1):
		if nodes[i]['name']=='ReturnStatement':
			flag=1
			returnlist.append(FindBlockByNum(i))
		i=i+1
	if flag==0:
		returnlist.append(FindBlockByNum(num))
	#print(returnlist)
	return returnlist

def MatchIfBlock():
	for i in IfStatementBlock:
		in_block=FindBlockByNum(i['num'])
		out_block=FindBlockByNum(i['left'])
		path={'in':in_block,'out':out_block}
		Path.append(path)
		if i['right']>0:
			out_block=FindBlockByNum(i['right'])
			path={'in':in_block,'out':out_block}
			Path.append(path)


			if nodes[Block[FindBlockByNum(i['right'])-1]['start']]['name']!='MethodCall':
				in_block=FindBlockByNum(i['right'])-1
				j=i['right']+1
				if i['right']>=len(nodes)-1:
					break
				while nodes[j]['level']>nodes[i['right']]['level'] and j<=len(nodes)-2:
					j=j+1
				if nodes[j]['level']>3:
					out_block=FindBlockByNum(j)
					path={'in':in_block,'out':out_block}
					Path.append(path)

			j=i['right']+1
			while nodes[j]['level']>nodes[i['right']]['level'] and j<=len(nodes)-2:
				j=j+1
			if nodes[j]['level']>3 and nodes[Block[FindBlockByNum(j)-1]['start']]['name']!='MethodCall':
				out_block=FindBlockByNum(j)
				path={'in':out_block-1,'out':out_block}
				Path.append(path)

		if i['right']==0:
			j=i['left']+1
			while ((nodes[j]['level']>nodes[i['left']]['level']) or (nodes[j]['name']=='EmptyStatement')) and (j<i['end']):
					j=j+1
			if nodes[j]['level']>3 and nodes[Block[FindBlockByNum(j-1)]['start']]['name']!='MethodCall':
				out_block=FindBlockByNum(j)
				in_block=out_block-1
				path={'in':in_block,'out':out_block}
				Path.append(path)
	return

def MatchCallBlock():
	for i in MethodNode:
		in_block=FindBlockByNum(i['thisnum'])
		out_block=FindBlockByNum(FindBlockByName(i['callname']))
		path={'in':in_block,'out':out_block}
		Path.append(path)
		if i['returnnum']<0:
			continue
		for j in FindReturn(FindBlockByName(i['callname'])):
			in_block=j
			out_block=FindBlockByNum(i['returnnum'])
			path={'in':in_block,'out':out_block}
			Path.append(path)
	return

def MatchOtherBlock():
	for i in range(1,len(Block)):
		if (nodes[Block[i]['start']]['name']=='IfStatement' or nodes[Block[i]['start']]['name']=='MethodCall') and nodes[Block[i-1]['start']]['name']!='MethodCall':
			in_block=i-1
			out_block=i
			path={'in':in_block,'out':out_block}
			Path.append(path)
			#print(path)
	return


for i in range(0,len(script)):
	line=script[i][:-1]
	#print(line)
	#line=script.readline()
	if line.isspace() or line=='':
		break
	num=line.split(' ')[0]
	level=line.split(' ')[1]
	name=line.split(' ')[2]
	start=len(num+level+name)+5
	num=i
	level=int(level)
	value=line[start:]
	obj={'num':num,'level':level,'name':name,'value':value}
	nodes.append(obj)
	#print(obj)
	if name=='MethodNode':
		BlockFirstLine.append(num)
		MethodNodeName.append(value)
	if name=='MethodCall':
		MethodCall.append(num)
	if name=='IfStatement':
		ifblock={'num':num,'left':0,'right':0}
		IfStatementBlock.append(ifblock)
		BlockFirstLine.append(num)
		IfStatement.append(num)
	#i=i+1
f.close()
#将If语句划分成块



AddIfStatementToBlock()
#将调用划分成块，程序内的函数调用名为MethodCall，程序外的函数调用为APICall
AddMethodCallToBlock()
#print(BlockFirstLine)

#block去重排序，划分block
BlockFirstLine=num_set_list()

BuildTheBlock()

#分别连接三类block，形成CFG，存储进Path

#print(IfStatementBlock)

MatchIfBlock()
MatchCallBlock()
MatchOtherBlock()
source=[]
worklist=[]
InputVar=[]

for i in range(0,Block[0]['end']):
	if nodes[i]['name']=='APICall':
		if nodes[i]['value'].find('this.subscribe')>=0:
			#print(nodes[i]['value'])
			namestart=nodes[i]['value'].rfind(',')+2
			nameend=nodes[i]['value'].rfind(')')
			entryname=nodes[i]['value'][namestart:nameend]
			out_block=FindBlockByNum(FindBlockByName(entryname))
			in_block=0
			path={'in':in_block,'out':out_block}
			Path.append(path)
		if nodes[i]['value'].find('this.input')>=0:
			valname=nodes[i]['value'][nodes[i]['value'].find(',')+2:nodes[i]['value'].rfind(',')]
			#print(valname)
			device=nodes[i]['value'][nodes[i]['value'].rfind('.')+1:nodes[i]['value'].rfind(')')]
			#print(device)
			typee=nodes[i]['value'][nodes[i]['value'].find(':')+1:nodes[i]['value'].find(']')]
			#print(typee)
			if typee=='device':
				api={'Gnum':0,'valname':valname,'device':device,'command':'input','type':typee}
			else:
				typee=nodes[i]['value'][nodes[i]['value'].rfind(',')+2:nodes[i]['value'].rfind(')')]
				api={'Gnum':0,'valname':valname,'device':'none','command':'input','type':typee}
			source.append(api)
			id={'Gnum':0,'valname':valname}
			worklist.append(id)
			InputVar.append(valname)

#污染源API
sourceAPI=['source','latestValue','input','getContactBookEnabled','getCurrentMode','getId','getHubs','getLatitude','getLongitude','getMode','setMode','getTimeZone','getZipCode','getLocationId','getLocation','getManufacturerName'',getModeName','getName','getSupportedAttributes','getSupportedCommands','hasAttribute','hasCapability','hasCommand','getFirmwareVersionString','getId','getLocalIP','getLocalSrvPortTCP','getDataType','getValues','getType','getZigbeeId','getZigbeeEui','events','eventsBetween','eventsSince','getCapabilities','getDeviceNetworkId','getDisplayName','getHub','getLabel','getLastActivity','getManufacturerName','getModelName','latestState','statesSince','getArguments','getDateValue','getDescriptionText','getDoubleValue','getFloatValue','getIntegerValue','getJsonValue','getLastUpdated','getLongValue','getName','getNumberValue','getNumericValue','getUnit','getValue','getData','getDate','getDescription','getDevice','getDisplayName','getDeviceId','getIsoDate','getSource','getXyzValue','isPhysical','isStateChange','isDigital','currentState','currentValue','getStatus']
SourceDevice=['thermostat','Acceleration Sensor','Actuator','Air Conditioner Mode','Air Quality Sensor','Alarm','Audio Mute','Audio Notification','Audio Track Data','Audio Volume','Battery','Beacon','Bridge','Bulb','Button','Carbon Dioxide Measurement','Carbon Monoxide Detector','Color Control','Color Temperature','Color','Color Mode','Configuration','Consumable','Contact Sensor','Demand Response Load Control','Dishwasher Mode','Dishwasher Operating State','Door Control','Dryer Mode','Dryer Operating State','Dust Sensor','Energy Meter','Estimated Time Of Arrival','Execute','Fan Speed','Filter Status','Garage Door Control','Geolocation','Holdable Button','Illuminance Measurement','Image Capture','Indicator','Infrared Level','Light','Lock Only','Lock','Media Controller','Media Input Source','Media Playback Repeat','Media Playback Shuffle','Media Playback','Media Presets','Media Track Control','Momentary','Motion Sensor','Music Player','Notification','Odor Sensor','Outlet','Oven Mode','Oven Operating State','Oven Setpoint','pH Measurement','Polling','Power Consumption Report','Power Meter','Power Source','Presence Sensor','Rapid Cooling','Refresh','Refrigeration Setpoint','Relative Humidity Measurement','Relay Switch','Robot Cleaner Cleaning Mode','Robot Cleaner Movement','Robot Cleaner Turbo Mode','Sensor','Shock Sensor','Signal Strength','Sleep Sensor','Smoke Detector','Sound Pressure Level','Sound Sensor','Speech Recognition','Speech Synthesis','Step Sensor','Switch Level','Switch','Tamper Alert','Temperature Measurement','Thermostat Cooling Setpoint','Thermostat Fan Mode','Thermostat Heating Setpoint','Thermostat Mode','Thermostat Operating State','Thermostat Setpoint','Thermostat','Three Axis','Timed Session','Tone','Touch Sensor','Tv Channel','Ultraviolet Index','Valve','Video Clips','Video Stream','Voltage Measurement','Washer Mode','Washer Operating State','Water Sensor','Window Shade']


#####################################以上完成CFG，以下待完成

#这几个东西的定义见saint的paper，后向追踪改前向


done=[]
dep=[]

CallMap=[]
#G=nx.DiGraph()
#G.add_edge()
#通过sourceAPI[]寻找污染源变量，并存进worklist里，包括变量所在的block:Gnum，和变量valname

def ifIfBlock(num):
	result=0
	for i in IfStatementBlock:
		if num>= i['num'] and num<i['left']:
			return 1
	return 0

def ifExistingPath(entry,exit):
	global hasline
	global nodelist
	#print(entry,exit)
	#print(hasline)

	if entry==exit or hasline>0:
		hasline=1
		return 1

	if entry not in nodelist:
			nodelist.append(entry)
			#print(nodelist)
	else:
		return 0

	for i in dep:
		if i['in']==entry:
			ifExistingPath(i['out'],exit)

	return hasline


def IfInOneMethod(a,b):
	if a['Gnum']==0:
		return 1
	if b['Gnum']==0:
		return 2
	if a['Gnum']<b['Gnum']:
		start=Block[a['Gnum']]['start']
		end=Block[b['Gnum']]['end']
		result=1
	else:
		start=Block[b['Gnum']]['start']
		end=Block[a['Gnum']]['end']
		result=2
	for j in IfStatementBlock:
		if (start>=j['left'] and start<j['right'] and end>=j['right'] and end<=j['end']) or (start>=j['num'] and start<j['left']):
			return 0
	for i in range(start+1,end):
		if nodes[i]['name']=='MethodNode':
			return 0


	return result


def FindSource():
	for i in range(0,len(nodes)):
		if nodes[i]['name']=='APICall' and ifIfBlock(i)==0:
			start=nodes[i]['value'].find('-')+1
			end=nodes[i]['value'].find('.')
			callthis=nodes[i]['value'][start:end]
			start=nodes[i]['value'].find('.')+1
			end=nodes[i]['value'].find('(')
			callthat=nodes[i]['value'][start:end]
			#print(callthis)
			#print(callthat)
			#if callthis=='this' and callthat in sourceAPI:
			if callthis in SourceDevice or callthat in sourceAPI:
				lev=nodes[i]['level']
				j=i-1
				while nodes[j]['level']>lev or nodes[j]['name']=='Variable':
					j=j-1
				if nodes[j]['name']=='Binary' or nodes[j]['name']=='Declaration':
					start=nodes[j+1]['value'].find('-')+1
					end=nodes[j+1]['value'].find(':')-1
					valname=nodes[j+1]['value'][start:end]
					id={'Gnum':FindBlockByNum(j),'valname':valname}
					if callthis!='this':
						for m in source:
							if m['valname']==callthis:
								callthis=m['device']
								api={'Gnum':FindBlockByNum(j),'valname':valname,'device':callthis,'command':callthat,'type':'api'}
								break
					else:
						api={'Gnum':FindBlockByNum(j),'valname':valname,'device':none,'command':callthat,'type':'api'}
					
					if id not in worklist:
						source.append(api)
						#source.append(id)
						worklist.append(id)
					depend={'in':id,'out':id}
					if depend not in dep:
						dep.append(depend)
		if nodes[i]['name']=='Variable':
			start=nodes[i]['value'].find('-')+1
			end=nodes[i]['value'].find(':')-1
			valname=nodes[i]['value'][start:end]
			if valname in InputVar:
				id={'Gnum':FindBlockByNum(i),'valname':valname}
				if id not in worklist:
					worklist.append(id)
				tempin={'Gnum':0,'valname':valname}
				depend={'in':tempin,'out':id}
				if depend not in dep:
					dep.append(depend)

	return

#寻找id在路径中为其他值赋值
def TaintTrace(id):
	#print(Block[id['Gnum']]['start'])
	#print(Block[id['Gnum']]['end'])
	num=Block[id['Gnum']]['start']
	while num>=Block[id['Gnum']]['start'] and num<=Block[id['Gnum']]['end']:
		if (nodes[num]['name']=='Binary' or nodes[num]['name']=='Declaration') and ifIfBlock(num)==0:
			ifFind=0
			j=num+2
			#print(j)
			#ifLeftVal=0
			#print(num)
			while nodes[j]['level']>=nodes[num]['level'] and j<=len(nodes)-2:
				if nodes[j]['name']=='Variable' and ifFind==0:
					start=nodes[j]['value'].find('-')+1
					end=nodes[j]['value'].find(':')-1
					valname=nodes[j]['value'][start:end]
					if valname==id['valname']:#找到右值
						#print(j)
						#print(j,valname)
						ifFind=1
						i=num+1#连接右值左值
						start_=nodes[i]['value'].find('-')+1
						end_=nodes[i]['value'].find(':')-1
						valname_=nodes[i]['value'][start_:end_]
						ids={'Gnum':FindBlockByNum(i),'valname':valname_}
						if valname_!=id['valname']:
							if ids not in worklist:
								worklist.append(ids)
							depend={'in':{'Gnum':FindBlockByNum(j),'valname':id['valname']},'out':ids}
							if depend not in dep:
								dep.append(depend)
								
								#G.add_edge(id['valname'],ids['valname'])
								#print('&&&&&&',depend)
						
						i=j
						#print(i)
						#print('##########')
						while nodes[i]['level']<=nodes[i+1]['level']:
							#print(i,j)
							if nodes[i]['name']=='MethodCall':
								#print(nodes[i]['value'])
								count=0
								#print(i,j)
								for temp in range(i,j+1):
									#print(temp)
									if nodes[i]['level']==nodes[temp]['level']-2:
										count=count+1
								#print(count)
								start__=nodes[i]['value'].find('.')+1
								end__=nodes[i]['value'].find('(')
								valname__=nodes[i]['value'][start__:end__]
								#print(valname__)
								#print(FindBlockByName(valname__))
								#for k in range(FindBlockByName(valname__),)
								k=FindBlockByName(valname__)
								#print(k)
								counter=0
								while nodes[k]['name']!='Parameter' or counter!=count:
									k=k+1
									if nodes[k]['name']=='Parameter':
										counter=counter+1
								ids={'Gnum':FindBlockByNum(k),'valname':nodes[k]['value']}
								if valname__!=id['valname']:
									if ids not in worklist:
										worklist.append(ids)
									depend={'in':{'Gnum':FindBlockByNum(i),'valname':id['valname']},'out':ids}
									if depend not in dep:
										dep.append(depend)

										
										#G.add_edge(id['valname'],ids['valname'])
										#print(depend)
								CallMapVar={'Gnum':FindBlockByNum(i),'valname':id['valname']}
								CallMapName=valname__+'()'
								CallMapEnum={'var':CallMapVar,'name':CallMapName}
								if CallMapEnum not in CallMap:
									CallMap.append(CallMapEnum)
								break
							
							else:
								if nodes[i]['name']=='APICall':
									callthis=nodes[i]['value'][nodes[i]['value'].find('-')+1:nodes[i]['value'].find('.')]

									start__=nodes[i]['value'].find('.')+1
									end__=nodes[i]['value'].find('(')
									valname__=nodes[i]['value'][start__:end__]
									

									#k=FindBlockByName(valname__)
									if callthis!='this':
										for m in source:
											if m['valname']==callthis:
												valname__=m['device']+'.'+valname__
												break
									#ids={'Gnum':FindBlockByNum(k),'valname':nodes[k]['value']}
									'''
									if valname__!=id['valname']:
										if ids not in worklist:
											worklist.append(ids)
										depend={'in':id,'out':ids}
										if depend not in dep:
											dep.append(depend)
											#G.add_edge(id['valname'],ids['valname'])
											#print(depend)
									'''
									CallMapVar=id
									CallMapName=valname__+'()'
									CallMapEnum={'var':CallMapVar,'name':CallMapName}
									if CallMapEnum not in CallMap:
										CallMap.append(CallMapEnum)
									break

							i=i-1
							
				j=j+1
			num=j

			#判断左值是否是当前变量
			k=num+2
			k_start=nodes[k]['value'].find('-')+1
			k_end=nodes[k]['value'].find(':')-1
			k_valname=nodes[k]['value'][k_start:k_end]
			ids={'Gnum':FindBlockByNum(k),'valname':k_valname}
			#print(ids)
			
			if k_valname==id['valname']:
				m=k+1
				#print(ids)
				while nodes[m]['level']>=nodes[k]['level'] and m<=len(nodes)-1:
					if nodes[m]['name']=='Variable':
						start=nodes[m]['value'].find('-')+1
						end=nodes[m]['value'].find(':')-1
						valname=nodes[m]['value'][start:end]
						idt={'Gnum':FindBlockByNum(m),'valname':valname}
						if valname!='this' and ((idt in worklist) or (idt in done)):
							
							depend={'in':idt,'out':ids}
							if depend not in dep:
								dep.append(depend)
					m=m+1
				if (ids not in done):
					return


		if nodes[num]['name']=='IfStatement' and num<=Block[id['Gnum']]['end']:
			#print(num)
			#print(id)
			for j in range(Block[id['Gnum']]['start'],Block[id['Gnum']]['end']):
				#print(j)
				if nodes[j]['name']=='Variable' and (nodes[j]['value'][nodes[j]['value'].find('-')+1:nodes[j]['value'].find(':')-1]==id['valname']):
					depend={'in':id,'out':id}
					if depend not in dep:
						dep.append(depend)

					CallMapVar=id
					CallMapName='if '+nodes[num+1]['value']+' '
					CallMapEnum={'var':CallMapVar,'name':CallMapName}
					if CallMapEnum not in CallMap:
						CallMap.append(CallMapEnum)

		if nodes[num]['name']=='ReturnStatement':
			#return
			#print(num)
			j=num+1
			while nodes[j]['level']>nodes[num]['level'] and j<len(nodes)-1:
				if nodes[j]['name']=='Variable':
					start=nodes[j]['value'].find('-')+1
					end=nodes[j]['value'].find(':')-1
					valname=nodes[j]['value'][start:end]
					if id['valname']==valname:
						n=j-1
						#print(id,n)
						while nodes[n]['name']!='MethodNode':
							n=n-1
						callname=nodes[n]['value']
						for p in range(0,len(nodes)-1):
							if nodes[p]['name']=='Binary' or nodes[p]['name']=='Declaration':
								ifFind=0
								t=p+1
								while nodes[t]['level']>nodes[p]['level']and t<len(nodes)-1:
									if nodes[t]['name']=='MethodCall':
										start__=nodes[t]['value'].find('.')+1
										end__=nodes[t]['value'].find('(')
										valname__=nodes[t]['value'][start__:end__]
										if valname__==callname:
											st=nodes[p+1]['value'].find('-')+1
											en=nodes[p+1]['value'].find(':')-1
											va=nodes[p+1]['value'][st:en]
											ids={'Gnum':FindBlockByNum(p+1),'valname':va}
											mm=t+1
											iffind=0
											#print(ids)
											#print(worklist)
											if ids in worklist or ids in done:
												iffind=1
											if iffind==1:
												if ids not in worklist:
													worklist.append(ids)
												depend={'in':id,'out':ids}
												if depend not in dep:
													dep.append(depend)											
									t=t+1
				j=j+1
			num=j#id污染所有左值以及

		if nodes[num]['name']=='MethodCall' and nodes[num-1]['name']!='Binary' and nodes[num-1]['name']!='Declaration':
			i=num+1
			ifFind=0
			count=0
			while nodes[i]['level']>nodes[num]['level'] and nodes[i]['level']<=len(nodes):
				if nodes[i]['name']=='Variable':
					count=count+1
					if nodes[i]['value'][nodes[i]['value'].find('-')+1:nodes[i]['value'].find(':')-1] ==id['valname']:
						ifFind=1
						break
				i=i+1

			if ifFind>0:
				k=FindBlockByName(nodes[num]['value'][nodes[num]['value'].find('.')+1:nodes[num]['value'].find('(')])
				counter=0
				while nodes[k]['name']!='Parameter' or counter!=count:
					k=k+1
					#print(k)
					if k>=len(nodes)-1:
						break
					if nodes[k]['name']=='Parameter':
						counter=counter+1
				ids={'Gnum':FindBlockByNum(k),'valname':nodes[k]['value']}
				if ids not in worklist:
					worklist.append(ids)
				depend={'in':id,'out':ids}
				if depend not in dep:
					dep.append(depend)
					#G.add_edge(id['valname'],ids['valname'])
					#print(depend)
				CallMapVar=id
				CallMapName=nodes[num]['value'][nodes[num]['value'].find('.')+1:nodes[num]['value'].find('(')]+'()'
				CallMapEnum={'var':CallMapVar,'name':CallMapName}
				if CallMapEnum not in CallMap:
					CallMap.append(CallMapEnum)


				num=i

				break

		if nodes[num]['name']=='APICall':
			i=num+1
			ifFind=0
			while nodes[i]['level']>nodes[num]['level']:
				if nodes[i]['name']=='Variable':
					if nodes[i]['value'][nodes[i]['value'].find('-')+1:nodes[i]['value'].find(':')-1] ==id['valname']:
						ifFind=1
						#print('****',id)
						break
				i=i+1
				if i>=len(nodes):
					break
			if ifFind>0:
				depend={'in':id,'out':id}
				if depend not in dep:
					dep.append(depend)
				CallMapVar=id
				callthis=nodes[num]['value'][nodes[i]['value'].find('-')+1:nodes[num]['value'].find('.')]
				CallMapName=nodes[num]['value'][nodes[num]['value'].find('.')+1:nodes[num]['value'].find('(')]+'()'
				if callthis!='this':
					for m in source:
						if m['valname']==callthis:
							CallMapName=m['device']+'.'+CallMapName
							break
				CallMapEnum={'var':CallMapVar,'name':CallMapName}
				if CallMapEnum not in CallMap:
					CallMap.append(CallMapEnum)

		num=num+1
	return



def DFS(id):
	TaintTrace(id)
	#print(id)
	for i in Path:
		if i['in']==id['Gnum']:
			#print(i['in'],i['out'])
			tra={'in':i['in'],'out':i['out']}
			if tra not in traveled:
				traveled.append(tra)
				#print(id)
				DFS({'Gnum':i['out'],'valname':id['valname']})


for i in Block:
	print (i) 
#print(Block[0:])#将AST划分成块，num为块的编号，start和end代表起始和终止行数(AST遍历结果的行数)
for i in Path:
	print(i['in'],'->',i['out'])#控制流图
#print(len(nodes))
FindSource()
traveled=[]
#print(worklist)
while len(worklist)>0:
		id=worklist[-1]
		#print(id)
		worklist=worklist[:-1]
		done.append(id)
		traveled.clear()
		DFS(id)
'''
#print(dep)
for i in dep:
	print(str(i['in']['Gnum'])+':'+i['in']['valname']+'->'+str(i['out']['Gnum'])+':'+i['out']['valname'])
#print(worklist)
'''
for i in dep:
	for j in dep:
		if (i!=j) and (i['out']['valname']==j['in']['valname']) and (i['out']['Gnum']!=j['in']['Gnum']):
			tempResult=IfInOneMethod(i['out'],j['in'])
			if tempResult==0:
				continue
			else:
				if tempResult==1:
					depend={'in':i['out'],'out':j['in']}
					if depend not in dep:
						dep.append(depend)
				else:
					depend={'in':j['in'],'out':i['out']}
					if depend not in dep:
						dep.append(depend)




for i in dep:
	for j in IfStatementBlock:
		if i['out']['Gnum']==FindBlockByNum(j['num']):
			iftempblock=[]
			for k in range(int(FindBlockByNum(j['left'])),int(FindBlockByNum(j['end']))+1):
				#print(k)
				iftempblock.append(k)
			for m in dep:
				if m['in']['Gnum'] in iftempblock and m!=i and {'in':i['out'],'out':m['in']} not in dep:
					dep.append({'in':i['out'],'out':m['in']})
'''
for i in dep:
	print(str(i['in']['Gnum'])+':'+i['in']['valname']+'->'+str(i['out']['Gnum'])+':'+i['out']['valname'])
'''
print('***********')

delete=[]
for i in range(0,len(dep)):
	hasline=0
	nodelist.clear()
	tempIn=dep[i]['in']
	tempOut=dep[i]['out']
	temp=dep.pop(i)
	#print(temp)
	if ifExistingPath(tempIn,tempOut)!=0:
		delete.append(i)
		#print(i)
	dep.insert(i,temp)

#print(delete)
results=[]
for i in range(0,len(dep)):
	if i not in delete:
		results.append(dep[i])


for i in results:
	print(str(i['in']['Gnum'])+':'+i['in']['valname']+'->'+str(i['out']['Gnum'])+':'+i['out']['valname'])

traveled.clear()
def DFSS(id,level):
	#global traveled
	print(level*' '+str(id['Gnum'])+':'+id['valname']+':',end='')
	for j in CallMap:
		if j['var']==id:
			print(j['name'],end=',')
	print('\n',end='')
	for i in results:
		if i['in']==id:
			#print(i['in'],i['out'])
			tra={'in':i['in'],'out':i['out']}
			if tra not in traveled:
				traveled.append(tra)
				#print(i['out'],level)
				DFSS(i['out'],level+1)
				traveled.remove(tra)
				#print('\n',end='')
#print(source)


for i in source:
	id={'Gnum':i['Gnum'],'valname':i['valname']}
	print('\nSensitive Info: '+i['valname']+' , Source Device: '+i['device']+' , Source Api: '+i['command'],', type: '+i['type'])
	traveled.clear()
	DFSS(id,0)

#print('\n')
#print(CallMap)
#print(IfStatementBlock)


