import time
import csv

open('data.csv','w+') #Creating a csv file

#CREATING A KEY AND VALUE PAIR
def create(key,value,timeout=0):
    data=[]
    #reading a data from csv file
    with open('data.csv','r') as file:
        readData = csv.reader(file,delimiter=',',skipinitialspace=True)
        for row in readData:
            data.append(row[0])
        if key in data:
            print("This key is already is existing so please try another")
        else:
            if(key.isalpha()): #checking whether key is in alphabets
                if len(data)<(1024*1020*1024) and value<=(16*1024*1024):  #checking sizes.... 
                    if timeout!=0:
                        timeout=time.time()+timeout
                    if len(str(key))<=32:
                        #Append new data into a CSV file 
                        with open('data.csv','a',newline='') as file:
                            writeIntoFile = csv.writer(file)
                            writeIntoFile.writerow([key, value, timeout])
                        print("Created Successfully")
                    else:
                        print("Your key must be in 32 char")                                                                                    
            else:
                print("Please enter a valid key....key must be in alphabets")
                
         

#READING A KEY AND VALUE PAIR         
def read(key):
    data=[]
    #reading a data from csv file
    with open('data.csv','r') as file:
        readData = csv.reader(file,delimiter=',',skipinitialspace=True)
        for row in readData:
            data.append(row[0])
            if row[0]==key:
                value = row[1]
                timeout= row[2]
        if key not in data:
            print("Your Key is not exist in DataStore")
        else:
            if float(timeout)!=0:
                if time.time() < float(timeout):
                    yourData = key + ":" + str(value)
                    print(yourData)
                else:
                    print("your key has Expired")
            else:
                yourData = key + ":" + str(value)
                print(yourData)


#DELETING A KEY AND VALUE PAIR 
def delete(key):
    data=[]
    finalData=[]
    #reading a data from csv file
    with open('data.csv','r') as file:        
        readData = csv.reader(file,delimiter=',',skipinitialspace=True)
        for row in readData:            
            data.append(row[0])
            if row[0]==key:
                value = row[1]
                timeout= row[2]
            else:
                finalData.append(row)
        if key not in data:
            print("Your key does not exist in datastore")
        else:
            if float(timeout)!=0:
                if time.time() > float(timeout):
                    print("your key has expired")
                else:
                    return 0
            with open('data.csv','w',newline='') as file:
                write = csv.writer(file)
                for add in finalData:
                    write.writerow([add[0],add[1],add[2]])
                print("Your Key has been deleted")
                    



                    
        
    

 

 
 

 




 

        
 
   


 

