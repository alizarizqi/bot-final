from operator import index


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
        "pattern": r"nt",
        "message": "simple future tense",
        "correction": ""
    },
    {
        "pattern": r"wo",
        "message": "simple future tense",
        "correction": ""
    }
]


def simple_future(getPosition, posOutput4, textsFuture2, textsFuture, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outt = getPosition.replace(
            textsFuture2, token._.inflect("VB"))
        break
    outtsplit = outt.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSFuture in TSSimpleFuture:
            if outtsplit[i] == errTSFuture["pattern"]:
                indexPattern.append(outtsplit[i])
    if "tomorrow" in indexPattern or "tonight" in indexPattern or "soon" in indexPattern or "next" in indexPattern or "later" in indexPattern:
        if "will" in indexPattern and "not" in indexPattern:
            return outt
        elif "will" in indexPattern:
            return outt
        elif "not" in indexPattern:
            if textsFuture[0] == "she" or textsFuture[0] == "he" or textsFuture[0] == "it" or textsFuture[0] == "i" or textsFuture[0] == "you" or textsFuture[0] == "they" or textsFuture[0] == "we":
                outtsplit.insert(1, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "PRON" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "DET" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "NUM" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "PRON" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "DET" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "NUM" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            else:
                outtsplit.insert(1, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
        else:
            if textsFuture[0] == "she" or textsFuture[0] == "he" or textsFuture[0] == "it" or textsFuture[0] == "i" or textsFuture[0] == "you" or textsFuture[0] == "they" or textsFuture[0] == "we":
                outtsplit.insert(1, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "PRON" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "DET" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "NUM" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "PRON" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "DET" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "will")
                outFuture2 = " ".join(outtsplit)
                return outFuture2
            elif posOutput4[0] == "NUM" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "will")
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
