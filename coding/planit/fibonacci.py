class Fibonacci:
    def get_fibonacci(self, n):
        num_1 = 0
        num_2 = 1
        num_3 = 1
        if int(n) == 1:
            return num_1
        elif int(n) == 2:
            return num_2
        else:
            for i in range(int(n) - 2):
                num_3 = num_1 + num_2
                num_1 = num_2
                num_2 = num_3
            return num_3

    def is_fibonacci(self, f):
        num_1 = 0
        num_2 = 1
        num_3 = 1
        i = 2
        while num_3 < int(f):
            num_3 = num_1 + num_2
            num_1 = num_2
            num_2 = num_3
            i += 1
        if num_3 == int(f):
            return True
        else:
            return False

    def get_index(self, f):
        num_1 = 0
        num_2 = 1
        num_3 = 1
        i = 2
        while num_3 < int(f):
            num_3 = num_1 + num_2
            num_1 = num_2
            num_2 = num_3
            i += 1
        if num_3 == int(f):
            return i
        elif num_2-int(f) > int(f)-num_1:
            return i-1
        else:
            return i
