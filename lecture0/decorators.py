def announce(f):
    def wrapper(f):
        print("start")
        f()
        print("end")
        return wrapper

@announce
def hello():
    return "hello world"

