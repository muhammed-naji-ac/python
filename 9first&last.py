user_input = input("Enter a string: ")

if len(user_input) < 2:
<<<<<<< HEAD
    # No swap possible
=======
>>>>>>> f83e977 (16-10-25 change)
    result = user_input
else:
    first_char = user_input[0]
    last_char = user_input[-1]
    middle_part = user_input[1:-1]
    result = last_char + middle_part + first_char

print("Modified string:", result)
