#*** Comments ***
"""print("Hello Abuh")""" # This is also a comment for long paragraphs of code


# VARIABLES - Conatiner to hold data
number = 10
site_name = 'Power learn Project' # Declaring variable
print(number)
print(site_name)

site_name = 'apple.com' # changing value of variables
print(site_name)

a, b, c = 5, 3.2, 'Abuh' # Assigning multiple values to variables
print(a)
print(b)
print(c)

site1 = site2 = 'webmasters'
print(site1)
print(site2)

#DATATYPES
num1 = 5 
num2 = 8.9
num3 = 98+9
print(num1, 'is a type of', type(num1))
print(num2, 'is a type of', type(num2))
print(num3, 'is a type of', type(num3))

#1.LIST
programming_languages = ["java", 'js', "python"]
print(programming_languages)
print(programming_languages[0])
print(programming_languages[2])
print(programming_languages[1])

# 2.TUPLES - IMMUTABLE
product = ('xbox', 'playstation', 353)
print(product)
print(product[0])
print(product[1])

#3. STRING
message = 'First python code'
print(message)

# 4.  SET
student_id = {112, 114, 115}
print(student_id)

#5. DICTIONARY
capital_city = {'Nepal': 'kathmandu', 'italy': 'rome', 'kenya': 'nairobi'} # nepal,italy and Kenya are the keys
print(capital_city)
print(capital_city['Nepal'])
print(capital_city['kenya'])
print(capital_city['italy'])

# TYPE CONVERTION
#1. IMPLICIT CONVERTION - Automatic type convertion
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
print(new_number)
print(type(new_number))


# 2. EXPLICIT TYPE CONVERTION - Manual convertion
num_string = '12'
num_integer = 23

print(type(num_string))

num_string = int(num_string)
print(type(num_string))


#TYPE OF PYTHON OPERATORS
# 1. ARITHMETIC OPERATOR
 """ 
   + to add a and b
    - to subtract b from a
    * to multiply a and b
    / to divide a by b
    // to floor divide a by b
    % to get the remainder
    ** to get a to the power b"""

# 2. ASSIGNMENT OPERATOR
"""
a = 7 #Assignment
a += 1 # Addition
a -+ 3 #Subtraction
a *= 5 #Multiplication
a /= 6 #Division
a %= 8 # Remainder
a **= 10 # Exponent
"""

# 3. COMPARISON OPERATOR

"""
3 == 5 
3 != 5
3 > 5
3 < 5
3 >= 5
3 <= 5
"""

#LOGICAL OPERATORS
"""
and 
or
not
"""
x = {}
X[2] = 10
x[1] = [20, 30, 40]
print(x[1][2])