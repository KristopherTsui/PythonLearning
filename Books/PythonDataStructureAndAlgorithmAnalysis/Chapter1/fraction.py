def gcd(m: int, n: int) -> int:
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:

    def __init__(self, top: int, bottom: int) -> None:
        if type(top) == int and type(bottom) == int:
            common = gcd(top, bottom)
            self.num = top // common
            self.den = bottom // common
        else:
            raise TypeError("Error: NUMERATOR AND DENOMINATOR MUST BE INTEGERS.")

    def __str__(self) -> str:
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other: object) -> object:
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)
    
    def __sub__(self, other: object) -> object:
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other: object) -> object:
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other: object) -> object:
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __gt__(self, other: object) -> bool:
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __ge__(self, other: object) -> bool:
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum

    def __lt__(self, other: object) -> bool:
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __le__(self, other: object) -> bool:
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum

    def __eq__(self, other: object) -> bool:
        firstnumber = self.num * other.den
        secondnum = other.num * self.den

        return firstnumber == secondnum

    def __ne__(self, other: object) -> bool:
        firstnumber = self.num * other.den
        secondnum = other.num * self.den

        return firstnumber != secondnum

    def show(self) -> None:
        print(self.num, "/", self.den)

    def getNum(self) -> int:
        return self.num

    def getDen(self) -> int:
        return self.den


if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(1, -4)
    print(f1 * f2)