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
    count_balls = 0
    count_got_it = 0
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        hat_outp = h.draw(num_balls_drawn)
        for b in expected_balls:
            if hat_outp.count(b) >= expected_balls[b]:
                count_balls += 1
        if count_balls == len(expected_balls):
            count_got_it += 1
        count_balls = 0
    return count_got_it / num_experiments
