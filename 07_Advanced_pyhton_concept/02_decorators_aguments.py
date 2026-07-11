def repeat(n):          # Accept n
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def hello(a):
    print(f"Hello! {a}")

hello("Yash")