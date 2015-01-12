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
 
def matchmaker():
    guysfree = guys[:]
    engaged  = {}

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
            # Guy proposes
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