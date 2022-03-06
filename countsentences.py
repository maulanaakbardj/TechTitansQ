from collections import defaultdict
def countSentences(wordSet, sentences):
    # Write your code here
    dic = defaultdict(int)
    for s in wordSet:
		# dictionary key can't be list, so we sorted it and change it to string
        s = ''.join(sorted(s))
        dic[s] += 1
    
    res =[]
    
    for sent  in sentences:
        words = sent.split(' ')
        count = 1
        for word in words:
            k = ''.join(sorted(word))
            if k in dic:
                count *= dic[k]
        res.append(count)
    
    return res
