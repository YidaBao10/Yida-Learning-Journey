#%%
x = input("what's x?")
y = input("what's y?")
z = int(x) + int(y)
print(z)
# %%
x = int(input("what's x?"))
y = int(input("what's y?"))

print(x+y)
# %%
x = float(input("what's x?"))
y = float(input("what's y?"))
print(x+y)
# %%
x = float(input("what's x?"))
y = float(input("what's y?"))
z = round(x+y)  #round表示取x+y的整数部分  四舍五入
print(z)
# %%
x = float(input("what's x?"))
y = float(input("what's y?"))
z = round(x+y) 
print(f"{z:,}")  #能实现三位数一个逗号
# %%
x = float(input("what's x?"))
y = float(input("what's y?"))
z = round(x/y,2)
print(z)
# %%

def main():
    x = int(input("what's x?"))
    print("x squared is",square(x))


def square(n):
    return n*n  #return的作用是作为函数的出口，将内部计算得到的结果传递给另一个函数

main()
# %%

def main():
    x = int(input("what's x?"))
    print("x squared is",square(x))


def square(n):
    return pow(n,2)

main()