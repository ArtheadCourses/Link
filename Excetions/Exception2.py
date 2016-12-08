
def func(x, y):
    if y == 0:
        raise ValueError("Parameter y can't be zero")
    z = x / y
    print("After divs")
    return z


def main():
    try:
        result = func(10, 0)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print(result)
    finally:
        print("We will always end up here")



if __name__ == '__main__':
    main()