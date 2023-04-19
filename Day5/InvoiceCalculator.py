#Problem Statement: Create a command-line program in Python to Calculate the total invoice amount for the below purchases - 

#Book - Introduction to Python Programming: Rs 499.00
#Book - Python Libraries Cookbook: Rs. 855.00
#Book - Data Science in Python: Rs. 645.00


#Taxes and additional charges are described as details - 

#GST: 12%
#Delivery Charges: Rs. 250.00


books=["Introduction to Python Programming","Python Libraries Cookbook","Data Science in Python"]

book_price=[499.00,855.00,645.00]

GST=0.12 #12%
Delivery_charge=250.00

Amount_without_charges=0
Total_invoice_amount=0

for i in range(0,len(book_price)):
    Amount_without_charges +=book_price[i]
print("Cost of books without additional charges is Rs",Amount_without_charges)

extra_charges= GST*Amount_without_charges+Delivery_charge
Total_invoice_amount=extra_charges+Amount_without_charges

#Printing total Invoice amount for the Books 
print("Total Amount to be paid for the books is Rs",Total_invoice_amount)