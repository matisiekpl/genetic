    def benchmark_1_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 100
        return 0 if y[0] == input_array[0] + input_array[1] else 1000
