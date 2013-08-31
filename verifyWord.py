def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    # Your Code Here

    if madTemplate == '[ADJ]':
        if userWord in listOfAdjs:
            return True
        return False

    elif madTemplate == '[VERB]':
        if userWord in listOfVerbs:
            return True
        return False

    elif madTemplate == '[NOUN]':
        if userWord in listOfNouns:
            return True
        return False
