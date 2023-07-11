import numpy as np


def estimate(kms: float, x_min: float = 0.0, x_range: float = 1.0, theta: np.array = [[0],[0]]) -> float:
	"""Compute the estimated price of the car"""
	user_input_normalized = (kms - x_min) / x_range
	return user_input_normalized * theta[0] + theta[1]