    def test_bool_10_OR_fitness(input_array, y):
        if len(y) > k:
            return len(y)
        if len(y) == 0:
            return 100
        return 0 if y[0] == input_array[0] or y[1] == input_array[1] or y[2] == input_array[2] or y[3] == input_array[
            3] or y[4] == input_array[4] or y[5] == input_array[5] or y[6] == input_array[6] or y[7] == input_array[
                        7] or y[8] == input_array[8] or y[9] == input_array[9] else 1000
