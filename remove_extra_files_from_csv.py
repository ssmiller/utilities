import os, csv

filelist = r"C:\Users\smillers\Downloads\Remove_excess_NTFs.csv"

with open(filelist, 'r') as csvfile:
    imgreader = csv.DictReader(csvfile)

    for row in imgreader:
      fname = row['filepath']
      try:
          os.remove(fname)
          print("file removed! {}".format(fname))
      except:
          print("could not remove {}".format(fname))
