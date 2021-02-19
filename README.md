# simple-matrix-calculatorMATH133 Calculator by Christian Zhao

This calculator has 5 instructions:
calculate('determinant', 'dec'/'frac', decimal place/max denominator)
calculate('inverse', 'dec'/'frac', decimal place/max denominator)
calculate('rref', 'dec'/'frac', decimal place/max denominator)
calculate('curve fitting', 'dec'/'frac', decimal place/max 
denominator)

The first argument specifies the thing you want to calculate.
The second and third arguments are optional, and are to be
explained later in this user guide.

Please note:
Do not modify the name of the text file Input.txt
Do not modify the first line in CALCULATOR.py

How to use the calculator:
1. Enter your input in the text file Input.txt and save it
2. Use one or more of the above five instructions in CALCULATOR

*If you want to calculate the determinant, the inverse, or the 
RREF of a matrix, open the text file named Input, and enter in
your matrix in the following format:

1,3,4,5
0,1,2,5
4,3,1,6

, and use one of the first three instructions above.

*If you want to calculate the solution of an augmented matrix
Ax = y, enter y as the last column after A.
For example, if you want to solve for x with the above matrix
as A, and your y vector is [1,2,3], you should enter:

1,3,4,5,1
0,1,2,5,2
4,3,1,6,3

and use the instruction calculate('rref') to calculate.
The last column of the resulting matrix is the solution.

*If you want to find the polynomial equation of the best fit line
of any number of points you have, with any degree you want, 
enter the coordinates of the points and degree in the 
following format:

1,2
2,3
3,3
4,2
4

The last line is your wanted degree.
This one is to calculate the equation of the polynomial with 
degree 4 that best fits the points (1,2),(2,3),(3,3),(4,4).
With calculate('curve fitting'), you should get:
y = -0.0055x^4 + 0.0549x^3 + -0.6923x^2 + 2.7747x + -0.1319

*You can choose whether numbers are displayed as fractions
or not, and the default is decimal. You can enter your
wanted maximum denominator of these fractions, which is set by 
default 1000, you can also enter your wanted decimal places of
these numbers, which is set by default 4.
This functionality does not apply to the polynomial instruction.

examples:
calculate('curve fitting', 'frac')
calculate('curve fitting', 'frac', 100)
calculate('inverse', 'dec', 5)
