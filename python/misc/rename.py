# Renames all files with prefix "Untitled"
# using student number
# eg: Untitled1.txt -> 5555-100-1-raw.pnm

import os

beginning = "Untitled"
studentNumber = '5555'
secondaryPrefix = '100'

for filename in os.listdir("."):
    if (filename.startswith(beginning)):
        os.rename(filename, "%s-%s-" % (studentNumber, secondaryPrefix) + filename[len(beginning):-4] + '-raw.pnm')
