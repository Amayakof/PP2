#Parsing from JSON to Python
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["city"])

#From Python to JSON
c = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
z = json.dumps(c)
print(z)

""" 
#types that work with JSON
print(json.dumps({"name": "John", "age": 30}))#dict
print(json.dumps(["apple", "bananas"]))#list
print(json.dumps(("apple", "bananas")))#tuple
print(json.dumps("hello"))#string
print(json.dumps(42))
print(json.dumps(31.76))#float
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
"""

#indent to define the numbers
print(json.dumps(x, indent=2))

#separators
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#Sort keys
print(json.dumps(x, indent=4, sort_keys=True))
#sorts the results alphabetically