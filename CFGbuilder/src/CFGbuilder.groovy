number = 'A'
entry = []
list = []
edge=[]
def script=
"""1 3 MethodNode - run
2 4 BlockStatement - (7)
3 5 ExpressionStatement - MethodCallExpression
4 6 MethodCall - this.input([type:device], switchesoff, capability.switch)
5 7 Variable - this : java.lang.Object
6 7 Constant - input : java.lang.String
7 7 ArgumentList - ([type:device], switchesoff, capability.switch)
8 8 MapExpression
9 9 MapEntryExpression
10 10 Constant - type : java.lang.String
11 10 Variable - device : java.lang.Object
12 11 DynamicVariable - device
13 8 Variable - switchesoff : java.lang.Object
14 9 DynamicVariable - switchesoff
15 8 Property - switch
16 9 Variable - capability : java.lang.Object
17 10 DynamicVariable - capability
18 9 Constant - switch : java.lang.String
19 5 ExpressionStatement - MethodCallExpression
20 6 MethodCall - this.input([type:device], switcheson, capability.switch)
21 7 Variable - this : java.lang.Object
22 7 Constant - input : java.lang.String
23 7 ArgumentList - ([type:device], switcheson, capability.switch)
24 8 MapExpression
25 9 MapEntryExpression
26 10 Constant - type : java.lang.String
27 10 Variable - device : java.lang.Object
28 11 DynamicVariable - device
29 8 Variable - switcheson : java.lang.Object
30 9 DynamicVariable - switcheson
31 8 Property - switch
32 9 Variable - capability : java.lang.Object
33 10 DynamicVariable - capability
34 9 Constant - switch : java.lang.String
35 5 ExpressionStatement - MethodCallExpression
36 6 MethodCall - this.input([type:device], lock1, capability.lock)
37 7 Variable - this : java.lang.Object
38 7 Constant - input : java.lang.String
39 7 ArgumentList - ([type:device], lock1, capability.lock)
40 8 MapExpression
41 9 MapEntryExpression
42 10 Constant - type : java.lang.String
43 10 Variable - device : java.lang.Object
44 11 DynamicVariable - device
45 8 Variable - lock1 : java.lang.Object
46 9 DynamicVariable - lock1
47 8 Property - lock
48 9 Variable - capability : java.lang.Object
49 10 DynamicVariable - capability
50 9 Constant - lock : java.lang.String
51 5 ExpressionStatement - MethodCallExpression
52 6 MethodCall - this.input([type:user_defined], newMode, mode)
53 7 Variable - this : java.lang.Object
54 7 Constant - input : java.lang.String
55 7 ArgumentList - ([type:user_defined], newMode, mode)
56 8 MapExpression
57 9 MapEntryExpression
58 10 Constant - type : java.lang.String
59 10 Variable - user_defined : java.lang.Object
60 11 DynamicVariable - user_defined
61 8 Variable - newMode : java.lang.Object
62 9 DynamicVariable - newMode
63 8 Variable - mode : java.lang.Object
64 9 DynamicVariable - mode
65 5 ExpressionStatement - MethodCallExpression
66 6 MethodCall - this.input([type:user_defined], waitfor, number)
67 7 Variable - this : java.lang.Object
68 7 Constant - input : java.lang.String
69 7 ArgumentList - ([type:user_defined], waitfor, number)
70 8 MapExpression
71 9 MapEntryExpression
72 10 Constant - type : java.lang.String
73 10 Variable - user_defined : java.lang.Object
74 11 DynamicVariable - user_defined
75 8 Variable - waitfor : java.lang.Object
76 9 DynamicVariable - waitfor
77 8 Variable - number : java.lang.Object
78 9 DynamicVariable - number
79 5 ExpressionStatement - MethodCallExpression
80 6 MethodCall - this.subscribe(app, appTouch)
81 7 Variable - this : java.lang.Object
82 7 Constant - subscribe : java.lang.String
83 7 ArgumentList - (app, appTouch)
84 8 Variable - app : java.lang.Object
85 9 DynamicVariable - app
86 8 Variable - appTouch : java.lang.Object
87 9 DynamicVariable - appTouch
88 5 ExpressionStatement - MethodCallExpression
89 6 MethodCall - this.subscribe(app, appTouch)
90 7 Variable - this : java.lang.Object
91 7 Constant - subscribe : java.lang.String
92 7 ArgumentList - (app, appTouch)
93 8 Variable - app : java.lang.Object
94 9 DynamicVariable - app
95 8 Variable - appTouch : java.lang.Object
96 9 DynamicVariable - appTouch
97 3 MethodNode - appTouch
98 4 Parameter - evt
99 4 BlockStatement - (5)
100 5 IfStatement
101 6 Boolean - (location.mode != newMode)
102 7 Binary - (location.mode != newMode)
103 8 Property - mode
104 9 Variable - location : java.lang.Object
105 10 DynamicVariable - location
106 9 Constant - mode : java.lang.String
107 8 Variable - newMode : java.lang.Object
108 9 DynamicVariable - newMode
109 6 BlockStatement - (1)
110 7 ExpressionStatement - MethodCallExpression
111 8 MethodCall - this.setLocationMode(newMode)
112 9 Variable - this : java.lang.Object
113 9 Constant - setLocationMode : java.lang.String
114 9 ArgumentList - (newMode)
115 10 Variable - newMode : java.lang.Object
116 11 DynamicVariable - newMode
117 6 BlockStatement - (0)
118 5 ExpressionStatement - MethodCallExpression
119 6 MethodCall - lock1.lock()
120 7 Variable - lock1 : java.lang.Object
121 8 DynamicVariable - lock1
122 7 Constant - lock : java.lang.String
123 7 ArgumentList - ()
124 5 ExpressionStatement - MethodCallExpression
125 6 MethodCall - switcheson.on()
126 7 Variable - switcheson : java.lang.Object
127 8 DynamicVariable - switcheson
128 7 Constant - on : java.lang.String
129 7 ArgumentList - ()
130 5 ExpressionStatement - BinaryExpression
131 6 Binary - (delay = (((waitfor != null) && (waitfor != ))) ? (waitfor * 1000) : 120000)
132 7 Variable - delay : java.lang.Object
133 8 DynamicVariable - delay
134 7 TernaryExpression
135 8 Boolean - ((waitfor != null) && (waitfor != ))
136 9 Binary - ((waitfor != null) && (waitfor != ))
137 10 Binary - (waitfor != null)
138 11 Variable - waitfor : java.lang.Object
139 12 DynamicVariable - waitfor
140 11 Constant - null : java.lang.Object
141 10 Binary - (waitfor != )
142 11 Variable - waitfor : java.lang.Object
143 12 DynamicVariable - waitfor
144 11 Constant -  : java.lang.String
145 8 Binary - (waitfor * 1000)
146 9 Variable - waitfor : java.lang.Object
147 10 DynamicVariable - waitfor
148 9 Constant - 1000 : int
149 8 Constant - 120000 : int
150 5 ExpressionStatement - MethodCallExpression
151 6 MethodCall - switchesoff.off([delay:delay])
152 7 Variable - switchesoff : java.lang.Object
153 8 DynamicVariable - switchesoff
154 7 Constant - off : java.lang.String
155 7 ArgumentList - ([delay:delay])
156 8 MapExpression
157 9 MapEntryExpression
158 10 Constant - delay : java.lang.String
159 10 Variable - delay : java.lang.Object
160 11 DynamicVariable - delay
"""
def transcall(def tmp)
{
    if(tmp.contains("this."))
        tmp=tmp.replace("this.","")
    if(tmp.contains("("))
        tmp=tmp.substring(0,tmp.indexOf("("))
    return tmp
}

