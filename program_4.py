# Logan H's Coordinate Calculator

# 1st, IMPORT math for Square Root
import math


# 2nd, DEFINE distance function to calculate distance between 2 points
def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

# 3rd, SET UP formula for distance, then return this.
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    return dist


# 4th, SET UP main function (ask for points, set up error messages, print the distance).
def main():
    try:
        coord1 = tuple(map(int, input("Enter the first 3D point (x1, y1, z1): ").strip('()').split(',')))
        coord2 = tuple(map(int, input("Enter the second 3D point (x2, y2, z2): ").strip('()').split(',')))

        if len(coord1) != 3 or len(coord2) != 3:
            raise ValueError("Both points must have exactly 3 coordinates.")

        dist = distance(coord1, coord2)

        print(f"The distance between the points {coord1} and {coord2} is: {dist:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 5th, FINALLY, run program
main()
