import numpy as np
import spacy
from englishDetect import language_detection
from flask import Flask, request
from autocorrect import Speller
from positionChecker import position_checker
from presentContinuous import present_continuous, correct_continuous
from presentPerfect import present_perfect, correct_perfect
from simplePast import simple_past
from simpleFuture import simple_future
from simplePresent import SVAPresent
from detectSentence import detect
from positionCheckerQuest import position_checker_quest
from simplePresentQuest import simple_present_quest, VBZVBP
from simplePastQuest import simple_past_quest, VBD
from simpleFutureQuest import simple_future_quest
from presentPerfectQuest import present_perfect_quest, VBN
from presentContinuousQuest import present_continuous_quest, VBG
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


def timeSignalQuest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, text3, doc6, textsOutput424):
    if doubleTense(textsOutput4):
        return doubleTense(textsOutput4)
    elif anotherTense(textsOutput4):
        return anotherTense(textsOutput4)
    elif simple_future_quest(getPosition, textsOutput42Verb, doc6):
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+simple_future_quest(getPosition, textsOutput42Verb, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textFuture+'*'
    elif simple_past_quest(getPosition, textsOutput42Verb, doc6):
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+simple_past_quest(getPosition, textsOutput42Verb, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPast+'*'
    elif present_perfect_quest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+present_perfect_quest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPerfect+'*'
    elif present_continuous_quest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6):
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+present_continuous_quest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textContinuous+'*'
    else:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+simple_present_quest(getPosition, tagOutput4, textsOutput424, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'


def correctVerbQuest(getPosition, textsOutput4, textsOutput42Verb, tagOutput4, tagOutput42, tagOutput43, text3, doc6):
    if "VBD" in tagOutput42 and "VBD" in tagOutput43:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+VBD(getPosition, textsOutput42Verb, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPast+'*'
    elif "VBD" in tagOutput42 and "VBN" in tagOutput43:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+VBN(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPerfect+'*'
    elif "VBN" in tagOutput42 and "VBN" in tagOutput43:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+VBN(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPerfect+'*'
    elif "VBG" in tagOutput43:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+VBG(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textContinuous+'*'
    elif "VBZ" in tagOutput42:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+VBZVBP(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'
    elif "VBP" in tagOutput42:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+VBZVBP(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'
    elif "VB" in tagOutput42:
        return "Original text : " + text3 + " \n" + "_Correction text :_ " + '_'+VBZVBP(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, doc6).capitalize()+'_' + "\n" + "*The tense is :* " + '*'+textPresent+'*'


def quest(text2split):
    text3 = text2split
    splittext = text2split.split()
    count = len(splittext)
    if count < 30:
        grammar_id = []
        englishLanguage = language_detection(text3)

        if englishLanguage == 'en' or englishLanguage == 'no' or englishLanguage == 'da' or englishLanguage == 'nl' or englishLanguage == 'af' or englishLanguage == 'cy' or englishLanguage == 'ca' or englishLanguage == 'tl' or englishLanguage == 'hr' or englishLanguage == 'it':
            checkk = Speller(lang='en')
            sp = checkk(text3)
            textsplit = sp.split()
            doc = nlp(sp)
            poss = [token.pos_ for token in doc]
            possTAG = [token.tag_ for token in doc]
            texts3 = [token.text for token in doc]

            # return " ".join(poss)
            if "X" in poss:
                return "*Sorry, the system cannot process abbreviations or unknown words*"
            else:
                if "PRON" and "VERB" in poss or "NOUN" and "VERB" in poss:
                    getPosition = " ".join(
                        position_checker_quest(poss, texts3))
                    docOutput4 = nlp(getPosition)
                    posOutput4 = [token.pos_ for token in docOutput4]
                    textsOutput4 = [token.text for token in docOutput4]
                    tagOutput4 = [token.tag_ for token in docOutput4]

                    posOutput44 = [token.pos_ for token in docOutput4]
                    textsOutput44 = [token.text for token in docOutput4]
                    tagOutput44 = [token.tag_ for token in docOutput4]
                    iii = posOutput44.index('VERB')
                    textsOutput424 = textsOutput44[iii]
                    doc6 = nlp(textsOutput424)
                    tagOutput424 = tagOutput44[iii]
                    tagOutput434 = [token.tag_ for token in doc6]

                    posOutput4Verb = posOutput4[1:]
                    textsOutput4Verb = textsOutput4[1:]
                    tagOutput4Verb = tagOutput4[1:]
                    iiii = posOutput4Verb.index('VERB')
                    textsOutput42Verb = textsOutput4Verb[iiii]
                    doc6 = nlp(textsOutput42Verb)
                    tagOutput42 = tagOutput4Verb[iiii]
                    tagOutput43 = [token.tag_ for token in doc6]
                    try:
                        return timeSignalQuest(getPosition, tagOutput4, textsOutput42Verb, textsOutput4, text3, doc6, textsOutput424)
                    except:
                        return correctVerbQuest(getPosition, textsOutput4, textsOutput42Verb, tagOutput4, tagOutput42, tagOutput43, text3, doc6)
                else:
                    return "*Sorry, the sentence must have subject and verb*" + "\n" + "*Please place the subject or the verb or the object or the adverb in the right place*" + "\n" + "For examples, click or type /help"

        else:
            return "*Sorry, we can't detect the sentence, you must input the sentence with english language or you must input the complete sentence*" + "\n" + "For examples, click or type /help"
    else:
        return "*Sorry, the sentence is too much, you must input the simple sentence*" + "\n" + "For examples, click or type /help"

        # else:
        #     message = "*Sorry, the sentence must have subject and verb*" + "\n" + "*Please place the subject or the verb or the object or the adverb in the right place*" + "\n" + "_Example :_" + "\n" + \
        #         "_- He goes to the library every day_" + "\n" + "_- He went to the library yesterday_" + "\n" + \
        #         "_- He will go to the library_" + "\n" + "_- He is going to the library_" + \
        #         "\n" + "_- He has gone to the library_"
        #     return message
