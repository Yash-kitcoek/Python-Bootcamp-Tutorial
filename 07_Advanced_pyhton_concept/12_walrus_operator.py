def very_slow_func():
    print("something...")
    print("something...")
    print("something...")
    print("something...")

    return 7

if((a:= very_slow_func()) > 10):
    print(a)

else:
    print("its not greater than 10")