#--------------CLASSES--------------
class main_calc():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2


class addition(main_calc):
    def __init__(self,n1,n2):
        super().__init__(n1,n2)

    def adding(self):
        print(f"The sum is: {self.n1 + self.n2}")


class subtraction(main_calc):
    def __init__(self,n1,n2):
        super().__init__(n1,n2)

    def minus(self):
        print(f"The difference is: {self.n1 - self.n2}")

class multiplication(main_calc):
    def __init__(self,n1,n2):
        super().__init__(n1,n2)

    def multiply(self):
        print(f"The product is: {self.n1 * self.n2}")

class division(main_calc):
    def __init__(self,n1,n2):
        super().__init__(n1,n2)

    def dividing(self):
        try:
            print(f"On division we get: {self.n1 / self.n2}")
        except ZeroDivisionError:
            print("Division by zero is not possible")


class addall():
    def __init__(self,list1):
        self.list1 = list1

    def add(self):
        sum = 0
        for i in range(len(self.list1)):
            sum += self.list1[i]
        print(f"The sum of all the numbers is: {sum}")


class multiplyall():
    def __init__(self, list1):
        self.list1 = list1

    def multiply(self):
        product = 1
        for i in range(len(self.list1)):
            product *= self.list1[i]
        print(f"The product of all the numbers is: {product}")

#------------------FUNCTIONS------------------------
def menu():
    print('''------MAIN MENU------
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division

    For more than 2 numbers:
    5. Add all
    6. Multiply all''')

    while True:
        choice = input("Enter your choice: ")
        if choice.isnumeric():
            return int(choice)
        else:
            print("Invalid choice")


def input_num():
    while True:
        n1 = input("Enter the first number: ")
        n2 = input("Enter the second number: ")

        if n1.isnumeric() and n2.isnumeric():
            return int(n1), int(n2)
        else:
            print("Please enter a valid number")


def input_list():
    list1 = []
    while True:
        num = input("Enter number (alphabet to stop): ")
        if num.isnumeric():
            list1.append(int(num))
        else:
            return list1


#------------------Main programme-----------------------
ans = "Y"
while ans == "Y":
    c1 = menu()

    l1 = [1,2,3,4]
    l2 = [5,6]
    if c1 in l1:
        a,b = input_num()
        if c1 == 1:
            sum = addition(a,b)
            sum.adding()
        elif c1 == 2:
            diff = subtraction(a,b)
            diff.minus()
        elif c1 == 3:
            product = multiplication(a,b)
            product.multiply()
        else:
            div = division(a,b)
            div.dividing()

    elif c1 in l2:
        list1 = input_list()
        if c1 == 5:
            total_sum = addall(list1)
            total_sum.add()
        else:
            total_product = multiplyall(list1)
            total_product.multiply()

    else:
        print("Invalid choice")

    ans = input("Do you want to continue? (Y/N): ")
    ans = ans.capitalize()


print("Thank you for using our calculator")


