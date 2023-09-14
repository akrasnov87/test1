
import numpy as np

print('Hello, World!!!')

w = 'World'
print(f'Hello, {w}!!!')

print(f'Hello,', 'World!!!')

def hello_world():
    return 'Hello, World!!!'

print(hello_world())

def hello(name):
    return f'Hello, {name}!!!'

print(hello('World'))

print('''
      Hello, World!!!   
''')

idx = 0

while True:
    idx += 1

    if idx >= 4:
        break
    else:
        print('Hello, World!!!')

s = 'Hello, World!!!'

print(s.replace(', World!!!', ''))

#n = input("Число: ")
#print(n.replace('.', '', 1).isdigit())

a = True
b = False

print(a)