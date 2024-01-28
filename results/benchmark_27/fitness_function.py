    def benchmark_27_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 100
        return 0 if y[0] == sorted(input_array)[1] else 1000
