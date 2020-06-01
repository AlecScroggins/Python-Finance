# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:06:17 2020

@author: ascroggins
"""


from MyFinancial import MyFinancial

def filemenu():
    x=None
    while x== None:
        print()
        print("File Menu")
        print("0. Quit", "\n","1. Find payment on loan", "\n", "2. Find the future value of an investment", "\n", "3. Find the present value of a future amount", "\n", "4. Graph the closing price of a stock ", "\n", "5. Change Account Settings")
        response = int(input("Enter 0-5: "))
        if (response < 0) or (response >5):
            print("Invalid Response")
        else:
            x=1
            return response
def accountmenu():
    x=None
    print()
    print("Account Menu")
    while x== None:
        print("0. Quit", "\n","1. Change Account Name", "\n", "2. Get Account Name","\n", "3. Return to File Menu")
        response = int(input("Enter 0-3: "))
        if (response <0) or (response >3):
            print("Invalid Response")
        else:
            x=1
            return response

def getFile():
    file = None
    while file == None:
        filename = input("Enter Filename: ")
        try :
            file = open(filename)
        except IOError:
            print("Could not find file. Check if name is correct or try a differfent file")   
    return file


# Main Body
name = input("Enter Name: ")
account = MyFinancial(name)

x=None
while x != 0:
    response = filemenu()
    if (response ==1):
        rate = int(input("Rate per year: "))
        periods = int(input("Number of years: "))
        amount = int(input("Loan amount: "))
        pmt = account.payment(rate, periods, amount)
        print()
        print("Monthly Payment: {pmt:.2f}".format(pmt=pmt))
    else:
        if (response ==2):
            rate = int(input("Rate per year: "))
            years = int(input("Number of years: "))
            amount = int(input("Original Investment amount: "))
            fv = account.futurevalue(rate, years, amount)
            print()
            print("Future Value: {fv:.2f}".format(fv=fv))
        else:
            if (response == 3):
                rate = int(input("Rate per year: "))
                years = int(input("Number of years: "))
                amount = int(input("Future value: "))
                pv = account.presentvalue(rate,years,amount)
                print()
                print("Present Value: {pv:.2f}".format(pv=pv))
            else:
                if (response == 4):
                    file = getFile()
                    graph = account.analysis(file)
                    print("Monthly closing price of stock")
                else:
                    if (response ==5): 
                         x=1
                         while x==1:
                            choice = accountmenu()
                            if (choice == 1):
                               newname = input("Enter New Account Name: ")
                               account.setName(newname)
                               print("\n","New Account Name Is: ", account.getName())
                            else: 
                                if (choice == 2):
                                    print("\n","Account Name is : ", account.getName())
                                else:
                                    if (choice == 3):
                                        x=None
                                    else:
                                        if (choice == 0):
                                            x=0

                    else:
                        if (response == 0 ):
                            x=0
