# Importar a classe ErrNum
from math import sqrt

class ErrNum:
    def __init__(self, value, error):
        self.value = float(value)
        self.error = float(error)

    def __repr__(self):
        return f"{self.value}({self.error})"

    def __add__(self, other):
        if isinstance(other, ErrNum):
            value = self.value + other.value
            error = sqrt(self.error**2 + other.error**2)
            return ErrNum(value, error)
        elif isinstance(other, (int, float)):
            value = self.value + other
            return ErrNum(value, self.error)
        else:
            raise TypeError("Unsupported operand types")

    def __sub__(self, other):
        if isinstance(other, ErrNum):
            value = self.value - other.value
            error = sqrt(self.error**2 + other.error**2)
            return ErrNum(value, error)
        elif isinstance(other, (int, float)):
            value = self.value - other
            return ErrNum(value, self.error)
        else:
            raise TypeError("Unsupported operand types")

    def __mul__(self, other):
        if isinstance(other, ErrNum):
            value = self.value * other.value
            error = sqrt(
                (other.value * self.error)**2 + (self.value * other.error)**2
            )
            return ErrNum(value, error)
        elif isinstance(other, (int, float)):
            value = self.value * other
            return ErrNum(value, abs(self.error * other))
        else:
            raise TypeError("Unsupported operand types")

    def __truediv__(self, other):
        if isinstance(other, ErrNum):
            if other.value != 0:
                value = self.value / other.value
                error = sqrt(
                    (self.error / other.value)**2
                    + (self.value * other.error / other.value**2)**2
                )
                return ErrNum(value, error)
            else:
                raise ZeroDivisionError("Division by zero")
        elif isinstance(other, (int, float)):
            if other != 0:
                value = self.value / other
                return ErrNum(value, abs(self.error / other))
            else:
                raise ZeroDivisionError("Division by zero")
        else:
            raise TypeError("Unsupported operand types")

    def __pow__(self, power):
        if isinstance(power, (int, float)):
            value = self.value**power
            error = abs(power * self.value**(power - 1) * self.error)
            return ErrNum(value, error)
        else:
            raise TypeError("Unsupported operand types")

    def __eq__(self, other):
        if isinstance(other, ErrNum):
            return abs(self.value - other.value) <= sqrt(
            self.error**2 + other.error**2
        )
        elif isinstance(other, (int, float)):
            return abs(self.value - other) <= self.error
        else:
            return False



# Exemplo de utilização da classe ErrNum
num1 = ErrNum(5.0, 0.2)
num2 = ErrNum(3.0, 0.1)
num3 = ErrNum(2.0, 0.3)

# Testar as operações numéricas
print(f"num1: {num1}")
print(f"num2: {num2}")
print(f"num3: {num3}")

sum_num1_num2 = num1 + num2
print(f"num1 + num2: {sum_num1_num2}")

diff_num1_num2 = num1 - num2
print(f"num1 - num2: {diff_num1_num2}")

mul_num1_num2 = num1 * num2
print(f"num1 * num2: {mul_num1_num2}")

div_num1_num2 = num1 / num2
print(f"num1 / num2: {div_num1_num2}")

pow_num1_2 = num1 ** 2
print(f"num1 ** 2: {pow_num1_2}")

print(f"num1 == num2: {num1 == num2}")
print(f"num1 == 5: {num1 == 5}")