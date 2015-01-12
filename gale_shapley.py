import copy
 
guyprefers = {
 'frank':  ['kate', 'mary', 'rhea', 'jill'],
 'dennis':  ['mary', 'jill', 'rhea', 'kate'],
 'mac':  ['kate', 'rhea', 'jill', 'mary'],
 'charlie':  ['rhea', 'mary', 'kate', 'jill']}
galprefers = {
 'rhea':  ['frank', 'mac', 'dennis', 'charlie'],
 'mary':  ['mac', 'charlie', 'dennis', 'frank'],
 'kate': ['dennis', 'mac', 'charlie', 'frank'],
 'jill':  ['charlie', 'dennis', 'frank', 'mac']}
 
guys = sorted(guyprefers.keys())
gals = sorted(galprefers.keys())
 
 
# def check(engaged):
#     inverseengaged = dict((v,k) for k,v in engaged.items())
#     for she, he in engaged.items():
#         shelikes = galprefers[she]
#         shelikesbetter = shelikes[:shelikes.index(he)]
#         helikes = guyprefers[he]
#         helikesbetter = helikes[:helikes.index(she)]
#         for guy in shelikesbetter:
#             guysgirl = inverseengaged[guy]
#             guylikes = guyprefers[guy]
#             if guylikes.index(guysgirl) > guylikes.index(she):
#                 print("%s and %s like each other better than "
#                       "their present partners: %s and %s, respectively"
#                       % (she, guy, he, guysgirl))
#                 return False
#         for gal in helikesbetter:
#             girlsguy = engaged[gal]
#             gallikes = galprefers[gal]
#             if gallikes.index(girlsguy) > gallikes.index(he):
#                 print("%s and %s like each other better than "
#                       "their present partners: %s and %s, respectively"
#                       % (he, gal, she, girlsguy))
#                 return False
#     return True
 
def matchmaker():
    guysfree = guys[:]
    engaged  = {}
    # guyprefers2 = copy.deepcopy(guyprefers)
    # galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
            print("  %s and %s" % (guy, gal))
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged
 
 
print('\nEngagements:')
engaged = matchmaker()
 
print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))

# print()
# print('Engagement stability check PASSED'
#       if check(engaged) else 'Engagement stability check FAILED')
 
# print('\n\nSwapping two fiances to introduce an error')
# engaged[gals[0]], engaged[gals[1]] = engaged[gals[1]], engaged[gals[0]]
# for gal in gals[:2]:
#     print('  %s is now engaged to %s' % (gal, engaged[gal]))
# print()
# print('Engagement stability check PASSED'
#       if check(engaged) else 'Engagement stability check FAILED')