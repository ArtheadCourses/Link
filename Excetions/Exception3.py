class MyException(Exception):
    def __init__(self, error_code, location, msg):
        super().__init__()
        self.error_code = error_code
        self.location = location
        self.msg = msg

    def __str__(self):
        return "There was an error in {0} with code: {1}. Message: {2}.".\
            format(self.location, self.error_code, self.msg)

def func1():
    # some code
    # something goes wrong
    raise MyException(34, "func1()", "Something went wrong")

def main():
    try:
        func1()
    except MyException as e:
        print(e)
    
if __name__ == '__main__':
    main()