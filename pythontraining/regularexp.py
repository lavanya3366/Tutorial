#regular ex;pression allow you to locate and change
#strings in very powerful ways
#they work in almost exactly the same way in every
#programming language as well

#Regular expression(Regex) are used to
#1. Search for a specific string in a large amount of data
#2. Verify that a string has the proper format(Email, Phone #)
#3. Find a string and replace it with another string
#4. Format data into the proper form for importing for example

import re
# if re.search("ape","The ape was at the apex"):
#     print("there is an ape")

# allApes=re.findall("ape.","the ape was at the apex")
# for i in allApes:
#     print(i)
    
#finditer returns an iterator of matching objects
#You can use span to get the Location

# theStr="The ape was at the apex"
# for i in re.finditer("ape.",theStr):
#     locTuple=i.span()
#     print(locTuple)
#     print(theStr[locTuple[0]:locTuple[1]])

#-----------Match 1 of several letters----------
#square brackets will match any one of the characters between
#the brackets not including upper and lowercase varieties
#unless they are listed

# animalStr="Cat rat mat fat pat"
# allAnimal=re.findall("[crmfp]at",animalStr)
# for i in allAnimal:
#     print(i)
# print()

#We can also allow for characters in a range
#remember to include upper and lowercase letters
# animalStr="Cat rat mat fat pat"
# someAnimals=re.findall("[c-mC-M]at",animalStr)
# for i in someAnimals:
#     print(i)
# print()
    
#Use ^ to denote any character but whatever characters are
#between the brackets
# animalStr="Cat rat mat fat pat"
# someAnimals=re.findall("[^Cr]at",animalStr)
# for i in someAnimals:
#     print(i)
# print()

# #-----------replace all matches-----------------
# #replace matching items in a string
# owlFood="rat cat mat pat"
# #You can compile a regex into pattern objects which
# #provide additional methods
# regex=re.compile("[cr]at")
# #sub()replaces items that matches the regex in the string
# #with the 1st attribute string passed to sub
# owlFood=regex.sub("owl",owlFood)
# print(owlFood)

#-----------Solving Backslash Problems---------------------
#Regex use the backslash to designate special characters
#and python does the same inside strings which causes
#issues.

#Let's try to get "\\stuff" out of a string 
# randStr="Here is \\stuff"
# #this won't find it
# print("Find \\stuff: ",re.search("\\stuff",randStr))
# #This does,btt we have to put in 4 slashes which is 
# #messy
# print("Find \\stuff:",re.search("\\\\stuff",randStr))
# #you can get around this by using raw strings which
# #don't treat backslash as special
# print("Find \\stuff:",re.search(r"\\stuff",randStr))

#----------Matching Any Character---------------
#We swa that . matches any characters, but what if we
#want to match a period. Backslash the period
#You do the same with [, ] and others

# randStr="F.B.I. I.R.S. CIA"
# print("Matches: ", len(re.findall(".\..\..", randStr)))
# print("Matches: ",re.findall(".\..\..",randStr))

#----------Matching whitespace-------------
#We can match many whitespace characters
# randStr="""This is a long
# string that goes
# on for many lines"""
# print(randStr)
# #remove newlines
# regex=re.compile("\n")
# randStr=regex.sub(" ",randStr)
# print(randStr)
#You can also match
#\b: Backspace
#\f: Form Feed
#\f: Carriage Return 
#\t: Tab
#\v: vertical Tab

#---------Matching Any Single Number------------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]
# randStr="12345"
# print("Matches :", len(re.findall("\d", randStr)))
# print("Matches :", re.findall("\d",randStr))

#---------Matching multiple Numbers----------
#You can match multiple digits by following the \d with{numOfValues}

#Match 5 numbers only
# if re.search("\d{5}","12345"):
#     print("It is a zip code")

# #You can also match within a range
# #Match values that are between 5 and 7 digits
# numStr="123 12345 123456 123567"
# print("Matches :", len(re.findall("\d{5,7}",numStr)))

#---------Matching Any Single Letter or Number----------
#\w is the same as [a-zA-Z0-9_]
#\w is the same as [^a-zA-Z0-9_]
phNum="412-555-1212"
#Check if it is a phone number
if re.search("\w{3}-\w{3}-\w{4}",phNum):
    print("It is a Phone number")
#check for the valid name between 2 and 20 characters
if re.search("\w{2,20}","Ultraman"):
    print("It is a valid name")