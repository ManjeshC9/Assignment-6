# passed string is palindrome or not
def main():
    user_input = str(input("Enter the string here - "))
    string = user_input.replace(" " , "")
    reverse = string[::-1]
    if reverse == string:
        print("The string is palindrome")
    else:
        print("The string is not a palindrome")
main()
