# fizzbuzz
# If a number is divisble by 3, print fizz
# If a number is divisble by 5, print buzz
# If a number is divisible by both, print fizzbuzz

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")

for num in range(1,100):
    fizzbuzz(num)