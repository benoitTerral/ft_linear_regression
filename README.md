# ft_linear_regression

A 42 project

The aim of this project is to introduce you to the basic concept behind machine learning.
For this project, you will have to create a program that predicts the price of a car by
using a `linear function` train with a `gradient descent algorithm`.

> The use of python’s numpy.polyfit (or any other library such as scipy) is considered cheating.

## Goal

Perform a linear regression on the below dataset:

![Screenshots](/graphs/dataset_scatterplot.png)

In order to provide a program accepting the mileage as an input and estimate the price of a used car.

## Usage

Git clone the repository.

Train the model:
`<python-binary> programs/train.py`

> Training the program generates a pickle file containing the theta in in the notebook folder. This data file is a parameter of the estimation program.

Estimate the price of a used car:
`<python-binary> programs/estimate.py`

Check the results in `notebook/train.ipynb`

A prompt will invite users to insert odometer values and returns the expected price according to the linear regression.

> If there is no trained model, theta values are 0.

## Linear regression explanation

### Model

Linear regression aims to find the `a` and `b` parameters:

$$f(x) = ax + b$$

> At first, a and b will be set randomly.

### Cost Function (Mean squared error)

For the Linear regression model, the cost function is convex obtained by subtracting the predicted values by the actual values.

$$J(a, b) = \frac{1}{2m} \sum_{i=1}^m (f(x_i) - y_i)^2$$

### Gradient descent algorithm

Iterative optimization algorithm for finding a minimum of a differentiable function.
One must choose a step size called `learning rate` (or $ \alpha ∈ \mathbb {N+} $ )

$$ a_{i+1} = a_i - \alpha \frac{\partial J(a_i,b)}{\partial a}$$
$$ b_{i+1} = b_i - \alpha \frac{\partial J(a,b_i)}{\partial b}$$

And the gradients are ([math explanation](math_cheat_sheet/gradient.ipynb)):

$$ \frac{\partial J(a, b)}{\partial a} = \frac{1}{m} \sum_{i = 1}^m x_i (ax_i + b - y_i)$$
$$ \frac{\partial J(a, b)}{\partial b} = \frac{1}{m} \sum_{i = 1}^m (ax_i + b - y_i)$$

### Matrix Equation

More explanations about matrix [here](math_cheat_sheet/matrix.ipynb)


**Model**

$$ F = X . \theta $$

**Cost Function**

$$ J(\theta) = \frac{1}{2m} \sum (X\theta - y)^2 $$

**Gradients**

$$ \frac{\partial J(a, b)}{\partial \theta} = \frac{1}{m} X^T (X\theta - Y) $$

**Gradient descent**

$$ \theta = \theta - \alpha \frac{\partial J}{\partial \theta} $$

