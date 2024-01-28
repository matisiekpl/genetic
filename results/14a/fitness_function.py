    def test_14a_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000

        avg = sum(input_array) / len(input_array)
        return abs(avg - y[0])
