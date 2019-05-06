#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.git()
pasteText = ""
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexes in the "lines" list
    # add star to each string in "lines" list
    pasteText += '* ' + lines[i]+' ++\n'
pyperclip.copy(pasteText)
