try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except:
    print('an error occured')

try:
    x = 5
    y = 0
    z = x/y
except:
    print('there is a zero division error')
finally:
    print('All Done')

def ask():
    while True:
        try:
            result = int(input('Type and integer: '))
        except:
            print('This is not an integer')
            continue
        else:
            return (result ** 2)
            break

print(ask())