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
    "pattern": r"nt",
    "pesan": "present perfect tense",
    "correction": ""
}
]


def present_perfect_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBN = getPosition.replace(textsOutput42, token._.inflect("VBN"))
        break

    outtsplit = outtVBN.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSPerfect in TSPresentPerfect:
            if outtsplit[i] == errTSPerfect["pattern"]:
                indexPattern.append(outtsplit[i])

    if "already" in indexPattern or "since" in indexPattern or "once" in indexPattern or "twice" in indexPattern or "times" in indexPattern or "yet" in indexPattern:
        if "have" in indexPattern and "not" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                return outtVBN
            elif tagOutput4[0] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                return outtVBN
            else:
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
        # --------------------------sudah dicek------------------------------------
        elif "have" in indexPattern and "nt" in indexPattern:
            indexPattern[indexPattern.index("nt")] = "not"
            outNott2 = outtVBN.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
                indexPattern[indexPattern.index("not")]))
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                return outNott2
            elif tagOutput4[0] == "NNS":
                return outNott2
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outNott2
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outNott2
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outNott2
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                return outNott2
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                return outNott2
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                return outNott2
            else:
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outNott2.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
        # --------------------------sudah dicek------------------------------------
        elif "has" in indexPattern and "not" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outtVBN
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            else:
                return outtVBN
        # --------------------------sudah dicek------------------------------------
        elif "has" in indexPattern and "nt" in indexPattern:
            indexPattern[indexPattern.index("nt")] = "not"
            outNott2 = outtVBN.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
                indexPattern[indexPattern.index("not")]))
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                return outNott2
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                return outNott2
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                return outNott2
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                return outNott2
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outNott2
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outNott2
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outNott2
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outNott2.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            else:
                return outNott2
        # --------------------------sudah dicek------------------------------------
        elif "have" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                return outtVBN
            elif tagOutput4[0] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                return outtVBN
            else:
                indexPattern[indexPattern.index(
                    "have")] = "has"
                outHave34 = outtVBN.replace(
                    "have", "".join(indexPattern[indexPattern.index(
                        "has")]))
                return outHave34
        # --------------------------sudah dicek------------------------------------
        elif "has" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                return outtVBN
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outtVBN
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outtVBN
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index(
                    "has")] = "have"
                outHas34 = outtVBN.replace(
                    "has", "".join(indexPattern[indexPattern.index(
                        "have")]))
                return outHas34
            else:
                return outtVBN
        # --------------------------sudah dicek------------------------------------
        elif "not" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(1, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(1, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "NNS":
                outtsplit.insert(1, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "have")
                outtAddHaveV3 = " ".join(outtsplit)
                return outtAddHaveV3
            else:
                outtsplit.insert(1, "has")
                outtAddHasV3 = " ".join(outtsplit)
                return outtAddHasV3
        # --------------------------sudah dicek------------------------------------
        else:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(1, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(1, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            elif tagOutput4[0] == "NNS":
                outtsplit.insert(1, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "have")
                outtAddHave = " ".join(outtsplit)
                return outtAddHave
            else:
                outtsplit.insert(1, "has")
                outtAddHas = " ".join(outtsplit)
                return outtAddHas
        # --------------------------sudah dicek------------------------------------
    elif "have" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBN
        elif tagOutput4[0] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBN
        else:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
     # --------------------------sudah dicek------------------------------------
    elif "have" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBN.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outNott2
        elif tagOutput4[0] == "NNS":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outNott2
        else:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        else:
            return outtVBN
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBN.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outNott2
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        else:
            return outNott2
    # --------------------------sudah dicek------------------------------------
    elif "have" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBN
        elif tagOutput4[0] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBN
        else:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
     # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        else:
            return outtVBN
    # --------------------------sudah dicek------------------------------------


def correct_perfect_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBN = getPosition.replace(textsOutput42, token._.inflect("VBN"))
        break

    outtsplit = outtVBN.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSPerfect in TSPresentPerfect:
            if outtsplit[i] == errTSPerfect["pattern"]:
                indexPattern.append(outtsplit[i])
    if "have" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBN
        elif tagOutput4[0] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBN
        else:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
    # --------------------------sudah dicek------------------------------------
    elif "have" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBN.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outNott2
        elif tagOutput4[0] == "NNS":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outNott2
        else:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outNott2.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        else:
            return outtVBN
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBN.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outNott2
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outNott2
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outNott2
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outNott2
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outNott2.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        else:
            return outNott2
    # --------------------------sudah dicek------------------------------------
    elif "have" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBN
        elif tagOutput4[0] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBN
        else:
            indexPattern[indexPattern.index(
                "have")] = "has"
            outHave34 = outtVBN.replace(
                "have", "".join(indexPattern[indexPattern.index(
                    "has")]))
            return outHave34
    # --------------------------sudah dicek------------------------------------
    elif "has" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBN
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBN
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index(
                "has")] = "have"
            outHas34 = outtVBN.replace(
                "has", "".join(indexPattern[indexPattern.index(
                    "have")]))
            return outHas34
        else:
            return outtVBN
    # --------------------------sudah dicek------------------------------------
    elif "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "have")
            outtAddHaveV3 = " ".join(outtsplit)
            return outtAddHaveV3
        else:
            outtsplit.insert(1, "has")
            outtAddHasV3 = " ".join(outtsplit)
            return outtAddHasV3
    # --------------------------sudah dicek------------------------------------
    else:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "have")
            outtAddHave = " ".join(outtsplit)
            return outtAddHave
        else:
            outtsplit.insert(1, "has")
            outtAddHas = " ".join(outtsplit)
            return outtAddHas
# --------------------------sudah dicek------------------------------------
