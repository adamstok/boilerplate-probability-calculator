import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color in kwargs:
            self.color = kwargs[color]
            for _ in range(kwargs[color]):
                self.contents.append(color)

    def draw(self, numToDraw):
        outp = []
        if numToDraw > len(self.contents):
            outp = self.contents[::]
            self.contents = []
            return outp
        else:
            for _ in range(numToDraw):
                outp.append(self.contents.pop(
                    random.randint(0, len(self.contents) - 1)))
            return outp


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
