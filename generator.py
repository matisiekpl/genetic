import random

from graphviz import Digraph

from interpreter import check


class Node:
    def __init__(self, symbol, kind, color=None):
        self.symbol = symbol
        self.kind = kind
        self.children = []
        self.color = color

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
        elif self.kind == 'read':
            return f'{self.children[0]} = read;'
        elif self.kind == 'number':
            return self.symbol
        return

    def mutate(self):
        c = self.deepcopy()
        if random.random() < 0.8:
            mutation_point = c.get_random_node()
            new_fragment = random_program(mutation_point.get_depth())
            if len(mutation_point.children) > 0:
                mutation_point.children[0] = new_fragment
        else:
            c.remove_random_block_child()

        return c

    def get_all_block_nodes_at_any_depth(self):
        block_nodes = []
        if self.kind == 'block':
            block_nodes.append(self)
        for child in self.children:
            block_nodes += child.get_all_block_nodes_at_any_depth()
        return block_nodes

    def remove_random_block_child(self):
        block_nodes = self.get_all_block_nodes_at_any_depth()
        if len(block_nodes) > 0:
            block_node = random.choice(block_nodes)
            if len(block_node.children) > 0:
                block_node.children.remove(random.choice(block_node.children))

    def get_depth(self):
        if len(self.children) == 0:
            return 1
        else:
            return 1 + max([child.get_depth() for child in self.children])

    def get_random_node(self):
        return random.choice(self.get_all_nodes_in_subtree())

    def get_all_nodes_in_subtree(self):
        nodes = [self]
        for child in self.children:
            nodes += child.get_all_nodes_in_subtree()
        return nodes

    def replace_subtree(self, new_subtree):
        self.symbol = new_subtree.symbol
        self.kind = new_subtree.kind
        self.children = new_subtree.children

    def deepcopy(self):
        # Create a new node with the same symbol, kind, and color
        new_node = Node(self.symbol, self.kind, self.color)
        # Recursively copy all children
        for child in self.children:
            new_node.children.append(child.deepcopy())
        return new_node


def visualize(node, graph=None):
    if graph is None:
        graph = Digraph(comment='Program Visualization')
    graph.node(f'{id(node)}', f'{node.symbol}')
    for child in node.children:
        graph = visualize(child, graph)
        graph.edge(f'{id(node)}', f'{id(child)}')
    return graph


used_variables = []


def random_tree(depth=5, choices=None):
    global used_variables
    if choices is None:
        choices = ['block']
    choice = random.choice(choices)
    if choice == 'block':
        node = Node('{', 'block')
        for i in range(random.randint(2, 10)):
            available_choices = ['read']
            if len(used_variables) > 0:
                available_choices.append('assignment')
                # for _ in range(10):
                #     available_choices.append('print')
            if depth > 0 and len(used_variables) > 0:
                available_choices.append('if')
                available_choices.append('for')
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
        if node.children[1].symbol == 'read':
            used_variables.append(node.children[0].symbol)
        return node
    elif choice == 'expression':
        node = Node(random.choice(['+', '-', '*', '/']), 'expression')
        node.children.append(random_tree(depth - 1, ['variable']))
        node.children.append(random_tree(depth - 1, ['variable']))
        return node
    elif choice == 'variable':
        v = random.choice(used_variables)
        return Node(v, 'variable')
    elif choice == 'new_variable':
        v = chr(random.randint(97, 122))
        while v in used_variables:
            v = chr(random.randint(97, 122))
        used_variables.append(v)
        return Node(v, 'variable')
    elif choice == 'comparison':
        node = Node(random.choice(['>', '<', '==', '!=', '>=', '<=']), 'comparison')
        node.children.append(random_tree(depth - 1, ['variable']))
        node.children.append(random_tree(depth - 1, ['variable']))
        return node
    elif choice == 'print':
        node = Node('print', 'print')
        node.children.append(
            random_tree(depth - 1, ['variable', 'number', 'number', 'number', 'number', 'number', 'number']))
        return node
    elif choice == 'number':
        v = random.randint(-2, 20)
        return Node(str(v), 'number')
    elif choice == 'read':
        node = Node('read', 'read')
        node.children.append(random_tree(depth - 1, ['new_variable']))
        return node


def random_program(depth=5):
    global used_variables
    used_variables = []
    return random_tree(depth)


def crossover(tree1, tree2):
    if not tree1.children or not tree2.children:
        return None, None
    copied_tree1 = tree1.deepcopy()
    copied_tree2 = tree2.deepcopy()
    crossover_point1 = copied_tree1.get_random_node()
    crossover_point2 = copied_tree2.get_random_node()
    subtree1 = crossover_point1.deepcopy()
    subtree2 = crossover_point2.deepcopy()
    crossover_point1.replace_subtree(subtree2)
    crossover_point2.replace_subtree(subtree1)

    if check(str(copied_tree1)):
        return copied_tree1, copied_tree2

    return crossover(tree1, tree2)
