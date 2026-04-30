import os.path
import sys
from unicodedata import name

fname = input("Enter the filename to sort: ")#input file
if not os.path.isfile(fname):
 print("File", fname, "doesn't exists") 
sys.exit(0)
infile = open(fname, "r")#read mode
lines = infile.readlines()#list of lines from file
infile.close() # Close the input file
lineList = []#Empty List
for line in lines:
 lineList.append(line.strip()) # remove '\n'
lineList.sort() #Sort the list
putfile = open("sorted.txt", "w+") #write and read mode
if not os.path.isfile("sorted.txt"):
 print("Not able to create sorted.txt")
sys.exit(0)
for line in lineList:
  putfile.write(line + "\n") 
putfile.seek(0,0) # Move the file pointer to the beginning of the file
fstr= putfile.read() # Read the contents of the file
print("Sorted.txt content"),len(lineList), "lines"
putfile.close()