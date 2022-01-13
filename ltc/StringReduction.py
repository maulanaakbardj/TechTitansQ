def getMinDeletions(s):
	#Since the substring contain length 1 character, so we need to remove duplicate characters 
    return len(s) - len(set(s))
