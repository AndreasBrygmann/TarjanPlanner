import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import calculator as calc

def findOneDistance():
    from seoul import relatives
    print("\nSelect two relatives:")
    i = 0
    for r in relatives:
        print(f'Press "{i}" for {r[0]}')
        i += 1
    relative1 = int(input("\nEnter fist number... "))
    relative2 = int(input("\nEnter second number... "))

    if relative1 >= 0 and relative1 < len(relatives):
        distance = calc.findOneDistance(relatives[relative1], relatives[relative2])
        print(f"\nThe distance between {relatives[relative1][0]} and {relatives[relative2][0]} is {distance:.1f} km")
    else:
        print("Please type a valid number")

def main():
    print("Welcome to the Tarjan planner")
    print("Select an option")
    print("To calulate the optimal route to all 10 relatives press 1")
    print("To calulate the distance between 2 relatives press 2\n")
    choice = input("type a number... ")
    
    if choice == "1":
        print(calc.findShortestPath(calc.createPaths(calc.findDistances())))

    elif choice == "2":
        findOneDistance()
    
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()