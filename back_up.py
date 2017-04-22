import os # used for finding directories
import datetime
import platform # used for validating operating system
import shutil # used for copying files

# see which OS computer is running
MY_SYSTEM = platform.system()

# Name of backup drive and folder
BACKUPDRIVE = "TWOSIE"
BACKUPFOLDER = "backup"

# Declare Directories to Back Up
BU_DIRS = ['.', '../nfl-api']

def main_script(bu_dirs, dest_dir):

    # get the name of the current python script (this file)
    thisScript = os.path.basename(__file__)

    # create a file object
    log = open(dest_dir + '/log.txt', 'a')


    # create an list of strings to write to log file
    writeLines = []

    # list that holds file name strings
    files = []
    for one_dir in bu_dirs:
        # change directory each iteration
        # otherwise os.path.isfile() checks for files in cwd
        os.chdir(one_dir)
        print "##########CWD: ", os.getcwd()
        for f in os.listdir(one_dir):
            if os.path.isfile(f):
                # copy the files
                shutil.copy2(f, dest_dir)
                # add to list for log
                files.append(f)

    for f in files:
         # do not include this script or log in log.txt
        if f not in ['log.txt', thisScript]:
            writeLines.append( f + '\n')

    # create datetime object
    myDate = datetime.datetime.now()
    # add a timestamp at end of log entry
    writeLines.append('backup performed ' + myDate.strftime('%m/%d/%Y %T') + '\n \n')

    # add lines to log.txt
    log.writelines(writeLines)

    # close log
    log.close()

if MY_SYSTEM == "Darwin":
    print("Using OS X")
    MYUSBPATH = "/Volumes/" + BACKUPDRIVE + "/" + BACKUPFOLDER

    # create folder if doesn't exist
    if not os.path.exists(MYUSBPATH):
        os.makedirs(MYUSBPATH)

    os.path.ismount(MYUSBPATH) # returns true if selected drive is mounted

    main_script(BU_DIRS, MYUSBPATH)

else:
    print "not yet configured for systems other than OS X"
