import random
import time
import re


def main_menu():
    time.sleep(1)
    print("MAIN MENU")
    print("1. String Operation")
    print("2. Number Operation")
    print("3. Prime Number Checker") 
    print("4. Palindrome Checker")
    print("5. Factorial Sum Calculator")  
    print("6. String Length Calculator") 
    print("7. EXIT")

def main():
    
    while (True):
        main_menu()
        choice = input('\nEnter choice(1, 2, 3, 4, 5, 6, or 7): ')
        print()

        if choice == '1':
            while True:
                rchoice = input('Choice(1-> EmailValidation, 2-> RandomNumberGenerator, 3-> Pyramid, 4-> Convert to Uppercase): ')
                print()
                if rchoice == '1':
                    email = input("\nEnter an email address: ")
                    if (fnEmailValidation(email)) is True:
                        print(f"\nProvided email address [{email}] is valid")
                    else:
                        print(f"\nProvided email address [{email}] not valid")
                elif rchoice == '2':
                    filename = "outputFile.txt"  
                    write_lines_to_file(filename)
                elif rchoice == '3':
                    n = int(input("How many number? "))
                    createPyramid(n)
                elif rchoice == '4':
                    text = input("Enter a string: ")
                    print(f"Uppercase string: {fnConvertToUppercase(text)}")
                elif rchoice == '5':
                    break
                else:
                    print('\nInvalid input !!!')
                print()

        if choice == '2':
            while True:
                print("\n 1 for Number Reverse")
                print("\n 2 for Fibonacci Series")
                print("\n 3 for Find Factorial of a Number")
                print("\n 4 for Even Number Set")
                print("\n 5 for Greatest number between 3")
                print("\n 6 for Generate 100 Random Numbers and write in a file")
                print("\n 7 for Armstrong Number Check")
                echoice = input('\nEnter choice(1-7): ')
                print()
                if echoice == '1':
                    fnReverseNumber()
                elif echoice == '2':
                    fibo()
                elif echoice == '3':
                    n = int(input("Enter a number: "))
                    print(f"Factorial of {n} is {fnFactorial(n)}")
                elif echoice == '4':
                    fnEvenNumberSet()
                elif echoice == '5':
                    x = input("Enter a number: ")
                    y = input("Enter a number: ")
                    z = input("Enter a number: ")
                    print(f"Greatest number between {x}, {y}, and {z} is {max_of_three(x, y, z)}")
                elif echoice == '6':
                    fnRandomNumberGenerator()
                elif echoice == '7':
                    n = int(input("Enter a number: "))
                    if fnArmstrongNumberCheck(n):
                        print(f"{n} is an Armstrong number.")
                    else:
                        print(f"{n} is not an Armstrong number.")
                else:
                    print('\nInvalid input !!!')
                    break

       
        elif choice == '3':  
            number = int(input("Enter a number to check if it's prime: "))
            if fnPrimeNumberChecker(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")

        elif choice == '4':  
            user_input = input("Enter a string or number to check if it's a palindrome: ")
            if fnPalindromeChecker(user_input):
                print(f"'{user_input}' is a palindrome.")
            else:
                print(f"'{user_input}' is not a palindrome.")

        elif choice == '5': 
            number = int(input("Enter a number: "))
            print(f"The sum of factorials of digits of {number} is {fnFactorialSum(number)}")

        elif choice == '6':  
            text = input("Enter a string: ")
            print(f"The length of the string '{text}' is {len(text)}")

        elif choice == '7':
            print('Thanks for using the program')
            break        

        else:
            print('Invalid input!!!')
            print()



def fnConvertToUppercase(text):
    return text.upper()



def fnArmstrongNumberCheck(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number


def fnFactorialSum(number):
    return sum(fnFactorial(int(digit)) for digit in str(number))


def fnPrimeNumberChecker(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def fnPalindromeChecker(value):
    value = str(value).replace(" ", "").lower()
    return value == value[::-1]


def write_lines_to_file(filename):
    lines = []
    print("Enter multiple lines of text (type 'DONE' on a new line to finish):")
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
        print(f"File [{filename}] has been saved successfully!")


def fnEvenNumberSet():
    print("Print even numbers from 1 to N")
    n = int(input("Enter a number to set range: "))
    i = -1
    while i < n:
        i += 1
        if i % 2 == 1:
            continue
        print(i, end=" ")


def max_of_two(x, y):
    if x > y:
        return x
    return y


def fnRandomNumberGenerator():
    file = open("100Numbers.txt", "w")
    for i in range(100):
        number = random.randint(1, 100)
        file.write(str(number) + " ")
    file.close()

    file2 = open("100Numbers.txt", "r")
    print(file2.read())
    file2.close()


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


def fnEmailValidation(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


def createPyramid(n):
    for i in range(0, n):
        print("#" * i)

    for i in range(n, 0, -1):
        print("#" * i)


def fnFactorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * fnFactorial(n - 1)


def fnReverseNumber():
    n = int(input("Enter a number: "))
    l = len(str(n))
    print("Reverse number is: ")
    for i in range(l):
        x = n % 10
        y = int(n / 10)
        print(x, end=' ')
        n = y


def fibo():
    n = int(input("\nEnter a number for the series: "))
    a, b = 0, 1
    print(a, end=' ')
    x = 0
    while x <= n:
        c = a + b
        x += 1
        print(c, end=' ')
        a = b
        b = c


main()
