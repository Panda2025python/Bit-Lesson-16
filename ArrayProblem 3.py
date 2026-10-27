def group_reverse(n):
    arr = [1,2,3,4,5,6]
    for i in range(0,6,n):
        arr[i:1+n] = arr[i:1+n][::-1]   
    return arr
print("group_reverse(2)", group_reverse(2))
print("group_reverse(3)", group_reverse(3))
n = int(input("group size "))
print(" group_reverse" + str(n) + "=", group_reverse(n))