def SetToEntry(def obj)
{
    def temp = [num: 'A', line: 0,lastline:list.size(),obj:obj]
    temp.num = number
    temp.line = obj.line
    number = number.next()
    entry.add(temp)
    //obj.Entry=true
}
def nextBro(def obj)
{
    for(def i=obj.line;;i++)
    {
        if (list[i].level<=obj.level)
        {
            if(((list[i].type!="MethodNode")&&(list[i].type!="IfChild2")&&(list[i].type!="IfChild1"))) return list[i]
            else return null
        }
    }

}

def nextBlock(def k)
{
    for (def i=k+1;i<entry.size();++i)
    {
        if(entry[i].obj.level<=entry[k].obj.level)
        {
            if(((entry[i].obj.type!="MethodNode")&&(entry[i].obj.type!="IfChild2")&&(entry[i].obj.type!="IfChild1"))) return i
            else return null
        }
    }
}

def findExpress(def obj)
{
    def count=0
    for(def i=obj.line+1;;i++)
    {
        if (list[i].level==obj.level+1)
        {
           if (!list[i].Entry)list[i].Entry=true
            if(count==0)list[i].type="IfChild1"
            else list[i].type="IfChild2"
            count++
            if (count==2)return
        }
    }

}

def findReturn(def i,def next)
{
    for(def j=i;j<entry.size();j++)
    {
        if(entry[j].obj.level>entry[i].obj.level||j==i)
        {
            for(def k=entry[j].line;k++;k<entry[j].lastline+1)
            {
                if(list[k-1].type=="ReturnStatement")
                {
                    addEdge(j,next)
                    break
                }

            }
        }

    }
}

