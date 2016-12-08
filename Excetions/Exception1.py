
def func(x, y):
    z = x / y
    print("After divs")
    return z


def main():
    try:
        result = func(10, 0)
    except ZeroDivisionError as e:
        print(e)
    except FileExistsError:
        pass
    else:
        print(result)
    finally:
        print("We will always end up here")



if __name__ == '__main__':
    main()