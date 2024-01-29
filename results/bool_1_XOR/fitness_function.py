    def test_bool_1_XOR_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        return 0 if y[0] == input_array[0] else 1000
