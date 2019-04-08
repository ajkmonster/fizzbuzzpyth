for x in range(1,100,1):
    if x%5==0 & x%3==0:
        print ('Fizzbuzz')
    elif x%5==0:
        print('Buzz')
    elif x%3==0:
        print('Fizz')
    else:
        print(x)
