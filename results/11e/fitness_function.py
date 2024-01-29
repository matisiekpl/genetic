    def test_11e_fitness(input_array, y):
        if len(y) == 0:
            return 1000
        return 0 if y[0] == 789 else 1000
