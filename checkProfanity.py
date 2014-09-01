import urllib

def readText(fileLoc):
    quotes = open(fileLoc)
    contents = quotes.read()
    #print contents
    quotes.close()
    check_profanity(contents)
    return contents

def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdyl.com/profanity?q=%s' % text_to_check)
    output = connection.read()
    connection.close()
    #print output
    return output

def check_doc(text):
    output = check_profanity(text)
    if "true" in output:
        print "profanity found\n"
        for word in text.split():
            if "true" in check_profanity(word):
                print word+" is profane\n"
            
    elif "false" in output:
        print "document has no curse words"
    else:
        print "count not scan the document properly"
                  
contents = readText(r'C:\Users\Seth\Desktop\Courses\UDACITY\Programming Foundations with Python\movie_quotes.txt')    
check_doc(contents)
