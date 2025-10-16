from orca.orca_state import lastInputEvent

value=input("enter the name")
if  len(value)<2:
    print(value)
else:
     first_value=value[0]
     last_value=value[-1]
     middle_value=value[1:-1]
     result=last_value+middle_value+first_value
print("modified string is",result)