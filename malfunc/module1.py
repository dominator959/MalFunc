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
