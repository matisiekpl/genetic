    def test_bool_9_AND_fitness(input_array, y):
        if len(y) > 1:
            return len(y)
        if len(y) == 0:
            return 1000
        return 0 if y[0] == input_array[0] and y[1] == input_array[1] and y[2] == input_array[2] and y[3] == \
                    input_array[3] and y[4] == input_array[4] and y[5] == input_array[5] and y[6] == input_array[6] and \
                    y[7] == input_array[7] and y[8] == input_array[8] else 1000
