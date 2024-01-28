import inspect
import os
import random
import numpy as np
from tqdm import tqdm
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

import generator
import interpreter


def run(program, input_array):
    # TODO uruchom program i zwróć wynik
    y = interpreter.interpret(str(program), input_array)
    if len(y) == 0:
        # print('INVALID PROGRAM')
        return []
    return y


class Individual:
    def __init__(self, label, program, input_set, F):
        self.label = label
        self.program = program
        self.input_set = input_set
        self.F = F
        self.fit = 0

    def fitness(self):
        fit = 0
        for input_array in self.input_set:
            y = run(self.program, input_array)
            fit += self.F(input_array, y)
        if fit == 0:
            if not os.path.exists(f'results/{self.label}'):
                os.makedirs(f'results/{self.label}')
            with open(f'results/{self.label}/best_program.txt', 'w') as f:
                f.write(str(self.program))
        self.fit = fit
        return self.fit

    def code(self):
        return str(self.program)


class Generation:
    def __init__(self, label, input_set, F):
        self.label = label
        self.input_set = input_set
        self.F = F
        self.population = []
        self.fit = []
        self.best_fitness = 0
        self.best_fitness_index = 0
        self.average_fitness = 0

    def calculate(self):
        self.best_fitness = min(self.fit)
        self.average_fitness = np.mean(self.fit)
        self.best_fitness_index = self.fit.index(self.best_fitness)

        if not os.path.exists(f'results/{self.label}'):
            os.makedirs(f'results/{self.label}')
        with open(f'results/{self.label}/best_program.txt', 'w') as f:
            # print(self.population[self.best_fitness_index].code())
            f.write(self.population[self.best_fitness_index].code())

        return self.best_fitness, self.average_fitness

    def best(self):
        return self.population[self.best_fitness_index]

    def spawn(self, previous_generation=None):
        individual = self.generate(previous_generation)
        individual_fitness = individual.fitness()
        if individual_fitness == -1:
            self.spawn(previous_generation)
            return
        self.fit.append(individual_fitness)
        self.population.append(individual)

    def generate(self, previous_generation=None):
        if previous_generation is None:
            program = generator.random_program()
            return Individual(self.label, program, self.input_set, self.F)
        else:
            latest_population = previous_generation.population
            sorted_population = sorted(latest_population, key=lambda x: x.fit)
            if random.random() < 0.5:
                # TODO skrzyżuj najlepszego osobnika z drugim najlepszym
                best = sorted_population[0]
                second_best = sorted_population[1]
                crossed = generator.crossover(best.program, second_best.program)[0]
                return Individual(self.label, crossed, self.input_set, self.F)
            else:
                best = sorted_population[0]
                # TODO zmutuj najlepszego osobnika
                mutated = best.program.mutate()
                return Individual(self.label, mutated, self.input_set, self.F)

    def fitness(self):
        return np.mean(self.fit)


# simulate przeprowadza ewolucję. Przyjmuje rows tworząc tablicę wejścia i przekszałca go w output_text
# według funkcji F. Następnie tworzy wybraną ilość pokoleń. W każdym pokoleniu tworzy nowych osobników mutując lub
# krzyżując najlepszych
def simulate(label, input_set, F, population_count=1000, generations_count=100):
    try:
        generations = {}
        best_fitness_history = []
        average_fitness_history = []
        for generation in range(generations_count):

            # Stwórz pokolenie i dodaj population_count osobników
            gen = Generation(label, input_set, F)
            for i in tqdm(range(population_count)):
                if generation > 0:
                    gen.spawn(generations[generation - 1])
                else:
                    gen.spawn()

            best_fitness, average_fitness = gen.calculate()
            best_fitness_history.append(best_fitness)
            average_fitness_history.append(average_fitness)
            print(f'Generation #{generation + 1}: avg fitness: {gen.fitness()}, best fitness: {gen.best().fitness()}')

            if best_fitness == 0:
                print('Found solution')
                plt.clf()
                if len(best_fitness_history) > 1:
                    plt.plot(best_fitness_history, label='best')
                    plt.plot(average_fitness_history, label='average')
                else:
                    plt.plot(best_fitness_history, label='best', marker='o', markersize=3)
                    plt.plot(average_fitness_history, label='average', marker='o', markersize=3)
                plt.legend()
                plt.title('Fitness')
                plt.savefig(f'results/{label}/fitness.png')
                return best_fitness
            generations[generation] = gen

        plt.clf()
        if len(best_fitness_history) > 1:
            plt.plot(best_fitness_history, label='best')
            plt.plot(average_fitness_history, label='average')
        else:
            plt.plot(best_fitness_history, label='best', marker='o', markersize=3)
            plt.plot(average_fitness_history, label='average', marker='o', markersize=3)
        plt.legend()
        plt.title('Fitness')
        plt.savefig(f'results/{label}/fitness.png')
        return best_fitness
    except Exception as e:
        raise e
        print(e)
        return 99999


POP = 1000
GEN = 3


