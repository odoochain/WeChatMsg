import os
def verify_source_file(full_path):
    """
    Verify if a file exists at the given path. If not, search for it in parent directory and its subdirectories.
    
    Args:
        full_path: Full path to the file to verify
        
    Returns:
        str: Original path if file exists, path to found file if found elsewhere, or empty string if not found
    """

    if os.path.exists(full_path) and os.path.isfile(full_path):
        return full_path
    
    # File doesn't exist, search in parent directory
    file_name = os.path.basename(full_path)
    parent_dir = os.path.dirname(os.path.dirname(full_path))
    
    print(f'---找不到文件:{full_path}，开始搜索')
    # Walk through all directories and subdirectories
    for root, _, files in os.walk(parent_dir):
        for file in files:
            if file == file_name:
                found_path = os.path.join(root, file)
                print(f'+++重定位文件:{found_path}')
                return found_path
    print(f'***搜索结束，未找到文件:{full_path}')            
    return ''
