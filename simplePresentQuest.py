import re
import spacy
from simplePresent import SVAPresent
nlp = spacy.load("en_core_web_sm")

TSSimplePresent = [
    {
        "pattern": r"every",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"frequently",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"always",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"sometimes",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"generally",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"usually",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"often",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"occasionally",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"seldom",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"rarely",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"do",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"does",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"not",
        "message": "simple present tense",
        "correction": "",
    },
    {
        "pattern": r"n't",
        "message": "simple present tense",
        "correction": "",
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


def simple_present_quest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42Verb, token._.inflect("VB"))
        break

    outtsplit = outt4.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errPresent in TSSimplePresent:
            if outtsplit[i] == errPresent["pattern"]:
                indexPattern.append(outtsplit[i])
    if "every" in indexPattern or "frequently" in indexPattern or "always" in indexPattern or "sometimes" in indexPattern or "generally" in indexPattern or "usually" in indexPattern or "often" in indexPattern or "occasionally" in indexPattern or "seldom" in indexPattern or "rarely" in indexPattern:
        if "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
            if "much" in indexPattern or "long" in indexPattern:
                if "do" in indexPattern and "not" in indexPattern:
                    indexPattern[indexPattern.index("do")] = "does"
                    outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                        indexPattern[indexPattern.index("does")]))
                    if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        return outt4
                    elif tagOutput4[3] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        return outt4
                    elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        return outNotDoes
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outNotDoes
                    else:
                        return outNotDoes
                # -------------------------------SUDAH DICEK---------------------------------------
                elif "does" in indexPattern and "not" in indexPattern:
                    indexPattern[indexPattern.index("does")] = "do"
                    outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                        indexPattern[indexPattern.index("do")]))
                    if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        return outNotDo
                    elif tagOutput4[3] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outt4
                    else:
                        return outt4
                # ------------------------------------SUDAHDICEK----------------------------------------
                elif "do" in indexPattern:
                    indexPattern[indexPattern.index("do")] = "does"
                    outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                        indexPattern[indexPattern.index("does")]))
                    if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        return outt4
                    elif tagOutput4[3] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        return outt4
                    elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        return outNotDoes
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outNotDoes
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outNotDoes
                    else:
                        return outNotDoes
                # --------------------------------SUDAH DICEK-------------------------------------------
                elif "does" in indexPattern:
                    indexPattern[indexPattern.index("does")] = "do"
                    outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                        indexPattern[indexPattern.index("do")]))
                    if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                        return outNotDo
                    elif tagOutput4[3] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outt4
                    elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outt4
                    elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                        return outt4
                    else:
                        return outt4
                # --------------------------------SUDAH DICEK-------------------------------------
                elif "not" in indexPattern:
                    if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "NNS" or tagOutput4[3] == "DT" or tagOutput4[4] == "CD":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    else:
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                # ------------------------------------SUDAH DICEK-------------------------------------------------
                else:
                    if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "NNS" or tagOutput4[3] == "DT" or tagOutput4[4] == "CD":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        outtsplit.insert(2, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    else:
                        outtsplit.insert(2, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                # -------------------------------------SUDAH DICEK--------------------------------------
            else:
                if "do" in indexPattern and "not" in indexPattern:
                    indexPattern[indexPattern.index("do")] = "does"
                    outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                        indexPattern[indexPattern.index("does")]))
                    if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        return outt4
                    elif tagOutput4[2] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        return outt4
                    elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        return outNotDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outNotDoes
                    else:
                        return outNotDoes
                # ---------------------------------SUDAH DICEK--------------------------------------------
                elif "does" in indexPattern and "not" in indexPattern:
                    indexPattern[indexPattern.index("does")] = "do"
                    outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                        indexPattern[indexPattern.index("do")]))
                    if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        return outNotDo
                    elif tagOutput4[2] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        return outNotDo
                    elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outt4
                    else:
                        return outt4
                # ---------------------------------SUDAH DICEK--------------------------------------------
                elif "do" in indexPattern:
                    indexPattern[indexPattern.index("do")] = "does"
                    outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                        indexPattern[indexPattern.index("does")]))
                    if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        return outt4
                    elif tagOutput4[2] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        return outt4
                    elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        return outNotDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outNotDoes
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outNotDoes
                    else:
                        return outNotDoes
                # ---------------------------------SUDAH DICEK--------------------------------------------
                elif "does" in indexPattern:
                    indexPattern[indexPattern.index("does")] = "do"
                    outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                        indexPattern[indexPattern.index("do")]))
                    if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                        return outNotDo
                    elif tagOutput4[2] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                        return outNotDo
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                        return outNotDo
                    elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                        return outt4
                    elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outt4
                    elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                        return outt4
                    else:
                        return outt4
                # ---------------------------------SUDAH DICEK--------------------------------------------
                elif "not" in indexPattern:
                    if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "NNS" or tagOutput4[2] == "DT" or tagOutput4[3] == "CD":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    else:
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                # ---------------------------------SUDAH DICEK--------------------------------------------
                else:
                    if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "NNS" or tagOutput4[2] == "DT" or tagOutput4[3] == "CD":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                        outtsplit.insert(1, "do")
                        outtAddDo = " ".join(outtsplit)
                        return outtAddDo
                    elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                    else:
                        outtsplit.insert(1, "does")
                        outtAddDoes = " ".join(outtsplit)
                        return outtAddDoes
                 # ---------------------------------SUDAH DICEK--------------------------------------------
        elif "do" in indexPattern and "not" in indexPattern:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outt4
            elif tagOutput4[1] == "NNS":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outt4
            elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outNotDoes
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outNotDoes
            else:
                return outNotDoes
         # ---------------------------------SUDAH DICEK--------------------------------------------
        elif "does" in indexPattern and "not" in indexPattern:
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outNotDo
            elif tagOutput4[1] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outNotDo
            elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outt4
            else:
                return outt4
        # ---------------------------------SUDAH DICEK--------------------------------------------
        elif "do" in indexPattern:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outt4
            elif tagOutput4[1] == "NNS":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outt4
            elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outNotDoes
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outNotDoes
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outNotDoes
            else:
                return outNotDoes
        # ---------------------------------SUDAH DICEK--------------------------------------------
        elif "does" in indexPattern:
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                return outNotDo
            elif tagOutput4[1] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                return outNotDo
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                return outNotDo
            elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outt4
            elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outt4
            elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                return outt4
            else:
                return outt4
        # ---------------------------------SUDAH DICEK--------------------------------------------
        elif "not" in indexPattern:
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "NNS" or tagOutput4[1] == "DT" or tagOutput4[2] == "CD":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            else:
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
        # ---------------------------------SUDAH DICEK--------------------------------------------
        else:
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "NNS" or tagOutput4[1] == "DT" or tagOutput4[2] == "CD":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(0, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            else:
                outtsplit.insert(0, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
        # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
        if "much" in indexPattern or "long" in indexPattern:
            if "do" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outt4
                elif tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outt4
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outNotDo
                elif tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                else:
                    return outt4
             # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "do" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outt4
                elif tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outt4
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outNotDo
                elif tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                else:
                    return outt4
            # ---------------------------------SUDAH DICEK--------------------------------------------
        else:
            if "do" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outt4
                elif tagOutput4[2] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outt4
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outNotDo
                elif tagOutput4[2] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                else:
                    return outt4
             # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "do" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outt4
                elif tagOutput4[2] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outt4
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
             # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outNotDo
                elif tagOutput4[2] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                else:
                    return outt4
             # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "do" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index("do")] = "does"
        outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
            indexPattern[indexPattern.index("does")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outt4
        elif tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outt4
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        else:
            return outNotDoes
     # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "does" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index("does")] = "do"
        outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
            indexPattern[indexPattern.index("do")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outNotDo
        elif tagOutput4[1] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outNotDo
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        else:
            return outt4
     # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "do" in indexPattern:
        indexPattern[indexPattern.index("do")] = "does"
        outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
            indexPattern[indexPattern.index("does")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outt4
        elif tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outt4
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        else:
            return outNotDoes
     # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "does" in indexPattern:
        indexPattern[indexPattern.index("does")] = "do"
        outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
            indexPattern[indexPattern.index("do")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outNotDo
        elif tagOutput4[1] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outNotDo
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        else:
            return outt4
     # ---------------------------------SUDAH DICEK--------------------------------------------


def VBZVBP(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42Verb, token._.inflect("VB"))
        break

    outtsplit = outt4.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errPresent in TSSimplePresent:
            if outtsplit[i] == errPresent["pattern"]:
                indexPattern.append(outtsplit[i])

    if "what" in indexPattern or "where" in indexPattern or "when" in indexPattern or "who" in indexPattern or "why" in indexPattern or "how" in indexPattern:
        if "much" in indexPattern or "long" in indexPattern:
            if "do" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outt4
                elif tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outt4
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outNotDo
                elif tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                else:
                    return outt4
             # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "do" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outt4
                elif tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outt4
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[3] == "you" or textsOutput4[3] == "i" or textsOutput4[3] == "they" or textsOutput4[3] == "we":
                    return outNotDo
                elif tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif textsOutput4[3] == "she" or textsOutput4[3] == "he" or textsOutput4[3] == "it":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[3] == "PRP$" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "DT" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                elif tagOutput4[3] == "CD" and tagOutput4[4] == "JJ" and tagOutput4[5] == "NN":
                    return outt4
                else:
                    return outt4
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "not" in indexPattern:
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "NNS" or tagOutput4[3] == "DT" or tagOutput4[4] == "CD":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                else:
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
            # ---------------------------------SUDAH DICEK--------------------------------------------
            else:
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "NNS" or tagOutput4[3] == "DT" or tagOutput4[4] == "CD":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    outtsplit.insert(2, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                else:
                    outtsplit.insert(2, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
             # ---------------------------------SUDAH DICEK--------------------------------------------
        else:
            if "do" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outt4
                elif tagOutput4[2] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outt4
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
             # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern and "not" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outNotDo
                elif tagOutput4[2] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                else:
                    return outt4
             # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "do" in indexPattern:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outt4
                elif tagOutput4[2] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outt4
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outNotDoes
                else:
                    return outNotDoes
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "does" in indexPattern:
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                if textsOutput4[2] == "you" or textsOutput4[2] == "i" or textsOutput4[2] == "they" or textsOutput4[2] == "we":
                    return outNotDo
                elif tagOutput4[2] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NNS":
                    return outNotDo
                elif textsOutput4[2] == "she" or textsOutput4[2] == "he" or textsOutput4[2] == "it":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "NN":
                    return outt4
                elif tagOutput4[2] == "PRP$" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "DT" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                elif tagOutput4[2] == "CD" and tagOutput4[3] == "JJ" and tagOutput4[4] == "NN":
                    return outt4
                else:
                    return outt4
            # ---------------------------------SUDAH DICEK--------------------------------------------
            elif "not" in indexPattern:
                if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "NNS" or tagOutput4[2] == "DT" or tagOutput4[3] == "CD":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                else:
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
             # ---------------------------------SUDAH DICEK--------------------------------------------
            else:
                if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "NNS" or tagOutput4[2] == "DT" or tagOutput4[3] == "CD":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
                    outtsplit.insert(1, "do")
                    outtAddDo = " ".join(outtsplit)
                    return outtAddDo
                elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
                else:
                    outtsplit.insert(1, "does")
                    outtAddDoes = " ".join(outtsplit)
                    return outtAddDoes
             # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "do" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index("do")] = "does"
        outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
            indexPattern[indexPattern.index("does")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outt4
        elif tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outt4
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        else:
            return outNotDoes
    # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "does" in indexPattern and "not" in indexPattern:
        indexPattern[indexPattern.index("does")] = "do"
        outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
            indexPattern[indexPattern.index("do")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outNotDo
        elif tagOutput4[1] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outNotDo
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        else:
            return outt4
    # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "do" in indexPattern:
        indexPattern[indexPattern.index("do")] = "does"
        outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
            indexPattern[indexPattern.index("does")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outt4
        elif tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outt4
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outNotDoes
        else:
            return outNotDoes
      # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "does" in indexPattern:
        indexPattern[indexPattern.index("does")] = "do"
        outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
            indexPattern[indexPattern.index("do")]))
        if textsOutput4[1] == "you" or textsOutput4[1] == "i" or textsOutput4[1] == "they" or textsOutput4[1] == "we":
            return outNotDo
        elif tagOutput4[1] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NNS":
            return outNotDo
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NNS":
            return outNotDo
        elif textsOutput4[1] == "she" or textsOutput4[1] == "he" or textsOutput4[1] == "it":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[1] == "PRP$" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "DT" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        elif tagOutput4[1] == "CD" and tagOutput4[2] == "JJ" and tagOutput4[3] == "NN":
            return outt4
        else:
            return outt4
    # ---------------------------------SUDAH DICEK--------------------------------------------
    elif "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "NNS" or tagOutput4[1] == "DT" or tagOutput4[2] == "CD":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        else:
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
      # ---------------------------------SUDAH DICEK--------------------------------------------
    else:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "NNS" or tagOutput4[1] == "DT" or tagOutput4[2] == "CD":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(0, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        else:
            outtsplit.insert(0, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
      # ---------------------------------SUDAH DICEK--------------------------------------------
