import numpy as np

grammar = [
    {
        "pattern": ["AUX", "PRON", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[1, 0, 2, 3, 4],
        "example":"i have read a book"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PROPN", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[1, 0, 2, 3, 4],
        "example":"Dave has read a book"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[1, 0, 2, 3, 4],
        "example":"people have read a book"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "VERB", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3, 4],
        "example":"i have read a book"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "VERB", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3, 4],
        "example":"George has read a book"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "VERB", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4, 5],
        "example":"my sister has read a book"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "VERB", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3, 4],
        "example":"people have read a book"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "VERB", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4, 5],
        "example":"the sister has read a book"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "NOUN", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5, 6],
        "example":"the old sister has read a book"
    },
    # sudah - no dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "NOUN", "VERB", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5, 6],
        "example":"my old sister has read a book"
    },
    # sudah - no dicek
    {
        "pattern": ["PRON", "VERB", "AUX", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3, 4],
        "example":"i am reading a book"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "VERB", "AUX", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3, 4],
        "example":"sister is reading a book"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "VERB", "AUX", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4, 5],
        "example":"my sister is reading a book"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "VERB", "AUX", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3, 4],
        "example":"people are reading a book"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "VERB", "AUX", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4, 5],
        "example":"the sister is reading a book"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "VERB", "AUX", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5, 6],
        "example":"the old sister is reading a book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "VERB", "AUX", "DET", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5, 6],
        "example":"my old sister is reading a book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "VERB", "AUX", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3],
        "example":"i am reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["PROPN", "VERB", "AUX", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3],
        "example":"George is reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "PRON", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[1, 0, 2, 3],
        "example":"i am reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "PROPN", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[1, 0, 2, 3],
        "example":"George is reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "NOUN", "VERB", "AUX", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4],
        "example":"my sister is reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["NOUN", "VERB", "AUX", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3],
        "example":"people are reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[1, 0, 2, 3],
        "example":"i am reading book"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "VERB", "AUX", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4],
        "example":"the sister is reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "VERB", "AUX", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5],
        "example":"the old sister is reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "VERB", "AUX", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5],
        "example":"my old sister is reading book"
    },
    # sudah -no dicek
    {
        "pattern": ["PROPN", "VERB", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3],
        "example":"mom has read magazine"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "VERB", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4],
        "example":"my sister has read magazine"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "VERB", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 2, 1, 3],
        "example":"people have read magazine"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "VERB", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 3, 2, 4],
        "example":"the sister has read magazine"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "VERB", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5],
        "example":"the old sister has read book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "VERB", "VERB", "NOUN"],
        "message":"verb placed after auxilary",
        "correction":[0, 1, 2, 4, 3, 5],
        "example":"my old sister has read book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "AUX", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3],
        "example":"i am reading the book"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "AUX", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3],
        "example":"George is reading the book"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 4, 3],
        "example":"i am reading the book"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PROPN", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 4, 3],
        "example":"George is reading the book"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "AUX", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 5, 4],
        "example":"my sister is reading the book"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "AUX", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3],
        "example":"people are reading the book"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 4, 3],
        "example":"i am reading the book"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "AUX", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 5, 4],
        "example":"the sister is reading the book"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "AUX", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 6, 5],
        "example":"the old sister is reading the book"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "AUX", "VERB", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 6, 5],
        "example":"my old sister is reading the book"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "VERB", "AUX", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 2, 1, 4, 3],
        "example":"i am reading the book"
    },
    {
        "pattern": ["PROPN", "VERB", "AUX", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 2, 1, 4, 3],
        "example":"George is reading the book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "NOUN", "VERB", "AUX", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 3, 2, 5, 4],
        "example":"my sister is reading the book"
    },
    # sudah -no dicek
    {
        "pattern": ["NOUN", "VERB", "AUX", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 2, 1, 4, 3],
        "example":"people are reading the book"
    },
    # sudah -no dicek
    {
        "pattern": ["DET", "NOUN", "VERB", "AUX", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 3, 2, 5, 4],
        "example":"the sister is reading the book"
    },
    # sudah -no dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "VERB", "AUX", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3, 6, 5],
        "example":"the old sister is reading the book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "VERB", "AUX", "NOUN", "DET"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3, 6, 5],
        "example":"my old sister is reading the book"
    },
    # sudah -no dicek
    {
        "pattern": ["PRON", "ADV", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 2, 1, 3],
        "example":"she lived here already"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "ADV", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 2, 1, 3],
        "example":"George lived here already"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "ADV", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 3, 2, 4],
        "example":"my sister lived here already"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "ADV", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 2, 1, 3],
        "example":"people lived here already"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "ADV", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 3, 2, 4],
        "example":"the sister lived here already"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "ADV", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3, 5],
        "example":"the old sister lived here already"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "ADV", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3, 5],
        "example":"my old sister lived here already"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "AUX", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 5, 4],
        "example":"they have bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "AUX", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 5, 4],
        "example":"George has bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 5, 4],
        "example":"they have bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PROPN", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 5, 4],
        "example":"George has bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "AUX", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 6, 5],
        "example":"my sister has bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "AUX", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 5, 4],
        "example":"people have bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 5, 4],
        "example":"people have bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "AUX", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 6, 5],
        "example":"the sister has bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "AUX", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 5, 7, 6],
        "example":"the old sister has bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "AUX", "VERB", "DET", "NOUN", "ADJ"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 5, 7, 6],
        "example":"my old sister has bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "AUX", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3],
        "example":"i have seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "AUX", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3],
        "example":"George has seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 4, 3],
        "example":"i have seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PROPN", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 4, 3],
        "example":"George has seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "AUX", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 5, 4],
        "example":"my sister has seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "AUX", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 4, 3],
        "example":"people have seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 4, 3],
        "example":"people have seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "AUX", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 5, 4],
        "example":"the sister has seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "AUX", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 6, 5],
        "example":"the old sister has seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "AUX", "VERB", "NOUN", "PRON"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 6, 5],
        "example":"my old sister has seen that movie"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "DET", "NOUN", "AUX", "VERB"],
        "message":"noun placed after determinan",
        "correction":[0, 3, 4, 1, 2],
        "example":"you have broken the glass"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "DET", "NOUN", "AUX", "VERB"],
        "message":"noun placed after determinan",
        "correction":[0, 3, 4, 1, 2],
        "example":"George has broken the glass"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "DET", "NOUN", "AUX", "VERB"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 4, 5, 2, 3],
        "example":"my sister has broken the glass"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "DET", "NOUN", "AUX", "VERB"],
        "message":"noun placed after determinan",
        "correction":[0, 3, 4, 1, 2],
        "example":"people have broken the glass"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "DET", "NOUN", "AUX", "VERB"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 4, 5, 2, 3],
        "example":"the baby has broken the glass"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "DET", "NOUN", "AUX", "VERB"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 5, 6, 3, 4],
        "example":"the old baby has broken the glass"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "DET", "NOUN", "AUX", "VERB"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 5, 6, 3, 4],
        "example":"my old baby has broken the glass"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "AUX", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 5, 6, 7, 2, 3, 4],
        "example":"we are watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "AUX", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 5, 6, 7, 2, 3, 4],
        "example":"George is watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 5, 6, 7, 2, 3, 4],
        "example":"we are watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PROPN", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 5, 6, 7, 2, 3, 4],
        "example":"George is watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "AUX", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 5, 6, 7, 2, 3, 4],
        "example":"people are watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 5, 6, 7, 2, 3, 4],
        "example":"people are watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "AUX", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 6, 7, 8, 3, 4, 5],
        "example":"my sister is watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "AUX", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 6, 7, 8, 3, 4, 5],
        "example":"the sister is watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "AUX", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 7, 8, 9, 4, 5, 6],
        "example":"the old sister is watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "AUX", "ADP", "DET", "NOUN", "VERB", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 7, 8, 9, 4, 5, 6],
        "example":"my old sister is watching a movie in this cineplex"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "AUX", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 6, 7, 8, 3, 4, 5],
        "example":"People are going to the beach with their friend"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 6, 7, 8, 3, 4, 5],
        "example":"People are going to the beach with their friend"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "AUX", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 6, 7, 8, 3, 4, 5],
        "example":"you are going to the beach with your friend"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 6, 7, 8, 3, 4, 5],
        "example":"you are going to the beach with your friend"
    },
    # sudah dicek
    {
        "pattern": ["PROPN", "AUX", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 6, 7, 8, 3, 4, 5],
        "example":"George going to the beach with his friend"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PROPN", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 6, 7, 8, 3, 4, 5],
        "example":"George is going to the beach with his friend"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "AUX", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 7, 8, 9, 4, 5, 6],
        "example":"my sister is going to the beach with her friend"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "AUX", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 7, 8, 9, 4, 5, 6],
        "example":"the sister is going to the beach with her friend"
    },
    # sudah dicek
    {
        "pattern": ["DET", "ADJ", "NOUN", "AUX", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 8, 9, 10, 5, 6, 7],
        "example":"the old sister is going to the beach with her friend"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "AUX", "VERB", "ADP", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 8, 9, 10, 5, 6, 7],
        "example":"my old sister is going to the beach with her friend"
    },
    # sudah dicek
    {
        "pattern": ["VERB", "PRON", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4],
        "example":"she went to the library"
    },
    # sudah dicek
    {
        "pattern": ["VERB", "PROPN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4],
        "example":"George went to the library"
    },
    # sudah dicek
    {
        "pattern": ["VERB", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4],
        "example":"people went to the library"
    },
    # sudah dicek
    {
        "pattern": ["VERB", "PRON", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"my sister went to the library"
    },
    # sudah -no dicek
    {
        "pattern": ["VERB", "DET", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"the sister went to the library"
    },
    # sudah -no dicek
    {
        "pattern": ["VERB", "DET", "ADJ", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"the old sister went to the library"
    },
    # sudah -no dicek
    {
        "pattern": ["VERB", "PRON", "ADJ", "NOUN", "ADP", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"my old sister went to the library"
    },
    # sudah -no dicek
    {
        "pattern": ["PROPN", "VERB", "ADV", "ADJ", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 5, 6, 3, 4],
        "example":"George came home very late last night"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "VERB", "ADV", "ADJ", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 5, 6, 3, 4],
        "example":"you came home very late last night"
    },
    # sudah dicek
    {
        "pattern": ["NOUN", "VERB", "ADV", "ADJ", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 5, 6, 3, 4],
        "example":"people came home very late last night"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "NOUN", "VERB", "ADV", "ADJ", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 6, 7, 4, 5],
        "example":"my sister came home very late last night"
    },
    # sudah dicek
    {
        "pattern": ["DET", "NOUN", "VERB", "ADV", "ADJ", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 6, 7, 4, 5],
        "example":"my sister came home very late last night"
    },
    # sudah dicek
    {
        "pattern": ["PRON", "ADJ", "NOUN", "VERB", "ADV", "ADJ", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[0, 1, 2, 3, 4, 7, 8, 5, 6],
        "example":"my old sister came home very late last night"
    },
    # sudah dicek
    # -----------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4],
        "example":"she have clean her room"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4],
        "example":"Dave have clean her room"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"my sister have clean her room"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"2 sisters have clean her room"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"the sister have clean her room"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"my old sister have clean her room"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"the old sister have clean her room"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "PRON", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"2 old sister have clean her room"
    },
    # sudah -no dicek
    # -----------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3],
        "example":"you are doing here"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3],
        "example":"Dave are doing here"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4],
        "example":"my sister are doing here"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4],
        "example":"the sister are doing here"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4],
        "example":"2 sisters are doing here"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"my old sister are doing here"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"the old sister are doing here"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"2 old sisters are doing here"
    },
    # sudah -no dicek
    # -----------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3],
        "example":"you will marry me"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3],
        "example":"Dave will marry me"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4],
        "example":"my sister will marry me"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4],
        "example":"the sister will marry me"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4],
        "example":"2 sisters will marry me"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"my old sister will marry me"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"the old sister will marry me"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "PRON"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"2 old sisters will marry me"
    },
    # sudah -no dicek
    # ------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6, 7],
        "example":"you will come to the dance with me"
    },
    {
        "pattern": ["AUX", "NOUN", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6, 7],
        "example":"Dave will come to the dance with me"
    },
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7, 8],
        "example":"my sister will come to the dance with me"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7, 8],
        "example":"the sister will come to the dance with me"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7, 8],
        "example":"2 sisters will come to the dance with me"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8, 9],
        "example":"my old sister will come to the dance with me"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8, 9],
        "example":"the old sister will come to the dance with me"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN", "ADP", "PRON"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8, 9],
        "example":"2 old sister will come to the dance with me"
    },
    # -------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6],
        "example":"we will go to cinema tonight"
    },
    {
        "pattern": ["AUX", "NOUN", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6],
        "example":"Dave will go to cinema tonight"
    },
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"my sister will go to cinema tonight"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"the sister will go to cinema tonight"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"2 sisters will go to cinema tonight"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"my old sister will go to cinema tonight"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"the old sister will go to cinema tonight"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"2 old sisters will go to cinema tonight"
    },
    # --------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"she is doing her homework now"
    },
    {
        "pattern": ["AUX", "NOUN", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"Dave is doing her homework now"
    },
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"my sister is doing her homework now"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"the sister is doing her homework now"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"2 sisters is doing her homework now"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"my old sister is doing her homework now"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"the old sister is doing her homework now"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "PRON", "NOUN", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"2 old sisters is doing her homework now"
    },
    # -----------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6],
        "example":"she is doing her homework right now"
    },
    {
        "pattern": ["AUX", "NOUN", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6],
        "example":"Dave is doing her homework right now"
    },
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"my sister is doing her homework right now"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"the sister is doing her homework right now"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"2 sisters is doing her homework right now"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"my old sister is doing her homework right now"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"the old sister is doing her homework right now"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "PRON", "NOUN", "ADV", "ADV"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"2 old sisters is doing her homework right now"
    },
    # -------------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6, 7, 8, 9],
        "example":"you have played the piano since you were a child"
    },
    {
        "pattern": ["AUX", "NOUN", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[1, 0, 2, 3, 4, 5, 6, 7, 8, 9],
        "example":"Dave have played the piano since you were a child"
    },
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10],
        "example":"my sister have played the piano since you were a child"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10],
        "example":"the sister have played the piano since you were a child"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10],
        "example":"2 sisters have played the piano since you were a child"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
        "example":"my old sister have played the piano since you were a child"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
        "example":"the old sister have played the piano since you were a child"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "DET", "NOUN", "SCONJ", "PRON", "AUX", "DET", "NOUN"],
        "message":"noun placed after determinan",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11],
        "example":"2 old sisters have played the piano since you were a child"
    },
    # --------------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3],
        "example":"he has just left"
    },
    {
        "pattern": ["AUX", "NOUN", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3],
        "example":"Dave has just left"
    },
    {
        "pattern": ["AUX", "PRON", "NOUN", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4],
        "example":"my sister has just left"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4],
        "example":"the sister has just left"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4],
        "example":"2 sisters has just left"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"my old sister has just left"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"the old sister has just left"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "ADV", "VERB"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5],
        "example":"2 old sisters has just left"
    },
    # --------------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"you have bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"Dave have bought a new car"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"my sister have bought a new car"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"the sister have bought a new car"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"2 sisters have bought a new car"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"my old sister have bought a new car"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"the old sister have bought a new car"
    },
    # sudah -no dicek
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "DET", "ADJ", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"2 old sisters have bought a new car"
    },
    # sudah -no dicek
    # -------------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4],
        "example":"you have just finished homework"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4],
        "example":"Dave have just finished homework"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"my sister have just finished homework"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"the sister have just finished homework"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"2 sisters have just finished homework"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"my old sister have just finished homework"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"the old sister have just finished homework"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "ADV", "VERB", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"2 old sisters have just finished homework"
    },
    # --------------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4],
        "example":"you will play video game"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4],
        "example":"Dave will play video game"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"my sister will play video game"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"the sister will play video game"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"2 sisters will play video game"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"my old sister will play video game"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"the old sister will play video game"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "NOUN", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"2 old sisters will play video game"
    },
    # -------------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4],
        "example":"you are going to school"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4],
        "example":"Dave are going to school"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"my sister are going to school"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"the sister are going to school"
    },
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5],
        "example":"2 sisters are going to school"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"my old sister are going to school"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"the old sister are going to school"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "PART", "VERB"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6],
        "example":"2 old sisters are going to school"
    },
    # ------------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"she have gone to the office"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"Dave have gone to the office"
    },
    # sudah dicek
    {
        "pattern": ["VERB", "PRON", "NOUN", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"my father have gone to the office"
    },
    {
        "pattern": ["VERB", "DET", "NOUN", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"the father have gone to the office"
    },
    {
        "pattern": ["VERB", "NUM", "NOUN", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"2 fathers have gone to the office"
    },
    {
        "pattern": ["VERB", "PRON", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"my old father have gone to the office"
    },
    {
        "pattern": ["VERB", "DET", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"the old father have gone to the office"
    },
    {
        "pattern": ["VERB", "NUM", "ADJ", "NOUN", "VERB", "ADP", "DET", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"2 old fathers have gone to the office"
    },
    # -----------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5, 6],
        "example":"you have not going to school yet"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5, 6],
        "example":"Dave have not going to school yet"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"my sister have not going to school yet"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"the sister have not going to school yet"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6, 7],
        "example":"2 sisters have not going to school yet"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"my old sister have not going to school yet"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"the old sister have not going to school yet"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "PART", "VERB", "ADP", "NOUN", "ADV"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7, 8],
        "example":"2 old sisters have not going to school yet"
    },
    # ----------------------------------------------------------------------------------------------------
    {
        "pattern": ["AUX", "PRON", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"you will come to my exhibition"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "NOUN", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[1, 0, 2, 3, 4, 5],
        "example":"Dave will come to my exhibition"
    },
    # sudah dicek
    {
        "pattern": ["AUX", "PRON", "NOUN", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"my sister will come to my exhibition"
    },
    {
        "pattern": ["AUX", "DET", "NOUN", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"the sister will come to my exhibition"
    },
    {
        "pattern": ["AUX", "NUM", "NOUN", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[2, 0, 1, 3, 4, 5, 6],
        "example":"2 sisters will come to my exhibition"
    },
    {
        "pattern": ["AUX", "PRON", "ADJ", "NOUN", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"my old sister will come to my exhibition"
    },
    {
        "pattern": ["AUX", "DET", "ADJ", "NOUN", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"the old sister will come to my exhibition"
    },
    {
        "pattern": ["AUX", "NUM", "ADJ", "NOUN", "VERB", "ADP", "PRON", "NOUN"],
        "message":"verb placed after already",
        "correction":[3, 0, 1, 2, 4, 5, 6, 7],
        "example":"2 old sisters will come to my exhibition"
    },
    # ----------------------------------------------------------------------------------------------------
    {
        "pattern": ["VERB", "PRON", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[1, 0, 2],
        "example":"we read book"
    },
    # sudah dicek
    {
        "pattern": ["VERB", "NOUN", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[1, 0, 2],
        "example":"Dave read book"
    },
    # sudah dicek
    {
        "pattern": ["VERB", "PRON", "NOUN", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[2, 0, 1, 3],
        "example":"my sister read book"
    },
    {
        "pattern": ["VERB", "DET", "NOUN", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[2, 0, 1, 3],
        "example":"the sister read book"
    },
    {
        "pattern": ["VERB", "NUM", "NOUN", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[2, 0, 1, 3],
        "example":"2 sisters read book"
    },
    {
        "pattern": ["VERB", "PRON", "ADJ", "NOUN", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[3, 0, 1, 2, 4],
        "example":"my old sister read book"
    },
    {
        "pattern": ["VERB", "DET", "ADJ", "NOUN", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[3, 0, 1, 2, 4],
        "example":"the old sister read book"
    },
    {
        "pattern": ["VERB", "NUM", "ADJ", "NOUN", "NOUN"],
        "message":"verb placed after pronoun",
        "correction":[3, 0, 1, 2, 4],
        "example":"2 old sisters read book"
    }
]


def grammar_checker_perfect(poss, texts3):
    #   check = 0
    for err in grammar:
        a1 = np.array(poss)
        a2 = np.array(err["pattern"])
        if np.array_equal(a1, a2) == True:
            res = [texts3[i] for i in err["correction"]]
            return res


def position_checker(poss, texts3):
    if grammar_checker_perfect(poss, texts3):
        return grammar_checker_perfect(poss, texts3)
    else:
        return texts3
