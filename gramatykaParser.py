# Generated from gramatyka.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,157,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        5,0,29,8,0,10,0,12,0,32,9,0,3,0,34,8,0,1,0,5,0,37,8,0,10,0,12,0,
        40,9,0,1,0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,5,0,49,8,0,10,0,12,0,
        52,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,
        2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,79,8,5,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,3,7,89,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,97,
        8,8,1,8,1,8,1,8,5,8,102,8,8,10,8,12,8,105,9,8,1,9,1,9,1,9,1,10,1,
        10,1,10,3,10,113,8,10,1,10,1,10,1,10,5,10,118,8,10,10,10,12,10,121,
        9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,131,8,11,1,11,
        1,11,1,11,5,11,136,8,11,10,11,12,11,139,9,11,1,12,1,12,5,12,143,
        8,12,10,12,12,12,146,9,12,1,12,1,12,5,12,150,8,12,10,12,12,12,153,
        9,12,1,12,1,12,1,12,0,3,16,20,22,13,0,2,4,6,8,10,12,14,16,18,20,
        22,24,0,4,1,0,8,13,1,0,14,15,1,0,17,18,1,0,21,22,164,0,33,1,0,0,
        0,2,64,1,0,0,0,4,66,1,0,0,0,6,68,1,0,0,0,8,71,1,0,0,0,10,73,1,0,
        0,0,12,80,1,0,0,0,14,84,1,0,0,0,16,96,1,0,0,0,18,106,1,0,0,0,20,
        112,1,0,0,0,22,130,1,0,0,0,24,140,1,0,0,0,26,34,3,2,1,0,27,29,5,
        27,0,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,
        34,1,0,0,0,32,30,1,0,0,0,33,26,1,0,0,0,33,30,1,0,0,0,34,44,1,0,0,
        0,35,37,5,27,0,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,43,3,2,1,0,42,38,1,0,0,0,
        43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,50,1,0,0,0,46,44,1,
        0,0,0,47,49,5,27,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,
        51,1,0,0,0,51,1,1,0,0,0,52,50,1,0,0,0,53,54,3,6,3,0,54,55,5,1,0,
        0,55,65,1,0,0,0,56,57,3,8,4,0,57,58,5,1,0,0,58,65,1,0,0,0,59,65,
        3,10,5,0,60,65,3,12,6,0,61,62,3,14,7,0,62,63,5,1,0,0,63,65,1,0,0,
        0,64,53,1,0,0,0,64,56,1,0,0,0,64,59,1,0,0,0,64,60,1,0,0,0,64,61,
        1,0,0,0,65,3,1,0,0,0,66,67,5,26,0,0,67,5,1,0,0,0,68,69,5,2,0,0,69,
        70,3,20,10,0,70,7,1,0,0,0,71,72,5,3,0,0,72,9,1,0,0,0,73,74,5,4,0,
        0,74,75,3,16,8,0,75,78,3,24,12,0,76,77,5,5,0,0,77,79,3,24,12,0,78,
        76,1,0,0,0,78,79,1,0,0,0,79,11,1,0,0,0,80,81,5,6,0,0,81,82,3,16,
        8,0,82,83,3,24,12,0,83,13,1,0,0,0,84,85,3,4,2,0,85,88,5,7,0,0,86,
        89,3,20,10,0,87,89,3,8,4,0,88,86,1,0,0,0,88,87,1,0,0,0,89,15,1,0,
        0,0,90,91,6,8,-1,0,91,92,3,20,10,0,92,93,7,0,0,0,93,94,3,20,10,0,
        94,97,1,0,0,0,95,97,3,18,9,0,96,90,1,0,0,0,96,95,1,0,0,0,97,103,
        1,0,0,0,98,99,10,1,0,0,99,100,7,1,0,0,100,102,3,16,8,2,101,98,1,
        0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,17,1,0,
        0,0,105,103,1,0,0,0,106,107,5,16,0,0,107,108,3,16,8,0,108,19,1,0,
        0,0,109,110,6,10,-1,0,110,113,3,22,11,0,111,113,3,8,4,0,112,109,
        1,0,0,0,112,111,1,0,0,0,113,119,1,0,0,0,114,115,10,2,0,0,115,116,
        7,2,0,0,116,118,3,20,10,3,117,114,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,21,1,0,0,0,121,119,1,0,0,0,122,123,6,
        11,-1,0,123,131,5,25,0,0,124,131,3,4,2,0,125,131,3,8,4,0,126,127,
        5,19,0,0,127,128,3,20,10,0,128,129,5,20,0,0,129,131,1,0,0,0,130,
        122,1,0,0,0,130,124,1,0,0,0,130,125,1,0,0,0,130,126,1,0,0,0,131,
        137,1,0,0,0,132,133,10,1,0,0,133,134,7,3,0,0,134,136,3,22,11,2,135,
        132,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,
        23,1,0,0,0,139,137,1,0,0,0,140,144,5,23,0,0,141,143,5,27,0,0,142,
        141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,
        147,1,0,0,0,146,144,1,0,0,0,147,151,3,0,0,0,148,150,5,27,0,0,149,
        148,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,
        154,1,0,0,0,153,151,1,0,0,0,154,155,5,24,0,0,155,25,1,0,0,0,16,30,
        33,38,44,50,64,78,88,96,103,112,119,130,137,144,151
    ]

