#!/usr/bin/env python

############################################################################
# Author Name: Seth Cram
# Date: 12/16/2021
# File: ReverseContents.py
# Goal:
#   Write a script to reverse the contents of a text file.
#
# Project Description:
#   -This script needs to be run with a file name
#   -File I/O is used to replace the changed file
#
# Clarifications:
#   -Also have to reverse ordering of words
#   -Assumed reversal meant reverse letters and ordering of each word
#   -Preserves file formatting
#
# Possible Expansion:
#   -Could pass in more than one file at a time or a directory
#
############################################################################

import sys #need for sys.argv

#reverse lines of f:
def revFile( f ):
    'Reverses file contents'

    #read in the whole contents of the file:
    lines = f.read()

    print "Original contents of file:"
    print lines

    #reverse contents of lines:
    lines = lines[::-1]

    return lines

#MAIN CODE

#error codes:
TOO_SHORT = 1
OPTION_ERR = 2

#account for this file's name passed in:
argvLen = len( sys.argv ) - 1 #subtr 1
argv = sys.argv[ 1:argvLen + 1 ] #slice to cut off

print "Number of args:", argvLen
print "Arg List:", argv

#if too few args:
if( argvLen < 1 ):
    print "Too few arguments passed"
    print "Suggested format: fileName"

    #exit with fail error code:
    sys.exit( TOO_SHORT ) 
    

#store input file and option:
inputFile = argv[0]

f = open( inputFile, 'r' ) #r for read

#reverse the lines in f:
fmtLines = revFile( f )

f.close()

#replace file w/ its formatted I/O:

f = open( inputFile, 'w' ) #w for write

print "New reversed contents:"
print fmtLines

#overwrite new reversed lines to file: 
f.write( fmtLines )

f.close()

