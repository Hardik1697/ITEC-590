def fizz_buzz(num):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        num_str = str(num)
        print(num_str)

def main():
    fizz_buzz(3)
    fizz_buzz(5)
    fizz_buzz(15)
    fizz_buzz(10)
    fizz_buzz(98)

if __name__ == "__main__":
    main()
