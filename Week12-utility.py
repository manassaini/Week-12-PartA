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

#this works
def UpdateString(s1, l1, index):
    output = ""
    output = s1.replace(s1[index], l1)
    print (output)

#THIS DOES NOT WORK
def FindWordCount(list_, string):
    word_counter = 0
    for i in range(0, len(list_)):
        list_[i] = list_[i].split()
    for x in list_:
        for y in x:
            if y == string:
                word_counter += 1
    print (word_counter)

def Union():
