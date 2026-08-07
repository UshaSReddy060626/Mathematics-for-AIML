learning_rates = [0.5, 0.1, 0.01]
for lr in learning_rates:
    print(f"\nLearning Rate = {lr}")
    x = 8
    for i in range(5):
        gradient = 2 * x
        x = x - lr * gradient
        print(f"Step {i+1}: x = {x:.4f}")