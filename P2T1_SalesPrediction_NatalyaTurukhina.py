# This program is going to calculate and display the profit
# based on the prjected amount of total sales.
# Date: 2/13/2019
# CTI-110 P2T1 - Sales Prediction
# Natalya Turukhina

#Get the projected total sales.
total_sales = float(input("Please, enter the projected amount of total sales: "))

#Calculate the profit as 23 percent of total sales and display the profit                    
print("This year the profit is going to be: $", format(total_sales * 0.23, ',.2f'))
