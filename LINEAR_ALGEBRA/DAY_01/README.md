# 📘Mathematics – Day 1: Linear Algebra I

## 🚀 Overview

Today, I started my Machine Learning Mathematics journey by learning the fundamentals of **Linear Algebra**, one of the core mathematical foundations behind Artificial Intelligence, Machine Learning, and Deep Learning.

---

# 📚 Topics Learned

## 1️⃣ What is Linear Algebra?

* Understood that Linear Algebra is the mathematics of vectors and matrices.
* Learned why it is essential in AI and Machine Learning.
* Discovered that computers represent images, text, audio, and other real-world data as numbers.

---

## 2️⃣ Scalars

* Learned that a **scalar** is a single numerical value.
* Examples:

  * Age
  * Salary
  * Temperature
  * Weight

### Python Example

```python
age = 22
salary = 50000
```

---

## 3️⃣ Vectors

* Learned that a **vector** is an ordered collection of numbers.
* Understood that vectors can represent:

  * Position
  * Direction
  * Features of a data point
  * Student marks
  * Customer information

### Example

```python
[170, 60, 21]
```

---

## 4️⃣ Vector Operations

Practiced the basic operations performed on vectors using NumPy.

### Operations Learned

* Vector Addition
* Vector Subtraction
* Scalar Multiplication

### Example

```python
import numpy as np

a = np.array([2,3])
b = np.array([4,5])

print(a+b)
print(a-b)
print(a*2)
```

---

## 5️⃣ Dot Product

Learned how the dot product is calculated by multiplying corresponding elements and adding the results.

### Formula

```text
(2×4) + (3×5) = 23
```

### NumPy Implementation

```python
np.dot(a,b)
```

---

## 6️⃣ Cosine Similarity

Learned how cosine similarity measures the similarity between two vectors based on their direction.

### Formula

```text
Cosine Similarity =
Dot Product / (||A|| × ||B||)
```

### NumPy Implementation

```python
dot = np.dot(a,b)
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

cosine = dot/(norm_a*norm_b)
```

---

# 💻 Hands-on Practice

## ✔ Program 1 – Identifying Scalars, Vectors, and Matrices

Implemented a program to classify data using:

* `isinstance()`
* `numpy.ndarray`
* `ndim`

Learned:

* Scalar → Single value
* Vector → 1D Array (`ndim == 1`)
* Matrix → 2D Array (`ndim == 2`)

---

## ✔ Program 2 – Vector Operations

Practiced:

* Vector Addition
* Vector Subtraction
* Scalar Multiplication

---

## ✔ Program 3 – Dot Product

Computed the dot product of two vectors using `np.dot()`.

---

## ✔ Program 4 – Cosine Similarity

Implemented cosine similarity using:

* `np.dot()`
* `np.linalg.norm()`

---

# 🤖 Real-World Applications

Learned where Linear Algebra is used in Machine Learning:

* Image Recognition
* Face Recognition
* ChatGPT and Large Language Models
* Recommendation Systems
* Search Engines
* Computer Vision
* Self-Driving Cars

---

# 📝 Key Learnings

* Every AI model works with numerical data.
* Scalars represent single values.
* Vectors represent collections of related values.
* Dot Product measures the relationship between two vectors.
* Cosine Similarity measures how similar two vectors are based on their direction.
* NumPy provides efficient tools for performing vector operations.

---

# 🛠 Libraries Used

* NumPy

---

# 🎯 Skills Practiced

* Creating NumPy arrays
* Vector manipulation
* Scalar multiplication
* Dot Product
* Cosine Similarity
* Using `ndim` to identify vectors and matrices
* Basic mathematical programming with NumPy

---

## ✅ Day 1 Successfully Completed

✔ Completed Theory

✔ Completed Coding Practice

✔ Understood Real-World Applications

✔ Ready to Continue with **Day 2 – Matrices and Matrix Operations** 🚀
