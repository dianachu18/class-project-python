import string

def reverse_string(a_string):
  '''Return the reverse order of the string'''
  if len(a_string) <= 1:
    return a_string
  else:
    return a_string[-1] + reverse_string(a_string[:-1])

def is_palindrome(a_string):
  '''Return True if the string spelled the same both forward and backward, and False otherwise.'''
  a_string = eliminate_space_and_punctuation(a_string)
  if a_string.lower() == reverse_string(a_string.lower()):
    return True
  else:
    return False

def eliminate_space_and_punctuation(a_string):
  '''Omit any space and punctuation in a sentence'''
  if len(a_string) == 0:
    return ""
  if a_string[0] in string.punctuation or (a_string[0].isspace()):
        return eliminate_space_and_punctuation(a_string[1:])
  else:
    return a_string[0] + eliminate_space_and_punctuation(a_string[1:])
    
user_input = input("Enter a string to check whether it is a palindrome: ")
print(is_palindrome(user_input))

