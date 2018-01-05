import numpy

a = numpy.arange(12)
print("numpy.arange(12)",a)

print("type(a)",type(a))

print("a.shape",a.shape)
a.shape = 3,4
print("a.shape = 3,4"+str(a))

print("a[2]",a[2])

print("a[2][1]",a[2][1])

print("Get column at index 1.",a[:,1])

print("Create a new array by transposing",a.transpose())

