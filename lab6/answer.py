#!/usr/bin/env python3

"""
78a37674619e6eeda9011b65b62b8f35
python
lab6
v4
mafh21
2021-10-09 13:19:56
v4.0.0 (2019-03-05)

Generated 2021-10-09 15:19:56 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 6 - python
#
# During these exercises we train on reading, writing and appending data to
# text file's.
#



# --------------------------------------------------------------------------
# Section 1. Files
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Read the `quotes.txt` -file in UTF-8 encoding and store the content into a
# variable. Answer with the number of characters in the file.
#
# Write your code below and put the answer into the variable ANSWER.
#
with  open("quotes.txt",encoding="UTF-8") as file:
    data = file.read()




ANSWER = len(data)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 4.
#
# Write your code below and put the answer into the variable ANSWER.
#
line = data.split('\n')

ANSWER = line[3]

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# First, read the content inside of quotes.txt and remove the 5 last rows.
# Then replace line number 6 with the new string "I am replaced".
# Then, create a new file called `newQuotes.txt` where you save the new
# changes. Replace `newQuotes.txt` if it already exists.
#
# Answer with the new content inside `newQuotes.txt`. Don't have a "\n" on
# the last line.
#
# Write your code below and put the answer into the variable ANSWER.
#
ln = len(line) - 5
afterDel = line[0: ln]
afterDel[5] = "I am replaced"
with open('newQuotes.txt',"w",encoding="UTF-8") as newFile:
    newFile.write("\n".join(afterDel))
    newFile.close()
with open('newQuotes.txt',encoding="UTF-8") as readFile:
    dataTwo = readFile.read()






ANSWER = dataTwo

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Append the following sentence on a new line at the end of newQuotes.txt and
# answer with the content.
#
# *"The important thing is not to stop questioning."*
#
# Write your code below and put the answer into the variable ANSWER.
#
with open('newQuotes.txt',"a") as fileWrite:
    fileWrite.write("\nThe important thing is not to stop questioning.")
    fileWrite.close()
with open('newQuotes.txt',encoding="UTF-8") as fileRead:





    ANSWER = fileRead.read()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Store the number of empty lines that `passwords.txt` has and create a new
# file called `newPasswords.txt` containing the lines that are not empty.
#
# Answer with the following:
#
# *passwords.txt has X empty lines and contains: Y*
#
# Replace `X` with the number of empty lines and `Y` with the new files
# content.
#
# Write your code below and put the answer into the variable ANSWER.
#
with open("passwords.txt",encoding="UTF-8") as file:
    dataNum = file.readlines()
    numberEmpty = 0
    NewList = []
    for line in dataNum:
        if line == "\n":
            numberEmpty += 1
        else:
            NewList.append(line)
with open('newPasswords.txt',"w",encoding="UTF-8") as newPassFile:
    newPassFile.write("".join(NewList))
    newPassFile.close()
with open('newPasswords.txt',encoding="UTF-8") as fileReadPass:
    



    ANSWER = f'passwords.txt has {numberEmpty} empty lines and contains: {fileReadPass.read()}'

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (3 points)
#
# Write the content of line numbers 4, 5 and 6 from `quotes.txt` to a new
# file that you create called `extraQuotes.txt`. Replace `extraQuotes.txt` if
# it already exists.
# Save the total number of characters and the 9 first characters of the
# second line into variables.
#
# Answer with the following string:
# "The file has X characters and the 9 first of the second row are: Y"
#
# **Example**:
# *"The file has 220 characters and the 9 first of the second row are: - Jon
# Doe"*
#
# Do not include newlines when you count the number of characters.
#
# Write your code below and put the answer into the variable ANSWER.
#
newQ = data.split("\n")
with open("extraQuotes.txt","w") as New_file:
    New_file.write("\n".join(newQ[3:6]))
    New_file.close()
with open("extraQuotes.txt",encoding="UTF-8") as NewRead_file:
    NumData = len(NewRead_file.read()) - 2
with open("extraQuotes.txt",encoding="UTF-8") as NewReadfile:
    newSplit = NewReadfile.readlines()
    secLine = newSplit[1]




ANSWER = f"The file has {NumData} characters and the 9 first of the second row are: {str(secLine[0:9])}"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)


dbwebb.exit_with_summary()
