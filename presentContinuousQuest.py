TSPresentCont = [{
    "pattern": r"is",
    "message": "present continuous tense",
    "correction": ""
},
    {
    "pattern": r"are",
    "message": "present continuous tense",
    "correction": ""
},
    {
    "pattern": r"am",
    "message": "present continuous tense",
    "correction": ""
},
    {
    "pattern": r"now",
    "message": "present continuous tense",
    "correction": ""
},
    {
    "pattern": r"not",
    "message": "present continuous tense",
    "correction": ""
},
    {
    "pattern": r"n't",
    "message": "present continuous tense",
    "correction": ""
},
    {
        "pattern": r"what",
        "message": "present continuous tense",
        "correction": "",
},
    {
        "pattern": r"where",
        "message": "present continuous tense",
        "correction": "",
},
    {
        "pattern": r"when",
        "message": "present continuous tense",
        "correction": "",
},
    {
        "pattern": r"who",
        "message": "present continuous tense",
        "correction": "",
},
    {
        "pattern": r"why",
        "message": "present continuous tense",
        "correction": "",
},
    {
        "pattern": r"how",
        "message": "present continuous tense",
        "correction": "",
},
    {
        "pattern": r"much",
        "message": "present continuous tense",
        "correction": "",
},
    {
        "pattern": r"long",
        "message": "present continuous tense",
        "correction": "",
}
]


