import os

import numpy as np
from antlr4 import *
from gramatykaLexer import gramatykaLexer
from gramatykaParser import gramatykaParser
import sys

SHOW_VISITS = False


# noinspection PyPep8Naming
class GeneticProgramInterpreter(ParseTreeListener):
    def __init__(self, input_array):
        self.input_array = input_array
        self.counter = 0
        self.output_array = []
        self.variables = {}
        self.instructions = 0

    def instruction(self):
        self.instructions += 1
        if self.instructions > 1000:
            raise Exception("Too many instructions")
        return False

    def output(self):
        return self.output_array

    def enterMain(self, ctx):
        if SHOW_VISITS:
            print("visit_main")
        for statement in ctx.statement():
            self.enterStatement(statement)

    def enterStatement(self, ctx: gramatykaParser.StatementContext):
        if self.instruction():
            return
        if SHOW_VISITS:
            print("visit_statement")
        if ctx.printStatement():
            self.enterPrintStatement(ctx.printStatement())
        elif ctx.inputStatement():
            self.enterInputStatement(ctx.inputStatement())
        elif ctx.conditionalStatement():
            self.enterConditionalStatement(ctx.conditionalStatement())
        elif ctx.loopStatement():
            self.enterLoopStatement(ctx.loopStatement())
        elif ctx.variableAssignmentStatement():
            self.enterVariableAssignmentStatement(ctx.variableAssignmentStatement())

    def enterPrintStatement(self, ctx):
        if SHOW_VISITS:
            print("visit_print")
        self.output_array.append(self.enterExpression(ctx.expression()))

    def enterInputStatement(self, ctx):
        if SHOW_VISITS:
            print("visit_input")
        value = self.input_array[self.counter]
        self.counter += 1
        if self.counter >= len(self.input_array):
            self.counter = 0
        return float(value)

    def enterConditionalStatement(self, ctx):
        if SHOW_VISITS:
            print("visit_conditional")
        if self.enterComparison(ctx.comparison()):
            self.enterCodeBlock(ctx.codeBlock(0))
        elif len(ctx.codeBlock()) > 1:
            self.enterCodeBlock(ctx.codeBlock(1))

    def enterLoopStatement(self, ctx):
        if SHOW_VISITS:
            print("visit_loop")
        if self.instruction():
            return
        while self.enterComparison(ctx.comparison()):
            self.enterCodeBlock(ctx.codeBlock())

    def enterVariableAssignmentStatement(self, ctx):
        if SHOW_VISITS:
            print("visit_assignment")
        name = ctx.name()
        value = self.enterExpression(ctx.expression())
        self.variables[name.getText()] = value

    def enterComparison(self, ctx):
        if SHOW_VISITS:
            print("visit_comparision")

        if ctx.notComparison():
            return self.enterNotComparison(ctx.notComparition())
        left = self.enterExpression(ctx.expression(0))
        op = ctx.getChild(1).getText()
        right = self.enterExpression(ctx.expression(1))
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right

    def enterNotComparison(self, ctx):
        return not ctx

    def enterExpression(self, ctx: gramatykaParser.ExpressionContext):
        if SHOW_VISITS:
            print("visit_expression")
        if ctx.term():
            return self.enterTerm(ctx.term())
        elif ctx.inputStatement():
            return self.enterInputStatement(ctx.inputStatement())
        elif ctx.expression():
            left = self.enterExpression(ctx.expression(0))
            right = self.enterExpression(ctx.expression(1))

            # if left is None or right is None:
            #     print(ctx.getText())
            #     print("ERROR")

            if ctx.getChild(1).getText() == '+':
                return left + right
            elif ctx.getChild(1).getText() == '-':
                return left - right

    def enterTerm(self, ctx: gramatykaParser.TermContext):
        if SHOW_VISITS:
            print("visit_term")
        if ctx.name():
            # print('VAR', ctx.name().getText())
            name = ctx.name().getText()
            if name not in self.variables:
                self.variables[name] = 0
            return self.variables[name]
        elif ctx.INTEGER():
            return float(ctx.INTEGER().getText())
        elif ctx.expression():
            return self.enterExpression(ctx.expression())
        elif ctx.term():
            left = self.enterTerm(ctx.term(0))
            right = self.enterTerm(ctx.term(1))

            if ctx.getChild(1).getText() == '*':
                return left * right
            elif ctx.getChild(1).getText() == '/':
                return left / right

    def enterCodeBlock(self, ctx):
        if SHOW_VISITS:
            print("visit_block")
        if ctx.main():
            self.enterMain(ctx.main())


def check(program):
    input_stream = InputStream(program)
    lexer = gramatykaLexer(input_stream)
    lexer.removeErrorListeners()
    token_stream = CommonTokenStream(lexer)
    parser = gramatykaParser(token_stream)
    parser.removeErrorListeners()
    try:
        parser.main()
        return True
    except Exception as e:
        return False


def interpret(program, input_array):
    program = program[1:]
    program = program[:-1]

    lexer = gramatykaLexer(InputStream(program))
    lexer.removeErrorListeners()
    token_stream = CommonTokenStream(lexer)
    parser = gramatykaParser(token_stream)
    parser.removeErrorListeners()
    tree = parser.main()

    interpreter = GeneticProgramInterpreter(input_array)
    try:
        interpreter.enterMain(tree)
        y = interpreter.output()
        for r in y:
            if np.isnan(r):
                return []
    except Exception as e:
        return []
    return y
