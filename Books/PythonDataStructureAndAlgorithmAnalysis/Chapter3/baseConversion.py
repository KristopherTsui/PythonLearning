from stack import Stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]
    
    return newString


if __name__ == '__main__':
    number10 = 233
    number8 = baseConverter(number10, 8)
    print(f"The octal number corresponding to a decimal number {number10} is", number8)
    number16 = baseConverter(number10, 16)
    print(f"The hexadecimal number corresponding to the decimal number {number10} is", number16)