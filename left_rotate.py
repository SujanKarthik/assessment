def left_rotate(d,arr):
    d=d%len(arr)
    return arr[d:]+arr[:d]
arrnew=[1,2,3,4,5]
print(left_rotate(12,arrnew))