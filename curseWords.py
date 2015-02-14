__author__ = 'MR028042'

import urllib

def read_text():
    quotes = open("C:\detect_profanity\movie_quotes.txt")
    content_of_file = quotes.read()

    quotes.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()

    if "true" in output:
        print("There is profanity in text")
    elif "false" in output:
        print("There is NO profanity in text")
    else:
        print("File cannot be read")

read_text()



