

# Data types
# Indexing, Negative indexing.

# Integers
print(123_342_534)


# precedence
# () >  literal ( **  ) >  / *  > - +    (    Left to right )

# round :> This function rounds the passed number.

# f String :
# print(f"String here {variable_1}, Data here {variable_2}")


# Tip Calculator Project:
str1 = "Welcome to Tip calculator "
str2 = "What was the Total Bill? $ : "
str3 = "What tip ( % ) would you like to give? 10 | 12 or 15 " 
str4 = "How many people to Split the bill with? "
resultDisplay = f"Each Person should Amount : $ "

print(str1)
totalBill = float(input(str2))
perTip = int(input(str3))
split = int(input(str4))

result = (totalBill * (  perTip / 100  ) ) + totalBill
result = round(result,2)

if split > 0:
    result = result / split
    print("Each need to pay $ :" ,result)


print("Total Bill :  ", result)
print("Tipeed  %", perTip)
