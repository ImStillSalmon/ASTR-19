import math

def main():
    steps = 1000
    for i in range(steps + 1):
        x = 2 * i / steps
        print(x, math.sin(x))

if __name__ == "__main__":
    main()