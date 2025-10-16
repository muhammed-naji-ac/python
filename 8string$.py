user_input = input("Enter a string: ")
first_char = user_input[0]
rest_of_string = user_input[1:]
modified_rest = rest_of_string.replace(first_char, "$")
result = first_char + modified_rest
print("Modified string:", result)
