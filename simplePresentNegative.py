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
        "correction": ""
    },
    {
        "pattern": r"does",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"not",
        "message": "simple present tense",
        "correction": ""
    },
    {
        "pattern": r"nt",
        "message": "simple present tense",
        "correction": ""
    }]


def simple_present_negative(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42, token._.inflect("VB"))
        break

    outtsplit = outt4.split()
    indexPattern = []
    for i in range(len(outtsplit)):
        for errPresent in TSSimplePresent:
            if outtsplit[i] == errPresent["pattern"]:
                indexPattern.append(outtsplit[i])
    # return " ".join(indexPattern)
    if "every" in indexPattern or "frequently" in indexPattern or "always" in indexPattern or "sometimes" in indexPattern or "generally" in indexPattern or "usually" in indexPattern or "often" in indexPattern or "occasionally" in indexPattern or "seldom" in indexPattern or "rarely" in indexPattern:
        if "do" in indexPattern and "not" in indexPattern:
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                return outt4
            elif tagOutput4[0] == "NNS":
                return outt4
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                return outt4
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                return outt4
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                return outt4
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            else:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
        # ---------------------------------SUDAH DICEK----------------------------------------------------
        elif "do" in indexPattern and "nt" in indexPattern:
            indexPattern[indexPattern.index("nt")] = "not"
            outNott = outt4.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
                indexPattern[indexPattern.index("not")]))
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                return outNott
            elif tagOutput4[0] == "NNS":
                return outNott
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outNott
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outNott
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outNott
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                return outNott
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                return outNott
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                return outNott
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
            else:
                indexPattern[indexPattern.index("do")] = "does"
                outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                    indexPattern[indexPattern.index("does")]))
                return outNotDoes
        # -----------------------------------SUDAH DICEK----------------------------------------------------
        elif "does" in indexPattern and "not" in indexPattern:
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                return outt4
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                return outt4
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                return outt4
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                return outt4
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outt4
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return outt4
            else:
                return outt4
        # -------------------------------------------SUDAH DICEK--------------------------------------------
        elif "does" in indexPattern and "nt" in indexPattern:
            indexPattern[indexPattern.index("nt")] = "not"
            outNott2 = outt4.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
                indexPattern[indexPattern.index("not")]))
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                indexPattern[indexPattern.index("does")] = "do"
                outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                    indexPattern[indexPattern.index("do")]))
                return outNotDo
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
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
            else:
                return outNott2
        # -----------------------------------SUDAH DICEK------------------------------------------------------
        elif "not" in indexPattern:
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                outtsplit.insert(1, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "NNS":
                outtsplit.insert(1, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                outtsplit.insert(3, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                outtsplit.insert(2, "do")
                outtAddDo = " ".join(outtsplit)
                return outtAddDo
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                outtsplit.insert(1, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                outtsplit.insert(2, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                outtsplit.insert(3, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
            else:
                outtsplit.insert(1, "does")
                outtAddDoes = " ".join(outtsplit)
                return outtAddDoes
        # -----------------------------------------SUDAH DICEK-------------------------------------------
        else:
            if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
                return outt4
            elif tagOutput4[0] == "NNS":
                return outt4
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
                return outt4
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
                return outt4
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
                return outt4
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
                return outt4
            elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
                return SVAPresent(doc6, getPosition, textsOutput42)
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
                return SVAPresent(doc6, getPosition, textsOutput42)
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
                return SVAPresent(doc6, getPosition, textsOutput42)
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
                return SVAPresent(doc6, getPosition, textsOutput42)
            elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return SVAPresent(doc6, getPosition, textsOutput42)
            elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return SVAPresent(doc6, getPosition, textsOutput42)
            elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
                return SVAPresent(doc6, getPosition, textsOutput42)
            else:
                return SVAPresent(doc6, getPosition, textsOutput42)
        # -----------------------------SUDAH DICEK-------------------------------------------------
    elif "do" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outt4
        elif tagOutput4[0] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outt4
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        else:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
    # -----------------------------------------SUDAH DICEK--------------------------------------------------
    elif "do" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott = outt4.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outNott
        elif tagOutput4[0] == "NNS":
            return outNott
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outNott
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outNott
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outNott
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        else:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(outtsplit[outtsplit.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
    # -----------------------SUDAH DICEK-------------------------------------------------------
    elif "does" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        else:
            return outt4
    # -------------------------SUDAH DICEK--------------------------------------------
    elif "does" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outt4.replace("".join(outtsplit[outtsplit.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(outtsplit[outtsplit.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
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
        else:
            return outNott2
    # -------------------------SUDAH DICEK---------------------------------------------


def VBZ(getPosition, tagOutput4, textsOutput4, textsOutput42, doc6):
    indexPattern = []
    for i in range(len(textsOutput4)):
        for errPresent in TSSimplePresent:
            if textsOutput4[i] == errPresent["pattern"]:
                indexPattern.append(textsOutput4[i])
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42, token._.inflect("VB"))
        break
    outtsplit = outt4.split()
    if "do" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outt4
        elif tagOutput4[0] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outt4
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        else:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
    # -----------------------------SUDAH DICEK--------------------------------------------------
    elif "do" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott = outt4.replace("".join(textsOutput4[textsOutput4.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outNott
        elif tagOutput4[0] == "NNS":
            return outNott
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outNott
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outNott
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outNott
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        else:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
    # -----------------------------------SUDAH DICEK---------------------------------------------------------
    elif "does" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        else:
            return outt4
    #--------------------------------------SUDAH DICEK---------------------------------------
    elif "does" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outt4.replace("".join(textsOutput4[textsOutput4.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
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
        else:
            return outNott2
    #-------------------------------SUDAH DICEK---------------------------------------------
    elif "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        else:
            outtsplit.insert(1, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
    else:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outt4
        elif tagOutput4[0] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outt4
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
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
        else:
            return getPosition


def VBP(getPosition, tagOutput4, textsOutput4, textsOutput42, doc6):
    indexPattern = []
    for i in range(len(textsOutput4)):
        for errPresent in TSSimplePresent:
            if textsOutput4[i] == errPresent["pattern"]:
                indexPattern.append(textsOutput4[i])
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42, token._.inflect("VB"))
        break
    outtsplit = outt4.split()
    if "do" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outt4
        elif tagOutput4[0] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outt4
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        else:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outt4.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
    #------------------------------SUDAH DICEK------------------------------------------------
    elif "do" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott = outt4.replace("".join(textsOutput4[textsOutput4.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outNott
        elif tagOutput4[0] == "NNS":
            return outNott
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outNott
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outNott
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outNott
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outNott
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
        else:
            indexPattern[indexPattern.index("do")] = "does"
            outNotDoes = outNott.replace("".join(textsOutput4[textsOutput4.index("do")]), "".join(
                indexPattern[indexPattern.index("does")]))
            return outNotDoes
    #------------------------------SUDAH DICEK------------------------------------------------
    elif "does" in indexPattern and "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outt4.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return outt4
        else:
            return outt4
    #------------------------------SUDAH DICEK------------------------------------------------
    elif "does" in indexPattern and "nt" in indexPattern:
        indexPattern[indexPattern.index("nt")] = "not"
        outNott2 = outt4.replace("".join(textsOutput4[textsOutput4.index("nt")]), "".join(
            indexPattern[indexPattern.index("not")]))
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            indexPattern[indexPattern.index("does")] = "do"
            outNotDo = outNott2.replace("".join(textsOutput4[textsOutput4.index("does")]), "".join(
                indexPattern[indexPattern.index("do")]))
            return outNotDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
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
        else:
            return outNott2
    #------------------------------SUDAH DICEK------------------------------------------------
    elif "not" in indexPattern:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            outtsplit.insert(1, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "NNS":
            outtsplit.insert(1, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            outtsplit.insert(3, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            outtsplit.insert(2, "do")
            outtAddDo = " ".join(outtsplit)
            return outtAddDo
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            outtsplit.insert(1, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            outtsplit.insert(2, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            outtsplit.insert(3, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
        else:
            outtsplit.insert(1, "does")
            outtAddDoes = " ".join(outtsplit)
            return outtAddDoes
    #------------------------------SUDAH DICEK------------------------------------------------
    else:
        if textsOutput4[0] == "you" or textsOutput4[0] == "i" or textsOutput4[0] == "they" or textsOutput4[0] == "we":
            return outt4
        elif tagOutput4[0] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NNS":
            return outt4
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NNS":
            return outt4
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NNS":
            return outt4
        elif textsOutput4[0] == "she" or textsOutput4[0] == "he" or textsOutput4[0] == "it":
            return SVAPresent(doc6, getPosition, textsOutput42)
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "NN":
            return SVAPresent(doc6, getPosition, textsOutput42)
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "NN":
            return SVAPresent(doc6, getPosition, textsOutput42)
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "NN":
            return SVAPresent(doc6, getPosition, textsOutput42)
        elif tagOutput4[0] == "PRP$" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return SVAPresent(doc6, getPosition, textsOutput42)
        elif tagOutput4[0] == "DT" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return SVAPresent(doc6, getPosition, textsOutput42)
        elif tagOutput4[0] == "CD" and tagOutput4[1] == "JJ" and tagOutput4[2] == "NN":
            return SVAPresent(doc6, getPosition, textsOutput42)
        else:
            return SVAPresent(doc6, getPosition, textsOutput42)
#-------------------------SUDAH DICEK-------------------------------------------------------