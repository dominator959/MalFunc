# MalFunc Library 🛠️

A versatile Python utility library designed for robust data manipulation, numeric operations, and recursive structure traversal. Developed as a collaborative project for the **Computer Programming** course.

## 👥 The Development Team

| Member | GitHub Username | Core Responsibilities |
| :--- | :--- | :--- |
| **Faizan Toheed** (Leader) | [@faizantoheed456](https://github.com/faizantoheed456) | `get_number()`, `get_sum()`, `get_indices()` |
| **Muhammad Usman** | [@dominator959](https://github.com/dominator959) | `get_mul()`, `vectorize_mul()` |
| **Shah Faisal Ilyas** | [@Faisalilyas17](https://github.com/Faisalilyas17) | `vectorize_sum()`, `get_unique_order_list()` |
| **Muhammad Rohan Jabbar** | [@mrj-005](https://github.com/mrj-005) | `get_flat()`, `get_dtypes()` |

---

## 📚 Detailed Function Reference

### 1. Operations Module (`ops.py`)
This module handles core mathematical and input-validation logic.

*   **`get_number(prompt, to_int=False)`** (Implemented by Faizan Toheed)
    *   **Logic:** Uses an infinite loop and `try-except` blocks to filter out non-numeric input.
*   **`get_sum(data)`** (Implemented by Faizan Toheed)
    *   **Logic:** A recursive function that traverses nested lists, ignoring non-numeric elements.
*   **`get_mul(data)`** (Assigned to Muhammad Usman)
    *   **Goal:** Robust multiplication logic for numeric lists.
*   **`vectorize_mul(data)`** (Assigned to Muhammad Usman)
    *   **Goal:** Applies element-wise multiplication across structures.
*   **`vectorize_sum(data)`** (Assigned to Shah Faisal Ilyas)
    *   **Goal:** Applies element-wise summation across structures.

### 2. Utilities Module (`utils.py`)
This module provides structural analysis and list manipulation tools.

*   **`get_indices(data)`** (Implemented by Faizan Toheed)
    *   **Logic:** Recursively tracks the positional path of every element in a structure.
*   **`get_unique_order_list(data)`** (Assigned to Shah Faisal Ilyas)
    *   **Goal:** Removes duplicates while preserving the original order.
*   **`get_flat(data)`** (Assigned to Muhammad Rohan Jabbar)
    *   **Goal:** Recursively flattens deeply nested lists.
*   **`get_dtypes(data)`** (Assigned to Muhammad Rohan Jabbar)
    *   **Goal:** Scans a collection and returns the specific data types found.

---

## 🚀 Getting Started

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/dominator959/MalFunc.git
```

### Basic Usage
```python
from malfunc import ops, utils

# Securely get an integer from a user (implemented by Faizan Toheed)
age = ops.get_number("Enter your age:", to_int=True)

# Deeply analyze nested indices (implemented by Faizan Toheed)
data = [1, [2, 3], 4]
paths = utils.get_indices(data)
```

---

## 📝 Project Goals
- **Robustness:** Using `try-except` and type-checking to prevent runtime crashes.
- **Recursion:** Mastering nested data traversal without depth limitations.
- **Modularity:** Separating logic into clean, reusable modules (`ops` and `utils`).

## 📜 License
This project is licensed under the MIT License.
