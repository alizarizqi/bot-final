TSPresentCont = [{
    "pattern": r"is",
    "message": "present continuous tense",
    "correction": "",
    "err_id": "RTPC001"
},
    {
    "pattern": r"are",
    "message": "present continuous tense",
    "correction": "",
    "err_id": "RTPC002"
},
    {
    "pattern": r"am",
    "message": "present continuous tense",
    "correction": "",
    "err_id": "RTPC003"
},
    {
    "pattern": r"now",
    "message": "present continuous tense",
    "correction": "",
    "err_id": "RTPC004"
}
]

def present_continuous(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
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

    if "are" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("am")]))
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
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
    elif "are" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("are")] = "is"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAre4
        elif textsOutput4[0] == "i":
            indexPattern[indexPattern.index("are")] = "am"
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("am")]))
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
            outAre4 = outtVBG.replace("".join(outtsplit[outtsplit.index("are")]), "".join(indexPattern[indexPattern.index("is")]))
    elif "am" in indexPattern and "now" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
    elif "am" in indexPattern:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
        elif textsOutput4[0] == "i":
            return outtVBG
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("am")] = "are"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("are")]))
            return outAm4 
        else:
            indexPattern[indexPattern.index("am")] = "is"
            outAm4 = outtVBG.replace("".join(outtsplit[outtsplit.index("am")]), "".join(indexPattern[indexPattern.index("is")]))
            return outAm4
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
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4 
        else:
            return outtVBG
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
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("am")]))
            return outIs4
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("is")] = "are"
            outIs4 = outtVBG.replace("".join(outtsplit[outtsplit.index("is")]), "".join(indexPattern[indexPattern.index("are")]))
            return outIs4 
        else:
            return outtVBG
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

def AUXCont(textsOutput4, tagOutput4, getPosition):
    for i in range(len(textsOutput4)):
        if textsOutput4[i] == "is":
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                return getPosition
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                return getPosition
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                return getPosition
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                return getPosition
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return getPosition
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return getPosition
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return getPosition
            elif textsOutput4[0] == "i":
                textsOutput4[i] = "am"
                outIs = " ".join(textsOutput4)
                return outIs
            elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            elif tagOutput4[0] == "NNS":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "are"
                outIs = " ".join(textsOutput4)
                return outIs
            else:
                return getPosition
        elif textsOutput4[i] == "are":
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
            elif textsOutput4[0] == "i":
                textsOutput4[i] = "am"
                outIs = " ".join(textsOutput4)
                return outIs
            elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
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
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
        elif textsOutput4[i] == "am":
            if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                textsOutput4[i] = "is"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                textsOutput4[i] = "is"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                textsOutput4[i] = "is"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                textsOutput4[i] = "is"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "is"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "is"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                textsOutput4[i] = "is"
                outAm = " ".join(textsOutput4)
                return outAm
            elif textsOutput4[0] == "i":
                return getPosition
            elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "NNS":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                textsOutput4[i] = "are"
                outAm = " ".join(textsOutput4)
                return outAm
            else:
                textsOutput4[i] = "is"
                outAre = " ".join(textsOutput4)
                return outAre
        

def correct_continuous(textsOutput4, tagOutput4, getPosition):
    if AUXCont(textsOutput4, tagOutput4, getPosition):
        return AUXCont(textsOutput4, tagOutput4, getPosition)
                           
    else:
        if textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            textsOutput4.insert(1, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            textsOutput4.insert(2, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            textsOutput4.insert(2, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            textsOutput4.insert(2, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            textsOutput4.insert(3, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            textsOutput4.insert(3, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            textsOutput4.insert(3, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
        elif textsOutput4[0] == "i":
            textsOutput4.insert(1, "am")
            outtAddAm = " ".join(textsOutput4)
            return outtAddAm
        elif textsOutput4[0] == "you" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            textsOutput4.insert(1, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        elif tagOutput4[0] == "NNS":
            textsOutput4.insert(1, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            textsOutput4.insert(3, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            textsOutput4.insert(3, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            textsOutput4.insert(3, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            textsOutput4.insert(2, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            textsOutput4.insert(2, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            textsOutput4.insert(2, "are")
            outtAddAre = " ".join(textsOutput4)
            return outtAddAre
        else:
            textsOutput4.insert(1, "is")
            outtAddIs = " ".join(textsOutput4)
            return outtAddIs
                                        