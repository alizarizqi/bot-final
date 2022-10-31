from langdetect import detect, detect_langs
from langdetect import DetectorFactory
DetectorFactory.seed = 0


def language_detection(text, method="single"):

    if(method.lower() != "single"):
        result = detect_langs(text)

    else:
        result = detect(text)

    return result
