# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:21:49 2021

@author: CS_Knit_tinK_SC
"""

#%%
# Import the pathlib and csv library
# from pathlib import Path
import csv
from pathlib import Path

# Set the file path
# csvpath = Path('../../Resources/sales.csv')
csvpath = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/menu_data.csv"



# Initialize list of records
records = []
#%%
# Initialize variables
menu = []

#%%
# Open the csv file as an object
with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Print the header
    print(csv_header)
    
        # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)
        menu.append([(row[0]), (row[1]), (row[2]), (row[3]), (row[4])])
        

        
#%%



csvpath = "C:/Users/CS_Knit_tinK_SC/Documents/My Data Sources/sales_data.csv"

sales = []

with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Print the header
    print(csv_header)
    
        # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)
        sales.append([(row[0]), (row[1]), (row[2]), (row[3]), (row[4])])
        
        
#%%

report={}

      
#%%

for transaction in sales:
#    establish dictionary of items, with qty as second element
#     commented out for part of process, back in now
        item_menu = transaction[4]
        item_sold_qty = transaction[3]
        this_item_sold = transaction[4]
        if this_item_sold in report:
            print(item_menu)
        else:
            print(f'add {item_menu}')
            report[this_item_sold]=sales[0][3]
            
        
  
        
#%%  
new_report={}
sub_report1={}
sub_report2={}
sub_report3={}
sub_report4={}
sub_report5={}
sub_report6={}
sub_report7={}
sub_report8={}
sub_report9={}
sub_report10={}
sub_report11={}
count = 1
for yum in report:
        if count == 1:
            sub_report1 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            }}  
            #report.{new_entry}
            print(yum)
            count += 1
        elif count == 2:
            sub_report2 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            }}
            count +=1
        elif count == 3:
            sub_report3 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 4:
            sub_report4 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 5:
            sub_report5 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 6:
            sub_report6 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 7:
            sub_report7 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 8:
            sub_report8 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 9:
            sub_report9 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 10:
            sub_report10 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
        elif count == 11:
            sub_report11 = {
            yum : {
            "01-count" : 0,
            "02-revenue" : 0,
            "03-cogs" : 0, 
            "04-profit" : 0
            } }
            count +=1
new_report = {**sub_report1,**sub_report2,**sub_report3,**sub_report4,**sub_report5,**sub_report6,**sub_report7,**sub_report8,**sub_report9,**sub_report10,**sub_report11}

