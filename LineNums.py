#!/usr/bin/env python

# or #!/bin/python

############################################################################
# Author Name: Seth Cram
# Date: 12/05/2021
# File: Line_Nums.py
# Goal:
#   Write a Python script to allow both the addition and removal of line numbers
#    from a text file.
#
# Project Description:
#   -This script needs to be run with an option to specify line number
#     removal (-r) or addition (-a)
#   -This needs to be specified before the file is passed in 
#   -File I/O is used to replace the changed file
#
# Clarifications:
#   -Indentation is not preserved when removing line numbers
#
# Possible Expansion:
#   -Could pass in more than one file at a time or a directory
#   -Could preserve document formatting after line number removal
#
############################################################################

import sys #need for sys.argv

#remove line numbers:
def Rm_Nums( f ):
    'Remove the line number from the start of each line and return them as a list'

    delim = ' ' #treat whitespace as delimiter
    lineNum = 0 #init lin num cntr var
    fmtLines = [] #store formatted lines in list

    line = f.readline() #read first line in

    while line != '': # empty string means end of file

        #check: print "Starting w/ line:", line

        # process line

        #split string into list args: (default delim = whitespace)
        listLine = line.split()
        #check: print "listLine:", listLine

        #if line is whitespace:
        if ( line == " " ):
            #check: print "Whitespace line:", line
            
            #add line w/o additional formatting:
            fmtLines.append( line )
    
        #if first argument is a number: 
        elif( listLine[0].isdigit() ):  #could also check if equal to lineNum              

            #remove only the first arg:
            newLine = listLine[1:len(listLine)]

            #convert list back into str: (needa add new line char bc removed somehow)
            line = delim.join( newLine ) + '\n'

            #check: print "formatted line:", line

            #add line w/ formatting:
            fmtLines.append( line )

        lineNum = lineNum + 1 #incr line cntr

        #check: print fmtLines

        #read in next line:
        line = f.readline()

    return fmtLines #give list of formatted lines

#add line numbers:
def Add_Nums( f ):
    'Add line numbers to the beginning of each line and return a list of the lines'

    print "Made it in Add_Nums"

    lineNum = 0 #init lin num cntr var
    fmtLines = [] #store formatted lines in list

    line = f.readline() #read first line in

    while line != '': # empty string means end of file
        #process line

        #append line number onto front of line and space:
        fmtLines.append( str( lineNum ) + ' ' + line ) 
        
        #check: print fmtLines 
        
        lineNum = lineNum + 1 #incr line cntr

        #read in next line:
        line = f.readline()

    return fmtLines #give list of formatted lines

#MAIN CODE

#error codes:
TOO_SHORT = 1
OPTION_ERR = 2

""" this is a multi
line comment """

#account for this file's name passed in:
argvLen = len( sys.argv ) - 1 #subtr 1 ( could also use .count() )
argv = sys.argv[ 1:argvLen + 1 ] #slice to cut off

print "Number of args:", argvLen
print "Arg List:", argv

#if too few args:
if( argvLen < 2 ):
    print "Too few arguments passed"
    print "Suggested format: [-r or -a] fileName"

    #exit with fail error code:
    sys.exit( TOO_SHORT ) 
    

#store input file and option:
inputFile = argv[1]
option = argv[0]

f = open( inputFile, 'r' ) #r for read

#Branch based off option passed:
if ( option == "-r" ):
    #check: print "Remove line numbers."

    fmtLines = Rm_Nums( f );

elif ( option == "-a" ):
    #check: print "Add line numbers."

    fmtLines = Add_Nums( f );

else:
    print "Incorrect option" 
    print "Suggested format: [-r or -a] fileName"

    #exit with fail error code:
    sys.exit( OPTION_ERR )

#replace file w/ its formatted I/O:

f.close()

f = open( inputFile, 'w' )

f.writelines( fmtLines )

f.close()

