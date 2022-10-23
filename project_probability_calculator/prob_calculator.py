import copy
import random


class Hat:
    def __init__(self, **b):
        self.balls = b
        self.contents = []
        for color in self.balls:
            for _ in range(self.balls[color]):
                self.contents.append(color)

    def draw(self, n):
        drawn = []
        if n > len(self.contents):
            n = len(self.contents)
        for _ in range(n):
            ball = self.contents.pop(random.randrange(len(self.contents)))
            drawn.append(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_expected = 0
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        draw = h.draw(num_balls_drawn)
        draw_count = {}
        for color in hat.balls:
            draw_count[color] = draw.count(color)
        expected = True
        for color in expected_balls:
            if draw_count[color] < expected_balls[color]:
                expected = False
        if expected:
            count_expected += 1
    return count_expected / num_experiments
