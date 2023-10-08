"""
Problem: Word Count Tool: 
    Write a function that
    reads a text file and counts
    the number of words in it.
"""
def read_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
        return word_count
    
    except FileNotFoundError:
        return 'File not found'
    except Exception as e:
        return f'An error occurred: {str(e)}'
    
# testing function
file_path = 'sample.txt'
word_count = read_words(file_path)
print(f'{word_count} words.')

