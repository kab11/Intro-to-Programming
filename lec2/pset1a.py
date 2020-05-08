#!usr/bin/python

# Problem Set 0
# Name: kab11


num = 1000
hold = num

if num > 1:
    for i in range(2, hold):
        if (num % i) == 0:
            print(num, " -> is not prime")
            break;
    else:
        print(num, " -> is prime")
else:
    print(num, " -> is not prime")
