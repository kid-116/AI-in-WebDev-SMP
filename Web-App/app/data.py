import numpy as np

# The Dataset
## Movies
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['The Godfather', 'Shawshank Redemption', 'Soul', 'Avengers', 'Inception', 'Titanic', "Schindler's List", 'American Made', 'Fight Club', 'Kingsglaive'],
    'action': [5, 1, 1, 10, 8, 1, 0, 9, 9, 9],
    'comedy': [0, 1, 6, 8, 0, 3, 0, 8, 0, 0],
    'crime': [10, 8, 1, 1, 7, 3, 6, 9, 9, 3],
    'romance': [1, 1, 3, 1, 3, 10, 0, 6, 3, 0],
    'thriller': [7, 6, 2, 2, 7, 1, 0, 8, 9, 9],
    'fantasy': [0, 0, 7, 8, 8, 0, 0, 0, 0, 10],
    'drama': [8, 1, 0, 0, 0, 8, 9, 1, 0, 0],
}

## Ratings
ratings = np.array([[
    [0, 5, 0, 4, 5, 4, 0, 0, 0, 0], # Madhav
    [4, 0, 0, 5, 0, 4, 0, 4, 0, 0], # Rounak Somani
    [4, 4, 3, 3, 4, 0, 0, 0, 4, 0], # Tejas
    [1, 5, 3, 2, 5, 4, 5, 5, 5, 5], # Mehul
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Satvik
    [5, 5, 5, 4, 5, 4, 5, 0, 5, 0], # Sapta
    [4.9, 4.2, 0, 1, 4.5, 4, 0, 2.5, 4.7, 0], # Janmansh
    [4, 0, 0, 4, 5, 4, 0, 0, 3, 0], # Samyak
    [0, 0, 0, 4, 3, 4, 0, 0, 0, 0], # Sashank
    [0, 5, 0, 3, 5, 0, 0, 0, 3, 0], # Pratham
    [0, 5, 0, 4, 5, 0, 0, 0, 0, 0], # Samhita
    [0, 4, 0, 4, 5, 4, 0, 0, 4, 0], # Rakshit
]])