from mxnet import np, npx
npx.set_np()

# x = np.arange(12)
# print(x.shape)
# print(x.size);

# x = x.reshape(2, 6)
# print(x)

# print(np.empty((3, 4)))

# #initialize array with all values filled by 0
# init_array = np.zeros((2, 3, 4))
# print(init_array)

# print(np.random.normal(0, 1, size=(2, 2)))

# Mathematic ------------------------------------------< JOHN TAG
# x = np.array([1, 2, 3, 4])
# y = np.array([2, 2, 2, 2])

# print((x+y, x-y, x*y, x/y, x**y))
# print (2*x)
# print (np.exp(x))

x = np.arange(12).reshape(3, 4)
y = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
# array_concatenate = np.concatenate([x, y], axis=1)
# print(array_concatenate)
# print(x == y)
# print(x.sum())
# Note: Same number of columns or rows

# Cơ chế lan truyền (broadcasting mechanism) ------------------------------------------< JOHN TAG
# x = np.arange(3).reshape(3, 1)
# y = np.arange(2).reshape(1, 2)
# print(x + y)

# Index, Slice ------------------------------------------< JOHN TAG
# print(x)
# print(x[-1])
# print(x[-1][1: 3])
# x[1, 2] = 10
# print(x)

# x[0:2, :] = 12
# print(x)

# Save memory ------------------------------------------< JOHN TAG
# z = np.zeros_like(x)
# print(x, z)
# print(id(z))
# z[:] = x+y
# print(id(z))

# Convert to another object
a = x.asnumpy()
b = np.array(a)
print(type(a), type(b))
print(float(y[0, 0]))

a = np.array([2.5])
print(int(a))