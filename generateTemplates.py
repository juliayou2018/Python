def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    # Your Code Here
    res = []
    spliymadLibsForm = madLibsForm.split()
    for e in spliymadLibsForm:
        if e == '[ADJ]' or e == '[VERB]' or e == '[NOUN]':
            res.append(e)
    return res

print generateTemplates('The [ADJ] [NOUN] started [VERB] [NOUN]')
