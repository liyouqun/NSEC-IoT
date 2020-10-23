package groovyastbrowser

class Debug {
    static boolean DEBUG = false
    static boolean flag=false
    static String output=""
    static int counter=0
    static File fileout=new File("PreCFG.txt")
    static printNode(node, level = 0) {
                def skipRetTuple = Utils.skipNode(node, true)
                if (skipRetTuple[0]) return


                if (node.userObject.toString() == "MethodNode - run") {
                    flag = true
                }
                if (node.userObject.toString() == "MethodNode - <clinit>") {
                    flag = false
                }
                if (flag)
                {
                    counter++
                    output=output+counter+" "+level + " " + node+'\n'
                }
                    //println(level + " " + node)

                //println node


        node.children.each {
            printNode(it, level + 1)
        }


    }

    static tryAstBrowserWeb() {
       File file = new File("D:\\project\\browser\\src\\IR.txt")
        def script=""
        file.eachLine
                {
                    script=script+it+'\n'
                }
      // println script
       // def script=


        def astBrowser = new AstBrowserWeb(script, 5)
        astBrowser.showScriptClass = true
        astBrowser.showScriptFreeForm = true
        def astRoot = astBrowser.createAST()
        printNode(astRoot)
        fileout.withWriter('utf-8') {
            writer ->
                writer.writeLine(output)
        }
    }

    static log(message) {
        if(DEBUG) println message
    }
}
