TSPresentPerfect = [{
    "pattern": r"have",
    "pesan": "present perfect tense",
    "correction": "",
    "err_id": "RTPP001"
},
    {
    "pattern": r"has",
    "pesan": "present perfect tense",
    "correction": "",
    "err_id": "RTPP002"
},
{
    "pattern": r"not",
    "pesan": "present perfect tense",
    "correction": "",
    "err_id": "RTPP002"
},
{
    "pattern": r"n't",
    "pesan": "present perfect tense",
    "correction": "",
    "err_id": "RTPP002"
},
    {
    "pattern": r"already",
    "pesan": "present perfect tense",
    "correction": "",
    "err_id": "RTPP003"
},
    {
    "pattern": r"since",
    "pesan": "present perfect tense",
    "correction": "",
    "err_id": "RTPP004"
}
]


def present_perfect(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
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

    if "have" in indexPattern and "already" in indexPattern:
        if "not" in indexPattern:
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
    elif "have" in indexPattern and "since" in indexPattern:
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
    elif "have" in indexPattern:
                                if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                                    indexPattern[indexPattern.index(
                                        "have")] = "has"
                                    outHave34 = outtVBN.replace(
                                        "have", "".join(indexPattern))
                                    return outHave34
                                elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                                    indexPattern[indexPattern.index(
                                        "have")] = "has"
                                    outHave34 = outtVBN.replace(
                                        "have", "".join(indexPattern))
                                    return outHave34
                                elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                                    indexPattern[indexPattern.index(
                                        "have")] = "has"
                                    outHave34 = outtVBN.replace(
                                        "have", "".join(indexPattern))
                                    return outHave34
                                elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                                    indexPattern[indexPattern.index(
                                        "have")] = "has"
                                    outHave34 = outtVBN.replace(
                                        "have", "".join(indexPattern))
                                    return outHave34
                                elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                                    indexPattern[indexPattern.index(
                                        "have")] = "has"
                                    outHave34 = outtVBN.replace(
                                        "have", "".join(indexPattern))
                                    return outHave34
                                elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                                    indexPattern[indexPattern.index(
                                        "have")] = "has"
                                    outHave34 = outtVBN.replace(
                                        "have", "".join(indexPattern))
                                    return outHave34
                                elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                                    indexPattern[indexPattern.index(
                                        "have")] = "has"
                                    outHave34 = outtVBN.replace(
                                        "have", "".join(indexPattern))
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
                                        "have", "".join(indexPattern))
                                    return outHave34
    elif "has" in indexPattern and "already" in indexPattern:
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
    elif "has" in indexPattern and "since" in indexPattern:
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
                                        "has", "".join(indexPattern))
                                    return outHas34
                                elif tagOutput4[0] == "NNS":
                                    indexPattern[indexPattern.index(
                                        "has")] = "have"
                                    outHas34 = outtVBN.replace(
                                        "has", "".join(indexPattern))
                                    return outHas34
                                elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                                    indexPattern[indexPattern.index(
                                        "has")] = "have"
                                    outHas34 = outtVBN.replace(
                                        "has", "".join(indexPattern))
                                    return outHas34
                                elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                                    indexPattern[indexPattern.index(
                                        "has")] = "have"
                                    outHas34 = outtVBN.replace(
                                        "has", "".join(indexPattern))
                                    return outHas34
                                elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                                    indexPattern[indexPattern.index(
                                        "has")] = "have"
                                    outHas34 = outtVBN.replace(
                                        "has", "".join(indexPattern))
                                    return outHas34
                                elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                                    indexPattern[indexPattern.index(
                                        "has")] = "have"
                                    outHas34 = outtVBN.replace(
                                        "has", "".join(indexPattern))
                                    return outHas34
                                elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                                    indexPattern[indexPattern.index(
                                        "has")] = "have"
                                    outHas34 = outtVBN.replace(
                                        "has", "".join(indexPattern))
                                    return outHas34
                                elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                                    indexPattern[indexPattern.index(
                                        "has")] = "have"
                                    outHas34 = outtVBN.replace(
                                        "has", "".join(indexPattern))
                                    return outHas34
                                else:
                                    return outtVBN
    elif "already" in indexPattern or "since" in indexPattern:
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


def AUXPerfect(textsOutput4, tagOutput4, getPosition):
    for i in range(len(textsOutput4)):
        if textsOutput4[i] == "have":
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                return getPosition
            elif tagOutput4[0] == "NNS":
                return getPosition
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return getPosition
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return getPosition
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return getPosition
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                return getPosition
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                return getPosition
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                return getPosition
            else:
                textsOutput4[i] = "has"
                outHaveV3 = " ".join(
                    textsOutput4)
                return outHaveV3
        elif textsOutput4[i] == "has":
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                return getPosition
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return getPosition
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return getPosition
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return getPosition
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                return getPosition
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                return getPosition
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                return getPosition
            elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(textsOutput4)
                return outHasV3
            elif tagOutput4[0] == "NNS":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(textsOutput4)
                return outHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(
                    textsOutput4)
                return outHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(
                    textsOutput4)
                return outHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(
                    textsOutput4)
                return outHasV3
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(
                    textsOutput4)
                return outHasV3
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(
                    textsOutput4)
                return outHasV3
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "have"
                outHasV3 = " ".join(
                    textsOutput4)
                return outHasV3
            else:
                return getPosition


def correct_perfect(textsOutput4, tagOutput4, getPosition):
    if AUXPerfect(textsOutput4, tagOutput4, getPosition):
        return AUXPerfect(textsOutput4, tagOutput4, getPosition)                                  
    else:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            textsOutput4.insert(1, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            textsOutput4.insert(2, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            textsOutput4.insert(2, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            textsOutput4.insert(2, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            textsOutput4.insert(3, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            textsOutput4.insert(3, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            textsOutput4.insert(3, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
        elif textsOutput4[0] == "i" or textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            textsOutput4.insert(1, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        elif tagOutput4[0] == "NNS":
            textsOutput4.insert(1, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            textsOutput4.insert(3, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            textsOutput4.insert(3, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            textsOutput4.insert(3, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            textsOutput4.insert(2, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            textsOutput4.insert(2, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            textsOutput4.insert(2, "have")
            outtAddHaveV3 = " ".join(textsOutput4)
            return outtAddHaveV3
        else:
            textsOutput4.insert(1, "has")
            outtAddHasV3 = " ".join(textsOutput4)
            return outtAddHasV3
                                        