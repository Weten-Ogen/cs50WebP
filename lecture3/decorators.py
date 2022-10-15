def announce(f):
    def wrapper():
        print("Before he said it: ")
        f()
        print("Afterwards....")
    return wrapper

@announce
def hello():
    print("hello World ")

hello()


