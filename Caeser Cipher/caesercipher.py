import resourcesforcc
alpha="abcdefghijklmnopqrstuvwxyz"
def caeser(task):
    result=[]
    if task=="e":
        msg=input("Enter text to encode: ")
        shift_num = int(input("Enter the shift number: "))
        for n in msg:
            if n in alpha:
                pos = alpha.index(n)
                pos += shift_num
                while pos > 26:
                    pos = pos % 26
                result += alpha[pos]
            else:
                result += n
    elif task=="d":
        msg = input("Enter text to decode: ")
        shift_num = int(input("Enter the shift number: "))
        for n in msg:
            if n in alpha:
                pos = alpha.index(n)
                pos -= shift_num
                result += alpha[pos]
            else:
                result += n
    return result


print(resourcesforcc.logo)
repeat='y'
while repeat=='y':
    task=input("What do you want to do? Type 'e' to encode and 'd' to decode.\n")
    print(f"The decoded message is {''.join(caeser(task))}")
    repeat=input("Wanna go again? Type 'y' for yes and 'n' for no.")
