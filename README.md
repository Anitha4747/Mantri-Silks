# Mantri-Silks
Mantri Silks Billing System
Description:

The Mantri Silks Billing System is a Python-based application designed to streamline the billing process for a dress shop. It calculates the total bill by applying discounts based on customer loyalty (credit points) and taxes (GST) based on the total purchase amount. The system also provides customers with a free gift at the end of the transaction.

Features:

Credit Point System: Randomly assigns a customer loyalty level (credit points) that determines the discount percentage. Customers range from new to over 1 year with varying discounts from 2% to 10%.
GST Calculation: Automatically calculates GST based on the total amount, applying 1% for totals ≤ Rs.1000, 1.5% for totals ≤ Rs.10,000, and 3% for totals above Rs.10,000.
Gift Feature: Each customer receives a randomly selected gift such as a pen, notebook, or tiffin box as a thank-you token.
Detailed Invoice: Displays a full breakdown of the total amount, discount, tax, and the final payable amount.
How It Works:

A customer’s total purchase amount is input into the system.
A random credit point is generated, which determines the discount applied.
GST is calculated based on the total amount.
The final bill, including discounts, tax, and a free gift, is displayed.
Technologies Used:

Python
Random and Datetime modules: For credit point assignment and timestamp generation.

Usage:

Clone the repository and run the script.
Enter the total purchase amount to generate the bill.
Example Usage:

python
Copy code
customer = DressShop(6754)
customer.display()
Future Enhancements:

Add customer-specific details (name, phone number, etc.).
Store billing records in a database or text file.
Expand gift options for customers.
