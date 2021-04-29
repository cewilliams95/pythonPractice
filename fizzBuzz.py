# Ye old classic FizzBuzz:
# Divisible by 3 => Fizz
# Divisible by 5 => Buzz
# Divisible by both => FizzBuzz
# Neither => return input in str form
import random

def fizzbuzz(i):
    res = ""
    if (i % 3 == 0):
        res = res + "Fizz"
    if (i % 5 == 0):
        res = res + "Buzz"
    if res == "":
        res = res + str(i)
    print("(" + str(i) + ") => " + res)
    return res

def main():
    tests = [random.randint(1,1000) for _ in range(10)]
    for test in tests:
        fizzbuzz(test)

if __name__ == "__main__":
    main()