# 1.1.A Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 1.
# Poza liczbą 1 może też zwrócić inne liczby.
def test_11a():
    def test_11a_fitness(input_array, y):
        return 0 if 1 in y else 1000

    fitness_function = inspect.getsource(test_11a_fitness)
    return fitness_function, simulate('11a', [[1, 2], [3, 4]], test_11a_fitness, POP, GEN)


# 1.1.B Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 789.
# Poza liczbą 789 może też zwrócić inne liczby.
def test_11b():
    def test_11b_fitness(input_array, y):
        return 0 if 789 in y else 1000

    fitness_function = inspect.getsource(test_11b_fitness)
    return fitness_function, simulate('11b', [[1, 2], [3, 4]], test_11b_fitness, POP, GEN)


# 1.1.C Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 31415.
# Poza liczbą 31415 może też zwrócić inne liczby.
def test_11c():
    def test_11c_fitness(input_array, y):
        return 0 if 31415 in y else 1000

    fitness_function = inspect.getsource(test_11c_fitness)
    return fitness_function, simulate('11c', [[1, 2], [3, 4]], test_11c_fitness, POP, GEN)


# 1.1.D Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.
def test_11d():
    def test_11d_fitness(input_array, y):
        if len(y) == 0:
            return 1000
        return 0 if y[0] == 1 else 1000

    fitness_function = inspect.getsource(test_11d_fitness)
    return fitness_function, simulate('11d', [[1, 2], [3, 4]], test_11d_fitness, POP, GEN)


# 1.1.E Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.
def test_11e():
    def test_11e_fitness(input_array, y):
        if len(y) == 0:
            return 1000
        return 0 if y[0] == 789 else 1000

    fitness_function = inspect.getsource(test_11e_fitness)
    return fitness_function, simulate('11e', [[1, 2], [3, 4]], test_11e_fitness, POP, GEN)


# 1.1.F Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. Poza liczbą 1 NIE powinien nic więcej wygenerować.
def test_11f():
    def test_11f_fitness(input_array, y):
        if len(y) == 0:
            return 1000
        if len(y) > 1:
            return len(y)
        return 0 if y[0] == 1 else 1000

    fitness_function = inspect.getsource(test_11f_fitness)
    return fitness_function, simulate('11f', [[1, 2], [3, 4]], test_11f_fitness, POP, GEN)


# 1.2.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
# Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]
def test_12b():
    def test_12b_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        s = input_array[0] + input_array[1]
        return abs(s - y[0])

    fitness_function = inspect.getsource(test_12b_fitness)
    return fitness_function, simulate('12b', [[1, 2], [3, 4]], test_12b_fitness, POP, GEN)


# 1.2.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
# Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]
def test_12a():
    def test_12a_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        s = input_array[0] + input_array[1]
        return abs(s - y[0])

    fitness_function = inspect.getsource(test_12a_fitness)
    return fitness_function, simulate('12a', [[1, 2], [3, 4], [5, 6], [7, 8], [9, 8]], test_12a_fitness, POP, GEN)


# 1.2.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
# Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]
def test_12b():
    def test_12b_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        s = input_array[0] + input_array[1]
        return abs(s - y[0])

    fitness_function = inspect.getsource(test_12b_fitness)
    return fitness_function, simulate('12b', [[1, 2], [3, 4]], test_12b_fitness, POP, GEN)


# 1.2.C Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
# Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
def test_12c():
    def test_12c_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        s = input_array[0] + input_array[1]
        return abs(s - y[0])

    fitness_function = inspect.getsource(test_12c_fitness)
    return fitness_function, simulate('12c', [[1, 2], [3, 4]], test_12c_fitness, POP, GEN)


# 1.2.D Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich różnicę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
def test_12d():
    def test_12d_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        s = input_array[0] - input_array[1]
        return abs(s - y[0])

    fitness_function = inspect.getsource(test_12d_fitness)
    return fitness_function, simulate('12d', [[1, 2], [3, 4]], test_12d_fitness, POP, GEN)


# 1.2.E Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich iloczyn. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
def test_12e():
    def test_12e_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        s = input_array[0] * input_array[1]
        return abs(s - y[0])

    fitness_function = inspect.getsource(test_12e_fitness)
    return fitness_function, simulate('12e', [[1, 2], [3, 4]], test_12e_fitness, POP, GEN)


# 1.3.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]
def test_13a():
    def test_13a_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        if input_array[0] > input_array[1]:
            return 0 if y[0] == input_array[0] else 1000
        else:
            return 0 if y[0] == input_array[1] else 1000

    fitness_function = inspect.getsource(test_13a_fitness)
    return fitness_function, simulate('13a', [[1, 2], [3, 4]], test_13a_fitness, POP, GEN)


# def 1.3.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999]
def test_13b():
    def test_13b_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        if input_array[0] > input_array[1]:
            return 0 if y[0] == input_array[0] else 1000
        else:
            return 0 if y[0] == input_array[1] else 1000

    fitness_function = inspect.getsource(test_13b_fitness)
    return fitness_function, simulate('13b', [[1, 2], [3, 4]], test_13b_fitness, POP, GEN)


