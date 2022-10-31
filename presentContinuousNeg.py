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
    "pattern": r"nt",
    "message": "present continuous tense",
    "correction": ""
}
]


def present_continuous_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBG = getPosition.replace(textsOutput42, token._.inflect("VBG"))
        break

    outtsplit = outtVBG.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSCont in TSPresentCont:
            if outtsplit[i] == errTSCont["pattern"]:
                indexPattern.append(outtsplit[i])
    if "is" in indexPattern and "not" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern and "nt" in indexPattern and "now" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
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
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outNott2
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
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
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outNott2
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------

    elif "is" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "am" in indexPattern and "not" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
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
    elif "am" in indexPattern and "nt" in indexPattern and "now" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outNott2
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
    elif "am" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
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
    elif "am" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outNott2
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
    elif "am" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
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
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
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
    elif "are" in indexPattern and "not" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBG
        elif tagOutput4[0] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern and "nt" in indexPattern and "now" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
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
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBG
        elif tagOutput4[0] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
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
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBG
        elif tagOutput4[0] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBG
        elif tagOutput4[0] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "not" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif textsOutput4[0] == "i":
            outtsplit.insert(1, "am")
            outtAddAm = " ".join(outtsplit)
            return outtAddAm
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        else:
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
    # -------------------------------------sudah dicek------------------------------------------
    elif "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif textsOutput4[0] == "i":
            outtsplit.insert(1, "am")
            outtAddAm = " ".join(outtsplit)
            return outtAddAm
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        else:
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
    # -------------------------------------sudah dicek------------------------------------------


def VBG(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outtVBG = getPosition.replace(textsOutput42, token._.inflect("VBG"))
        break

    outtsplit = outtVBG.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errTSCont in TSPresentCont:
            if outtsplit[i] == errTSCont["pattern"]:
                indexPattern.append(outtsplit[i])
    if "is" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
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
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outNott2.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outNott2
    # -------------------------------------sudah dicek------------------------------------------
    elif "is" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outtVBG
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("is")] = "am"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outIs4
        else:
            return outtVBG
    # -------------------------------------sudah dicek------------------------------------------
    elif "am" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
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
    elif "am" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outNott2
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outNott2.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
    elif "am" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(
                indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
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
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBG
        elif tagOutput4[0] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outtVBG.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
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
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outNott2.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "are" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("am")]))
            return outAre4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outtVBG
        elif tagOutput4[0] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outtVBG
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outtVBG
        else:
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(
                indexPattern[indexPattern.index("is")]))
            return outAre4
    # -------------------------------------sudah dicek------------------------------------------
    elif "not" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif textsOutput4[0] == "i":
            outtsplit.insert(1, "am")
            outtAddAm = " ".join(outtsplit)
            return outtAddAm
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        else:
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
    # -------------------------------------sudah dicek------------------------------------------
    else:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
        elif textsOutput4[0] == "i":
            outtsplit.insert(1, "am")
            outtAddAm = " ".join(outtsplit)
            return outtAddAm
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "are")
            outtAddAre = " ".join(outtsplit)
            return outtAddAre
        else:
            outtsplit.insert(1, "is")
            outtAddIs = " ".join(outtsplit)
            return outtAddIs
# -------------------------------------sudah dicek------------------------------------------
