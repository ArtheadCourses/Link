# Note Variable type annotations only work in Python 3.6 and upward
def main():
    values: list[int] = []
    values.append('Hi')
    print(values)

    x: int = 10
    x = 'Hi'
    print(x)



    
if __name__ == '__main__':
    main()