def present_continuous_quest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBG = getPosition.replace(
            textsOutput42Verb, token._.inflect("VBG"))
        break

    outtsplit = outtVBG.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSCont in TSPresentCont:
            if outtsplit[i] == errTSCont["pattern"]:
                indexPattern.append(outtsplit[i])

    if "now" in indexPattern:
        if "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
            if "much" in indexPattern or "long" in indexPattern:
                if "is" in indexPattern and "not" in indexPattern:
                    if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outtVBG
                    elif textsOutput4[3] == "i":
                        indexPattern[indexPattern.index("is")] = "am"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outIs4
                    elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    else:
                        return outtVBG
                # -------------------------------------sudah dicek------------------------------------------
                elif "is" in indexPattern:
                    if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outtVBG
                    elif textsOutput4[3] == "i":
                        indexPattern[indexPattern.index("is")] = "am"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outIs4
                    elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    else:
                        return outtVBG
                # -------------------------------------sudah dicek------------------------------------------
                elif "am" in indexPattern and "not" in indexPattern:
                    if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif textsOutput4[3] == "i":
                        return outtVBG
                    elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    else:
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                # -------------------------------------sudah dicek------------------------------------------
                elif "am" in indexPattern:
                    if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif textsOutput4[3] == "i":
                        return outtVBG
                    elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    else:
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                # -------------------------------------sudah dicek------------------------------------------
                elif "are" in indexPattern and "not" in indexPattern:
                    if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif textsOutput4[3] == "i":
                        indexPattern[indexPattern.index("are")] = "am"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outAre4
                    elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        return outtVBG
                    elif tagOutput4[3] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        return outtVBG
                    else:
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                # -------------------------------------sudah dicek------------------------------------------
                elif "are" in indexPattern:
                    if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif textsOutput4[3] == "i":
                        indexPattern[indexPattern.index("are")] = "am"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outAre4
                    elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        return outtVBG
                    elif tagOutput4[3] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        return outtVBG
                    else:
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                # -------------------------------------sudah dicek------------------------------------------
                elif "not" in indexPattern:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif textsOutput4[2] == "i":
                        outtsplit.insert(2, "am")
                        outtAddAm = " ".join(outtsplit)
                        return outtAddAm
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    else:
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                # -------------------------------------sudah dicek------------------------------------------
                else:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif textsOutput4[2] == "i":
                        outtsplit.insert(2, "am")
                        outtAddAm = " ".join(outtsplit)
                        return outtAddAm
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    else:
                        outtsplit.insert(2, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                # -------------------------------------sudah dicek------------------------------------------
            else:
                if "is" in indexPattern and "not" in indexPattern:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif textsOutput4[2] == "i":
                        indexPattern[indexPattern.index("is")] = "am"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outIs4
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    else:
                        return outtVBG
                # -------------------------------------sudah dicek------------------------------------------
                elif "is" in indexPattern:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outtVBG
                    elif textsOutput4[2] == "i":
                        indexPattern[indexPattern.index("is")] = "am"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outIs4
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("is")] = "are"
                        outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outIs4
                    else:
                        return outtVBG
                # -------------------------------------sudah dicek------------------------------------------
                elif "am" in indexPattern and "not" in indexPattern:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif textsOutput4[2] == "i":
                        return outtVBG
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    else:
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                # -------------------------------------sudah dicek------------------------------------------
                elif "am" in indexPattern:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                    elif textsOutput4[2] == "i":
                        return outtVBG
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        indexPattern[indexPattern.index("am")] = "are"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("are")]))
                        return outAm4
                    else:
                        indexPattern[indexPattern.index("am")] = "is"
                        outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAm4
                # -------------------------------------sudah dicek------------------------------------------
                elif "are" in indexPattern and "not" in indexPattern:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif textsOutput4[2] == "i":
                        indexPattern[indexPattern.index("are")] = "am"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outAre4
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        return outtVBG
                    elif tagOutput4[2] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        return outtVBG
                    else:
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                # -------------------------------------sudah dicek------------------------------------------
                elif "are" in indexPattern:
                    if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                    elif textsOutput4[2] == "i":
                        indexPattern[indexPattern.index("are")] = "am"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("am")]))
                        return outAre4
                    elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        return outtVBG
                    elif tagOutput4[2] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        return outtVBG
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        return outtVBG
                    else:
                        indexPattern[indexPattern.index("are")] = "is"
                        outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                            indexPattern[indexPattern.index("is")]))
                        return outAre4
                # -------------------------------------sudah dicek------------------------------------------
                elif "not" in indexPattern:
                    if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif textsOutput4[1] == "i":
                        outtsplit.insert(1, "am")
                        outtAddAm = " ".join(outtsplit)
                        return outtAddAm
                    elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    else:
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                # -------------------------------------sudah dicek------------------------------------------
                else:
                    if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                    elif textsOutput4[1] == "i":
                        outtsplit.insert(1, "am")
                        outtAddAm = " ".join(outtsplit)
                        return outtAddAm
                    elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "are")
                        outtAddAre = " ".join(outtsplit)
                        return outtAddAre
                    else:
                        outtsplit.insert(1, "is")
                        outtAddIs = " ".join(outtsplit)
                        return outtAddIs
                # -------------------------------------sudah dicek------------------------------------------
        elif "is" in indexPattern and "not" in indexPattern:
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBG
            elif textsOutput4[1] == "i":
                indexPattern[indexPattern.index("is")] = "am"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("am")]))
                return outIs4
            elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            else:
                return outtVBG
        # -------------------------------------sudah dicek------------------------------------------
        elif "is" in indexPattern:
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outtVBG
            elif textsOutput4[1] == "i":
                indexPattern[indexPattern.index("is")] = "am"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("am")]))
                return outIs4
            elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("is")] = "are"
                outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outIs4
            else:
                return outtVBG
        # -------------------------------------sudah dicek------------------------------------------
        elif "am" in indexPattern and "not" in indexPattern:
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif textsOutput4[1] == "i":
                return outtVBG
            elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            else:
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
        # -------------------------------------sudah dicek------------------------------------------
        elif "am" in indexPattern:
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
            elif textsOutput4[1] == "i":
                return outtVBG
            elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("am")] = "are"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("are")]))
                return outAm4
            else:
                indexPattern[indexPattern.index("am")] = "is"
                outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAm4
        # -------------------------------------sudah dicek------------------------------------------
        elif "are" in indexPattern and "not" in indexPattern:
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif textsOutput4[1] == "i":
                indexPattern[indexPattern.index("are")] = "am"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("am")]))
                return outAre4
            elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outtVBG
            elif tagOutput4[1] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outtVBG
            else:
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
        # -------------------------------------sudah dicek------------------------------------------
        elif "are" in indexPattern:
            if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
            elif textsOutput4[1] == "i":
                indexPattern[indexPattern.index("are")] = "am"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("am")]))
                return outAre4
            elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outtVBG
            elif tagOutput4[1] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outtVBG
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outtVBG
            else:
                indexPattern[indexPattern.index("are")] = "is"
                outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                    indexPattern[indexPattern.index("is")]))
                return outAre4
        # -------------------------------------sudah dicek------------------------------------------
        elif "not" in indexPattern:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif textsOutput4[0] == "i":
                outtsplit.insert(0, "am")
                outtAddAm = " ".join(outtsplit)
                return outtAddAm
            elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            else:
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
        # -------------------------------------sudah dicek------------------------------------------
        else:
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
            elif textsOutput4[0] == "i":
                outtsplit.insert(0, "am")
                outtAddAm = " ".join(outtsplit)
                return outtAddAm
            elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "are")
                outtAddAre = " ".join(outtsplit)
                return outtAddAre
            else:
                outtsplit.insert(0, "is")
                outtAddIs = " ".join(outtsplit)
                return outtAddIs
        # -------------------------------------sudah dicek------------------------------------------
    elif "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
        if "much" in indexPattern or "long" in indexPattern:
            if "is" in indexPattern and "not" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "is" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern and "not" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[3] == "i":
                    return outtVBG
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[3] == "i":
                    return outtVBG
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern and "not" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outtVBG
                elif tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
            # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outtVBG
                elif tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
            # -------------------------------------sudah dicek------------------------------------------
        else:
            if "is" in indexPattern and "not" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "is" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern and "not" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[2] == "i":
                    return outtVBG
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[2] == "i":
                    return outtVBG
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern and "not" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outtVBG
                elif tagOutput4[2] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outtVBG
                elif tagOutput4[2] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
            # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern and "not" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "am" in indexPattern and "not" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[1] == "i":
            return outtVBG
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
    # -------------------------------------sudah dicek------------------------------------------
    elif "am" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[1] == "i":
            return outtVBG
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern and "not" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBG
        elif tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBG
        elif tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------


