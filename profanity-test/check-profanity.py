import urllib


def read_text():
    quotes = open("quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity_text(contents_of_file)



def check_profanity_text(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()



read_text()