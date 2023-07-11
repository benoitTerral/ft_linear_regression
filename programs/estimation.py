import numpy as np
import pickle
import os


def estimate(estimation: float, trained_data: dict) -> float:
	if not isinstance(estimation, float):
		raise TypeError("estimation must be a float.")
	if not np.issubdtype(trained_data['theta'].dtype, np.floating):
		raise TypeError("theta must be a NumPy array containing floats.")
	user_input_normalized = (estimation - trained_data['x_min']) / trained_data['x_range']
	return float(user_input_normalized * trained_data['theta'][0] + trained_data['theta'][1])


def main():
	file_path = 'trained_model.pkl'
	if (os.path.isfile(file_path)):
		with open('trained_model.pkl', 'rb') as f:
			trained_data = pickle.load(f)
	else:
		print('\033[93m' + "WARNING: unable to find trained data" + '\033[0m')
		trained_data = {
			'theta': np.array([0.0, 0.0]),
    		'x_min': 0.0,
    		'x_range': 1.0
		}
	print("Welcome to the car pricer, please enter 'exit' to quit")
	while True:
		mileage = input("Enter mileage in kilometers: ")
		if mileage.lower() == "exit":
				return None
		try:
			mileage = float(mileage)
			estimated_price = estimate(mileage, trained_data)
			print(f"The estimated price for a used after {mileage:.2f} km is {estimated_price:.2f}")
		except ValueError:
			print("Invalid input. Please enter a valid float value.")
		except TypeError as e:
			print(e)


if __name__ == "__main__":
    main()