def VBG(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBG = getPosition.replace(
            textsOutput42Verb, token._.inflect("VBG"))
        break

    outtsplit = outtVBG.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSCont in TSPresentCont:
            if outtsplit[i] == errTSCont["pattern"]:
                indexPattern.append(outtsplit[i])
    if "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
        if "much" in indexPattern or "long" in indexPattern:
            if "is" in indexPattern and "not" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "is" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outtVBG
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern and "not" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[3] == "i":
                    return outtVBG
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[3] == "i":
                    return outtVBG
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern and "not" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outtVBG
                elif tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
            # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern:
                if textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[3] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[3] == "you" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outtVBG
                elif tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
            # -------------------------------------sudah dicek------------------------------------------
            elif "not" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif textsOutput4[2] == "i":
                    outtsplit.insert(2, "am")
                    outtAddAm = " ".join(outtsplit)
                    return outtAddAm
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                else:
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
            # -------------------------------------sudah dicek------------------------------------------
            else:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif textsOutput4[2] == "i":
                    outtsplit.insert(2, "am")
                    outtAddAm = " ".join(outtsplit)
                    return outtAddAm
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                else:
                    outtsplit.insert(2, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
            # -------------------------------------sudah dicek------------------------------------------
        else:
            if "is" in indexPattern and "not" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "is" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outtVBG
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("is")] = "am"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outIs4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("is")] = "are"
                    outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outIs4
                else:
                    return outtVBG
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern and "not" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[2] == "i":
                    return outtVBG
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "am" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
                elif textsOutput4[2] == "i":
                    return outtVBG
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    indexPattern[indexPattern.index("am")] = "are"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("are")]))
                    return outAm4
                else:
                    indexPattern[indexPattern.index("am")] = "is"
                    outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAm4
            # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern and "not" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outtVBG
                elif tagOutput4[2] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
            # -------------------------------------sudah dicek------------------------------------------
            elif "are" in indexPattern:
                if textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
                elif textsOutput4[2] == "i":
                    indexPattern[indexPattern.index("are")] = "am"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("am")]))
                    return outAre4
                elif textsOutput4[2] == "you" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outtVBG
                elif tagOutput4[2] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outtVBG
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outtVBG
                else:
                    indexPattern[indexPattern.index("are")] = "is"
                    outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                        indexPattern[indexPattern.index("is")]))
                    return outAre4
            # -------------------------------------sudah dicek------------------------------------------
            elif "not" in indexPattern:
                if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif textsOutput4[1] == "i":
                    outtsplit.insert(1, "am")
                    outtAddAm = " ".join(outtsplit)
                    return outtAddAm
                elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                else:
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
            # -------------------------------------sudah dicek------------------------------------------
            else:
                if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
                elif textsOutput4[1] == "i":
                    outtsplit.insert(1, "am")
                    outtAddAm = " ".join(outtsplit)
                    return outtAddAm
                elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "are")
                    outtAddAre = " ".join(outtsplit)
                    return outtAddAre
                else:
                    outtsplit.insert(1, "is")
                    outtAddIs = " ".join(outtsplit)
                    return outtAddIs
            # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern and "not" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outtVBG
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "am" in indexPattern and "not" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[1] == "i":
            return outtVBG
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
    # -------------------------------------sudah dicek------------------------------------------
    elif "am" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[1] == "i":
            return outtVBG
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern and "not" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBG
        elif tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern:
        if textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[1] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[1] == "you" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outtVBG
        elif tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif textsOutput4[0] == "i":
            outtsplit.insert(0, "am")
            outtAddAm = " ".join(outtsplit)
            return outtAddAm
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        else:
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
    # -------------------------------------sudah dicek------------------------------------------
    else:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif textsOutput4[0] == "i":
            outtsplit.insert(0, "am")
            outtAddAm = " ".join(outtsplit)
            return outtAddAm
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        else:
            outtsplit.insert(0, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
    # -------------------------------------sudah dicek------------------------------------------
