import os

#folder = r'C:\Users\Seth\Desktop\Courses\UDACITY\Programming Foundations with Python\prank'
folder = r'C:\Users\Seth\Desktop\Courses\UDACITY\Programming Foundations with Python\alphabet'

def renameFile(folder):
    #get all the file names
    fileLis = os.listdir(folder)
    print fileLis
    # for each file; rename
    for fname in fileLis:
        os.rename(os.path.join(folder, fname),
                  os.path.join(folder, fname.translate(None, '0123456789')
                  ))
renameFile(folder)
