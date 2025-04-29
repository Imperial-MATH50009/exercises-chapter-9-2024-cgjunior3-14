import numbers


class Expression:
    def __init__(self, operands):
        self.operands = operands

    def __add__(a, b):
        return Add(a, b)

    def __sub__(a, b):
        return Sub(a, b)

    def __mul__(a, b):
        return Mul(a, b)

    def __truediv__(a, b):
        return Div(a, b)

    def __pow__(a, b):
        return Pow(a, b)


class Operator(Expression):
    super().__init__([])

    def __repr__(self):
        return type(self).__name__ + repr(self.operands)


class Add(Operator):
    super().__init__([])


class Sub(Operator):
    super().__init__([])


class Mul(Operator):
    super().__init__([])


class Div(Operator):
    super().__init__([])


class Pow(Operator):
    super().__init__([])


class Terminal(Expression):
    def __init__(self, value):
        self.value = value
        super().__init__([])

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


class Symbol(Terminal):
    def __init__(self, value):
        if isinstance(value, str):
            super().__init__(value)
        else:
            raise TypeError(f"Expected a string, got {type(value)}")


class Number(Terminal):
    def __init__(self, value):
        if isinstance(value, numbers.Number):
            super().__init__(value)
        else:
            raise TypeError(f"Expected a number, got {type(value)}")
