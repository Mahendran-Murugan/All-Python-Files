def toggleCaseOfNextLetterOfVowel():
    S = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(S)):
        if (S[i] in vowels) and (i + 1 < len(S)):
            S = S[:i + 1] + S[i + 1].upper() + S[i + 2:]
    print(S)


toggleCaseOfNextLetterOfVowel()
toggleCaseOfNextLetterOfVowel()