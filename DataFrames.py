''' Write a program to iterate over a dataframe containing names and marks, then calculates grades as per marks (as per guidlines below)
and them to the grade column.
Marks >=90 grade A+ ;                  Marks 50-60 grade C ;
Marks 70-90 grade A ;                  Marks 40-50 grade D ;
Marks 60-70 grade B ;                  Marks <40 grade F ;'''

import pandas as pd
import numpy as np
names=pd.Series(['Rohan','Misha','Mike','Simran','Aakash','Raj','Shena','Kiran']) #Enter the values 
marks=pd.Series([76.0,56.0,91.0,67.0,90.0,87.0,56.0,98.0])  #Enter the values 
stud={'Name':names,'Marks':marks}

df1 = pd.DataFrame(stud,columns=['Name','Marks'])
df1['Grade']=np.NaN
print("Initial Values in Dataframe")
print("")
print(df1)      
for(col,colSeries) in df1.iteritems():
    length=len(colSeries)            #number of enteries in colSeries

    if col=='Marks':
        lstMarks=[]      #initialize an empty list
        for row in range(length):
            mrks=colSeries[row]
            if mrks>=90:                                       #checking marks and appending grades to the list 
               lstMarks.append('A+')
            elif mrks>=70:
               lstMarks.append('A')
            elif mrks>=60:
               lstMarks.append('B')
            elif mrks>=50:
              lstMarks.append('C')
            elif mrks>=40:
              lstMarks.append('D')
            else:
              lstMarks.append('F')
              
df1['Grade']=lstMarks                                              
print("\n Dataframe after calculating Grades") 
print(df1)           

