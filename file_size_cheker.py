'''
File Size Checker: 
    Create a script that calculates 
    and displays the size of a file in bytes, 
    kilobytes, megabytes, etc.
'''
import os
import math

def get_file_size(file_path):
    try:
        # file size
        size = os.path.getsize(file_path)
        # list of units
        units = ['bytes', 'KB','MB', 'GB', 'TB']
        # unit index
        index = min(4, int(math.floor(math.log(size, 1024))))

        # size in unit
        size_in_unit = size / (1024 ** index)
        
        return f"{size_in_unit:.2f} {units[index]}"
    
    except FileNotFoundError: 
        return "File not found."
    except Exception as e: 
        return f"An error occurred: {str(e)}"
    

if __name__ == "__main__":
    # Replace with your file path
    print(get_file_size("sample.txt"))  
