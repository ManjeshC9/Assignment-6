# perfect number or not 
# test cases = 6 28 496 8128 
def main():
    user_input = int(input("Enter the number here - "))
    divisor_list = []
    sum = 0
    for i in range(1,user_input):
        if user_input % i == 0:
            divisor_list.append(i)
    for j in range(0 , len(divisor_list)):
        sum = sum + divisor_list[j]
    
    if sum == user_input:
        print("The number entered is a perfect number")
    else:
        print("The number entered is not a perfect number")
main()
