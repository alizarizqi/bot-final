import re
import spacy
nlp = spacy.load("en_core_web_sm")

TSSimplePresent = [
    {
        "pattern": r"every",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP001"
    },
    {
        "pattern": r"frequently",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP002"
    },
    {
        "pattern": r"always",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP003"
    },
    {
        "pattern": r"sometimes",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP004"
    },
    {
        "pattern": r"do",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP004"
    },
    {
        "pattern": r"does",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP004"
    },
    {
        "pattern": r"not",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP004"
    },
    {
        "pattern": r"n't",
        "message": "simple present tense",
        "correction": "",
        "err_id": "RTSP004"
    }]


def SVAPresent(doc6, getPosition, textsOutput42):
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42, token._.inflect("VB"))
        break
    docPresent2 = nlp(outt4)
    posPresent2 = [token.pos_ for token in docPresent2]
    textsPresent3 = [token.text for token in docPresent2]
    iii = posPresent2.index('VERB')
    textsPresent4 = textsPresent3[iii]
    textsPresent4Last = textsPresent4[-3:]
    pattern1 = r'[a-z]+ss'
    pattern2 = r'[a-z]+sh'
    pattern3 = r'[a-z]+ch'
    pattern4 = r'[a-z]+x'
    pattern5 = r'[a-z]+o'
    pattern6 = r'[b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z]+y'
    pattern7 = r'[a, i, u, e, o]+y'
    search1 = re.search(pattern1, textsPresent4Last)
    search2 = re.search(pattern2, textsPresent4Last)
    search3 = re.search(pattern3, textsPresent4Last)
    search4 = re.search(pattern4, textsPresent4Last)
    search5 = re.search(pattern5, textsPresent4Last)
    search6 = re.search(pattern6, textsPresent4Last)
    search7 = re.search(pattern7, textsPresent4Last)
    if search1 or search2 or search3 or search4 or search5:
        out6 = re.sub(r'(\b\w+\b)', r'\1es', textsPresent4)
        outt2 = outt4.replace(textsPresent4, out6)
        return outt2
    elif search6:
        strYlist = list(textsPresent4)
        y = strYlist.index("y")
        strYlist[y] = "i"
        str3 = "".join(strYlist)
        out6 = re.sub(r'(\b\w+\b)', r'\1es', str3)
        outt2 = outt4.replace(textsPresent4, out6)
        return outt2
    elif search7:
        out6 = re.sub(r'(\b\w+\b)', r'\1s', textsPresent4)
        outt2 = outt4.replace(textsPresent4, out6)
        return outt2
    else:
        out6 = re.sub(r'(\b\w+\b)', r'\1s', textsPresent4)
        outt2 = outt4.replace(textsPresent4, out6)
        return outt2


def simple_present(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
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
    if "every" in indexPattern or "sometimes" in indexPattern or "always" in indexPattern or "frequently" in indexPattern:
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


def VBZ(getPosition, tagOutput4, textsOutput4, textsOutput42, doc6):
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42, token._.inflect("VB"))
        break
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
    for i in range(len(doc6)):
        token = doc6[i]
        outt4 = getPosition.replace(
            textsOutput42, token._.inflect("VB"))
        break
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
