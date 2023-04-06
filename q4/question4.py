def factorial(a) :
    if a == 0 :
        return 1;
    else :
        return a * factorial(a-1)   


def main() :
    print("******Factorial Program******")
    print("Result of 0:  ",factorial(0))
    print("Result of 2:  ",factorial(2))
    print("Result of 4:  ",factorial(4))
    print("Result of 6:  ",factorial(6))
    print("Result of 8:  ",factorial(8))
    print("Result of 10: ",factorial(10))
    print("Result of 12: ",factorial(12))
    print("Result of 14: ",factorial(14))


if __name__ == "__main__":
    main()
