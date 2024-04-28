from mxnet import np, npx
npx.set_np()

x = np.arange(12)
print(x.shape)
print(x.size)

x = x.reshape(2, 6)
print(x)

print(np.empty((3, 4)))

#initialize array with all values filled by 0
init_array = np.zeros((2, 3, 4))
print(init_array)

print(np.random.normal(0, 1, size=(2, 2)))

