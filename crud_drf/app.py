import re

def break_conjunct(text):
    # Define a regular expression pattern for identifying conjunct characters
    conjunct_pattern = re.compile(r'([ক-হ])([অ-ও])([া- ৌ])')

    # Use the sub function to break conjunct characters
    broken_text = conjunct_pattern.sub(r'\1 \2', text)

    return broken_text

# Example usage
input_text = "দুই বা তার অধিক ব্যঞ্জনবর্ণের সংযুক্ত রূপ বা সমষ্টিকে যুক্তবর্ণ বলে।"
broken_text = break_conjunct(input_text)
print(broken_text)
