def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if(sorted_word in anagrams):
           anagrams[sorted_word].append(word)
        else:
               anagrams[sorted_word]=[word]
    return list(anagrams.values())

test_cases=[
    ["eat","tea","tan","ate","nat","bat"],
    ]
for test_case in test_cases:
    print("output:",group_anagrams(test_case))
