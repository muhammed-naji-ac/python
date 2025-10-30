# Accept string from user
word = input("Enter a word: ")

# Check if the string already ends with 'ing'
if word.endswith('ing'):
    word = word + 'ly'
else:
    word = word + 'ing'

# Display the result
print("Modified word:", word)
