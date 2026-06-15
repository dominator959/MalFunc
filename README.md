# MalFunc Library

A versatile Python utility library designed for robust data manipulation, numeric operations, and nested structure traversal. This project was developed as a collaborative school project.

## 👥 The Team & Contributions

| Member | GitHub Username | Assigned Functions |
| :--- | :--- | :--- |
| **Muhammad Usman** (Leader) | [@dominator959](https://github.com/dominator959) | `get_number()`, `get_sum()`, `get_indices()`, `get_mul()`, `vectorize_mul()` |
| **Faizan Toheed** | [@faizantoheed456](https://github.com/faizantoheed456) | *[Reserved for assigned functions]* |
| **Shah Faisal Ilyas** | [@Faisalilyas17](https://github.com/Faisalilyas17) | `vectorize_sum()`, `get_unique_order_list()` |
| **Muhammad Rohan Jabbar** | [@mrj-005](https://github.com/mrj-005) | `get_flat()`, `get_dtypes()` |

---

## 🛠️ Modules & Functions

### 1. Operations Module (`ops.py`)
Focuses on numeric data processing and robust user input.

*   **`get_number(prompt, to_int=False)`**
    *   Safely prompts the user for numeric input.
    *   Uses `try-except` blocks to handle invalid characters and re-prompt the user until a valid number is entered.
*   **`get_sum(data)`**
    *   Recursively calculates the sum of a list.
    *   Ignores non-numeric items (with a warning) and returns a list of sums for every nested level found.
*   **`get_mul()`** *(Planned)* - Handles robust multiplication logic.
*   **`vectorize_mul()`** *(Planned)* - Applies multiplication across vector-like structures.
*   **`vectorize_sum()`** *(Planned)* - Applies summation across vector-like structures.

### 2. Utilities Module (`utils.py`)
Focuses on structure traversal and metadata.

*   **`get_indices(data)`**
    *   Recursively maps every item in a list (flat or nested) to its positional "index path" (e.g., `[1, 0]`).
    *   Works regardless of data type.
*   **`get_unique_order_list()`** *(Planned)* - Returns unique items while preserving original order.
*   **`get_flat()`** *(Planned)* - Flattens deeply nested lists into a single level.
*   **`get_dtypes()`** *(Planned)* - Analyzes and returns the data types present within a structure.

---

## 🚀 Installation & Usage

To use this library in your project, clone the repository:

```bash
git clone https://github.com/dominator959/MalFunc.git
```

Import the modules into your Python script:

```python
from malfunc import ops, utils

# Example: Safe numeric input
weight = ops.get_number("What is your weight?")

# Example: Get indices of a nested list
data = ["a", ["b", "c"]]
map = utils.get_indices(data)
```

## 📜 License
This project is licensed under the MIT License.
