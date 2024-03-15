n = int(input('Give me a Number : '))
print("\n")

for i in range(n):
    i += 1
    if i % 3 == 0 and i % 5 == 0 :
        print('FizzBuzz')
    elif i % 3 == 0 :
        print('Fizz')
    elif i % 5 == 0 and i % 3 != 0 :
        print('Buzz')
    elif i % 5 != 0 and i % 3 != 0:
        print(f'{i}')

    
    
