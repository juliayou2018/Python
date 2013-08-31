def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    adj = '[ADJ]'
    verb = '[VERB]'
    noun = '[NOUN]'
    words = story.split()
    res = ''
    for word in words:
        if word in listOfAdjs:
            res += adj
        elif word in listOfNouns:
            res += noun
        elif word in listOfVerbs:
            res += verb
        else:
            res += word
        res += ' '
    return res
            

story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
print '\n'
story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
