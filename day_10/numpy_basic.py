import numpy as np 
# marks = np.array([78, 85, 90, 66])
# print(marks)
# print(type(marks))


# numbers = [1, 2, 3] 
# print(numbers * 2) 
# print(np.array(numbers) * 2)


# print(np.arange(0, 10, 3)) 
# print(np.linspace(0, 1, 4)) 
# print(np.zeros((2, 2))) 
# print(np.ones(5)) 
# print(np.full((2, 3), 8)) 
# print(np.eye(4))

rng = np.random.default_rng(42) 
scores = rng.integers(40, 100, size=(4, 3)) 
print(scores)


# print(scores.shape) 
# print(scores.ndim) 
# print(scores.size) 


# print(scores[0]) 
# print(scores[2, 0]) 
# print(scores[:, 0]) 
# print(scores[1:3]) 
# print(scores[:, 1:])

# print(scores + 5) 
# print(scores / 100) 
# bonus = np.array([2, 0, 5]) 
# print(scores + bonus)


# print(scores.sum()) 
# print(scores.mean()) 
# print(scores.max(), scores.min()) 
# print(scores.std().round(2)) 
# print(scores.mean(axis=0)) 
# print(scores.mean(axis=1).round(1))
# print(scores.sum(axis=1).argmax ())


# print(scores >= 75) 
# print(scores[scores >= 75]) 


# print((scores >= 75).sum()) 
# print(np.where(scores >= 60, "Pass", "Fail")


