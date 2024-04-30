from mxnet import np, npx
npx.set_np()

# Bieu dien so vo huong
# x = np.array(1.0)
# y = np.array(2.0)
# print(x+y, x*y, x/y, x**y)

# Bieu dien vector
x = np.arange(4)
print(x)
# Do dai, chieu va kich thuoc (so chieu cua mot vector = do dai vector)
print(len(x))
print(x.shape)

# Ma tran (matrix)
M = np.arange(20).reshape(5, 4)
print(M)

# Ma tran chuyen vi
print("Ma tran chuyen vi: \n", M.T)

# Phep toan
## Cong tung phan tu
print(M+M)
print(M*M)

# Sum
print(M.sum(axis=1))
print(M.sum(axis=1, keepdims=True))

# Tich vo huong
print(x)
print(np.dot(x, x))
# hoac la
print(np.sum(x*x))

# Tich ma tran vs vector
print(M.shape, x.shape, np.dot(M, x))

# Nhan hai ma tran
print(np.dot(M, np.ones(shape=(4, 3))))

# Chuan (norm)
