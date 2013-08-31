def insertNewlines(text, lineLength):
    """
   Given text and a desired line length, wrap the text as a typewriter would.
   Insert a newline character ("\n") after each word that reaches or exceeds
   the desired line length.
 
   text: a string containing the text to wrap.
   lineLength: the number of characters to include on a line before wrapping
       the next word.
   returns: a string, with newline characters inserted appropriately.
   """
    if len(text) <= lineLength:
        return text
    elif text[lineLength-1] == ' ':
        return text[:lineLength] + "\n" + insertNewlines(text[lineLength:], lineLength)
    else:
        return text[0] + insertNewlines(text[1:], lineLength)
##My answer

##def insertNewlines(text, lineLength):
##    """
##    Given text and a desired line length, wrap the text as a typewriter would.
##    Insert a newline character ("\n") after each word that reaches or exceeds
##    the desired line length.
##
##    text: a string containing the text to wrap.
##    lineLength: the number of characters to include on a line before wrapping
##        the next word.
##    returns: a string, with newline characters inserted appropriately. 
##    """
##    ### TODO
##    if len(text) / float(lineLength) < 1.25:
##        return text
##    else:
##        newLength = insertNewlinesRec(text, lineLength)
##        return text[:newLength] + '\n' + insertNewlines(text[newLength:], lineLength)
##
##def insertNewlinesRec(text, lineLength):
##    if text[lineLength-1] != " ":
##        return insertNewlinesRec(text, lineLength+1)
##    return lineLength
