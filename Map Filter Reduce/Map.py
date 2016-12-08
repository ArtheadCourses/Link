
def c2f(t):
    return (9.0/5) * t + 32

def main():
    temp_in_c = [16.5, 19.7, 23.4, 15.3]

    #temp_in_f = list(map(c2f, temp_in_c))
    #temp_in_f = list(map(lambda t: (9.0/5) * t + 32, temp_in_c))
    temp_in_f = [(9.0/5) * t + 32 for t in temp_in_c]

    print(temp_in_f)



if __name__ == '__main__':
    main()