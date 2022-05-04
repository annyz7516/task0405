from fibonacci import Fibonacci
fib = Fibonacci()

print('Get the nth number in the fibonacci sequence.')
n = input('Enter a positive integer n: ')
print('Fibonacci number is:', fib.get_fibonacci(n))

print('------------------------')

print('Is number F a fibonacci number?')
f = input('Enter a positive integer F: ')
if fib.is_fibonacci(f):
    print(f, 'is a fibonacci number, index is', fib.get_index(f))
else:
    print(f, 'is not a fibonacci number, the closest fibonacci number index is', fib.get_index(f))






