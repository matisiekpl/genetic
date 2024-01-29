    def test_14b_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        avg = sum(input_array[1:]) / len(input_array[1:])
        return abs(avg - y[0])
