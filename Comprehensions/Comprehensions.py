
def main():

    num_list = [1, 2, 3, 4, 5, 6, 7]
    result_list = []
    for value in num_list:
        if value != 3:
            result_list.append(value**2)
        else:
            result_list.append(value**3)

    print(result_list)
    comp_list = [value**2 if value != 3 else value**3 for value in num_list]
    print(comp_list)


if __name__ == '__main__':
    main()