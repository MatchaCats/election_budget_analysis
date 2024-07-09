#!/usr/bin/env python
# coding: utf-8

# In[220]:


##Import and Export

import csv
import os

budget_csv = os.path.join(".", "resources", "budget_data.csv")

analysis_output = os.path.join(".", "budget_analysis.txt")


##Reading the csv file
#with open(budget_csv, 'r') as csv_file:
with open(budget_csv) as csv_file:

    #Starting point for the counters
    total_months = 0 
    net_total = 0

    net_change_list = []
    
    csvreader = csv.reader(csv_file)
    
    ##Reading the header
    header = next(csvreader)
    
    row_one = next(csvreader)
    #print(int(row_one[1]))

    ##Establishing where net_total starts
    net_total += int(row_one[1])
    #print(net_total)
    last_net = int(row_one[1])
   
    
    #print(f"header: {header}")
 
    for row in csvreader:
        
        total_months += 1 
        net_total += int(row[1])
        #print(row)
    
        ##Average Change in Profits
       
        net_change = int(row[1]) - last_net
        last_net = int(row[1])
        net_change_list.append(net_change)
    
  
##Greatest Increase in Profits  
greatest_increase = str(max(net_change_list))
#print(greatest_increase)

##Greatest Decrease in Profits

greatest_decrease = str(min(net_change_list))
#print(greatest_decrease)

#print(net_change_list)
net_monthly_average = sum(net_change_list)/ len(net_change_list)


##Final Output
financial_analysis = (f"Financial Analysis\n"
f"---------------------------------------\n"                      
f"Total Number of Months: {total_months}\n"
f"Net Total: ${net_total}\n"
f"Average Change: ${net_monthly_average:.2f}\n"
f"Greatest Increase in Profits ${greatest_increase}\n"
f"Greatest Decrease in Profits ${greatest_decrease}")
print(financial_analysis)

with open(analysis_output, "w") as txt_file:
    txt_file.write(financial_analysis)
                                                                                  


# In[ ]:




