# Importing Libraries
import numpy as np
import tensorflow as tf
import pandas as pd
import random
import data

def predict(input_ratings):
    df = pd.DataFrame(data.data)

    ratings = data.ratings

    # Some Constants
    user_count = ratings.shape[1]
    movie_count = df.shape[0]
    k = df.shape[1] - 2 # Number of genres

    # Extracting Movie Features
    V = df.to_numpy()[:, 2:]
    V /= 10 # Normalization
    
    input_ratings = np.array([[input_ratings]])

    ratings = np.hstack((ratings, input_ratings))
    
    data.ratings = ratings

    movies = tf.Variable(V, dtype=tf.float64)
    users  = tf.Variable(np.random.rand(user_count + 1,k), dtype=tf.float64)

    mask = np.ma.masked_not_equal(ratings, 0).mask

    ratings = tf.constant(ratings, dtype=tf.float64)

    optimizer = tf.optimizers.Adam()

    trainable_weights = [users, movies]

    steps = 2000

    for step in range(steps):
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

    recs = {}

    for i, pred in enumerate(predictions[-1]):
        if input_ratings[0][0][i] == 0:
            recs[df['name'][i]] = pred

    recs = dict(sorted(recs.items(), key=lambda x:x[1]))
    recs = list(recs.keys())[-5:]
    list.reverse(recs)

    return recs