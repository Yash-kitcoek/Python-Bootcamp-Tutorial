import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Calculator")

    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"],
                        help="Operation to perform")

    args = parser.parse_args()

    if args.operation == "add":
        print(args.num1 + args.num2)
    elif args.operation == "sub":
        print(args.num1 - args.num2)
    elif args.operation == "mul":
        print(args.num1 * args.num2)
    elif args.operation == "div":
        if args.num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(args.num1 / args.num2)

if __name__ == "__main__":
    main()