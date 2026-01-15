import numpy as np


def generate(n_points=100, n_revolutions=3, radius_growth=1):
    """
    Generate points along a spiral.

    Args:
        n_points: Number of points to generate
        n_revolutions: Number of complete revolutions
        radius_growth: Rate at which spiral radius increases

    Returns:
        Tuple of (x_coordinates, y_coordinates)
    """
    # Generate angle values
    theta = np.linspace(0, 2 * np.pi * n_revolutions, n_points)

    # Calculate radius for each point (grows with angle)
    radius = radius_growth * theta

    # Convert polar coordinates to Cartesian
    x = 96 + radius * np.cos(theta)
    y = 96 + radius * np.sin(theta)

    return np.array([x, y])


# Example usage
if __name__ == "__main__":
    coords = generate()
    # Points can be plotted or used for further calculations
    print(coords)
