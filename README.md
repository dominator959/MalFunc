# MalFunc Library 🛠️

A versatile Python utility library designed for robust data manipulation, numeric operations, and recursive structure traversal. Developed as a collaborative **University Data Science** project.

## 👥 The Development Team

| Member | GitHub Username | Core Responsibilities |
| :--- | :--- | :--- |
| **Faizan Toheed** | [@faizantoheed456](https://github.com/faizantoheed456) | `get_number()`, `get_sum()`, `get_indices()` |
| **Muhammad Usman** | [@dominator959](https://github.com/dominator959) | `get_mul()`, `vectorize_mul()` |
| **Shah Faisal Ilyas** | [@Faisalilyas17](https://github.com/Faisalilyas17) | `vectorize_sum()`, `get_unique_order_list()` |
| **Muhammad Rohan Jabbar** | [@mrj-005](https://github.com/mrj-005) | `get_flat()`, `get_dtypes()` |

---

## 🚀 Getting Started

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/dominator959/MalFunc.git
cd MalFunc
```

### Basic Usage

```python
import ops
import utils

# Securely get an integer from the user
age = ops.get_number("Enter your age:", to_int=True)

# Sum a nested list (ignoring non-numeric values)
result = ops.get_sum([1, [2, 3], "x", 4])
# => [5, 5]  (inner [2,3]=5, outer [1,4]=5)

# Flatten a deeply nested list
flat = utils.get_flat([1, [2, [3, [4, 5]]]])
# => [1, 2, 3, 4, 5]
```

---

## 📚 Function Reference

### Module: `ops.py` — Operations

#### `get_number(prompt, to_int=False)`
Repeatedly prompts the user until valid numeric input is provided. Eliminates the need for repetitive `try-except` blocks in calling code.

```python
age   = ops.get_number("Enter your age:", to_int=True)  # returns int
price = ops.get_number("Enter price:")                  # returns float
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `prompt` | `str` | Message displayed to the user |
| `to_int` | `bool` | If `True`, returns `int`; otherwise returns `float` (default: `False`) |

**Returns:** `int` or `float`

---

#### `get_sum(data, results=None)`
Recursively sums numeric items in a (possibly nested) list, ignoring non-numeric values. Returns a list of sums — one per nesting level encountered.

```python
ops.get_sum([1, 2, 3])          # => [6]
ops.get_sum([1, "x", 2])        # => [3]  ("x" ignored with notice)
ops.get_sum([1, [2, 3], 4])     # => [5, 5]
ops.get_sum([1, [2, [3, 4]]])   # => [7, 2, 1]
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `data` | `list` | Input list (may contain numbers, strings, or nested lists) |
| `results` | `list` | Used internally for recursion; leave as `None` |

**Returns:** `list` of sums (innermost levels first)

---

#### `get_mul(data)`
Calculates the product of all numeric items in a (possibly nested) list. Non-numeric values are ignored. Returns a list of products — one per nesting level.

```python
ops.get_mul([2, 3, 4])      # => [24]
ops.get_mul([2, "x", 3])    # => [6]
ops.get_mul([2, [3, 4]])    # => [12, 2]
ops.get_mul(["a", "b"])     # => [0]  (no numeric items)
ops.get_mul([])             # => [0]
```

**Returns:** `list` of products (innermost levels first)

---

#### `get_indices(data, current_path=None)`
Recursively traverses a list and returns the exact positional path of every element, including those inside nested lists.

```python
ops.get_indices(["a", "b"])
# => [{"path": [0], "value": "a"}, {"path": [1], "value": "b"}]

ops.get_indices([1, [2, 3]])
# => [
#      {"path": [0],    "value": 1},
#      {"path": [1],    "value": [2, 3]},
#      {"path": [1, 0], "value": 2},
#      {"path": [1, 1], "value": 3},
#    ]
```

**Returns:** `list` of `dict` with keys `"path"` (index trail) and `"value"` (item)

---

#### `vectorize_sum(a, b)`
Performs element-wise addition of two lists of equal length. Supports nested lists recursively. Raises errors on mismatched lengths, types, or nesting structures.

```python
ops.vectorize_sum([1, 2, 3], [4, 5, 6])          # => [5, 7, 9]
ops.vectorize_sum([1, [2, 3]], [10, [20, 30]])    # => [11, [22, 33]]
```

**Raises:** `TypeError` for non-list inputs, non-numeric elements, or mismatched nesting; `ValueError` for unequal lengths.

---

### Module: `utils.py` — Utilities

#### `vectorize_mul(a, b)`
Performs element-wise multiplication of two lists of equal length. Supports nested lists recursively. Raises errors on mismatched lengths, types, or nesting structures.

```python
utils.vectorize_mul([1, 2, 3], [4, 5, 6])       # => [4, 10, 18]
utils.vectorize_mul([2, [3, 4]], [10, [5, 5]])   # => [20, [15, 20]]
```

**Raises:** `TypeError` for non-list inputs, non-numeric elements, or mismatched nesting; `ValueError` for unequal lengths.

---

#### `get_unique_order_list(data)`
Removes duplicate items from a list while preserving the original order of first appearance — something a plain `set()` conversion cannot do.

```python
utils.get_unique_order_list([3, 1, 3, 2, 1, 4])        # => [3, 1, 2, 4]
utils.get_unique_order_list(["b", "a", "b", "c", "a"]) # => ["b", "a", "c"]
```

> **Note:** Items must be hashable (e.g., integers, strings, tuples).

**Returns:** `list` with duplicates removed, original order preserved.

---

#### `get_flat(data)`
Recursively flattens a deeply nested list into a single-level list, preserving element order and mixed types.

```python
utils.get_flat([1, [2, 3], 4])              # => [1, 2, 3, 4]
utils.get_flat([1, [2, [3, [4, 5]], 6], 7]) # => [1, 2, 3, 4, 5, 6, 7]
utils.get_flat([1, ["a", [2.5, "b"]], None])# => [1, "a", 2.5, "b", None]
```

**Returns:** Flat `list` containing all elements in order.

---

#### `get_dtypes(data)`
Scans a collection and counts occurrences of each data type, useful for quick data profiling and cleaning.

```python
utils.get_dtypes([1, "a", 2.5, "b", 3])
# => {"int": 2, "str": 2, "float": 1}

utils.get_dtypes([1, [2, 3], None, "x"])
# => {"int": 1, "list": 1, "NoneType": 1, "str": 1}
```

**Returns:** `dict` mapping type names (`str`) to their occurrence count (`int`).

---

## 🧪 Running Tests

All 9 functions have full unit test coverage in `tests.py`.

```bash
# Run all tests with verbose output
python -m unittest tests.py -v

# Or simply
python tests.py
```

Test coverage includes: valid inputs, edge cases (empty lists, no numeric items), error-raising conditions, and retry behaviour for `get_number`.

---

## 📝 Project Goals

- **Robustness** — `try-except` blocks and type-checking prevent runtime crashes on bad input.
- **Recursion** — Nested data structures are handled cleanly without depth limitations.
- **Modularity** — Logic is separated into two focused modules: `ops` for numeric operations and `utils` for structural utilities.

---

## 📜 License

This project is licensed under the MIT License.