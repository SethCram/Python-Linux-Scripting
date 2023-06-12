#!/usr/bin/env python

############################################################################
# Author Name: Seth Cram
# Date: 12/06/2021
# File: Backup.py
#
# Goal:
#  Write a script to backup files and directories into a special
#   subdirectory (.backup). Your backup script should handle the case of
#   an existing file or directory of the same name in the subdirectory
#   .backup.
#
# Project Description:
#  Creates a .backup dir in user's home directory if doesn't already exist.
#   Copies the passed in file or directory to the backup directory. If
#   naming conflicts, prompts user about whether to overwrite the backed-up
#   file/dir or not back up the file/dir at all.
#
# Clarifications:
#  -If user decides not to overwrite existing file/dir, passed in file/dir
#    is not backed up.
#  -Current version of python is python 2 so uses raw_input(), use input() if python 3
#  -Only works on directories within current directory script called from
#  -works on files external to current directory
#
# Possible Expansion:
#  Could take in multiple files and/or directories at one time from cmd line
#
############################################################################

import sys #need for sys.argv

import os #needed for os.rename() and os.path.exists()

import shutil #needed for shutil.copy()

#copy fileName into backupDir:
def cp( fileName, backupDir ):
      #new directory if copying dir:
      newDir =  backupDir + "/" + fileName

      try:
            #copy file into backup dir:
            shutil.copy( fileName, backupDir )

      except IOError: #fileName is a dir
            try:
                  #copy dir into backup dir:
                  shutil.copytree( fileName, newDir ) 
                  #copy tree not working for dirs not in curr dir
            
            except OSError: #dir already backed up
                  #delete existing backed up dir:
                  shutil.rmtree( newDir )

                  #copy dir into backup dir:
                  shutil.copytree( fileName, newDir )

#MAIN CODE

#error codes:
TOO_SHORT = 1
NO_OVERWRITE = 2

#account for this file's name passed in:
argvLen = len( sys.argv ) - 1 #subtr 1
argv = sys.argv[ 1:argvLen + 1 ] #slice to cut off

#if too few args:
if( argvLen < 1 ):
    print "Too few arguments passed"
    print "Suggested format: fileName.extension desiredExtension"

    #exit with fail error code:
    sys.exit( TOO_SHORT )

fileName = argv[0]

#verify file exists in file syst: (only works for local dirs)
assert os.path.exists( fileName ), fileName + " doesn't exist"

#stores user's home dir:
home = os.path.expanduser("~")
backupDir = home + "/.backup"

#check:
print home
print backupDir

#check backup dir exist:
if ( os.path.exists ( backupDir ) ):
    print "Backup dir already exists"

else: #if doesnt exist
    os.mkdir( backupDir ) #if fails, raises 'FileExistsError'

#find index of last forward slash in fileName:
fsIndex = fileName.rfind( '/' )

#if user passed in path name of file/dir:
if ( fsIndex != -1 ):
      #cutoff path:
      newFileName = fileName[ fsIndex+1:len(fileName) ]
      
      #check:
      print newFileName

else:
      newFileName = fileName

#if file to back up already backed up:
if( os.path.exists ( backupDir + '/' + newFileName ) ):
    #get user decision:
    decision = raw_input("Overwrite old backed up version of " + newFileName + "? (yes/no)\n")

    #take action based on user input:
    if ( decision == "yes" ):

        #copy file/dir into backupDir:
        cp( newFileName, backupDir )

    else:
        #exit with fail error code:
        sys.exit( NO_OVERWRITE )

else:
    #copy file/dir into backupDir:
    cp( newFileName, backupDir )

#comfirmation feedback:
print newFileName + " backed up into " + backupDir


