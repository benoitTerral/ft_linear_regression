import papermill as pm
import os


def main():
    os.chdir(os.path.dirname(__file__))
    notebook = '../notebook/train.ipynb'
    kernel_name = 'python3'  # Specify the kernel name
    pm.execute_notebook(notebook, notebook, kernel_name=kernel_name)


if __name__ == "__main__":
    main()