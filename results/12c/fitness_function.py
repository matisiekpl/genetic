    def test_12c_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        s = input_array[0] + input_array[1]
        return abs(s - y[0])
