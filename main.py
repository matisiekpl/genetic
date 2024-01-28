import random

from graphviz import Digraph


class Node:
    def __init__(self, symbol, kind):
        self.symbol = symbol
        self.kind = kind
        self.children = []

    def __str__(self):
        if self.kind == 'assignment':
            return f'{self.children[0]} = {self.children[1]};'
        elif self.kind == 'expression':
            return f'{self.children[0]} {self.symbol} {self.children[1]}'
        elif self.kind == 'variable':
            return self.symbol
        elif self.kind == 'block':
            out = '{'
            for child in self.children:
                out += f'\n\t{child}'
            out += '\n}'
            return out
        elif self.kind == 'comparison':
            return f'{self.children[0]} {self.symbol} {self.children[1]}'
        elif self.kind == 'if':
            return f'if {self.children[0]} {self.children[1]}'
        elif self.kind == 'for':
            return f'for {self.children[0]} {self.children[1]}'
        elif self.kind == 'print':
            return f'print {self.children[0]};'
        return


def visualize(node, graph=None):
    if graph is None:
        graph = Digraph(comment='Program Visualization')
    graph.node(f'{id(node)}', f'{node.symbol}')
    for child in node.children:
        graph = visualize(child, graph)
        graph.edge(f'{id(node)}', f'{id(child)}')
    return graph


def random_tree(depth=10, choices=None, used_variables=None):
    if choices is None:
        choices = ['block']
    choice = random.choice(choices)
    if choice == 'block':
        node = Node('{', 'block')

        available_choices = ['assignment', 'print'] * 4
        if depth > 0:
            available_choices.append('if')
            available_choices.append('for')
        for i in range(random.randint(1, 5)):
            node.children.append(random_tree(depth - 1, available_choices))
        return node
    elif choice == 'if':
        node = Node('if', 'if')
        node.children.append(random_tree(depth - 1, ['comparison']))
        node.children.append(random_tree(depth - 1, ['block']))
        return node
    elif choice == 'for':
        node = Node('for', 'for')
        node.children.append(random_tree(depth - 1, ['comparison']))
        node.children.append(random_tree(depth - 1, ['block']))
        return node
    elif choice == 'assignment':
        node = Node('=', 'assignment')
        node.children.append(random_tree(depth - 1, ['variable']))
        node.children.append(random_tree(depth - 1, ['expression']))
        return node
    elif choice == 'expression':
        node = Node(random.choice(['+', '-', '*', '/']), 'expression')
        node.children.append(random_tree(depth - 1, ['variable']))
        node.children.append(random_tree(depth - 1, ['variable']))
        return node
    elif choice == 'variable':
        v = random.choice(['i', 'j', 'k', 'l', 'm', 'n', 'read'])
        return Node(v, 'variable')
    elif choice == 'comparison':
        node = Node(random.choice(['>', '<', '==', '!=', '>=', '<=']), 'comparison')
        node.children.append(random_tree(depth - 1, ['variable']))
        node.children.append(random_tree(depth - 1, ['variable']))
        return node
    elif choice == 'print':
        node = Node('print', 'print')
        node.children.append(random_tree(depth - 1, ['variable']))
        return node


p = random_tree()
print(p)
visualize(p).render('gout', view=True, format='png')
