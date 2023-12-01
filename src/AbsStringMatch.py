class AbsStringMatch:
    def __init__(self):
        self.iteration_counter = 0

    def cmp(self, x, y):
        self.iteration_counter += 1
        return x == y
