
import argparse
# Add optional argument -v
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=int, help="the base")
    parser.add_argument("exponent", type=int, help="the exponent")
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="increase putput verbosity")
    args = parser.parse_args()
    answer = args.base**args.exponent
    if args.verbose >= 2:
        print("{0} to the power of {1} equals {2}".format(args.base, args.exponent, answer))
    elif args.verbose == 1:
        print("{0}^{1} = {2}".format(args.base, args.exponent, answer))
    else:
        print(answer)
    
if __name__ == '__main__':
    main()