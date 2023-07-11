import numpy as np


def model(X: np.array, theta: np.array) -> np.array:
	"""Matrix product of X array and theta"""
	return X.dot(theta)


def cost_function(X, Y, theta):
    """Return the cost function according to the features (X), compared to the data points (Y)
    and the provided theta"""
    m = len(Y)
    return 1/(2*m) * np.sum((model(X, theta) - Y) ** 2)


def grad(X, y, theta):
	"""Return gradient"""
	m = len(y)
	return 1/m * X.T.dot(model(X, theta) - y)


def gradient_descent(X, y ,theta, learning_rate, n_iterations):
    """Gradient descent algorithm, returns theta"""
    cost_history = np.zeros(n_iterations)
    for i in range(0,  n_iterations):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history


def coeff_determination(y, pred):
    """also called r squared proportion of the variation in the dependent variable
    that is predictable from the independent variable(s)"""
    u = ((y - pred) ** 2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u / v