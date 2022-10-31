# import re
# text2 = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
regex = r"(?<![A-Z][a-z]\.)(?<=\.|\?)\s(?<!\w.\w.)"
# matches = re.split(regex, text2)

# print(matches[0])
