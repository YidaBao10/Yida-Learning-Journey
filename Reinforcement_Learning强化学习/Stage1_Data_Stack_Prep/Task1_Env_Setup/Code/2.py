#%%
name=input("what's your name?")
print ("hello,",name,sep="???")

#%%
name=input("what's your name?")
print (f"hello, {name}")

# %%
name = input("what's your name?")
name = name.strip()  #remove whitespace from string
print(f"hello,{name}")
# %%
name = input("what's your name?")
name = name.strip()  #remove whitespace from string
name = name.capitalize()  #capitalize user's name
print(f"hello,{name}")
# %%
name = input("what's your name?").strip().title()  #remove whitespace and capitalize every first letter
print(f"hello,{name}")
# %%
name = input("what's your name?").strip().title()
first, last = name.split(" ")  #split user's name into first name and last name
print(f"hello, {first}")
# %%
