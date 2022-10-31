TSPresentPerfect = [{
    "pattern": r"have",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"has",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"already",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"since",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"once",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"twice",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"times",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"yet",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"not",
    "pesan": "present perfect tense",
    "correction": ""
},
    {
    "pattern": r"n't",
    "pesan": "present perfect tense",
    "correction": ""
}
]


def present_perfect_quest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBN = getPosition.replace(
            textsOutput42Verb, token._.inflect("VBN"))
        break

    outtsplit = outtVBN.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSPerfect in TSPresentPerfect:
            if outtsplit[i] == errTSPerfect["pattern"]:
                indexPattern.append(outtsplit[i])

    if "already" in indexPattern or "since" in indexPattern or "once" in indexPattern or "twice" in indexPattern or "times" in indexPattern or "yet" in indexPattern:
        if "have" in indexPattern and "not" in indexPattern:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outHave34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outHave34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outHave34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outHave34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outHave34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outHave34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outHave34
            elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outtVBN
            elif tagOutput4[1] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outtVBN
            else:
                return outHave34
        # --------------------------sudah dicek------------------------------------
        elif "have" in indexPattern:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outHave34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outHave34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outHave34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outHave34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outHave34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outHave34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outHave34
            elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outtVBN
            elif tagOutput4[1] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outtVBN
            else:
                return outHave34
        # --------------------------sudah dicek------------------------------------
        elif "has" in indexPattern and "not" in indexPattern:
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBN
            elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outHas34
            elif tagOutput4[1] == "NNS":
                return outHas34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outHas34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outHas34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outHas34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outHas34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outHas34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outHas34
            else:
                return outtVBN
        # --------------------------sudah dicek------------------------------------
        elif "has" in indexPattern:
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBN
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBN
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBN
            elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outHas34
            elif tagOutput4[1] == "NNS":
                return outHas34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outHas34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outHas34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outHas34
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outHas34
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outHas34
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outHas34
            else:
                return outtVBN
        # --------------------------sudah dicek------------------------------------
        elif "not" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            else:
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
        # --------------------------sudah dicek------------------------------------
        else:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            else:
                outtsplit.insert(0, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
    # --------------------------sudah dicek------------------------------------
    elif "have" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index(
            "have")] = "has"
        outHave34 = outtVBN.replace(
            "have", "".join(indexPattern[indexPattern.index(
                "has")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBN
        elif tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBN
        else:
            return outHave34
    # --------------------------sudah dicek------------------------------------
    elif "have" in indexPattern:
        indexPattern[indexPattern.index(
            "have")] = "has"
        outHave34 = outtVBN.replace(
            "have", "".join(indexPattern[indexPattern.index(
                "has")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBN
        elif tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBN
        else:
            return outHave34
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index(
            "has")] = "have"
        outHas34 = outtVBN.replace(
            "has", "".join(indexPattern[indexPattern.index(
                "have")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outHas34
        elif tagOutput4[1] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outHas34
        else:
            return outtVBN
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern:
        indexPattern[indexPattern.index(
            "has")] = "have"
        outHas34 = outtVBN.replace(
            "has", "".join(indexPattern[indexPattern.index(
                "have")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outHas34
        elif tagOutput4[1] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outHas34
        else:
            return outtVBN
# --------------------------sudah dicek------------------------------------


def VBN(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBN = getPosition.replace(
            textsOutput42Verb, token._.inflect("VBN"))
        break

    outtsplit = outtVBN.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSPerfect in TSPresentPerfect:
            if outtsplit[i] == errTSPerfect["pattern"]:
                indexPattern.append(outtsplit[i])

    if "have" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index(
            "have")] = "has"
        outHave34 = outtVBN.replace(
            "have", "".join(indexPattern[indexPattern.index(
                "has")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBN
        elif tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBN
        else:
            return outHave34
    elif "have" in indexPattern:
        indexPattern[indexPattern.index(
            "have")] = "has"
        outHave34 = outtVBN.replace(
            "have", "".join(indexPattern[indexPattern.index(
                "has")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outHave34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outHave34
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBN
        elif tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBN
        else:
            return outHave34
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index(
            "has")] = "have"
        outHas34 = outtVBN.replace(
            "has", "".join(indexPattern[indexPattern.index(
                "have")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outHas34
        elif tagOutput4[1] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outHas34
        else:
            return outtVBN
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern:
        indexPattern[indexPattern.index(
            "has")] = "have"
        outHas34 = outtVBN.replace(
            "has", "".join(indexPattern[indexPattern.index(
                "have")]))
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBN
        elif textsOutput4[1] == "i" or textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outHas34
        elif tagOutput4[1] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outHas34
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outHas34
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outHas34
        else:
            return outtVBN
    # --------------------------sudah dicek------------------------------------
    elif "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        else:
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
    # --------------------------sudah dicek------------------------------------
    else:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        else:
            outtsplit.insert(0, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
# --------------------------sudah dicek------------------------------------
