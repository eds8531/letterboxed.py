#This program is designed to solve a the letterboxed puzzle game from the NYTimes website in 2 words. If it can't solve the puzzle in 2 words, it will try to solve it in 3.
#The game works as follows:
#12 letters are place on the sides of a square and the player must try to form words by connecting letters.
#The game is done when the player has used all of the letters on the outside of the box to form words.
#Restrictions:
#Letters from the same side of the box cannot be used next to one another in the same word. For Example: if ['M', 'X', 'A'] are on the same side of a box, The player cannot form the word 'MARK'. They could form the word 'AIM' assuming 'I' is available on another side.
#While the first word can begin with any letter, all other words must begin with the last letter of the words before them. For Example: if the first word is 'MARK', the second word must begin with a 'K'.

#Right now the program works, but there are a couple of issues it may have.
#1. I may not be using the exact list of words the NYTimes finds acceptable. So far this has meant that my porgram will occasionally produce solutions with proper names that the puzzle will not accept. I don't really care about this bug, however.
#2. The program runs very slow owing to the way I eliminate words that violate the above conditions. I find it very hard to run loops that eliminate items in a list using relatively complicated conditions like the ones above. If anyone could point me to a better way to perform this task, it would help me with other projects.

#Thanks and enjoy! Any feedback is welcome.

import pickle

#This part takes in the letters from the letterbox puts them in a list and also divides them into sublist 1 - 4 based on what side they are on.

letters = input('Enter Letters> ')

letters = letters.upper()
letters = list(letters)

letters1 = letters[:3]
letters2 = letters[3:6]
letters3 = letters[6:9]
letters4 = letters[9:]

#This part loads a list of all English words.

with open('objs.pkl', 'rb') as f:
    words = pickle.load(f)

words1 = []

words = words[0]

#This part eliminates all the words where the first letter isn't in the letters list.
#ELiminating words based on their first letter would be handled by the next step, but it runs in O(n) time and I think the next step is O(n**2), so I thought this would make things run fatser.

for word in words:
    if word[0] not in letters:
        words.remove(word)

#This part eliminates all words with any letters not in the letters list.
#I'm certain this part is taking way too long.
#The function loads words with letters not in the letters list into the words1 list to be removed later.
#The problem is it loads words with non-letters-list letters into the words1 list for each letter not in the list.
#This means most words are loaded several times no doubt slowing the program down substantially.
#I think there's a way to do this like the above part, but I'm not sure how.

def elim():
    for word in words:
        for j in range (0, len(word)):
            if word[j] not in letters:
                words1.append(word)

elim()

for word in words1:
    if word in words:
        words.remove(word)

words1 = []

#This part removes words with 2 adjacent letters that show up in the same sublist.
#This part is ugly, but I think the separate functions make the program run faster by eliminting bad words in batches, so the program has to scan fewer words in each iteration.

for w in range(0, len(words)):
    for i in range(1, len(words[w])):
        if words[w][i] in letters1:
            if words[w][i-1] in letters1:
                words1.append(words[w])

for word in words1:
    if word in words:
        words.remove(word)

words1 = []

for w in range(0, len(words)):
    for i in range(1, len(words[w])):
        if words[w][i] in letters2:
            if words[w][i-1] in letters2:
                words1.append(words[w])

for word in words1:
    if word in words:
        words.remove(word)

words1 = []

for w in range(0, len(words)):
    for i in range(1, len(words[w])):
        if words[w][i] in letters3:
            if words[w][i-1] in letters3:
                words1.append(words[w])

for word in words1:
    if word in words:
        words.remove(word)

words1 = []

for w in range(0, len(words)):
    for i in range(1, len(words[w])):
        if words[w][i] in letters4:
            if words[w][i-1] in letters4:
                words1.append(words[w])

for word in words1:
    if word in words:
        words.remove(word)

#This part determines if the first word ends with the same letter as the second word begins with
#and if the two words use all the letters in the letters list.
#I actually think using the if len(set(comb1)) == 12 condition was pretty clever.

c = 0

for word in words:
    for word2 in words:
        if word2[0] == word[-1]:
            comb = word + word2
            comb1 = list(comb)
            if len(set(comb1)) == 12:
                
                print(word + ' ' + word2)
                c += 1

if c == 0:
    for word in words:
        for word2 in words:
            for word3 in words:
                if word2[0] == word[-1]:
                    if word3[0] == word2[-1]:
                        comb1 = list(word + word2 + word3)
                        if len(set(comb1)) == 12:
                            print(word + ' ' + word2 + ' ' + word3)
