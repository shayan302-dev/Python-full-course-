# Python Operators
# python operators are use to perform operations on variables and values
print(45 + 5) # output 50

"""Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""
# Python arithmetic operators
# arithmetic operators are use for numeric values for performing mathmatical opertions

"""+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y"""

# Addition
print(5 + 1) # output 6
print()

# Subtraction
print(5 - 1) # output 4
print()

# Multiplication
print(5 * 2) #output 10
print()

# Division
print(4 / 2) # output 2.0
print()

# Modulus
print(10 % 2) # output 0
print()
# The % returns the remainder

# Exponentation
print(2**5) # The output is 32 
print()
# it does 2*2*2*2*2 = 32

# Floor Division
print(10 // 2) # The output is 5
"""To manually divide 7 by 2:

1. **Divide 7 by 2**: 
   - 2 goes into 7 three times (because \(2 \times 3 = 6\)).
2. **Subtract** 6 from 7:
   - \(7 - 6 = 1\).
3. **Result**: The quotient is 3, and the remainder is 1.

Thus, \( \frac{7}{2} = 3.5 \). In floor division, the result is 3.
its output is called quotient """ 
 


 # Python Assignment Operators
 # assignment operators are used  to assign values to the varaibles

"""Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)"""


# Python Logical Operatosand 	Returns True if both statements are true	x < 5 and  x < 10	
# logical opertors are use to combine the conditional statements

"""Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)"""


# Python Identity Operators
"""Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y"""


# Python Membership Operators
"""
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
"""


# Python bitwise Operators
"""
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description	Example	Try it
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2"""


# Operator Precedence
# Operator precedence describes the order in which operations are performed.

"""Example
Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first"""
print((6 + 3) - (6 + 3)) # The output is 0
print()
# Multiplication * has higher precedence than the addition + , and therefore multiplications are evaluated before addiction
print(100 + 5 *3) #the output is 115

# The precedence order is described in the table below, starting with the highest precedence at the top:

"""Operator	Description	Try it
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR"""

# If two operators have the same precedence, the expression is evaluated from left to right.
# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3) #it evaluate from left to right

