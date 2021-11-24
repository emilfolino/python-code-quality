#!/usr/bin/env python3

"""
f6110ca89f074beff5a7b80a71a26856
python
lab6
v4
madx21
2021-10-14 14:23:15
v4.0.0 (2019-03-05)

Generated 2021-10-14 16:23:15 by dbwebb lab-utility v4.0.0 (2019-03-05).
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

with open("quotes.txt", encoding="utf-8") as f:
    text = f.read()






ANSWER = len(text)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 1.
#
# Write your code below and put the answer into the variable ANSWER.
#

lines = text.split("\n")




ANSWER = lines[0]

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


mod_text = []
for line in lines[:-5]:
    mod_text.append(line)
mod_text[5] = "I am replaced"
with open("newQuotes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(mod_text))

with open("newQuotes.txt", "r", encoding="utf-8") as f:
    answer = f.read()

ANSWER = answer

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
with open("newQuotes.txt", "a", encoding="utf-8") as f:
    f.write("\nAll creativity is an extended form of a joke.")

with open("newQuotes.txt", "r", encoding="utf-8") as f:
    answer = f.read()



ANSWER = answer

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
with open("passwords.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

counter = 0
new_text = []
for line in lines:
    if line == "\n":
        counter +=1
        continue
    new_text.append(line)
with open("newPasswords.txt", "w", encoding="utf-8") as f:
    f.write("".join(new_text))
with open("newPasswords.txt", "r", encoding="utf-8") as f:
    new_pass = f.read()
answer = "passwords.txt has {} empty lines and contains: {}".format(counter, new_pass)





ANSWER = answer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (3 points)
#
# Write the content of line numbers 1, 2 and 3 from `quotes.txt` to a new
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
with open("quotes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open ("extraQuotes.txt", "w", encoding="utf-8") as f:
    f.write("".join(lines[:3]))
with open ("extraQuotes.txt", "r", encoding="utf-8") as f:
    extra_q = f.readlines()

counter = 0

for line in extra_q:
    counter += len(line.strip())
second_line = (extra_q[1].strip())[:9]
answer = ("The file has {} characters and the 9 first of the second row "
          "are: {}".format(counter, second_line))








ANSWER = answer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)


dbwebb.exit_with_summary()
