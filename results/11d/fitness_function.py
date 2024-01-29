    def test_11d_fitness(input_array, y):
        if len(y) == 0:
            return 1000
        return 0 if y[0] == 1 else 1000
