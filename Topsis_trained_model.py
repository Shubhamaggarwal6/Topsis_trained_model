import numpy as np

def normalize_matrix(matrix):
    """
    Normalize the decision matrix.
    """
    norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))
    return norm_matrix

def weighted_normalization(norm_matrix, weights):
    """
    Apply weights to the normalized matrix.
    """
    weighted_matrix = norm_matrix * weights
    return weighted_matrix

def find_ideal_solutions(weighted_matrix, criteria):
    """
    Find the ideal (best) and negative-ideal (worst) solutions.
    """
    ideal_solution = np.max(weighted_matrix, axis=0) if criteria == "benefit" else np.min(weighted_matrix, axis=0)
    negative_ideal_solution = np.min(weighted_matrix, axis=0) if criteria == "benefit" else np.max(weighted_matrix, axis=0)
    return ideal_solution, negative_ideal_solution

def calculate_distance(weighted_matrix, ideal_solution, negative_ideal_solution):
    """
    Calculate the distance from the ideal and negative-ideal solutions.
    """
    distance_to_ideal = np.sqrt(((weighted_matrix - ideal_solution) ** 2).sum(axis=1))
    distance_to_negative_ideal = np.sqrt(((weighted_matrix - negative_ideal_solution) ** 2).sum(axis=1))
    return distance_to_ideal, distance_to_negative_ideal

def calculate_closeness(distance_to_ideal, distance_to_negative_ideal):
    """
    Calculate the closeness score for each alternative.
    """
    return distance_to_negative_ideal / (distance_to_ideal + distance_to_negative_ideal)

def topsis(matrix, weights, criteria):
    """
    Implement TOPSIS method.
    """
    # Step 1: Normalize the matrix
    norm_matrix = normalize_matrix(matrix)
    
    # Step 2: Apply the weights
    weighted_matrix = weighted_normalization(norm_matrix, weights)
    
    # Step 3: Identify ideal and negative-ideal solutions
    ideal_solution, negative_ideal_solution = find_ideal_solutions(weighted_matrix, criteria)
    
    # Step 4: Calculate the distances
    distance_to_ideal, distance_to_negative_ideal = calculate_distance(weighted_matrix, ideal_solution, negative_ideal_solution)
    
    # Step 5: Calculate the closeness score
    closeness = calculate_closeness(distance_to_ideal, distance_to_negative_ideal)
    
    # Step 6: Rank alternatives based on closeness scores
    ranking = np.argsort(closeness)[::-1]
    return closeness, ranking

# Example usage
if __name__ == "__main__":
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
