import numpy as np


def estimate(estimation: float, x_min: float, x_range: float, theta: np.array = [[0],[0]]) -> float:
	user_input_normalized = (estimation - x_min) / x_range
	return user_input_normalized * theta[0] + theta[1]