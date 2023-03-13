Python Iterators, Generators
Python Scope
Python Modules
Python Dates
Python Math
Python JSON:
 -Exercises to parse json data in python

#Iterator/Generators#
An iterator is an object that contains a countable number of values.
You can traverse through all the values of an iterator;
Iterable objects: -Lists, tuples, dictionaries, and sets

Разница в том что итераторы вызывают класс, а генератор работает с функцией
Чтобы функция возвращала объект-генератор, в ее теле должен быть оператор yield. 
Чтобы итератор не вызывался бесконечно, модно вызвать функцию StopIteration

#Scope#
A variable is only available from inside the region it is created. This is called scope.

- Local scope 
  A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

- Global scope
  A variable created in the main body of the Python code is a global variable and belongs to the global scope.

  Global variables are available from within any scope, global and local.

#Modules#

Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

To create a Module save a file with .py
- Now we can use the module we just created, by using the import statement

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
import mymodule as mx

a = mx.person1["age"]
print(a)

use dir() to list all names in module

You can import only one function from a module if you want to:
from mymodule import person1
print(person1["age'])

#Date module#
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime
x = datetime.datetime.now()
print(x)
>> 2023-03-09 14:27:22.364688 standard output
 methods
 - day, year, month
 - strftime(for weekday)
 - tzone(timezone)
 - microsecond
 - total_seconds
 to create a date, use class constructor

x = datetime.datetime(2005, 9, 21) //dont start with the '0' when writing dates

strftime() Method
use it as a shortcut to format the class into the readable version:

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

%A - weekday long
%a - weekday short
%B - Month long ver.
%b - Month short ver.

#Math
- min(), max() -> find values in range
- abs() -> absolute(module)
- pow() -> power
- math.sqrt()
- math.ceil() / math.floor() -> ronds num to the nearest int upwards/downwards
- math.pi() -> PI value

#JSON
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

Python has a built-in package called json, which can be used to work with JSON data.

Парсинг — это процесс автоматического сбора данных и их структурирования.
Парсить — собирать и систематизировать информацию, размещенную на определенных сайтах, с помощью специальных программ,
автоматизирующих процесс. 
Можно перевести с Python на json и обратно