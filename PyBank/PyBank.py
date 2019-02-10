#!/usr/bin/env python
# coding: utf-8

# In[21]:


import csv

d_list=[]


# In[22]:


filename = "Resources/budget_data.csv"
with open (filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    data = list(csvreader)
    current_volume = int(data[0][1])


# In[23]:


#Calculations
for row in data:
    next_volume = int(row[1])
    difference =  next_volume - current_volume
    current_volume = next_volume
    d_list.append(difference)
# Number of months
n_months = len(d_list)
# total profit over all months
total_profit = sum(int(row[1]) for row in data)
# average change
average = sum(d_list)/(len(d_list)-1)
# find greatest increase in profits
g_increase = max(int(row[1]) for row in data)
# find greatest decrease in profits
g_decrease = min(int(row[1]) for row in data)


# In[27]:


# Print out Summary
line1 = print("Finanical Analysis")
line2 = print("-----------------------")
line3 = print(f"Total Months: {n_months}")
line4 = print(f"Total: $ {total_profit}")
line5 = print(f"Average Change: $ {average:+.2f}")
line6 = print(f"Greatest Increase in Profits: {g_increase}")
line7 = print(f"Greatest Decrease in Profits: {g_decrease}")


# In[34]:


# Write updated data to a text file
budget_data_output = "budget_data_output.txt"
with open(budget_data_output, 'w') as output:
    output.write(f"Finanical Analysis\n")
    output.write(f"-----------------------\n")
    output.write(f"Total Months: {n_months}\n")
    output.write(f"Total: $ {total_profit}\n")
    output.write(f"Average Change: $ {average:+.2f}\n")
    output.write(f"Greatest Increase in Profits: {g_increase}\n")
    output.write(f"Greatest Decrease in Profits: {g_decrease}\n")   

