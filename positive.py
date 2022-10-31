import numpy as np
import spacy
from englishDetect import language_detection
from flask import Flask, request
from autocorrect import Speller
from positionChecker import position_checker
from presentContinuous import correct_continuous
from presentPerfectNeg import present_perfect_neg, correct_perfect_neg
from presentContinuousNeg import present_continuous_neg, VBG
from simplePast import simple_past

from simpleFuture import simple_future

from simplePresentNegative import simple_present_negative, VBZ, VBP
from simplePastNegative import simple_past_negative, VBD
from detectSentence import detect
from anotherTenses import anotherTense
from doubleKey import doubleTense
import os
import telegram
import re
import pyinflect
nlp = spacy.load("en_core_web_sm")
textPresent = "Simple Present Tense"
textPast = "Simple Past Tense"
textFuture = "Simple Future Tense"
textContinuous = "Present Continuous Tense"
textPerfect = "Present Perfect Tense"


def timeSignal(getPosition, tagOutput4, textsOutput42, textsOutput4, posOutput4, textOri, doc6):
    if doubleTense(textsOutput4):
        return doubleTense(textsOutput4)
    elif anotherTense(textsOutput4):
        return anotherTense(textsOutput4)
    elif present_perfect_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+present_perfect_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPerfect+'*'
    elif present_continuous_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6):
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+present_continuous_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textContinuous+'*'
    elif simple_future(getPosition, posOutput4, textsOutput42, textsOutput4, doc6):
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+simple_future(getPosition, posOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textFuture+'*'
    elif simple_past_negative(getPosition, posOutput4, textsOutput4, textsOutput42, doc6):
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+simple_past_negative(getPosition, posOutput4, textsOutput4, textsOutput42, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPast+'*'
    else:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+simple_present_negative(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'


def correctVerb(getPosition, posOutput4, textsOutput4, textsOutput42, tagOutput4, tagOutput42, tagOutput43, textOri, doc6):
    if "VBD" in tagOutput42 and "VBD" in tagOutput43:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+VBD(getPosition, posOutput4, textsOutput4, textsOutput42, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPast+'*'
    elif "VBD" in tagOutput42 and "VBN" in tagOutput43:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+correct_perfect_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPerfect+'*'
    elif "VBN" in tagOutput42 and "VBN" in tagOutput43:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+correct_perfect_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPerfect+'*'
    elif "VBG" in tagOutput43:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+VBG(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textContinuous+'*'
    elif "VBZ" in tagOutput42:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+VBZ(getPosition, tagOutput4, textsOutput4, textsOutput42, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'
    elif "VBP" in tagOutput42:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+VBP(getPosition, tagOutput4, textsOutput4, textsOutput42, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'
    elif "VB" in tagOutput42:
        return "Original text : " + textOri + " \n" + "_Correction text :_ " + '_'+VBP(getPosition, tagOutput4, textsOutput4, textsOutput42, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'


def positive(text2split, text):
    textOri = text
    text3 = text2split
    splittext = text2split.split()
    if "what" in splittext or "where" in splittext or "when" in splittext or "who" in splittext or "why" in splittext or "how" in splittext:
        return "*Sorry, you must input question mark (?) for the interrogative sentence*"
    else:
        count = len(splittext)
        if count < 30:
            grammar_id = []
            englishLanguage = language_detection(text3)
            if englishLanguage == 'en' or englishLanguage == 'no' or englishLanguage == 'da' or englishLanguage == 'nl' or englishLanguage == 'af' or englishLanguage == 'cy' or englishLanguage == 'ca' or englishLanguage == 'tl' or englishLanguage == 'hr' or englishLanguage == 'it':
                checkk = Speller(lang='en')
                sp = checkk(text3)
                textsplit = sp.split()
                getPosition2 = re.sub(r"[n]\'[t]", " not", sp)
                getPosition2 = re.sub(r"\'[v][e]", " have", getPosition2)
                getPosition2 = re.sub(r"\'[m]", " am", getPosition2)
                getPosition2 = re.sub(r"\'[r][e]", " are", getPosition2)
                getPosition2 = re.sub(r"\'[s]", " is", getPosition2)
                getPosition2 = re.sub(r"\'[v][e]", " have", getPosition2)
                getPosition2 = re.sub(r"\'[l][l]", " will", getPosition2)
                getPosition2 = re.sub(r"\'[d]", " would", getPosition2)

                doc = nlp(getPosition2)
                poss = [token.pos_ for token in doc]
                possTAG = [token.tag_ for token in doc]
                texts3 = [token.text for token in doc]
                if "X" in poss:
                    return "*Sorry, the system cannot process abbreviations or unknown words*" + "\n" + "For examples, click or type /help"
                else:
                    if "PRON" and "VERB" in poss or "NOUN" and "VERB" in poss:
                        getPosition = " ".join(position_checker(poss, texts3))
                        docOutput4 = nlp(getPosition)
                        posOutput4 = [token.pos_ for token in docOutput4]
                        textsOutput4 = [token.text for token in docOutput4]
                        tagOutput4 = [token.tag_ for token in docOutput4]

                        iii = posOutput4.index('VERB')
                        textsOutput42 = textsOutput4[iii]
                        doc6 = nlp(textsOutput42)
                        tagOutput42 = tagOutput4[iii]
                        tagOutput43 = [token.tag_ for token in doc6]

                        try:
                            return timeSignal(getPosition, tagOutput4, textsOutput42, textsOutput4, posOutput4, textOri, doc6)
                        except:
                            return correctVerb(getPosition, posOutput4, textsOutput4, textsOutput42, tagOutput4, tagOutput42, tagOutput43, textOri, doc6)

                    else:
                        return "*Sorry, the sentence must have subject and verb*" + "\n" + "*Please place the subject or the verb or the object or the adverb in the right place*" + "\n" + "For examples, click or type /help"
            else:
                return "*Sorry, we can't detect the sentence, you must input the sentence with english language or you must input the complete sentence*" + "\n" + "For examples, click or type /help"
        else:
            return "*Sorry, the sentence is too much, you must input the simple sentence*" + "\n" + "For examples, click or type /help"

        #     # return " ".join(posOutput4)

        #     # return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+present_continuous_neg(getPosition, tagOutput4, textsOutput42, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textContinuous+'*'
        #     # try:
        #     #     return timeSignal(getPosition, tagOutput4, textsOutput42, textsOutput4, posOutput4, text3, doc6)
        #     # except:
        #     #     return correctVerb(getPosition, posOutput4, textsOutput4, textsOutput42, tagOutput4, tagOutput42, tagOutput43, text3, doc6)

        # else:
        #     message = "*Sorry, the sentence must have subject and verb*" + "\n" + "*Please place the subject or the verb or the object or the adverb in the right place*" + "\n" + "_Example :_" + "\n" + \
        #         "_- He goes to the library every day_" + "\n" + "_- He went to the library yesterday_" + "\n" + \
        #         "_- He will go to the library_" + "\n" + "_- He is going to the library_" + \
        #         "\n" + "_- He has gone to the library_"
        #     return message
