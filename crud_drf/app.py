import re

def break_conjunct(text):
    # Define a regular expression pattern for identifying conjunct characters
    conjunct_pattern = re.compile(r'([ক-হ])([া- ৌ])')

    # Use the sub function to break conjunct characters
    broken_text = conjunct_pattern.sub(r'\1 \2', text)

    return broken_text

# Example usage
input_text = " ব্যঞ্জনবর্ণের"
broken_text = break_conjunct(input_text)
print(broken_text)
