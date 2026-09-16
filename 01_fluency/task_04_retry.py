
from functools import wraps


def retry(max_attempts):

    def decorator(function):

        @wraps(function) # preserve metadata info of the original function
        def wrapper(*args, **kwargs):

            for i in range(max_attempts):
                try:
                    return function(*args, **kwargs)

                except Exception:
                    if i == max_attempts - 1:
                        raise

        return wrapper

    return decorator

def announce(function): 
    def wrapper(*args, **kwargs):
        print("calling " + function.__name__)
        result = function(*args, **kwargs)
        print("finished " + function.__name__)
        return result
    return wrapper

def repeat(n): 
    def decorator(function):
        def wrapper(*args, **kwargs): 
            for i in range(n): 
                function(*args, **kwargs)
        return wrapper
    return decorator


def limit_calls(n): 
    calls = 0
    def decorator(function): 
        def wrapper(*args, **kwargs): 
            nonlocal calls
            calls += 1
            if calls <= 3: 
                return function(*args, **kwargs)
            else: 
                raise RuntimeError("Too many calls")
        return wrapper 
    return decorator
            


def log_calls(function): 
    def wrapper(*args, **kwargs): 
        print("calling " + function.__name__)
        print("args:", args)
        print("kwargs:", kwargs)
        result = function(*args, **kwargs)
        print("result: ", result)
        return result
        
    return wrapper

def main():
    @limit_calls(3)
    def foo(x):
        return x * 2


    print(foo(10))
    print(foo(20))
    print(foo(30))

    try:
        print(foo(40))
    except RuntimeError as e:
        print("Errore:", e)
if __name__ == "__main__":
    main()
