    def test_bool_7_OR_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        return 0 if y[0] == input_array[0] or y[1] == input_array[1] or y[2] == input_array[2] or y[3] == input_array[
            3] or y[4] == input_array[4] or y[5] == input_array[5] or y[6] == input_array[6] else 1000
