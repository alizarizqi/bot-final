TSSimplePast = [
    {
        "pattern": r"last",
        "message": "simple past tense",
        "correction": ""
    },
    {
        "pattern": r"yesterday",
        "message": "simple past tense",
        "correction": ""
    },
    {
        "pattern": r"ago",
        "message": "simple past tense",
        "correction": ""
    },
    {
        "pattern": r"did",
        "message": "simple past tense",
        "correction": ""
    },
    {
        "pattern": r"not",
        "message": "simple past tense",
        "correction": ""
    },
    {
        "pattern": r"n't",
        "message": "simple past tense",
        "correction": ""
    },
    {
        "pattern": r"what",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"where",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"when",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"who",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"why",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"how",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"much",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"long",
        "message": "simple present tense",
        "correction": "",
    }]


def simple_past_quest(getPosition, textsOutput42Verb, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVB = getPosition.replace(
            textsOutput42Verb, token._.inflect("VB"))
        break
    outtsplit = outtVB.split()
    indexPattern = []

    for i in range(len(outtsplit)):
        for errTSPast in TSSimplePast:
            if outtsplit[i] == errTSPast["pattern"]:
                indexPattern.append(outtsplit[i])

    if "yesterday" in indexPattern or "last" in indexPattern or "ago" in indexPattern:
        if "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
            if "did" in indexPattern and "not" in indexPattern:
                return outtVB
            elif "did" in indexPattern:
                return outtVB
            elif "not" in indexPattern:
                if "much" in indexPattern or "long" in indexPattern:
                    outtsplit.insert(2, "did")
                    outNotDid = " ".join(outtsplit)
                    return outNotDid
                else:
                    outtsplit.insert(1, "did")
                    outNotDid = " ".join(outtsplit)
                    return outNotDid
            else:
                if "much" in indexPattern or "long" in indexPattern:
                    outtsplit.insert(2, "did")
                    outNotDid = " ".join(outtsplit)
                    return outNotDid
                else:
                    outtsplit.insert(1, "did")
                    outNotDid = " ".join(outtsplit)
                    return outNotDid
        elif "did" in indexPattern and "not" in indexPattern:
            return outtVB
        elif "did" in indexPattern:
            return outtVB
        elif "not" in indexPattern:
            outtsplit.insert(0, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        else:
            outtsplit.insert(0, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
    elif "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
        if "did" in indexPattern and "not" in indexPattern:
            return outtVB
        elif "did" in indexPattern:
            return outtVB

    elif "did" in indexPattern and "not" in indexPattern:
        return outtVB
    elif "did" in indexPattern:
        return outtVB


def VBD(getPosition, textsOutput42Verb, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVB = getPosition.replace(
            textsOutput42Verb, token._.inflect("VB"))
        break
    outtsplit = outtVB.split()
    indexPattern = []

    for i in range(len(outtsplit)):
        for errTSPast in TSSimplePast:
            if outtsplit[i] == errTSPast["pattern"]:
                indexPattern.append(outtsplit[i])

    if "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
        if "did" in indexPattern and "not" in indexPattern:
            return outtVB
        elif "did" in indexPattern:
            return outtVB
        elif "not" in indexPattern:
            if "much" in indexPattern or "long" in indexPattern:
                outtsplit.insert(2, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            else:
                outtsplit.insert(1, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
        else:
            if "much" in indexPattern or "long" in indexPattern:
                outtsplit.insert(2, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            else:
                outtsplit.insert(1, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
    elif "did" in indexPattern and "not" in indexPattern:
        return outtVB
    elif "did" in indexPattern:
        return outtVB
    elif "not" in indexPattern:
        outtsplit.insert(0, "did")
        outNotDid = " ".join(outtsplit)
        return outNotDid
    else:
        outtsplit.insert(0, "did")
        outNotDid = " ".join(outtsplit)
        return outNotDid
