#%%
def hello():  #def is for define, means to set up your own function
    print("hello")
name = input("what's your name?")
hello()
print(name)
# %%
def hello(to):  
    print("hello,",to)
name = input("what's your name?")
hello(name)
# %%
hello()
name = input("what's your name?")
hello(name)


def hello(to="world"):
    print("hello,",name)
#错误写法  必须在前面先定义函数才能使用
# %%
def main():  
    name = input("what's your name?")
    hello()


def hello():
    print("hello,",name)


main()
# %%
