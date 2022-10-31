TSAnotherTenses = [
    {
        "pattern": r"would"
    },
    {
        "pattern": r"was"
    },
    {
        "pattern": r"were"
    },
    {
        "pattern": r"will"
    },
    {
        "pattern": r"have"
    },
    {
        "pattern": r"be"
    },
    {
        "pattern": r"had"
    },
    {
        "pattern": r"been"
    }
]


def anotherTense(textsOutput4):
    indexPattern = []
    for i in range(len(textsOutput4)):
        for errAnother in TSAnotherTenses:
            if textsOutput4[i] == errAnother["pattern"]:
                indexPattern.append(textsOutput4[i])
    if "would" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
    elif "had" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
    elif "was" in indexPattern or "were" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
    elif "will" in indexPattern and "be" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
    elif "would" in indexPattern and "be" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
    elif "will" in indexPattern and "have" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
    elif "would" in indexPattern and "have" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
    elif "been" in indexPattern:
        return "*Sorry, this bot can not detect tense of the sentence*" + "\n" + "For examples, click or type /help"
