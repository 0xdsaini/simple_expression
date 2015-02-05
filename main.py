#!/usr/bin/env python

# Copyright (C) 2015 Devesh Saini(futuredevesh@gmail.com).
#
# This file is part of simpleexpr.
#
#     simpleexpr is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     simpleexpr is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with simpleexpr.  If not, see <http://www.gnu.org/licenses/>.

plus = lambda x, y : x + y
minus = lambda x, y : x - y
multiply = lambda x, y : x * y
divide = lambda x, y : float(x) / float(y)

operations = {'+':plus, '-':minus, '*':multiply, '/':divide} #Key is operation sign and lambda function as values.

raw_expr = raw_input("Enter Expression : ")

expr = "".join(raw_expr.split()) #Remove spaces

num1 = int(expr[0])
num2 = None

for i in expr[1:]:

	if i in operations.keys():
		operation = operations[i]

	else:
		num2 = int(i)
		num1 = operation(num1, num2)

print num1
