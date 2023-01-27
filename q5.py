# sorting alphabetically
def main():
    input_string = str(input("Enter the string here - "))
    list = input_string.split("-")
    list.sort()
    for i in range(0 , len(list)):
        print(f"-{list[i]}" , end = " ")
        
    
main()
