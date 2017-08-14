import os, sys
from datetime import date

def removefiles(filelist):
    today = date.today()
    logfile = os.path.join(r"LOGS", str(today) +"_removefiles_LOG.txt")
    temp = sys.stdout
    print "Directing output to {} ".format(logfile)
    sys.stdout = open(logfile, 'w')
    with open(filelist, 'r') as f:
        deletelist = f.readlines()
        for row in deletelist:
          fname = row.strip()
          try:
              os.remove(fname)
              print("file removed! {}".format(fname))
          except:
              print("could not remove {}".format(fname))
    sys.stdout.close()                # ordinary file object
    sys.stdout = temp                 # restore print commands to interactive prompt
    print("Output back to normal")           # this shows up in the interactive prompt


if __name__ == "__main__":
    flist = r"gm4extra_ortho_delete.txt"
    removefiles(flist)
