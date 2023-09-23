from time import sleep

def scheduler(ms, f, **kwargs):
    sleep(ms/1000)
    f(**kwargs)


def userinfo(name, age):
    print(f"Name: {name}  Age: {age}")


scheduler(ms=2500, f=userinfo, name="Mohammad", age=21)