from stack import Stack


def bracketsChecker(symbolString: str) -> bool:
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        elif s.isEmpty():
            balanced = False
        else:
            top = s.pop()
            if not matches(top, symbol):
                balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)


if __name__ == '__main__':
    print(bracketsChecker("{{([][])}()}"))
    print(bracketsChecker("[[{{(())}}]]"))
    print(bracketsChecker("[][][](){}"))
    print(bracketsChecker("([)]"))
    print(bracketsChecker("((()]))"))
    print(bracketsChecker("[{()]"))