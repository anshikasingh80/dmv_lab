import matplotlib.pyplot as plt

x = list(map(float, input("Enter x values separated by space: ").split()))
y = list(map(float, input("Enter y values separated by space: ").split()))

if len(x) != len(y):
    print("Error: X and Y must have same number of values.")
else:
    plt.figure(figsize=(8, 5))
    
    plt.plot(x, y, marker='o', color='pink')
    
    plt.title("Line Graph (User Input)")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.grid(True)

    plt.show()
