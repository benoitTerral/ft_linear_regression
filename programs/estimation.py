import numpy as np
import pickle


def estimate(estimation: float, x_min: float, x_range: float, theta: np.array = [[0],[0]]) -> float:
	if not isinstance(estimation, float):
		raise TypeError("estimation must be a float.")
	if not np.issubdtype(theta.dtype, np.floating):
		raise TypeError("theta must be a NumPy array containing floats.")
	user_input_normalized = (estimation - x_min) / x_range
	return float(user_input_normalized * theta[0] + theta[1])


def main():
	# Load variables from the pickle file
	with open('trained_model.pkl', 'rb') as f:
		saved_data = pickle.load(f)
		theta = saved_data['theta']
		x_min = saved_data['x_min']
		x_range = saved_data['x_range']
	print("Welcome to the car pricer, please enter 'exit' to quit")
	while True:
		mileage = input("Enter mileage in kilometers: ")
		if mileage.lower() == "exit":
				return None
		try:
			mileage = float(mileage)
			estimated_price = estimate(mileage, x_min, x_range, theta)
			print(f"The estimated price for a used after ${mileage:.2f} km is ${estimated_price:.2f}")
		except ValueError:
			print("Invalid input. Please enter a valid float value.")


if __name__ == "__main__":
    main()