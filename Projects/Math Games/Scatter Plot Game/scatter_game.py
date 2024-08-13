import matplotlib.pyplot as plt
import random

score = 0

factor = random.uniform(0.5, 1.5)
xmin = int(-10*factor)
xmax = int(10*factor)
ymin = int(-10*factor)
ymax = int(10*factor)

fig, ax = plt.subplots()

while True:
    xpoint = random.randint(xmin, xmax)
    ypoint = random.randint(ymin, ymax)
    x = [xpoint]
    y = [ypoint]

    fig, ax = plt.subplots()  # Create a new figure each time
    plt.axis([xmin, xmax, ymin, ymax])  # Set window size
    plt.plot([xmin, xmax], [0, 0], 'b')  # Blue x-axis
    plt.plot([0, 0], [ymin, ymax], 'b')  # Blue y-axis
    plt.plot(x, y, 'ro')  # Red point

    plt.grid()  # Displays grid lines on the graph
    plt.show()

    guess = input("Enter the coordinates of the red point (or type 'exit' to quit): \n")
    if guess.lower() == 'exit':
        break

    guess_array = guess.split(",")
    try:
        xguess = int(guess_array[0])
        yguess = int(guess_array[1])
    except ValueError:
        print("Invalid input. Please enter the coordinates in the format x,y.")
        continue

    if xguess == xpoint and yguess == ypoint:
        score += 1
        print("Correct! Your current score is:", score)
    else:
        print("Incorrect. The correct coordinates were:", (xpoint, ypoint))
        print("Your current score is:", score)

print("Game Over! Your final score: ", score)