# 1.4.A Program powinien odczytać dziesięć pierwszych liczy z wejścia i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99]
def test_14a():
    def test_14a_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        avg = sum(input_array) / len(input_array)
        return abs(avg - y[0])

    fitness_function = inspect.getsource(test_14a_fitness)
    return fitness_function, simulate('14a', [[1, 2], [3, 4]], test_14a_fitness, POP, GEN)


# 1.4.B Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna) a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana pierwsza odczytana liczba, która mówi z ilu liczb chcemy obliczyć średnią). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].
def test_14b():
    def test_14b_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        avg = sum(input_array[1:]) / len(input_array[1:])
        return abs(avg - y[0])

    fitness_function = inspect.getsource(test_14b_fitness)
    return fitness_function, simulate('14b', [[1, 2], [3, 4]], test_14b_fitness, POP, GEN)


def test_bool_1_AND():
    k = 1

    def test_bool_1_AND_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        return 0 if y[0] == 0 else 1000

    fitness_function = inspect.getsource(test_bool_1_AND_fitness)
    return fitness_function, simulate('bool_1_AND', [[random.randint(0, 1) for _ in range(k)] for i in range(100)],
                                      test_bool_1_AND_fitness, POP, GEN)


def test_bool_1_OR():
    k = 1

    def test_bool_1_OR_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        return 0 if y[0] == input_array[0] else 1000

    fitness_function = inspect.getsource(test_bool_1_OR_fitness)
    return fitness_function, simulate('bool_1_OR', [[random.randint(0, 1) for _ in range(k)] for i in range(100)],
                                      test_bool_1_OR_fitness, POP, GEN)


def test_bool_1_XOR():
    k = 1

    def test_bool_1_XOR_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        return 0 if y[0] == input_array[0] else 1000

    fitness_function = inspect.getsource(test_bool_1_XOR_fitness)
    return fitness_function, simulate('bool_1_XOR', [[random.randint(0, 1) for _ in range(k)] for i in range(100)],
                                      test_bool_1_XOR_fitness, POP, GEN)


def test_bool_2_AND():
    k = 2

    def test_bool_2_AND_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        return 0 if y[0] == input_array[0] and y[1] == input_array[1] else 1000

    fitness_function = inspect.getsource(test_bool_2_AND_fitness)
    return fitness_function, simulate('bool_2_AND', [[random.randint(0, 1) for _ in range(k)] for i in range(100)],
                                      test_bool_2_AND_fitness, POP, GEN)


def test_bool_2_OR():
    k = 2

    def test_bool_2_OR_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        return 0 if y[0] == input_array[0] or y[1] == input_array[1] else 1000

    fitness_function = inspect.getsource(test_bool_2_OR_fitness)
    return fitness_function, simulate('bool_2_OR', [[random.randint(0, 1) for _ in range(k)] for i in range(100)],
                                      test_bool_2_OR_fitness, POP, GEN)


def test_bool_2_XOR():
    k = 2

    def test_bool_2_XOR_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 1:
            return 1000
        if len(y) == 0:
            return 1000

        return 0 if y[0] == input_array[0] ^ y[1] == input_array[1] else 1000

    fitness_function = inspect.getsource(test_bool_2_XOR_fitness)
    return fitness_function, simulate('bool_2_XOR', [[random.randint(0, 1) for _ in range(k)] for i in range(100)],
                                      test_bool_2_XOR_fitness, POP, GEN)


tests = [
    # ('11a', test_11a),
    # ('11b', test_11b),
    # ('11c', test_11c),
    # ('11d', test_11d),
    # ('11e', test_11e),
    # ('11f', test_11f),
    # ('12b', test_12b),
    # ('12a', test_12a),
    # ('12c', test_12c),
    # ('12d', test_12d),
    # ('12e', test_12e),
    # ('13a', test_13a),
    # ('13b', test_13b),
    # ('14a', test_14a),
    # ('14b', test_14b),
    # ('bool_1_AND', test_bool_1_AND),
    ('bool_1_OR', test_bool_1_OR),
    # ('bool_1_XOR', test_bool_1_XOR),
    # ('bool_2_AND', test_bool_2_AND),
    # ('bool_2_OR', test_bool_2_OR),
    # ('bool_2_XOR', test_bool_2_XOR),
]


def run_all():
    summary = ''
    for label, test in tests:
        print('Running:', label)
        if not os.path.exists(f'results/{label}'):
            os.makedirs(f'results/{label}')
        fitness_function, best_fitness = test()
        with open(f'results/{label}/best_fitness.txt', 'w') as f:
            f.write(str(best_fitness))
        with open(f'results/{label}/fitness_function.py', 'w') as f:
            f.write(fitness_function)
        summary += f'{label}: {best_fitness}\n'
    with open('summary.txt', 'w') as f:
        f.write(summary)


run_all()
