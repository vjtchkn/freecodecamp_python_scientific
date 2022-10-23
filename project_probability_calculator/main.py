import prob_calculator
from unittest import main

# prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
for color, count in hat.balls.items():
    print(color, count)
print("Initial hat with 12 balls")
print(hat.contents)
print("Draw 3")
print(hat.draw(3))
print(hat.contents)
print("Draw 3 more")
print(hat.draw(3))
print(hat.contents)
print("Try to draw 8 with only 6 balls in the hat")
print(hat.draw(8))
print(hat.contents)

print("Probability calculator")
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat, {"blue": 1, "red": 1, "green": 1}, 3, 1000
)
print(probability)

hat = prob_calculator.Hat(black=6, red=4, green=3)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)
print(probability)

# Run unit tests automatically
main(module="test_module", exit=False)
