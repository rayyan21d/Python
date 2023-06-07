# The NATO phonetic alphabet 

## The NATO phonetic alphabet, is the most widely used set of clear code words for communicating the letters of the Roman alphabet.

To create the code, a series of international agencies assigned 26 code words acrophonically to the letters of the Roman alphabet, with the intention of the letters and numbers being easily distinguishable from one another over radio and telephone, regardless of language barriers and connection quality. The specific code words varied, as some seemingly distinct words were found to be ineffective in real-life conditions. In 1956, NATO modified the then-current set of code words used by the International Civil Aviation Organization (ICAO); this modification then became the international standard a few years later. The words were chosen to be accessible to speakers of English, French and Spanish.


## What is List Comprehension ?

### List comprehension is an elegant way to define and create lists based on existing lists. This feature is added in Python 2.0. List comprehension is generally more compact and faster than normal functions and loops for creating list. Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension. You can also use it with strings.

### How to use it?

`
list =[1,2,3,4]
new_list = [new_item for item in list]
`

### It gets better: You can add conditions!

`
list =[1,2,3,4,5,6,7,8,9,10]
new_list = [new_item for item in list if item % 2 != 0]
`

`
numbers_list = [1,2,3,4,5,6,7,8,9,10,11]
odd_sq_nums =[num**2 for num in numbers_list if num % 2 != 0]
`

## What is Dictionary Comprehension ?

### Dictionary comprehension is an elegant and concise way to create dictionaries. We can create dictionaries using simple expressions. A dictionary comprehension takes the form {key: value for (key, value) in iterable}. A dictionary comprehension is like a list comprehension, but it constructs a dict instead of a list. They are convenient to quickly operate on each (key, value) pair of a dict. And often in one line of code, maybe two after checking PEP8

### How to use it?

`
new_dict = {new_key:new_value for item in list}
`

## What are Python Sequences?

### A sequence is an *ordered* collection of similar or different data types. Python has the following built-in sequence data types: String, List, Tuple, Range

String: A string value is a collection of one or more characters put in single, double or triple quotes. In python there is no character data type, a character is a string of length one. It is represented by str class. Strings in python are immutable. Python doesn’t support a character type; these are treated as strings of length one, thus also considered a substring.

range: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

tuple: A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

list: A list is a collection which is ordered and changeable. In Python lists are written with square brackets.