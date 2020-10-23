
File file=new File('IR.txt')
file.eachLine
        {
            String str=it
            str=str.replace("java.lang.Object","")
            str=str.replace("public","def")
            str=str.replace("private","def")
           // str=str.replace("\$","\\"+"\$")
            if(str.contains("log.debug"))
            {
                int iStart=str.indexOf('(')-9
                int iEnd=str.lastIndexOf(')')
                str=str.substring(0,iStart)+str.substring(iEnd+1,str.length())
            }
            if(str.contains("."))
            {

                for (int i = 0; i < str.length(); i++) {
                    if (str.charAt(i) == "."&&str.charAt(i-1)==" ")
                    {
                        str=str.substring(0,i-1)+str.substring(i,str.length())
                    }
                }
            }
            String temp=str;
            temp=temp.replace(" ","")
          if(temp!="") println str
        }

