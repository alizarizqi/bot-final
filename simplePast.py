TSSimplePast = [
    {
        "pattern": r"last",
        "message": "simple past tense",
        "correction": "",
        "err_id": "RTSPA001"
    },
    {
        "pattern": r"yesterday",
        "message": "simple past tense",
        "correction": "",
        "err_id": "RTSPA002"
    },
    {
        "pattern": r"ago",
        "message": "simple past tense",
        "correction": "",
        "err_id": "RTSPA003"
    }]


def simple_past(getPosition, textsPast2, doc6):

    for i in range(len(doc6)):
        token = doc6[i]
        outtVBD = getPosition.replace(
            textsPast2, token._.inflect("VBD"))
        break
    outtsplit = outtVBD.split()

    for i in range(len(outtsplit)):
        for errTSPast in TSSimplePast:
            if outtsplit[i] == errTSPast["pattern"]:
                return outtVBD
