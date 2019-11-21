#https://github.com/manassaini/Week-12-PartA.git

#Manas Saini
#CSCI 102- Section C
#Week 12 Part A

#this works
def PrintOutput(s):
    print ("OUTPUT", s)

#this works
def LoadFile(filename):
    all_words = []
    read_file = open(filename, "r+")
    content = read_file.read()
    all_words = content.split()
    print ("OUTPUT", all_words)
