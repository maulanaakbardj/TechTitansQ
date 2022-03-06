def is_palindrome(word):
  if (type(word) == int):
    word = str(word)
  return word == word[::-1]

print(is_palindrome('katak')) # true
print(is_palindrome('kotak')) # false
print(is_palindrome(696)) # true
print(is_palindrome(213)) # false     