class gramatykaParser ( Parser ):

    grammarFileName = "gramatyka.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'print '", "'read'", "'if '", 
                     "' else '", "'for '", "'='", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "' and '", "' or '", "'not'", 
                     "'+'", "'-'", "'('", "')'", "'*'", "'/'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTEGER", "STRING", "NL", "WS" ]

    RULE_main = 0
    RULE_statement = 1
    RULE_name = 2
    RULE_printStatement = 3
    RULE_inputStatement = 4
    RULE_conditionalStatement = 5
    RULE_loopStatement = 6
    RULE_variableAssignmentStatement = 7
    RULE_comparison = 8
    RULE_notComparison = 9
    RULE_expression = 10
    RULE_term = 11
    RULE_codeBlock = 12

    ruleNames =  [ "main", "statement", "name", "printStatement", "inputStatement", 
                   "conditionalStatement", "loopStatement", "variableAssignmentStatement", 
                   "comparison", "notComparison", "expression", "term", 
                   "codeBlock" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    INTEGER=25
    STRING=26
    NL=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.StatementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatykaParser.NL)
            else:
                return self.getToken(gramatykaParser.NL, i)

        def getRuleIndex(self):
            return gramatykaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = gramatykaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 26
                self.statement()
                pass

            elif la_ == 2:
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 27
                        self.match(gramatykaParser.NL) 
                    self.state = 32
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass


            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==27:
                        self.state = 35
                        self.match(gramatykaParser.NL)
                        self.state = 40
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 41
                    self.statement() 
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 47
                    self.match(gramatykaParser.NL) 
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStatement(self):
            return self.getTypedRuleContext(gramatykaParser.PrintStatementContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(gramatykaParser.InputStatementContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(gramatykaParser.ConditionalStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(gramatykaParser.LoopStatementContext,0)


        def variableAssignmentStatement(self):
            return self.getTypedRuleContext(gramatykaParser.VariableAssignmentStatementContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = gramatykaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.printStatement()
                self.state = 54
                self.match(gramatykaParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.inputStatement()
                self.state = 57
                self.match(gramatykaParser.T__0)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.conditionalStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.loopStatement()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.variableAssignmentStatement()
                self.state = 62
                self.match(gramatykaParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramatykaParser.STRING, 0)

        def getRuleIndex(self):
            return gramatykaParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = gramatykaParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(gramatykaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = gramatykaParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(gramatykaParser.T__1)

            self.state = 69
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatykaParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)




    def inputStatement(self):

        localctx = gramatykaParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(gramatykaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(gramatykaParser.ComparisonContext,0)


        def codeBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.CodeBlockContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.CodeBlockContext,i)


        def getRuleIndex(self):
            return gramatykaParser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)




    def conditionalStatement(self):

        localctx = gramatykaParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(gramatykaParser.T__3)
            self.state = 74
            self.comparison(0)
            self.state = 75
            self.codeBlock()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 76
                self.match(gramatykaParser.T__4)
                self.state = 77
                self.codeBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(gramatykaParser.ComparisonContext,0)


        def codeBlock(self):
            return self.getTypedRuleContext(gramatykaParser.CodeBlockContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)




    def loopStatement(self):

        localctx = gramatykaParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(gramatykaParser.T__5)
            self.state = 81
            self.comparison(0)
            self.state = 82
            self.codeBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(gramatykaParser.NameContext,0)


        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(gramatykaParser.InputStatementContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_variableAssignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableAssignmentStatement" ):
                listener.enterVariableAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableAssignmentStatement" ):
                listener.exitVariableAssignmentStatement(self)




    def variableAssignmentStatement(self):

        localctx = gramatykaParser.VariableAssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableAssignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.name()
            self.state = 85
            self.match(gramatykaParser.T__6)
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 86
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 87
                self.inputStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.ExpressionContext,i)


        def notComparison(self):
            return self.getTypedRuleContext(gramatykaParser.NotComparisonContext,0)


        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.ComparisonContext,i)


        def getRuleIndex(self):
            return gramatykaParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)



    def comparison(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatykaParser.ComparisonContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_comparison, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 19, 25, 26]:
                self.state = 91
                self.expression(0)
                self.state = 92
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93
                self.expression(0)
                pass
            elif token in [16]:
                self.state = 95
                self.notComparison()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramatykaParser.ComparisonContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_comparison)
                    self.state = 98
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 99
                    _la = self._input.LA(1)
                    if not(_la==14 or _la==15):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 100
                    self.comparison(2) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NotComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(gramatykaParser.ComparisonContext,0)


        def getRuleIndex(self):
            return gramatykaParser.RULE_notComparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotComparison" ):
                listener.enterNotComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotComparison" ):
                listener.exitNotComparison(self)




    def notComparison(self):

        localctx = gramatykaParser.NotComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_notComparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(gramatykaParser.T__15)
            self.state = 107
            self.comparison(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(gramatykaParser.TermContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(gramatykaParser.InputStatementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return gramatykaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatykaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 110
                self.term(0)
                pass

            elif la_ == 2:
                self.state = 111
                self.inputStatement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramatykaParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 114
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 115
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 116
                    self.expression(3) 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(gramatykaParser.INTEGER, 0)

        def name(self):
            return self.getTypedRuleContext(gramatykaParser.NameContext,0)


        def inputStatement(self):
            return self.getTypedRuleContext(gramatykaParser.InputStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(gramatykaParser.ExpressionContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatykaParser.TermContext)
            else:
                return self.getTypedRuleContext(gramatykaParser.TermContext,i)


        def getRuleIndex(self):
            return gramatykaParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramatykaParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 123
                self.match(gramatykaParser.INTEGER)
                pass
            elif token in [26]:
                self.state = 124
                self.name()
                pass
            elif token in [3]:
                self.state = 125
                self.inputStatement()
                pass
            elif token in [19]:
                self.state = 126
                self.match(gramatykaParser.T__18)
                self.state = 127
                self.expression(0)
                self.state = 128
                self.match(gramatykaParser.T__19)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramatykaParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 132
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 133
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 134
                    self.term(2) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CodeBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(gramatykaParser.MainContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatykaParser.NL)
            else:
                return self.getToken(gramatykaParser.NL, i)

        def getRuleIndex(self):
            return gramatykaParser.RULE_codeBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeBlock" ):
                listener.enterCodeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeBlock" ):
                listener.exitCodeBlock(self)




    def codeBlock(self):

        localctx = gramatykaParser.CodeBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_codeBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(gramatykaParser.T__22)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 141
                    self.match(gramatykaParser.NL) 
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 147
            self.main()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 148
                self.match(gramatykaParser.NL)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(gramatykaParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.comparison_sempred
        self._predicates[10] = self.expression_sempred
        self._predicates[11] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def comparison_sempred(self, localctx:ComparisonContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




