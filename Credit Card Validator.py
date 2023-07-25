#Valid or Not!!
sum_of_odd = 0
sum_of_even = 0
credit_card = input("Enter the Credit Card Number without any characters or spaces: ")

if credit_card[0] == "5" or credit_card[0] == "2": 
    type = "Mastercard"

elif credit_card[0] == "4":
    type = "Visa"

else:
    type = "American Express"

credit_card = credit_card[::-1]


for i in credit_card[::2]:
    sum_of_odd += int(i)


for i in credit_card[1::2]:
    i = int(i) *2
    if int(i)>=10:
        sum_of_even += (1+int(i)%10)
    else:
        sum_of_even += int(i)




total = sum_of_even + sum_of_odd

if total % 10 == 0:
    print("The %s Credit Card is Valid" %type)
else:
    print("The Credit Card is NOT Valid")
