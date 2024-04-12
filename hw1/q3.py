from scipy.interpolate import interp1d, interp2d
import numpy as np
import matplotlib.pyplot as plt

"""
Write a program to read in a two column table from a file and perform linear 
interpolation at an arbitrary point. You may assume that the data is evenly 
spaced in the independent variable (this makes it easier to determine which 
points to use for interpolation).
"""


def main():
    data = np.loadtxt("./hw1/hw1_data.txt")
    x = data[:, 0]
    y = data[:, 1]

    linear_interp = interp1d(x, y, kind="linear")
    quad_interp = interp1d(x, y, kind="quadratic")
    quad_interp_first_half = interp1d(
        x[: len(x) // 2 + 1], y[: len(y) // 2 + 1], kind="quadratic"
    )
    quad_interp_second_half = interp1d(
        x[len(x) // 2 :], y[len(y) // 2 :], kind="quadratic"
    )
    forth_interp = lambda _x: (
        quad_interp_first_half(_x)
        if _x < x[len(x) // 2]
        else quad_interp_second_half(_x)
    )

    x1 = 2.88
    print(f"Linear Interpolation at x = {x1}: {linear_interp(x1)}")

    x_plot = np.linspace(1, 5, 100)

    y_plot_linear = linear_interp(x_plot)
    y_plot_quad = quad_interp(x_plot)
    y_plot_forth = [forth_interp(x) for x in x_plot]

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot_linear, label="Linear Interpolation")
    plt.plot(x_plot, y_plot_quad, label="Quadratic Interpolation")
    plt.plot(x_plot, y_plot_forth, label="Forth Order Interpolation")
    plt.plot(x, y, "o", color="red", label="Data Points")
    plt.title("Polynomial Interpolation Comparisons")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend()
    plt.grid(True)
    plt.show()

    x2 = 4.75
    y1_linear = linear_interp(x2)
    y1_quad = quad_interp(x2)
    y1_forth = forth_interp(x2)
    print(f"Linear Interpolation at x = {x2}: {linear_interp(x2)}")
    print(f"Quadratic Interpolation at x = {x2}: {quad_interp(x2)}")
    print(f"Forth Order Interpolation at x = {x2}: {y1_forth}")

    def f(x):
        return 100 / x**2

    y1_actual = f(x2)
    print(
        f"Difference between actual and linear interpolation: {abs(y1_actual - y1_linear)}"
    )
    print(
        f"Difference between actual and quadratic interpolation: {abs(y1_actual - y1_quad)}"
    )
    print(
        f"Difference between actual and forth order interpolation: {abs(y1_actual - y1_forth)}"
    )


if __name__ == "__main__":
    main()
