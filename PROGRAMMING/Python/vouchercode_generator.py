print("""
+----------------------------+
|  *VOUCHER CODE GENERATOR*  |
+----------------------------+
""")

website = "www.udemy.com/"

discount_amount = int(input(" DISCOUNT AMOUNT "))
voucher_amount = int(input(" VOUCHER AMOUNT "))

code_start = 10
amount = code_start + voucher_amount

for code in range(code_start,amount):
    print(f"{website}?voucherCode ={discount_amount}{code}")
    code_start = amount

print(" CODE START = ",code_start)    
