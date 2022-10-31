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
        "pattern": r"nt",
        "message": "simple past tense",
        "correction": ""
    }]


def simple_past_negative(getPosition, posOutput4, textsOutput4, textsPast2, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBD = getPosition.replace(
            textsPast2, token._.inflect("VBD"))
        break

    for i in range(len(doc6)):
        token = doc6[i]
        outtVB = getPosition.replace(
            textsPast2, token._.inflect("VB"))
        break
    outtsplit = outtVB.split()
    indexPattern = []

    for i in range(len(outtsplit)):
        for errTSPast in TSSimplePast:
            if outtsplit[i] == errTSPast["pattern"]:
                indexPattern.append(outtsplit[i])

    if "yesterday" in indexPattern or "last" in indexPattern or "ago" in indexPattern:
        if "did" in indexPattern and "not" in indexPattern:
            return outtVB
        elif "did" in indexPattern and "nt" in indexPattern:
            indexPattern[indexPattern.index("nt")] = "not"
            outNott = outtVB.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
                indexPattern[indexPattern.index("not")]))
            return outNott
        elif "not" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it" or textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(1, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            elif posOutput4[0] == "PRON" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            elif posOutput4[0] == "DET" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            elif posOutput4[0] == "NUM" and posOutput4[1] == "NOUN":
                outtsplit.insert(2, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            elif posOutput4[0] == "PRON" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            elif posOutput4[0] == "DET" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            elif posOutput4[0] == "NUM" and posOutput4[1] == "ADJ":
                outtsplit.insert(3, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            elif posOutput4[0] == "PROPN" and posOutput4[1] == "PROPN":
                outtsplit.insert(2, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
            else:
                outtsplit.insert(1, "did")
                outNotDid = " ".join(outtsplit)
                return outNotDid
        else:
            return outtVBD
    elif "did" in indexPattern and "not" in indexPattern:
        return outtVB
    elif "did" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott = outtVB.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        return outNott


def VBD(getPosition, posOutput4, textsOutput4, textsPast2, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBD = getPosition.replace(
            textsPast2, token._.inflect("VBD"))
        break

    for i in range(len(doc6)):
        token = doc6[i]
        outtVB = getPosition.replace(
            textsPast2, token._.inflect("VB"))
        break
    outtsplit = outtVB.split()
    indexPattern = []

    for i in range(len(outtsplit)):
        for errTSPast in TSSimplePast:
            if outtsplit[i] == errTSPast["pattern"]:
                indexPattern.append(outtsplit[i])

    if "did" in indexPattern and "not" in indexPattern:
        return outtVB
    elif "did" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott = outtVB.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        return outNott
    elif "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it" or textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        elif posOutput4[0] == "PRON" and posOutput4[1] == "NOUN":
            outtsplit.insert(2, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        elif posOutput4[0] == "DET" and posOutput4[1] == "NOUN":
            outtsplit.insert(2, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        elif posOutput4[0] == "NUM" and posOutput4[1] == "NOUN":
            outtsplit.insert(2, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        elif posOutput4[0] == "PRON" and posOutput4[1] == "ADJ":
            outtsplit.insert(3, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        elif posOutput4[0] == "DET" and posOutput4[1] == "ADJ":
            outtsplit.insert(3, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        elif posOutput4[0] == "NUM" and posOutput4[1] == "ADJ":
            outtsplit.insert(3, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        elif posOutput4[0] == "PROPN" and posOutput4[1] == "PROPN":
            outtsplit.insert(2, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
        else:
            outtsplit.insert(1, "did")
            outNotDid = " ".join(outtsplit)
            return outNotDid
    else:
        return outtVBD
