# Decision matrix (models x criteria)
matrix = np.array([
    [0.8, 0.6, 0.7],  # Model 1
    [0.9, 0.7, 0.6],  # Model 2
    [0.7, 0.8, 0.9],  # Model 3
    [0.6, 0.9, 0.8],  # Model 4
])

# Weights for each criterion
weights = np.array([0.4, 0.35, 0.25])

# Criteria type ("benefit" means higher values are better)
criteria = "benefit"

# Applying TOPSIS
closeness, ranking = topsis(matrix, weights, criteria)

print("Closeness scores:", closeness)
print("Ranking of models:", ranking + 1)  # Adding 1 to convert to 1-based index
