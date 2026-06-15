# MalFunc Library 🛠️

A versatile Python utility library designed for robust data manipulation, numeric operations, and recursive structure traversal. Developed as a collaborative project for the **Computer Programming** course.

## 👥 The Development Team

| Member | GitHub Username | Core Responsibilities |
| :--- | :--- | :--- |
| **Muhammad Usman** (Leader) | [@dominator959](https://github.com/dominator959) | `get_number()`, `get_sum()`, `get_indices()`, `get_mul()`, `vectorize_mul()` |
| **Shah Faisal Ilyas** | [@Faisalilyas17](https://github.com/Faisalilyas17) | `vectorize_sum()`, `get_unique_order_list()` |
| **Muhammad Rohan Jabbar** | [@mrj-005](https://github.com/mrj-005) | `get_flat()`, `get_dtypes()` |
| **Faizan Toheed** | [@faizantoheed456](https://github.com/faizantoheed456) | *[Assigned Operations]* |

---

## 📚 Detailed Function Reference

### 1. Operations Module (`ops.py`)
This module handles core mathematical and input-validation logic.

*   **`get_number(prompt, to_int=False)`**
    *   **Logic:** Uses an infinite loop and `try-except` blocks to filter out non-numeric input.
    *   **Feature:** Re-prompts the user until valid data is entered, ensuring program stability.
*   **`get_sum(data)`**
    *   **Logic:** A recursive function that traverses nested lists.
    *   **Feature:** Ignores non-numeric elements (with notification) and returns a collection of sums for each nesting level encountered.
*   **`get_mul(data)`**
    *   **Goal:** Robust multiplication logic for numeric lists, handling non-numeric types gracefully.
*   **`vectorize_sum(data)` / `vectorize_mul(data)`**
    *   **Goal:** Applies element-wise operations across structures, simulating vectorized math without external libraries like NumPy.

### 2. Utilities Module (`utils.py`)
This module provides structural analysis and list manipulation tools.

*   **`get_indices(data)`**
    *   **Logic:** Recursively tracks the positional path of every element in a structure.
    *   **Feature:** Returns a detailed map of "index paths" (e.g., `[0, 2, 1]`) for both items and sub-lists.
*   **`get_unique_order_list(data)`**
    *   **Goal:** Removes duplicates from a list while strictly maintaining the original order of first appearance.
*   **`get_flat(data)`**
    *   **Goal:** Recursively flattens any level of nested lists into a single-dimensional list.
*   **`get_dtypes(data)`**
    *   **Goal:** Scans a collection and returns a list or dictionary of the specific data types found (int, float, str, etc.).

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

# Securely get an integer from a user
age = ops.get_number("Enter your age:", to_int=True)

# Deeply analyze nested indices
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
