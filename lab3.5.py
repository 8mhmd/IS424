x = int(input("Enter a number of repetitions"))

def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(x):
            func(*args, **kwargs)
    return wrapper

@repeat
def hello():
    print('Hello')

hello()
