    def test_bool_6_XOR_fitness(input_array, y):
        if len(y) > k:
            return len(y)
        if len(y) == 1:
            return 1000
        if len(y) == 0:
            return 1000
        return 0 if y[0] == input_array[0] ^ y[1] == input_array[1] ^ y[2] == input_array[2] ^ y[3] == input_array[3] ^ \
                    y[4] == input_array[4] ^ y[5] == input_array[5] else 1000
