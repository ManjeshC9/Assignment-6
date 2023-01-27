# first n rows of pascals triangle
from math import factorial
def main():
    rows = int(input("Enter the number of rows - "))

    for i in range(rows):
        for j in range(rows - i+ 1):
            print( end = " ")
        
        for t in range(i+1):
            answer = factorial(i)//(factorial(t) * factorial(i-t))
            print(answer , end = " ")
        print()
main()
