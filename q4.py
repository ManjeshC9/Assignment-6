# string is a panagram or not (contains every word of the alphabet table )
def main():
    Input = str(input("Enter the string here - "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in Input.lower():
            flag = True
        else:
            flag = False
    if flag:
        print("Not Panagram")
    else:
        print("Panagram")
main()
