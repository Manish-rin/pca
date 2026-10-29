import pca2main
# Given Dataset[cite: 1]
x1 = [1.2, 2.5, 3.1, 4.7, 5.3, 6.8, 7.4, 8.9, 9.5, 10.2, 11.6, 12.3, 13.7, 14.4, 15.8]
x2 = [2.1, 1.8, 3.6, 2.9, 4.5, 3.7, 5.2, 4.8, 6.1, 5.5, 7.3, 6.7, 8.2, 7.6, 9.1]
y  = [4.8, 5.9, 8.2, 9.1, 12.4, 13.6, 15.8, 18.2, 19.7, 22.1, 24.3, 25.8, 28.4, 30.1, 32.6]

n = len(y)
# Construct design matrix X with bias term (x0 = 1)
X = [[1.0, x1[i], x2[i]] for i in range(n)]

# Initialize weights [w0, w1, w2]
weights = [0.0, 0.0, 0.0]
learning_rate = 0.0001
epochs = 50000

# Gradient Descent Optimization
for epoch in range(epochs):
    dw = [0.0, 0.0, 0.0]
    for i in range(n):
        prediction = sum(weights[j] * X[i][j] for j in range(3))
        error = prediction - y[i]
        for j in range(3):
            dw[j] += error * X[i][j]
    for j in range(3):
        weights[j] -= (learning_rate / n) * dw[j]

# Predict for new data point (x1, x2) = (6.0, 4.0)[cite: 1]
new_x = [1.0, 6.0, 4.0]
predicted_y = sum(weights[j] * new_x[j] for j in range(3))

print(f"Learned Weights: w0={weights[0]:.4f}, w1={weights[1]:.4f}, w2={weights[2]:.4f}")
print(f"Predicted y for (6.0, 4.0): {predicted_y:.4f}")