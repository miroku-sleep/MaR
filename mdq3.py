def shift(char, n):
    t=ord(char)-n
    if t<65:
        t+=26
    return chr(t)

code=input("code: ")
code=code.upper()
i=1
decode=""
for char in code:
    decode=decode+shift(char, i)
    i+=1

print(f"decoded message: {decode}")