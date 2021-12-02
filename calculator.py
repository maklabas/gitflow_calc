class Calculator:
    def __init__(self, num1: float, num2: float, oper: str):
        self.num1 = num1
        self.num2 = num2
        self.oper = oper
        self.__supported_operations = ("+", "-", "/", "*")
        self.__supported_compare_operations = ("<", ">")

    @property
    def calculation(self):
        if self.oper in self.__supported_operations:
            if self.num1 == 0 and self.oper == "/":
                return "Division by zero"
            return eval(f"{self.num1}{self.oper}{self.num2}")
        elif self.oper == "<":
            return f"{self.num1} bigger than {self.num2}"
        elif self.oper == ">":
            return f"{self.num2} bigger than {self.num1}"
        else:
            return "Unexpected format"


if __name__ == "__main__":
    running = True
    while running:
        number1 = float(input("\n\nEnter first number "))
        number2 = float(input("Enter second number "))
        operator = input("Enter operator    ")

        calc = Calculator(number1, number2, operator)
        print(calc.calculation)
        guess = input("Do you want to continue?\n"
                      "Press 'y' or 'yes' to continue\n")

        if guess not in ('y', 'yes'):
            running = False
