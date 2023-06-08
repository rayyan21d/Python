# Tkinter

## Tkinter


## Deep dive on Python arguments.

### Positional arguments
These are the arguments that are passed to the function in correct positional order. The number of arguments in the function call should match exactly with the function definition.

### Keyword arguments
When we call a function with some values, these values get assigned to the arguments according to their position. Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed. Following calls to the above function are all valid and produce the same result.

### Default arguments
A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument. 

### Positional variable-length arguments
In the function definition, we use an asterisk (*) before the parameter name to denote this kind of argument. The arguments are passed as a tuple and these passed arguments make tuple inside the function with same name as the parameter excluding asterisk.
`
def add(*args):
    '''You can also do whatever you can using tuples, like indexing, slicing, etc. 
    '''
    first = args[0]
    
    sum = 0
    for i in args:
        sum += i
    print(sum)
`

### Keyword variable-length arguments
We use two asterisk (**) before the parameter name to denote this type of argument. The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as the parameter excluding two asterisks.
`
def calculate(**kwargs):
    print(type(kwargs)) #<class 'dict'>

    '''It allows you to do whatever you can do with dictionaries, like indexing, slicing, etc.
    '''
    
`

`
class Car:
    def __init__(self, **kw):
    
        #using get will return None if the user key is not found
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='Nissan', model='GT-R')
`

### Unpacking arguments
The single asterisk form can be used to unpack an iterable into the list. The double asterisk form can be used to unpack an iterable into the dictionary.
Example:
```python
def sum(a, b, c):
    print(a + b + c)

# A list of arguments
list = [1, 2, 3]

# Unpacking list into arguments
sum(*list) # sum(1, 2, 3)

# A dictionary of arguments
dict = {'a': 1, 'b': 2, 'c': 3}

# Unpacking dictionary into arguments
sum(**dict) # sum(1, 2, 3)
```

### Lambda functions
In Python, anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions. It has the following syntax:


### Python Closures
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

### Python Decorators
Python has an interesting feature called decorators to add functionality to an existing code. This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
Decorators are usually called before the definition of a function you want to decorate.

### Python Property
Python has a great concept called property which makes the life of an object oriented programmer much simpler. While using getters and setters we have to explicitly define the getter and setter functions and then call them separately. There is a lot of boilerplate code to be written for this simple looking code as seen in the above example.

### Python Iterators
Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

### Python Generators
Python generators are a simple way of creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). Generators are best for calculating large sets of results (particularly calculations involving loops themselves) in cases where we don’t want to allocate the memory for all of the results at the same time. Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly. The infinite sequence generator above does not have such a problem as the values it returns are generated on the fly. Generator functions are syntactic sugar for writing objects that support the iterator protocol. Generators abstract away much of the boilerplate code needed when writing class-based iterators. Python generators are a simple way of creating iterators. Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).



### Python Decorators

Python has an interesting feature called decorators to add functionality to an existing code. This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.

Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

Decorators are usually called before the definition of a function you want to decorate.
