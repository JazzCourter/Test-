"""
Author: Jazz Courter
Date Written: 10/25/2024
Assignment: Module 01 Practice Exercise 2-2
This program is designed to ask for the parameters of the cube, calculate the input, and then print the results.
"""

while True:
    # Input cube edge length
    intCubeEdge = int(input("Enter the edge length of the cube: "))

    # Calculate surgace area of the cube
    surfaceArea = 6 * (intCubeEdge ** 2)

    # Print the calculated surface area
    print("The surface area of the cube is: ", surfaceArea)

    # Ask user if they want to continue
    response = input("\nDo you wan to calculate another cube? (yes/no): ")

    # Break loop is user chooses no
    if response.lower() != "yes":
        break
    
