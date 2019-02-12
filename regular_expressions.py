#jon olafur
#æfingaverkefni regular expressions
import re

#lidur 1
#athuga hvort strengur inniheldur bara tölustafi og s i enda
setning = "þessi setings"

if re.search("s$", setning):
    print("s er í enda setninganar")
else:
    print("s er ekki í enda setningar")
