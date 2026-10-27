def left_rotate(n):
    arr = [1,2,3,4,5]
    n = n % len(arr)
    return arr[n:] + arr[:n]
print("left_rotate(1)", left_rotate(1))
print("left_rotate(2)", left_rotate(2))
n = int(input("Rotate how many times"))
print("left_rotate" + str(n) + "=", left_rotate(n))