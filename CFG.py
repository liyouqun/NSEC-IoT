#coding:utf-8
script="""-2 3 MethodNode - run
-1 4 BlockStatement - (0)
0 3 MethodNode - f
1 4 BlockStatement - (4)
2 5 ExpressionStatement - BinaryExpression
3 6 Binary - (y = this.source())
4 7 Variable - y : java.lang.Object
5 8 DynamicVariable - y
6 7 MethodCall - this.source()
7 8 Variable - this : java.lang.Object
8 8 Constant - source : java.lang.String
9 8 ArgumentList - ()
10 5 ExpressionStatement - BinaryExpression
11 6 Binary - (x = (y * 3))
12 7 Variable - x : java.lang.Object
13 8 DynamicVariable - x
14 7 Binary - (y * 3)
15 8 Variable - y : java.lang.Object
16 9 DynamicVariable - y
17 8 Constant - 3 : int
18 5 IfStatement
19 6 Boolean - (x > 100)
20 7 Binary - (x > 100)
21 8 Variable - x : java.lang.Object
22 9 DynamicVariable - x
23 8 Constant - 100 : int
24 6 ExpressionStatement - MethodCallExpression
25 7 MethodCall - this.println(x)
26 8 Variable - this : java.lang.Object
27 8 Constant - println : java.lang.String
28 8 ArgumentList - (x)
29 9 Variable - x : java.lang.Object
30 10 DynamicVariable - x
31 6 ExpressionStatement - BinaryExpression
32 7 Binary - (z = this.g(x))
33 8 Variable - z : java.lang.Object
34 9 DynamicVariable - z
35 8 MethodCall - this.g(x)
36 9 Variable - this : java.lang.Object
37 9 Constant - g : java.lang.String
38 9 ArgumentList - (x)
39 10 Variable - x : java.lang.Object
40 11 DynamicVariable - x
41 5 ExpressionStatement - MethodCallExpression
42 6 MethodCall - this.sink(z)
43 7 Variable - this : java.lang.Object
44 7 Constant - sink : java.lang.String
45 7 ArgumentList - (z)
46 8 Variable - z : java.lang.Object
47 9 DynamicVariable - z
48 3 MethodNode - g
49 4 Parameter - t
50 4 BlockStatement - (2)
51 5 ExpressionStatement - BinaryExpression
52 6 Binary - (m = (t * 10))
53 7 Variable - m : java.lang.Object
54 8 DynamicVariable - m
55 7 Binary - (t * 10)
56 8 Variable - t : java.lang.Object
57 9 Parameter - t
58 8 Constant - 10 : int
59 5 ReturnStatement - return m
60 6 Variable - m : java.lang.Object
61 7 DynamicVariable - m


"""

nodes=[]
MethodNode=[]
BlockFirstLine=[]
MethodNodeName=[]
MethodCall=[]
IfStatement=[]
IfStatementBlock=[]
Block=[]
Path=[]

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
					returnnum=0
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
				if nodes[j]['level']>3:
					BlockFirstLine.append(j)
			j=j+1
	return

def BuildTheBlock():
	num=0
	for i in range(0,len(BlockFirstLine)-1):
		block_start=BlockFirstLine[i]
		block_end=BlockFirstLine[i+1]-1
		block={'num':num,'start':block_start,'end':block_end}
		Block.append(block)
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
				while nodes[j]['level']>nodes[i['right']]['level']:
					j=j+1
				if nodes[j]['level']>3:
					out_block=FindBlockByNum(j)
					path={'in':in_block,'out':out_block}
					Path.append(path)

			j=i['right']+1
			while nodes[j]['level']>nodes[i['right']]['level']:
				j=j+1
			if nodes[j]['level']>3 and nodes[Block[FindBlockByNum(j)-1]['start']]['name']!='MethodCall':
				out_block=FindBlockByNum(j)
				path={'in':out_block-1,'out':out_block}
				Path.append(path)

		if i['right']==0:
			j=i['left']+1
			while (nodes[j]['level']>nodes[i['left']]['level']) or (nodes[j]['name']=='EmptyStatement'):
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


#读取script并预处理，其中每行AST(即每个节点)提取四个属性：行数num，树的层数level，节点类型name以及节点的值value，存进nodes[]
for i in range(2,len(script.split('\n'))):
	line=script.split('\n')[i]
	if line.isspace() or line=='':
		break
	num=line.split(' ')[0]
	level=line.split(' ')[1]
	name=line.split(' ')[2]
	start=len(num+level+name)+5
	num=int(num)
	level=int(level)
	value=line[start:]
	obj={'num':num,'level':level,'name':name,'value':value}
	nodes.append(obj)
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



#将If语句划分成块
AddIfStatementToBlock()
#将调用划分成块，程序内的函数调用名为MethodCall，程序外的函数调用为APICall
AddMethodCallToBlock()

#block去重排序，划分block
BlockFirstLine=num_set_list()
BuildTheBlock()

#分别连接三类block，形成CFG，存储进Path
MatchIfBlock()
MatchCallBlock()
MatchOtherBlock()
#污染源API
sourceAPI=['source']


#####################################以上完成CFG，以下待完成

#这几个东西的定义见saint的paper，后向追踪改前向
worklist=[]
done=[]
dep=[]
ids=[]

#通过sourceAPI[]寻找污染源变量，并存进worklist里，包括变量所在的block:Gnum，和变量valname
def FindSource():
	for i in range(0,len(nodes)):
		if nodes[i]['name']=='APICall':
			start=nodes[i]['value'].find('-')+1
			end=nodes[i]['value'].find('.')
			callthis=nodes[i]['value'][start:end]
			start=nodes[i]['value'].find('.')+1
			end=nodes[i]['value'].find('(')
			callthat=nodes[i]['value'][start:end]
			#print(callthis)
			#print(callthat)
			if callthis=='this' and callthat in sourceAPI:
				lev=nodes[i]['level']
				j=i-1
				while nodes[j]['level']>lev or nodes[j]['name']=='Variable':
					j=j-1
				if nodes[j]['name']=='Binary':
					start=nodes[j+1]['value'].find('-')+1
					end=nodes[j+1]['value'].find(':')-1
					valname=nodes[j+1]['value'][start:end]
					id={'Gnum':FindBlockByNum(j),'valname':valname}
					if id not in worklist:
						worklist.append(id)
	return
'''以下未完成，应该只会用到Path和nodes

def DFS(id):

	for i in Path:
		if i['in']==id['Gnum']:
			print(i['in'],i['out'])
			DFS({'Gnum':i['out'],'valname':id['valname']})


def BuildDataFlow():
	while len(worklist)>0:
		id=worklist[-1]
		worklist=worklist[:-1]
		done.append(id)
		DFS(id)
	return
'''



FindSource()
#print(worklist)

print(Block[0:])#将AST划分成块，num为块的编号，start和end代表起始和终止行数(AST遍历结果的行数)

print(Path)#控制流图

#print(MethodNode)
#print(FindBlockByName('f'))
