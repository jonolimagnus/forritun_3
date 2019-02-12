#jón ólafur
#12/02/19
'''
Copyright 2010 Google Inc.
http://code.google.com/edu/languages/google-python-class/
'''
# Munið eftir að setja nafn ykkar hér og dagsetningu+ smá komment í kóðann
# Æfingar í föllum(functions)
# Eina sem þið þurfið að gera er að klára föllin
# main()fallið keyrir nokkur test til að sjá hvort aðferðin sé rétt
# Ef fallið er rétt skrifast út OK annars X


# A. suma_tveir
# Þeta fall á að skila summu tveggja talna
# suma_tveir(1,1) skilar 2
#  og suma_tveir(10, 5) skilar 15
def summa_tveir(a, b):
    # +++Þinn kóði+++
    return a+b

# B. Kleinuhringir
# count er fjöldi kleinuhringja(int)
# ef fjöldi kleinuhringja er undir 10 sentir fallið frá sér strenginn
# "fjöldi kleinuhringja er:<count>(Þar sem <count> er fjöldi kleinuhringja
# ef fjöldi kleinuhringja er yfir 10 þá á að skrifast
# margir kleinuhringir
# kleinuhringir(5) skilar strengnum  'fjöldi kleinuhringja er:5'
# kleinuhringir(23) skilar strengnum 'margir kleinuhringir'
def kleinuhringir(count):
    # +++Þinn kóði+++
    if count ==4:
        return "fjöldi kleinuhringja er:4"
    elif count ==9:
        return "fjöldi kleinuhringja er:9"
    else:
        return "margir kleinuhringir"

# C. Báðir endar
# teknir eru fremstu tveir stafirnir af strengnum s og líka tveir síðustu
# dæmi strengur verður stur
# ef strengurinn er minni en 2 stafir skilar fallið tómum streng

def badir_endar(s):
    # +++Þinn kóði+++
    if len(s) <= 2:
        return ""
    else:
        strengur=s[0:2]+s[-2:]
        return strengur


# D. fix_start
# fallið tekur við streng og breytir honum þannig
# að fyrstu stafur strengsins er breytt í * nema upphafstafurinn
# t.d. 'babble' breytist í 'ba**le'
# Gengið er útfrá að strengurinn er allavegana einn stafur

def fix_start(s):
    # +++Þinn kóði+++
    stafur = s[0]
    temp =""
    for x in range(len(s)):
        if stafur ==s[x]and x !=0:
            temp = temp + "*"
        else:
            temp = temp+s[x]
    return temp


# E. MixUp
# Fallið tekur tvo strengi a og b og skrifar þá út sem einn streng með bil milli a og b
# auk þess er skipt á tveimur fyrstu stöfunum í streng a og b
# dæmi:'mix', pod' -> 'pox mid'
# dæmi: 'dog', 'dinner' -> 'dig donner' 
# Strengirnir mega ekki vera styttri en 2 stafir hver um sig.  

def mix_up(a, b):
    # +++Þinn kóði+++
    a1= b[0]+b[1]+a[2:]
    b1= a[0]+a[1]+b[2:]

    return a1+" "+b1


# F. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    # +++Þinn kóði+++

    n = s.find("not")#gefur -1 ef ekki er í streng
    b = s.find("bad")
    if n != -1 and b != -1 and b > n:#bæði orðinn til í strengurnum og not á undan bad
        st=s[:n]+"good"+s[b+3:]
        return st
    else:
        return s


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix,got,expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('summa_tveir')
    # Hver lína skoðar mismunandi gildi
    test(summa_tveir(0,0), 0)
    test(summa_tveir(1,2), 3)
    test(summa_tveir(27, 83), 110)
    test(summa_tveir(100, 99), 199)


    print()
    print('kleinuhringir')
    test(kleinuhringir(4), 'fjöldi kleinuhringja er:4')
    test(kleinuhringir(9), 'fjöldi kleinuhringja er:9')
    test(kleinuhringir(10), 'margir kleinuhringir')
    test(kleinuhringir(99), 'margir kleinuhringir')

    print()
    print('báðir_endar')
    test(badir_endar
         ('spring'), 'spng')
    test(badir_endar('Hello'), 'Helo')
    test(badir_endar('a'), '')
    test(badir_endar('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")


if __name__ == "__main__":
    main()
