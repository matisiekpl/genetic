# Generated from gramatyka.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatykaParser import gramatykaParser
else:
    from gramatykaParser import gramatykaParser

# This class defines a complete listener for a parse tree produced by gramatykaParser.
class gramatykaListener(ParseTreeListener):

    # Enter a parse tree produced by gramatykaParser#main.
    def enterMain(self, ctx:gramatykaParser.MainContext):
        pass

    # Exit a parse tree produced by gramatykaParser#main.
    def exitMain(self, ctx:gramatykaParser.MainContext):
        pass


    # Enter a parse tree produced by gramatykaParser#statement.
    def enterStatement(self, ctx:gramatykaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#statement.
    def exitStatement(self, ctx:gramatykaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#name.
    def enterName(self, ctx:gramatykaParser.NameContext):
        pass

    # Exit a parse tree produced by gramatykaParser#name.
    def exitName(self, ctx:gramatykaParser.NameContext):
        pass


    # Enter a parse tree produced by gramatykaParser#printStatement.
    def enterPrintStatement(self, ctx:gramatykaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#printStatement.
    def exitPrintStatement(self, ctx:gramatykaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#inputStatement.
    def enterInputStatement(self, ctx:gramatykaParser.InputStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#inputStatement.
    def exitInputStatement(self, ctx:gramatykaParser.InputStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:gramatykaParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:gramatykaParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#loopStatement.
    def enterLoopStatement(self, ctx:gramatykaParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#loopStatement.
    def exitLoopStatement(self, ctx:gramatykaParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#variableAssignmentStatement.
    def enterVariableAssignmentStatement(self, ctx:gramatykaParser.VariableAssignmentStatementContext):
        pass

    # Exit a parse tree produced by gramatykaParser#variableAssignmentStatement.
    def exitVariableAssignmentStatement(self, ctx:gramatykaParser.VariableAssignmentStatementContext):
        pass


    # Enter a parse tree produced by gramatykaParser#comparison.
    def enterComparison(self, ctx:gramatykaParser.ComparisonContext):
        pass

    # Exit a parse tree produced by gramatykaParser#comparison.
    def exitComparison(self, ctx:gramatykaParser.ComparisonContext):
        pass


    # Enter a parse tree produced by gramatykaParser#notComparison.
    def enterNotComparison(self, ctx:gramatykaParser.NotComparisonContext):
        pass

    # Exit a parse tree produced by gramatykaParser#notComparison.
    def exitNotComparison(self, ctx:gramatykaParser.NotComparisonContext):
        pass


    # Enter a parse tree produced by gramatykaParser#expression.
    def enterExpression(self, ctx:gramatykaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramatykaParser#expression.
    def exitExpression(self, ctx:gramatykaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramatykaParser#term.
    def enterTerm(self, ctx:gramatykaParser.TermContext):
        pass

    # Exit a parse tree produced by gramatykaParser#term.
    def exitTerm(self, ctx:gramatykaParser.TermContext):
        pass


    # Enter a parse tree produced by gramatykaParser#codeBlock.
    def enterCodeBlock(self, ctx:gramatykaParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by gramatykaParser#codeBlock.
    def exitCodeBlock(self, ctx:gramatykaParser.CodeBlockContext):
        pass



del gramatykaParser