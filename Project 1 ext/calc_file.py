# ---------------- CLASSES ----------------
class MainCalc:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2


class Addition(MainCalc):
    def result(self):
        return self.n1 + self.n2, "+"


class Subtraction(MainCalc):
    def result(self):
        return self.n1 - self.n2 , "-"


class Multiplication(MainCalc):
    def result(self):
        return self.n1 * self.n2, "*"


class Division(MainCalc):
    def result(self):
        try:
            return self.n1 / self.n2, "/"
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero is not allowed.")


class AddAll:
    def __init__(self, numbers):
        self.numbers = numbers

    def result(self):
        total = 0
        for x in self.numbers:
            total += x
        return total, "+"


class MultiplyAll:
    def __init__(self, numbers):
        self.numbers = numbers

    def result(self):
        if not self.numbers:
            return 1
        product = 1
        for x in self.numbers:
            product *= x
        return product, "*"


# ---------------- FUNCTIONS ----------------
def get_history():
    with open("../project 1/trial.csv", "r") as file:
        for line in file:
            print(line)

def history(operation, n1=None, n2=None, list1=None):
    new_rec = f"\n{operation}, {n1}, {n2}, {list1}"
    try:
        with open("../project 1/trial.csv", "a") as file:
            file.write(new_rec)

        print("History updated.")

    except Exception as e:
        print("Encountered an error: " + str(e))


def menu():
    print('''------MAIN MENU------
1. Addition
2. Subtraction
3. Multiplication
4. Division

For more than 2 numbers:
5. Add all
6. Multiply all

7. View History
8. Exit
''')
    while True:
        choice = input("Enter your choice (1-8): ").strip()
        if choice.isdigit():
            ci = int(choice)
            if 1 <= ci <= 8:
                return ci
        print("Invalid choice — enter a number from 1 to 6.")


def get_two_numbers(prompt1="Enter the first number: ", prompt2="Enter the second number: "):
    while True:
        try:
            n1 = float(input(prompt1).strip())
            n2 = float(input(prompt2).strip())
            return n1, n2
        except ValueError:
            print("Please enter valid numbers (integers or decimals).")


def get_number_list():
    numbers = []
    print("Enter numbers one by one. Type 'done' (or press Enter on an empty line) to stop.")
    while True:
        s = input("Number (or done): ").strip()
        if s == "" or s.lower() == "done":
            break
        try:
            num = float(s)
            numbers.append(num)
        except ValueError:
            print("Not a number — stopping input.")
            break
    return numbers


# ---------------- MAIN PROGRAM ----------------
def main():
    ans = "Y"
    while ans.upper() == "Y":
        res = None
        opr = None
        a = b = None
        nums = None

        c1 = menu()

        if c1 in {1, 2, 3, 4}:
            a, b = get_two_numbers()
            if c1 == 1:
                res,opr = Addition(a, b).result()
                print(f"The sum is: {res}")
            elif c1 == 2:
                res,opr = Subtraction(a, b).result()
                print(f"The difference is: {res}")
            elif c1 == 3:
                res,opr = Multiplication(a, b).result()
                print(f"The product is: {res}")
            else:  # division
                try:
                    res,opr = Division(a, b).result()
                    print(f"On division we get: {res}")
                except ZeroDivisionError as e:
                    print(e)

        elif c1 in {5, 6}:
            nums = get_number_list()
            if c1 == 5:
                res,opr = AddAll(nums).result()
                print(f"The sum of all the numbers is: {res}")
            else:
                res,opr = MultiplyAll(nums).result()
                print(f"The product of all the numbers is: {res}")


        elif c1 == 7:
            get_history()


        elif c1 == 8:
            print("Thank you for using our calculator")
            quit()

        else:
            print("Invalid choice")

        if res is not None:
            history(opr, n1=a, n2=b, list1=nums)


        ans = input("Do you want to continue? (Y/N): ").strip() or "N"

    print("Thank you for using our calculator")


if __name__ == "__main__":
    main()
