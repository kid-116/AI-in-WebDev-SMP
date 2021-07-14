import os
from numpy.random import seed
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np
import tensorflow as tf
np.random.seed(1234)


# Feature

user_count = 5
movie_count = 5
k = 10

# P
users  = tf.Variable(np.random.rand(user_count,k), dtype=tf.float64)

# Q
movies = tf.Variable(np.random.rand(movie_count,k), dtype=tf.float64)

# Ratings
ratings=np.array([[
    [0, 4, 4, 5, 1],
    [5, 0, 4, 5, 2],
    [3, 3, 1, 2, 0],
    [3, 3, 2, 0, 5],
    [0, 3, 0, 2, 4],
]])

mask = np.ma.masked_not_equal(ratings, 0).mask

ratings = tf.constant(ratings, dtype=tf.float64)

optimizer = tf.optimizers.Adam()




trainable_weights = [users, movies]

for step in range(2000):

    with tf.GradientTape() as tape:

        predictions = tf.matmul(users, movies, transpose_b=True)
        predictions = tf.nn.relu(predictions)
        predictions = predictions*mask

        loss = tf.losses.mean_squared_error(ratings, predictions)
        
        gradients = tape.gradient(loss, trainable_weights)
        optimizer.apply_gradients(zip(gradients, trainable_weights))




predictions = tf.matmul(users, movies, transpose_b=True)
predictions = tf.nn.relu(predictions)

predictions = np.rint(predictions.numpy())

print(predictions)