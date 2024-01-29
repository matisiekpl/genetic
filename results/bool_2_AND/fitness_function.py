    def test_bool_2_AND_fitness(input_array, y):
        if len(y) > k:
            return len(y)
        if len(y) == 0:
            return 1000

        return 0 if y[0] == input_array[0] and y[1] == input_array[1] else 1000
