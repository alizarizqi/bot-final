TSDoubleTenses = [
    {
        "pattern": r"every"
    },
    {
        "pattern": r"frequently"
    },
    {
        "pattern": r"always"
    },
    {
        "pattern": r"sometimes"
    },
    {
        "pattern": r"generally"
    },
    {
        "pattern": r"usually"
    },
    {
        "pattern": r"often"
    },
    {
        "pattern": r"occasionally"
    },
    {
        "pattern": r"seldom"
    },
    {
        "pattern": r"rarely"
    },
    {
        "pattern": r"last"
    },
    {
        "pattern": r"yesterday"
    },
    {
        "pattern": r"ago"
    },
    {
        "pattern": r"tomorrow"
    },
    {
        "pattern": r"tonight"
    },
    {
        "pattern": r"will"
    },
    {
        "pattern": r"soon"
    },
    {
        "pattern": r"next"
    },
    {
        "pattern": r"later"
    },
    {
        "pattern": r"is"
    },
    {
        "pattern": r"are"
    },
    {
        "pattern": r"am"
    },
    {
        "pattern": r"now"
    },
    {
        "pattern": r"have"
    },
    {
        "pattern": r"has"
    },
    {
        "pattern": r"already"
    },
    {
        "pattern": r"since"
    },
    {
        "pattern": r"once"
    },
    {
        "pattern": r"twice"
    },
    {
        "pattern": r"times"
    },
    {
        "pattern": r"yet"
    },

]


def doubleTense(textsOutput4):
    indexPattern = []
    for i in range(len(textsOutput4)):
        for errDouble in TSDoubleTenses:
            if textsOutput4[i] == errDouble["pattern"]:
                indexPattern.append(textsOutput4[i])
    # return indexPattern
    if ("will" in indexPattern) and ("every" in indexPattern or "always" in indexPattern or "sometimes" in indexPattern or "frequently" in indexPattern or "generally" in indexPattern or "usually" in indexPattern or "often" in indexPattern or "occasionally" in indexPattern or "seldom" in indexPattern or "rarely" in indexPattern or "last" in indexPattern or "yesterday" in indexPattern or "ago" in indexPattern or "is" in indexPattern or "are" in indexPattern or "am" in indexPattern or "now" in indexPattern or "have" in indexPattern or "has" in indexPattern or "already" in indexPattern or "since" in indexPattern or "once" in indexPattern or "twice" in indexPattern or "times" in indexPattern or "yet" in indexPattern):
        return "*Sorry, your sentence is ambiguous*" + "\n" + "For examples, click or type /help"
    elif ("is" in indexPattern or "are" in indexPattern or "am" in indexPattern) and ("every" in indexPattern or "always" in indexPattern or "sometimes" in indexPattern or "frequently" in indexPattern or "generally" in indexPattern or "usually" in indexPattern or "often" in indexPattern or "occasionally" in indexPattern or "seldom" in indexPattern or "rarely" in indexPattern or "last" in indexPattern or "yesterday" in indexPattern or "ago" in indexPattern or "tomorrow" in indexPattern or "tonight" in indexPattern or "will" in indexPattern or "soon" in indexPattern or "next" in indexPattern or "later" in indexPattern or "have" in indexPattern or "has" in indexPattern or "already" in indexPattern or "since" in indexPattern or "once" in indexPattern or "twice" in indexPattern or "times" in indexPattern or "yet" in indexPattern):
        return "*Sorry, your sentence is ambiguous*" + "\n" + "For examples, click or type /help"
    elif ("has" in indexPattern or "have" in indexPattern) and ("every" in indexPattern or "always" in indexPattern or "sometimes" in indexPattern or "frequently" in indexPattern or "generally" in indexPattern or "usually" in indexPattern or "often" in indexPattern or "occasionally" in indexPattern or "seldom" in indexPattern or "rarely" in indexPattern or "last" in indexPattern or "yesterday" in indexPattern or "ago" in indexPattern or "tomorrow" in indexPattern or "tonight" in indexPattern or "will" in indexPattern or "soon" in indexPattern or "next" in indexPattern or "later" in indexPattern or "is" in indexPattern or "are" in indexPattern or "am" in indexPattern or "now" in indexPattern):
        return "*Sorry, your sentence is ambiguous*" + "\n" + "For examples, click or type /help"
