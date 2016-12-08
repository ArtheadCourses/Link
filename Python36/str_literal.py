# Note String literals only work in Python 3.6 and upward
def main():
    name = 'John'
    age = 37

    message = "Hi {0}, you are {1} years old".format(name, age)
    print(message)

    message2 = f"Hi {name}, you are {age} years old"
    print(message2)


if __name__ == '__main__':
    main()