def addEdge(def i,def j)
{
    def inE=entry[i].num
    def outE=entry[j].num
    def temp=[in:inE,out:outE]
    edge.add(temp)
}

    def localMethod = []
    script.eachLine
            {
                def node = [line: 0, level: 0, type: "", val: "",Entry:false]
                def a, b, c
                a = it.indexOf(' ')
                b = it.indexOf(' ', a + 1)
                c = it.indexOf("-")
                d = it.lastIndexOf(":")
                node.line = it.substring(0, a).toInteger()
                node.level = it.substring(a + 1, b).toInteger()
                if (c > 0) node.type = it.substring(b + 1, c - 1) else {node.type = it.substring(b + 1);node.val=node.type}
                if (c>0) if (d > 0) node.val = it.substring(c + 2, d - 1) else node.val = it.substring(c + 2)
                if (node.type == "MethodNode") {

                    localMethod.add(node.val)
                }
                list.add(node)
                // println node
            }



    list.each
            {
                if(it.type=="IfStatement")
                {
                    it.Entry=true
                    findExpress(it)
                    next=nextBro(it)
                    if (next)
                        if (next.Entry==false)next.Entry=true
                }

                if (it.type == "MethodNode") it.Entry=true
                if ((it.type == "MethodCall" && localMethod.find { key -> key == transcall(it.val) })||(it.type=="IfChild1")||(it.type=="IfChild2"))
                {
                    it.Entry=true
                    def next=nextBro(it)
                    if (next)
                    if (next.Entry==false)next.Entry=true
                }


            }
   list.each{if(it.Entry==true)SetToEntry(it)}
for(def i=0;i<entry.size()-1;++i)
{
    entry[i].lastline=entry[i+1].line-1
}

    entry.each{
        println it.num+",first line:"+it.line+" ,last line:"+it.lastline
    }


       for (def i=1;i<entry.size();i++)
       {
           if(entry[i].obj.type=="IfStatement")
           {
               def count=0
              for(def j=i+1;j<entry.size();++j)
                  if (entry[j].obj.level==entry[i].obj.level+1)
                  {
                      addEdge(i,j)
                      ++count
                      if(count==2)break
                  }
           }
           else
           if(entry[i].obj.type=="MethodCall")
             {
                 for(def j=0;j<entry.size();++j)
                         {
                                 if((entry[j].obj.type=="MethodNode")&&(entry[j].obj.val== transcall(entry[i].obj.val)))
                                 {
                                     addEdge(i,j)
                                     def next=nextBlock(i)
                                     if(next)
                                     findReturn(j,next)
                                     break
                                 }
                         }
             }
           else
           if(entry[i].obj.type=="IfChild2")
           {
               for (def j=i-1;j>=0;j--)
               {
                   if(entry[j].obj.type=="IfStatement" && entry[j].obj.level==entry[i].obj.level-1)
                   {
                       def next=nextBlock(j)
                       if(next)
                       {
                           addEdge(i - 1, next)
                           addEdge(next - 1, next)
                       }
                       break
                   }
               }
           }
           if((entry[i-1].obj.level<entry[i].obj.level)&&entry[i-1].obj.type!="MethodCall") {
              addEdge(i-1,i)
           }

       }
println edge.unique()



preBlock=[]

