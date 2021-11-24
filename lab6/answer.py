#!/usr/bin/env python3

"""
4241baea025bc106288ab8fb2b17077a
python
lab6
v4
kaab21
2021-10-13 11:57:37
v4.0.0 (2019-03-05)

Generated 2021-10-13 13:57:37 by dbwebb lab-utility v4.0.0 (2019-03-05).
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

quotesFile = open("quotes.txt", "r")
quotes = quotesFile.read()
quotesFile.close()
length = len(quotes)

ANSWER = length

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 2.
#
# Write your code below and put the answer into the variable ANSWER.
#

line2 = quotes.split("\n")[1]



ANSWER = line2

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

quotesFile = open("quotes.txt", "r")
lines = quotesFile.read().split("\n")
quotesFile.close()
lines = lines[:-5]
lines[5] = "I am replaced"
newQuotes = "\n".join(lines)
newFile = open("newQuotes.txt", "w")
newFile.write(newQuotes)
newFile.close()

ANSWER = newQuotes

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Append the following sentence on a new line at the end of newQuotes.txt and
# answer with the content.
#
# *"All creativity is an extended form of a joke."*
#
# Write your code below and put the answer into the variable ANSWER.
#

newFile = open("newQuotes.txt", "a")
newFile.write("\nAll creativity is an extended form of a joke.")
newFile.close()
newFile = open("newQuotes.txt", "r")
newQuotes = newFile.read()
newFile.close()

ANSWER = newQuotes

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

passwordsFile = open("passwords.txt", "r")
passwords = passwordsFile.read().split("\n")
passwordsFile.close()
emptyLines = passwords.count("")
while "" in passwords:
    passwords.remove("")
newPasswords = "\n".join(passwords)
newFile = open("newPasswords.txt", "w")
newFile.write(newPasswords)
newFile.close()

ANSWER = f"passwords.txt has {emptyLines} empty lines and contains: {newPasswords}"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (3 points)
#
# Write the content of line numbers 2, 3 and 4 from `quotes.txt` to a new
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

quotesFile = open("quotes.txt", "r")
extraQuotes = quotesFile.read().split("\n")[1:4]
quotesFile.close()
extraFile = open("extraQuotes.txt", "w")
extraFile.write("\n".join(extraQuotes))
extraFile.close()
number = 0
for line in extraQuotes:
    number += len(line)
first9 = extraQuotes[1][:9]

ANSWER = f"The file has {number} characters and the 9 first of the second row are: {first9}"

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)


dbwebb.exit_with_summary()
