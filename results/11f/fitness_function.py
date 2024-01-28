    def test_11f_fitness(input_array, y):
        if len(y) == 0:
            return 1000
        if len(y) > 1:
            return len(y)
        return 0 if y[0] == 1 else 1000
