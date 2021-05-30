
import math
import unittest
def wallis(x):
    n = 2
    product = 1
    for i in range(x):
        term = n**2 /(n**2 - 1)
        product *= term
        n += 2

    return 2*product





import random
import math
def monte_carlo(x):
    circle_inside_points = 0
    square_inside_points = 0
    for i in range(x):
        rand_x=random.uniform(-1,1)
        rand_y=random.uniform(-1,1)
        distance=math.sqrt(rand_x**2 + rand_y**2)


        if(distance<1):
            circle_inside_points += 1

        square_inside_points += 1


        pi= (4*circle_inside_points)/square_inside_points

    return pi


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        
@@ -30,3 +65,8 @@ def test_accuracy(self):

if __name__ == "__main__":
    unittest.main()




