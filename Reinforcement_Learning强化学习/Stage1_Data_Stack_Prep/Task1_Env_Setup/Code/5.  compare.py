#%%
x = int(input("what's x?"))
y = int(input("what's y?"))

if x<y:
    print("x is less than y")
if x>y:
    print("x is greater than y")
if x==y:  #不能用一个等号，不然就是赋值了
    print("x is equal to y")
# %%
x = int(input("what's x?"))
y = int(input("what's y?"))

if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else x==y:  
    print("x is equal to y")

# %%
x = int(input("what's x?"))
y = int(input("what's y?"))

if x<y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# %%
x = int(input("what's x?"))
y = int(input("what's y?"))

if x != y:  #!= means not be equal to
    print("x is not equal to y")
else:
    print("x is equal to y")
