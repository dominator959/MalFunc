def get_number(prompt, to_int=False):
    """
    Repeatedly prompts the user for a number until valid numeric input is provided.
    
    Args:
        prompt (str): The message to display to the user.
        to_int (bool): If True, returns an integer. If False (default), returns a float.
        
    Returns:
        int or float: The numeric value entered by the user.
    """
    while True:
        user_input = input(prompt + " ")
        try:
            if to_int:
                return int(user_input)
            return float(user_input)
        except ValueError:
            expected_type = "a whole number" if to_int else "a number"
            print(f"Error: Invalid input. Please enter {expected_type}.")


def get_sum(data, results=None):
    """
    Calculates the sum of numeric items in a list, ignoring non-numeric values.
    Handles nested lists by returning a list of sums for each level found.
    
    Args:
        data (list): The list containing numbers, strings, or nested lists.
        results (list, optional): Used for recursion to track sums.
        
    Returns:
        list: A list of sums (one for each nested list and the main list).
    """
    if results is None:
        results = []
    
    current_sum = 0
    
    for item in data:
        if isinstance(item, (int, float)):
            current_sum += item
        elif isinstance(item, list):
            # Recursively find sums in the nested list
            get_sum(item, results)
        else:
            print(f"Notice: '{item}' is not a number and was ignored.")
            
    results.append(current_sum)
    return results


def get_mul(data):
    """
    Calculates the product of all numeric items in a list, ignoring non-numeric values.
    Recursively processes nested lists and returns a list of products.
    
    Args:
        data (list): The list containing numbers, strings, or nested lists.
        
    Returns:
        list: A list of products (one for each nested list and the main list).
    """
    results = []
    
    def _recurse(lst):
        current_product = 1
        has_numeric = False
        for item in lst:
            if isinstance(item, (int, float)):
                current_product *= item
                has_numeric = True
            elif isinstance(item, list):
                _recurse(item)
            else:
                print(f"Notice: '{item}' is not a number and was ignored.")
        if not has_numeric:
            current_product = 0
        results.append(current_product)
        
    _recurse(data)
    return results


def get_indices(data, current_path=None):
    """
    Returns a list of dictionaries containing every item and its positional index path.
    Works for flat and nested lists.
    
    Args:
        data (list): The list to traverse.
        current_path (list, optional): The path of indices leading to the current list.
        
    Returns:
        list: A list of dicts with 'path' and 'value' keys.
    """
    if current_path is None:
        current_path = []
    
    results = []
    for index, item in enumerate(data):
        # Create the specific path for this item
        new_path = current_path + [index]
        
        # Add the item and its path to results
        results.append({"path": new_path, "value": item})
        
        # If it's a list, dive deeper
        if isinstance(item, list):
            results.extend(get_indices(item, new_path))
            
    return results


def vectorize_sum(a, b):
    """
    Performs element-wise addition of two numeric lists.
    If lists are nested, it recursively sums them element-wise.
    Raises errors if lengths or structures at any nesting level differ.
    
    Args:
        a (list): First list.
        b (list): Second list.
        
    Returns:
        list: A list containing element-wise sums.
    """
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists.")
    if len(a) != len(b):
        raise ValueError("Lists must be of equal length for vectorization.")
        
    results = []
    for x, y in zip(a, b):
        if isinstance(x, list) and isinstance(y, list):
            results.append(vectorize_sum(x, y))
        elif isinstance(x, list) or isinstance(y, list):
            raise TypeError("Cannot vectorize elements of mismatching nested structures.")
        else:
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Elements to sum must be numeric.")
            results.append(x + y)
            
    return results