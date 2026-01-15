# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib",
#     "numpy",
# ]
# ///
import numpy as np
import matplotlib.pyplot as plt

def generate_spiral_points(n_points=100, n_revolutions=3, radius_growth=1):
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
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    
    return x, y

def plot_spiral(n_points=100, n_revolutions=3, radius_growth=1):
    """
    Generate and plot a spiral.
    """
    x, y = generate_spiral_points(n_points, n_revolutions, radius_growth)
    
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'b-')
    plt.title('Archimedean Spiral')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    plot_spiral()