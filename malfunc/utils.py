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
