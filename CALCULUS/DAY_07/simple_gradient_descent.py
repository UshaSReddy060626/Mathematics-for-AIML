learning_rate = 0.1
x = 8
for i in range(15):
    gradient = 2 * x     
    x = x - learning_rate * gradient
    print(f"Step {i+1}: x = {x:.4f}")