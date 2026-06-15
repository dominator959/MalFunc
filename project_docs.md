# MalFunc Project Documentation
**Course:** Computer Programming  
**Project Leader:** Faizan Toheed  

---

## 1. get_number(prompt, to_int=False)
**Developer:** Faizan Toheed  

### Problem Statement
Programs often crash when users provide non-numeric input (like "abc" instead of "25") during numerical prompts. Developers usually have to write repetitive `try-except` blocks to handle these errors.

### Algorithm Approach
1.  **Initialize:** Enter an infinite `while` loop.
2.  **Input:** Prompt the user for input using the provided message.
3.  **Validation (Try):**
    -   If `to_int` is True, attempt to convert the input to an integer.
    -   Otherwise, attempt to convert the input to a float.
4.  **Success:** If conversion succeeds, return the numeric value immediately.
5.  **Exception (Except):** If a `ValueError` occurs, print a descriptive error message and repeat the loop.

---

## 2. get_sum(data)
**Developer:** Faizan Toheed  

### Problem Statement
Standard summing functions fail when encountering non-numeric types or nested lists within a collection.

### Algorithm Approach
1.  **Initialize:** Create a `current_sum` variable at 0 and a `results` list.
2.  **Traverse:** Iterate through each element in the list.
3.  **Recursive Check:**
    -   If the element is a number, add it to `current_sum`.
    -   If the element is a list, recursively call `get_sum` and store its results.
    -   If the element is non-numeric, skip it and notify the user.
4.  **Consolidate:** Append the `current_sum` to the `results` list.
5.  **Return:** Return the list of sums for each nested level.

---

## 3. get_indices(data)
**Developer:** Faizan Toheed  

### Problem Statement
Manually finding the exact coordinate path of an item in a deeply nested list is difficult and error-prone.

### Algorithm Approach
1.  **Initialize:** Start with an empty `results` list and a `current_path` (empty by default).
2.  **Enumerate:** Loop through the list using index and value.
3.  **Pathing:** Create a `new_path` by appending the current index to the `current_path`.
4.  **Record:** Store the current item and its `new_path` in the `results`.
5.  **Dive:** If the item is a list, recursively call `get_indices` with the `new_path` and extend the `results`.
6.  **Return:** Return the full mapping of indices.

---

## 4. get_mul(data)
**Developer:** Muhammad Usman  

### Problem Statement
Calculating the product of a list that may contain strings or other invalid data types requires robust pre-filtering.

### Algorithm Approach
1.  **Initialize:** Set a `product` variable to 1.
2.  **Filter:** Loop through the data; if a number is found, multiply it with the `product`.
3.  **Handling:** Ignore non-numeric types and return the final product.

---

## 5. vectorize_mul(data)
**Developer:** Muhammad Usman  

### Problem Statement
Applying a multiplier to every element in a list (vectorization) usually requires external libraries like NumPy.

### Algorithm Approach
1.  **Input:** Takes a list and a multiplier.
2.  **Map:** Iterate through the list and multiply every numeric element by the scalar.
3.  **Return:** Return a new list containing the modified values.

---

## 6. vectorize_sum(data)
**Developer:** Shah Faisal Ilyas  

### Problem Statement
Summing two lists element-wise (vector addition) is not a native operation for Python lists.

### Algorithm Approach
1.  **Validate:** Ensure both lists are of the same length.
2.  **Calculate:** Use a loop or comprehension to add elements at the same index.
3.  **Return:** A new list containing the element-wise sums.

---

## 7. get_unique_order_list(data)
**Developer:** Shah Faisal Ilyas  

### Problem Statement
Converting a list to a `set()` removes duplicates but destroys the original order of items.

### Algorithm Approach
1.  **Initialize:** Create an empty list `unique_items` and an empty `seen` set.
2.  **Iterate:** For each item, check if it exists in the `seen` set.
3.  **Action:** If not seen, add it to both `unique_items` and `seen`.
4.  **Return:** `unique_items` (preserving the original sequence).

---

## 8. get_flat(data)
**Developer:** Muhammad Rohan Jabbar  

### Problem Statement
Data structures with multiple levels of nesting are difficult to process sequentially.

### Algorithm Approach
1.  **Initialize:** Create an empty `flat_list`.
2.  **Recursive Check:** Iterate through the data.
    -   If an item is a list, call `get_flat` on it and extend the `flat_list`.
    -   Otherwise, append the item to the `flat_list`.
3.  **Return:** The single-level list.

---

## 9. get_dtypes(data)
**Developer:** Muhammad Rohan Jabbar  

### Problem Statement
Understanding the distribution of data types within a mixed collection is essential for data cleaning.

### Algorithm Approach
1.  **Initialize:** Create an empty dictionary to track counts.
2.  **Analyze:** Iterate through the collection and use `type(item).__name__` to identify the data type.
3.  **Update:** Increment the count for each data type found.
4.  **Return:** A summary of types and their frequencies.
