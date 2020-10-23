import org.codehaus.groovy.ast.ASTNode
import org.codehaus.groovy.ast.ClassNode
import org.codehaus.groovy.ast.CodeVisitorSupport
import org.codehaus.groovy.ast.ConstructorNode
import org.codehaus.groovy.ast.FieldNode
import org.codehaus.groovy.ast.GroovyClassVisitor

import org.codehaus.groovy.ast.MethodNode

import org.codehaus.groovy.ast.PropertyNode

import org.codehaus.groovy.ast.expr.Expression

import org.codehaus.groovy.ast.expr.MapEntryExpression

import org.codehaus.groovy.ast.expr.MethodCallExpression
import org.codehaus.groovy.ast.expr.BinaryExpression

import java.io.StringWriter

import org.codehaus.groovy.control.SourceUnit
import org.codehaus.groovy.transform.ASTTransformation
import org.codehaus.groovy.transform.GroovyASTTransformation
import groovy.inspect.swingui.AstNodeToScriptVisitor

import org.codehaus.groovy.control.CompilePhase
/*
* Created by TY on 2018/4/20.
*/


@GroovyASTTransformation(phase = CompilePhase.SEMANTIC_ANALYSIS)
class TestASTTransformation implements ASTTransformation {
    File fileOut = new File("IR.txt")
    static String getSourceFromNode(MethodNode methodNode){
        StringWriter writer = new StringWriter();
        AstNodeToScriptVisitor visitor = new AstNodeToScriptVisitor(writer);
        visitor.visitMethod(methodNode); // replace with proper visit****
//        System.out.println(writer.toString());
        return writer.toString();
    }
    @Override
    void visit(ASTNode[] nodes, SourceUnit source) {
        fileOut.withWriter('utf-8') {
            writer ->
                //get AST from source, for global transform, it is safe
                // to ignore this parameter
                def entry_points = []

                //Methods's name can be resoved
                def count = 0
                //def count_entry_pint = 0
                source.AST.classes.each {
                    it.visitContents(new GroovyClassVisitor() {
                        @Override
                        void visitClass(ClassNode node) {

                        }

                        @Override
                        void visitConstructor(ConstructorNode node) {

                        }

                        @Override
                        void visitMethod(MethodNode node) {
                            def method_name = node.getName()


                            /*
                        if (method_name != "main"){
                            writer.writeLine "method name is $method_name"
                        }
                         */

                            if (method_name == "run") {
                                //node.get
                                writer.writeLine ('// Permission Block')
                                def statements = node.getCode()
                                statements.visit(new CodeVisitorSupport() {
                                    @Override
                                    void visitMethodCallExpression(MethodCallExpression call) {
                                        super.visitMethodCallExpression(call)
                                        def called_name = call.getMethodAsString()
                                        //writer.writeLine called_name

                                        //find category info
                                        if (called_name == "definition") {
                                            //writer.writeLine "in definition"
                                            //def arg_iter = call.getArguments().iterator()
                                            //writer.writeLine arg_iter.toString()
                                            def args = call.getArguments()
                                            //writer.writeLine args
                                            args.visit(new CodeVisitorSupport() {
                                                @Override
                                                void visitMapEntryExpression(MapEntryExpression expression) {
                                                    super.visitMapEntryExpression(expression)
                                                    if (expression.getKeyExpression().text == "category") {
                                                        writer.write("category: ");
                                                        writer.writeLine(expression.getValueExpression().getText())
                                                        // writer.write ("category: ")
                                                        //writer.writeLine(expression.getValueExpression().getText())
                                                    }
                                                }
                                            })
                                        }

                                        //should be preference(), but every useful info is attached with input()
                                        //hence using the name "input" is sufficient
                                        if (called_name == "input") {
                                            //writer.writeLine "in input"
                                            writer.write('input (')
                                            def args = call.getArguments()
                                            def expressions = args.getExpressions()
                                            count = 0

                                            //choose the last two arguments in input argumentlist
                                            //assert #argument is 3
                                            def input_type = ' '
                                            for (Expression expression : expressions) {
                                                if (count > 1) { //why count>1???
                                                    writer.write ", "
                                                }
                                                if (count >= 1) {
                                                    input_type = expression.text
                                                    writer.write input_type
                                                }
                                                count++
                                            }
                                            assert count < 4

                                            def regex = 'capability'
                                            if (input_type =~ regex)
                                                writer.write ", type:device"
                                            else
                                                writer.write ", type:user_defined"
                                            writer.writeLine ")"
                                        }
                                    }
                                })
                                writer.writeLine ""
                                writer.writeLine "//Event/Actions block"
                            } else if (method_name == "uninstalled") {
                                //add  code to tackle installed()
                                //writer.writeLine "the following content is about uninstalled()"
                            } else if ((method_name == "initialize") || (method_name == "updated") || method_name == "installed") {
                                //writer.writeLine "the following content is about initialize()"
                                def statements = node.getCode()
                                statements.visit(new CodeVisitorSupport() {
                                    @Override
                                    void visitMethodCallExpression(MethodCallExpression call) {
                                        super.visitMethodCallExpression(call)
                                        def call_name = call.getMethodAsString()
                                        if (call_name == "subscribe") {
                                            writer.writeLine "subscribe" + call.getArguments().getText()
                                        }

                                        def args = call.getArguments()
                                        def expressions = args.getExpressions()
                                        count = 0

                                        //choose the last two arguments in input argumentlist
                                        //assert #argument is 3

                                        for (Expression expression : expressions) {
                                            '''
                                        add the third argument of subscribe() into entrypoint[]
                                        strange thing happens that in some case, the argument of subscribe
                                        is only 2. The default should be 3.
                                    '''
                                            if (count == 2) {
                                                //writer.writeLine "found entry point!"
                                                //writer.writeLine expression.text
                                                entry_points.add(expression.text)
                                            }
                                            count++
                                        }
                                        assert count < 4

                                    }
                                })
                                //writer.writeLine ""

                            } else if (method_name in entry_points) {
                                //extract call graphs
                                //writer.writeLine "the app defines entry points: $method_name"
                                writer.writeLine ""
                                writer.writeLine "//Entry point"

                                //copy code
                                writer.writeLine method_name + "(){"
                                def statements = node.getCode()
                                statements.visit(new CodeVisitorSupport() {
                                    @Override
                                    void visitMethodCallExpression(MethodCallExpression call) {
                                        super.visitMethodCallExpression(call)
                                        def call_name = call.getMethodAsString()
                                        if (call_name != "debug")
                                            writer.writeLine '\t' + call.getMethodAsString() + call.getArguments().getText()
                                    }
                                })
                                writer.writeLine "}"
                                writer.writeLine ""
                                writer.writeLine "//other  defined functions:"
                            } else if (!(method_name in entry_points) && method_name != 'main') {
                                //copy code
                                // writer.writeLine "other defined functions: $method_name"
                                writer.writeLine '\n'
                                writer.writeLine getSourceFromNode(node)
                                /*writer.writeLine ""
                                writer.writeLine "def "+method_name + "(){"
                                def statements = node.getCode()
                                statements.visit(new CodeVisitorSupport() {
                                    @Override
                                    void visitMethodCallExpression(MethodCallExpression call) {
                                        super.visitMethodCallExpression(call)
                                        def call_name = call.getMethodAsString()
                                        if (call_name != "debug")
                                            writer.writeLine '\t' + call.getMethodAsString() + call.getArguments().getText()
                                    }

                                })

                                writer.writeLine "}"*/
                            }
                        }

                        @Override
                        void visitField(FieldNode node) {
                            //writer.writeLine "field name is ${node.name}"
                        }

                        @Override
                        void visitProperty(PropertyNode node) {
                            //writer.writeLine "property name is ${node.name}"
                        }
                    })

                }
        }
        /*printWriter.flush()
    printWriter.close()*/
    }
}
