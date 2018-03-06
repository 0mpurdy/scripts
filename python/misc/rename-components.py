# replace .txt format with .md

import glob, os

for file in glob.glob("*"):
    print(file)

for file in glob.glob("*.txt"):
    fileNew = file
    if (file[0].isupper()):
        fileNew = file[0].lower() + file[1:]
    for i in range(1, len(file)):
        if (file[i].isupper()):
             fileNew = fileNew[:i] + "-" + fileNew[i].lower() + fileNew[i+1:]
    os.rename(file,fileNew[:len(fileNew)-4]  + ".md")
            
    

print("--------------------")

for file in glob.glob("*"):
    print(file)
