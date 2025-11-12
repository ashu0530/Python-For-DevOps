value_1 = float(input("Enter your first number: " ))
value_2 = float(input("Enter your first number: " ))
operator = input("Enter your operator: ")

if operator == '+':
    print("addition value of your value is: ", value_1 + value_2 )
elif operator == '-':
    print("substraction value of your value is: ", value_1 - value_2)
elif operator == '*':
    print("multiplication value of your given number is: ", value_1 * value_2)
elif operator == '/':
    print("Division of your given value is: ", value_1 // value_2)
else:
    print("please input valid operator")
        



