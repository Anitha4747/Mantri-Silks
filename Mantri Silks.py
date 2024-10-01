import random
import datetime


class DressShop:
    def __init__(self, total_amount):
        self.total_amount = total_amount
        self.credit_point = None
        self.discount = 0
        self.tax = 0

    def display(self):
        print("   MANTRI SILKS     ")
        print(" 23A, Gandhi street, Tiruppur  ")

        now = datetime.datetime.now()
        print(now.strftime(" %d-%m-%y       %H:%M:%S  "))
        print('Amount:', self.total_amount)
        self.generate_credit_point()
        self.display_discount()
        self.calculate_Gst()
        self.total()
        self.gift()
        print("Thank You!!")
        print("COME AGAIN...")

    def generate_credit_point(self):
        a = ["*", "**", "***", "****", "*****"]
        self.credit_point = random.choice(a)
        print('Credit point:', self.credit_point)

    def display_discount(self):
        if self.credit_point == "*":
            print('New customer')
            discount_percentage = 2
            self.discount = round(self.total_amount * 0.02, 2)
        elif self.credit_point == "**":
            print('3 months customer')
            discount_percentage = 2.5
            self.discount = round(self.total_amount * 0.025, 2)
        elif self.credit_point == "***":
            print('6 months customer')
            discount_percentage = 5
            self.discount = round(self.total_amount * 0.05, 2)
        elif self.credit_point == "****":
            print('9 months customer')
            discount_percentage = 7.5
            self.discount = round(self.total_amount * 0.075, 2)
        else:
            print('Above 1 year customer')
            discount_percentage = 10
            self.discount = round(self.total_amount * 0.1, 2)

        print("Amount     Discount%     Discount ")
        print(f"{self.total_amount}        {discount_percentage}%              {self.discount}")

    def calculate_Gst(self):
        if self.total_amount <= 1000:
            tax_percentage = 1
            self.tax = round(self.total_amount * 0.01, 2)
        elif self.total_amount <= 10000:
            tax_percentage = 1.5
            self.tax = round(self.total_amount * 0.015, 2)
        else:
            tax_percentage = 3
            self.tax = round(self.total_amount * 0.03, 2)

        print("Amount      Tax%     Tax ")
        print(f"{self.total_amount}           {tax_percentage}%     {self.tax}")

    def total(self):
        total = round(self.total_amount - self.discount + self.tax,2)
        print("Amount    Discount     Tax")
        print(f"{self.total_amount}      {self.discount}    {self.tax}")
        print("Total Amount after Discount and Tax:", round(total,2))
    def gift(self):
        lst = ["Pen", "Tiffin box", "Notebook", "Glass", "Plate"]
        gift = random.choice(lst)
        print("Gift:", gift)


cus2 = DressShop(6754)
cus2.display()