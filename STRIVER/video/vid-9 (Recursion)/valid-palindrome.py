# 125. Valid Palindrome
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# problem link: https://leetcode.com/problems/valid-palindrome/description/


# string = "Special $#! characters   spaces 888323"
# print(''.join(e for e in string if e.isalnum()))

def validate_palindrome(i:int, j:int, text:str, copy_text:str):
    if(i != len(text)//2 and j != len(copy_text)//2 ):
        if(text[i].lower() == copy_text[j].lower()):
            return validate_palindrome(i+1, j-1, text, copy_text)
        else:
            return False
        
    return True

# text = "Special $#! characters   spaces 888323"
# text = "AMANAMA"
text = "A man, a plan, a canal: Panama"
print(''.join(e for e in text if e.isalnum()))

print(validate_palindrome(0, -1,''.join(e for e in text if e.isalnum()),''.join(e for e in text if e.isalnum())))

# print(text[-1], text[0])
# print(text[-2], text[1])
# print(text[-3], text[2])