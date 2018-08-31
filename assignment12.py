#Q-1
import datetime 
date=datetime.datetime.now()
print(date.day)
#Q-2
import webbrowser as web
web.open("https://www.google.com")
#Q-3
import os
os.chdir("F:\changedirectory")#Used to change working directory
path =  os.getcwd()#Returns current working directory
filenames = os.listdir(path)#Returns list of files in the current directory
i=1
print(filenames)
for filename in filenames:

    os.rename(filename,str(i)+'.jpg')

    i=i+1
