#Siries
import pandas as pd

L1 = [1,2,3,4,5]                                            # Single List
L2 = [[1,2,3,4],[5,6,7,8]]                                  # List inside list
dic = {"A":123}                                             #1 Element Dictionary
dic2 = {"C":[1,2,3],"D":[4,5,6]}                            #2 Element in Dictionary


list_1 = pd.Series(L1)                                      # Creating List into Series
list_111 = pd.Series(L1,dtype = 'float')                    # all element for series turn into float from int
list_22 = pd.Series(L2)                                     # Creating List into Series
list_101 = pd.Series(L2 , index = ["A","B"])                # Index values changing using lke this
list_102 = pd.Series(L2 , name = "Welcome")                 # Index values changing using lke this
Any = pd.Series(10 , index=[1,2,3,4,5,6])              # One number make Series and its copied which given index number also
A = pd.Series([1,2,3,4,5])                                  # A for addition perform series
B = pd.Series([1,2,3])                                      # 2nd value for addition Sires


dic_11 = pd.Series(dic)                          # Creating Dictionary into Series single Element
dic_33 = pd.Series(dic2)                         # Creating Dictionary into Series multiple Element


print(type(list_1))                              # Check the type of Function
print(list_1)                                    # All in row 1D but work show like 2D
print(list_111)                                  # Reflect the data after converting the Data type from int to float
print(list_22)                                   # Show data element into one row by list
print(dic_11)                                    # Show Dictionary one element data no comma use
print(dic_33)                                    # Show Dictionary element data comma use list mainly
print(dic_33["C"])                               # Get the Value of C element
print(list_101)                                  # Reflect the index number after changing
print(list_102)                                  # Given name of element
print(Any)                                       # Reflect one number series into given index number
print(A+B)                                       # Addition perform but data showing lower element if all variables and other showing NAN