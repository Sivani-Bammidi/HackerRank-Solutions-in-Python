import numpy
def reshape(arr):
    reshaped=arr.reshape(3, 3)
    return reshaped


arr=input().strip().split(' ')
lista=list(map(int, arr))
arr=numpy.array(lista)
res=reshape(arr)
print(res)