for(def i=0;i<entry.size();++i)
{
	def prelist=[]
	edge.each
	{
		if (it.out==entry[i].num)
		{
			prelist.add(it.in)
		}
	}
	def tempBlock=[num:entry[i].num,pre:prelist]
	preBlock.add(tempBlock)

}
println  preBlock

taintcall=["SendSms","sink"]
worklist=[]
done=[]
dep=[]
def findparam(def i)
{
	for(int j=i+1;j<list.size();++j)
	{
		if(list[j].type=="Variable"&&list[j].level==list[i].level+2)
		{
            def tmp=[num:1,val:list[j].val]
           for(def k=0;k<entry.size();++k)
                   {
                       if(entry[k].line<=list[j].line&&entry[k].lastline>=list[j].line)
                       {
                           tmp.num=k
                           break
                       }
                   }
			worklist.add(tmp)
           // println list[j].val

		}
		else if(list[j].level<=list[i].level) break
	}
}

for (def i=list.size()-1;i>0;i--)
{
	if(list[i].type=="MethodCall" /*&& taintcall.find { key -> key == transcall(list[i].val) }*/)
		{
			findparam(i)
           // println(i)
		}
}

println worklist

def listminus(def list1,def list2)
{
    def list3=list1.intersect(list2)
    list3.each{list1=list1.minus(it)}
    return list1
}



def travel(def x,def s,def y) {
    for(def k=entry[x].lastline;k>=entry[x].line;--k)
    {
        if(list[k-1].type=="Binary" && list[k].type=="Variable" && list[k].val==s &&list[k-2].type!="Binary"&&list[k-2].type!="Boolean")
        {
          //  println list[k].val
            for(def m=k+1;;m++)
            {
                def ids=[num:x,val:list[m].val]
                if(list[m].level<=list[k-1].level)break
                if(list[m].type=="Variable"&&!done.find{key->key==ids}&&list[m].val!="this")
                {
                    worklist.add(ids)
                    //println worklist
                    def idtmp=[num:y,val:s]
                    def path=[in:idtmp,out:ids]
                    dep.add(path)
                }

            }

            return
        }
    }
    if (preBlock[x].pre.isEmpty()) return
    else {
        preBlock[x].pre.each
                {
                    for(int j=0;j<preBlock.size();++j)if(preBlock[j].num==it) {
                        travel(j,s,y)
                        break
                    }
                }

    }
}
//def id=worklist.pop()
//travel(1,"x")
//println ids
def findcall(def i,def count,def id,def name)
{
preBlock[i].pre.each
        {
            for(def k=0;k<entry.size();k++)
            {
                if(entry[k].num==it)
                {
                    def start,end
                    for(def m=entry[k].line-1;m<entry[k].lastline;++m)
                    {
                        if(list[m].type=="MethodCall"&&transcall(list[m].val)==name)
                        {
                            def stend=[]
                            for(def n=m+1;n<entry[k].lastline;++n)
                            {
                                if(list[n].level==list[m].level+2) stend.add(n)
                            }
                            stend.add(entry[k].lastline-1)
                           // println stend
                            start=stend[count-1]
                            end=stend[count]
                          // println start+" "+end
                            break

                        }
                    }
                    for(def j=start;j<end;++j)
                    {
                        if(list[j].type=="Variable"&&list[j].val!="this")
                        {
                            def ids=[num:k,val:list[j].val]
                            if(!done.find{key->key==ids})
                            {
                                worklist.add(ids)
                                //println worklist
                                def path=[in:id,out:ids]
                                dep.add(path)
                            }

                        }
                    }

                }
            }
        }
}
def ifpara(def id)
{
    for(def k=entry[id.num].lastline;k>0;k--)
    {
        if(list[k-1].type=="MethodNode")
        {
            boolean flag=false
            def count=1
            while(list[k-1+count].type=="Parameter")
            {
                if(list[k-1+count].val==id.val)
                {
                    flag=true
                    break
                }
                ++count
            }
            if(flag){
                for(def i=0;i<entry.size();++i)
                {
                    if(entry[i].line==k) findcall(i,count,id,list[k-1].val)
                }
            }
        }
    }
}
while (!worklist.isEmpty()) {
    def id = worklist.pop()
    done.add(id)
    ifpara(id)
    travel(id.num, id.val, id.num)
}
println dep.unique()




















