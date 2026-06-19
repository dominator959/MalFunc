def vectorize_mul(a, b):
    """
    Performs element-wise multiplication of two numeric lists.
    If lists are nested, it recursively multiplies them element-wise.
    Raises ValueError if lengths at any nesting level differ.
    
    Args:
        a (list): First list.
        b (list): Second list.
        
    Returns:
        list: A list containing element-wise products.
    """
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists.")
    if len(a) != len(b):
        raise ValueError("Lists must be of equal length for vectorization.")
        
    results = []
    for x, y in zip(a, b):
        if isinstance(x, list) and isinstance(y, list):
            results.append(vectorize_mul(x, y))
        elif isinstance(x, list) or isinstance(y, list):
            raise TypeError("Cannot vectorize elements of mismatching nested structures.")
        else:
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("Elements to multiply must be numeric.")
            results.append(x * y)
            
    return results


def get_unique_order_list(data):
    """
    Removes duplicate items from a list while preserving the original order
    in which they first appeared.
    
    Args:
        data (list): The list to deduplicate. Items must be hashable.
        
    Returns:
        list: A new list with duplicates removed, original order preserved.
    """
    unique_items = []
    seen = set()
    
    for item in data:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)
            
    return unique_items


def get_flat(data):
    """
    Recursively flattens a nested list into a single-level list.
    
    Args:
        data (list): A list that may contain nested lists at any depth.
        
    Returns:
        list: A single-level (flat) list containing all elements in order.
    """
    flat_list = []
    
    for item in data:
        if isinstance(item, list):
            flat_list.extend(get_flat(item))
        else:
            flat_list.append(item)
            
    return flat_list


def get_dtypes(data):
    """
    Scans a collection and counts the occurrences of each data type present.
    
    Args:
        data (list): The collection to analyze.
        
    Returns:
        dict: A mapping of type name (str) to the number of occurrences (int).
    """
    counts = {}
    
    for item in data:
        type_name = type(item).__name__
        counts[type_name] = counts.get(type_name, 0) + 1
        
    return counts