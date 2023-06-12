#!/usr/bin/env python

############################################################################
# Author Name: Seth Cram
# Date: 12/06/2021
# File: ChangeSuffix.py
# Goal:
#   Write a Python script to change file suffixes
#
# Project Description:
#   -This script needs to be run with a file name and then desired extension
#   -File I/O is used to replace the changed file
#
# Clarifications:
#   -Can pass either local file name or full path as the file name
#
# Possible Expansion:
#   -Could pass in more than one file at a time or a directory
#
############################################################################

import sys #need for sys.argv

import os #needed for os.rename() and os.path.exists()

#MAIN CODE

#error codes:
TOO_SHORT = 1

#account for this file's name passed in:
argvLen = len( sys.argv ) - 1 #subtr 1
argv = sys.argv[ 1:argvLen + 1 ] #slice to cut off

#checks:
# print "Number of args:", argvLen
# print "Arg List:", argv

#change std error from console to dump directory:
#sys.stderr = open("/dev/null", "w") #also redirs output from assertions

#if too few args:
if( argvLen < 2 ):
    print "Too few arguments passed"
    print "Suggested format: fileName.extension desiredExtension"

    #exit with fail error code:
    sys.exit( TOO_SHORT ) 
    

#store input file and option:
fileName = argv[0]
desiredExt = argv[1]
period = '.'

#verify file exists in file syst:
assert os.path.exists( fileName ), fileName + " doesn't exist"

#verify file passed in has an extension:
assert period in fileName, 'No file extension found.\nSuggested format: fileName.extension desiredExtension'

#find period's index:
periodIndex = fileName.find( period )

#separate file's extension into its own var:
currExt = fileName[ periodIndex+1:len(fileName) ] # +1 to keep period

#replace curr ext w/ desired:
newName = fileName.replace( currExt, desiredExt )

#check: print newName

#rename actual file:
os.rename( fileName, newName )

#verification feedback:
print fileName + " renamed to " + newName


