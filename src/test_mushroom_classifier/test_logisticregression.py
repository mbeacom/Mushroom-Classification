import unittest
from mushroom_classifier.logisticregression import LogisticRegression
import numpy as np

class LogisticRegressionTests(unittest.TestCase):
    def setUp(self):
        self.test_X = np.ndarray(shape=(2,2), dtype=int, buffer=np.array([[1,2],[3,4]]))
        self.test_y = np.ndarray(shape=(2,), dtype=int, buffer=np.array([1, 0]))
        self.test_theta = [0.2, 0.8]

    def test_hypothesis(self):
        expected_hypothesis=[0.85814894, 0.97811873]
        sut = LogisticRegression()

        actual_hypothesis = sut.hypothesis(self.test_X, self.test_theta)

        np.testing.assert_array_almost_equal(expected_hypothesis, actual_hypothesis, decimal=8)

    def test_cost_function(self):
        expected_cost = 0.22314355
        test_hypothesis=np.ndarray(shape=(1, 2), dtype=float, buffer=np.array([0.8, 0.2]))
        sut = LogisticRegression()

        actual_cost = sut.cost_function(test_hypothesis, self.test_y)

        self.assertAlmostEqual(expected_cost, actual_cost, places=7)
        
if __name__ == "__main__":
    unittest.main()