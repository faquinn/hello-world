def exact_change(user_total):
   num_dollars = user_total//100
   user_total -= num_dollars*100
   num_quarters = user_total//25
   user_total -= num_quarters*25
   num_dimes = user_total//10
   user_total -= num_dimes*10
   num_nickels = user_total//5
   user_total -= num_nickels*5
   num_pennies = user_total


def main():
   user_total = int(input(""))
   if user_total <= 0:
       print('no change')
   else:
       num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_total)
   if num_dollars > 0:
        if num_dollars > 1:
            print('%d dollars' %num_dollars)
        else:
            print('%d dollar' %num_dollars)
   if num_quarters > 0:
        if num_quarters > 1:
            print('%d quarters' %num_quarters)
        else:
            print('%d quarter' %num_quarters)
   if num_dimes > 0:
        if num_dimes > 1:
            print('%d dimes' %num_dimes)
        else:
            print('%d dime' %num_dimes)      
   if num_nickels > 0:
        if num_nickels > 1:
            print('%d nickels' %num_nickels)
        else:
            print('%d nickel' %num_nickels)
              
   if num_pennies > 0:
        if num_pennies > 1:
            print('%d pennies' %num_pennies)
        else:
            print('%d penny' %num_pennies)

main()   



            

