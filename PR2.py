import matplotlib.pyplot as plt

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_spiral_coordinates(n):
    """Find the coordinates (x, y) of the nth prime number in the Ulam spiral."""
    step_count, step_limit, adder = 1, 2, 1
    x, y = 0, 0

    for num in range(2, n + 1):
        if step_count <= 0.5 * step_limit:
            x += adder
        else:
            y += adder

        step_count += 1
        if step_count > step_limit:
            step_count = 1
            step_limit += 2
            adder *= -1

    return x, y

# Generate coordinates for the first 25 prime numbers
prime_coords = [prime_spiral_coordinates(i) for i in range(1, 1026)]

# Create a grid to display the Ulam spiral
grid_size = 10  # Adjust the grid size as needed
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

# Mark prime coordinates in the grid
for x, y in prime_coords:
    grid[y][x] = 'X'

# Display the Ulam spiral
for row in grid:
    print(' '.join(row))
