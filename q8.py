# find the three elements that sum to zero from a set of n real number
def main():
    class solution():
        def findTriplets(self , list1 , n):
            list2 = []
            for i in range(0 , n-2):
                for j in range(i+1 , n-1):
                    for k in range(j+1 , n):
                        if list1[i] + list1[j] + list1[k] == 0:
                            a = list1[i]
                            b = list1[j]
                            c = list1[k]
                            list_number = [a , b ,c]
                            list2.append(list_number)
            print(list2)
            
    solution1 = solution()
    list1 = [-25, -10, -7, -3, 2, 4, 8, 10]
    n = len(list1)
    solution1.findTriplets(list1 , n)
main()
