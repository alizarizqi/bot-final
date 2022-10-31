
TSSimpleFuture = [
    {
        "pattern": r"tomorrow",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"tonight",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"will",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"soon",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"next",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"later",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"not",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"n't",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"wo",
        "message": "simple future tense",
        "correction": ""
    },

    {
        "pattern": r"shall",
        "message": "simple future tense",
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
    }
]


def simple_future_quest(getPosition, textsOutput42Verb, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outt = getPosition.replace(
            textsOutput42Verb, token._.inflect("VB"))
        break
    outtsplit = outt.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSFuture in TSSimpleFuture:
            if outtsplit[i] == errTSFuture["pattern"]:
                indexPattern.append(outtsplit[i])
    if "tomorrow" in indexPattern or "tonight" in indexPattern or "soon" in indexPattern or "next" in indexPattern or "later" in indexPattern:
        if "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
            if "will" in indexPattern and "not" in indexPattern:
                return outt
            elif "will" in indexPattern:
                return outt
            elif "not" in indexPattern:
                if "much" in indexPattern or "long" in indexPattern:
                    outtsplit.insert(2, "will")
                    outFuture2 = " ".join(outtsplit)
                    return outFuture2
                else:
                    outtsplit.insert(1, "will")
                    outFuture2 = " ".join(outtsplit)
                    return outFuture2
            else:
                if "much" in indexPattern or "long" in indexPattern:
                    outtsplit.insert(2, "will")
                    outFuture2 = " ".join(outtsplit)
                    return outFuture2
                else:
                    outtsplit.insert(1, "will")
                    outFuture2 = " ".join(outtsplit)
                    return outFuture2
        elif "will" in indexPattern and "not" in indexPattern:
            return outt
        elif "will" in indexPattern:
            return outt
        elif "not" in indexPattern:
            outtsplit.insert(0, "will")
            outFuture2 = " ".join(outtsplit)
            return outFuture2
        else:
            outtsplit.insert(0, "will")
            outFuture2 = " ".join(outtsplit)
            return outFuture2
    elif "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
        if "will" in indexPattern and "not" in indexPattern:
            return outt
        elif "will" in indexPattern:
            return outt
    elif "will" in indexPattern and "not" in indexPattern:
        return outt
    elif "will" in indexPattern:
        return outt
