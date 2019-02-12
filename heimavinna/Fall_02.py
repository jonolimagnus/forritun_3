#jón ólafur
#12/02/19

# Copyright 2010 Google Inc.

# A. mod_sum
# Ef við söfnum saman öllum tölum undir 10
# sem 3 eða 5 gengur upp í fáum við tölurna 3,5,6,9. Summa þessara talna er 23
# Hannið fall mod_sum(n) sem tekur heiltölu n sem færibreytu
# og skilar summu allra talna undir n sem 3 eða 5 gengur upp í.
# mod_sum(10) skilar sem sagt 23.
def mod_sum(n):
    # +++your code here+++
    tala = 0
    if n //3 ==0 and n //5==0:
        return n

   



# B. remove_empty
# Hannið fall remove_empty sem hefur lista af strengjum sem færibreytu(parameters)
# Fallið á að skila sama lista nema búið er að fjalægja alla tóma strengi í listanum.
# remove_empty(['python', '', 'is', 'awesome', '']) skilar ['python', 'is', 'awesome']
def remove_empty(l):
    # +++your code here+++
   return 


# C. Snúa setningu við
# Hannið fall reverse_words(words) sem tekur streng sem parameter
# Strengurinn er aðeins ein lína(ekkert \n).
# Fallið skilar öllum orðunum réttum nema í öfugri röð.
# orðin í setningunni verða að vra aðskilin með einu bili
# Setningin 'in theory there is no difference between theory and practice'
# verður    'practice and theory between difference no is there theory in'
def reverse_words(words):
    # +++your code here+++
    return
# D. duplicates
# Hannið fall duplicates(s)sem tekur við lista af tölum eða strengjum
# og skilar lista með öllu sem kemur fyrir tvisvar í listanum(s)
# Þannig að duplicates([1337, 42, 5318008, 1337, 5318008, 5885522])
# returns [1337, 5318008]
def duplicates(s):
    # +++your code here+++
    stafur = s[0]
    if len(s) == 2:
        return [stafur]
    else:
        return []


# E. match_ends
# Hannið fall sem tekur við lista af orðum og skila fjölda orða sem er tveir eða fleiri stafir
# og byrja á sama staf og þau enda

def match_ends(words):
    # +++your code here+++
    return 


# F. front_x
# Hannið fall sem tekur við lista af orðum og skilar lista
# sem er í stafrófsröð nema hvað öll orð sem byrja á x er höfð fyrst
# Dæmi ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] 
# Skilar ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    # +++your code here+++
  return



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



def main():
    print('mod_sum')
    test(mod_sum(10), 23)
    test(mod_sum(20), 78)
    test(mod_sum(50), 543)

    print()
    print('remove_empty')
    test(
         remove_empty(['python', '', 'is', 'awesome', '']),
         ['python', 'is', 'awesome'])
    test(
         remove_empty(['', 'hello', 'world']),
         ['hello', 'world'])
    test(
         remove_empty(['learning', 'is', '', '', 'fun']),
         ['learning', 'is', 'fun'])

    print()
    print('reverse_words')
    test(
        reverse_words('hello world'),
        'world hello')
    test(
        reverse_words('python is so awesome'),
        'awesome so is python')
    test(
        reverse_words('in theory there is no difference between theory and practice'),
        'practice and theory between difference no is there theory in')

    print()
    print('duplicates')
    test(duplicates([1, 1]), [1])
    test(duplicates([1, 2, 3]), [])
    test(
         duplicates([1337, 42, 5318008, 1337, 5318008, 5885522]),
         [1337, 5318008])

    print()
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(
        front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(
        front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(
        front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


if __name__ == '__main__':
    main()
