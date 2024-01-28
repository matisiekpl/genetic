    def benchmark_17_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 100
        return 0 if y[0] == sum([i ** 2 for i in range(1, input_array[0] + 1)]) else 1000
