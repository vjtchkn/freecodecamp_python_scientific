class Category:
    def __init__(self, nm):
        self.name = nm
        self.ledger = []

    def get_balance(self):
        balance = 0
        for oper in self.ledger:
            balance += oper["amount"]
        return balance

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, other_cat):
        if self.withdraw(amount, f"Transfer to {other_cat.name}"):
            other_cat.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def get_spending(self):
        spending = 0
        for oper in self.ledger:
            if oper["amount"] < 0:
                spending += oper["amount"]
        return spending

    def __str__(self):
        title = self.name.center(30, "*")
        items = ""
        for item in self.ledger:
            items += (
                item["description"][:23].ljust(23)
                + f"{round(float(item['amount']), 2):.2f}"[:7].rjust(7)
                + "\n"
            )
        total = f"Total: {self.get_balance()}"

        output = title + "\n" + items + total
        return output


def create_spend_chart(categories):
    spending = []
    for cat in categories:
        spending.append({"name": cat.name, "spent": -cat.get_spending()})
    spent_total = 0
    for cat in spending:
        spent_total += cat["spent"]
    for cat in spending:
        cat["bar_height"] = int(cat["spent"] / spent_total * 10)
    print(spending)

    title = "Percentage spent by category\n"
    chart = ""
    width = 5 + len(categories) * 3
    for h in reversed(range(11)):
        line = f"{h * 10}| ".rjust(5)
        for cat in spending:
            if cat["bar_height"] >= h:
                line += "o  "
            else:
                line += " " * 3
        line = line.ljust(width) + "\n"
        chart += line
    h_line = " " * 4 + "-" * (width - 4)

    names = ""
    max_name_length = 0
    for cat in spending:
        if len(cat["name"]) >= max_name_length:
            max_name_length = len(cat["name"])

    for i in range(max_name_length):
        line = " " * 5
        for cat in spending:
            if len(cat["name"]) >= i + 1:
                line += cat["name"][i] + " " * 2
            else:
                line += " " * 3
        names += "\n" + line

    output = title + chart + h_line + names
    return output
