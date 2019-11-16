# letterboxed.py
This is a program designed to find a solution to the Letterboxed game on the NYTimes website: https://www.nytimes.com/puzzles/letter-boxed

This program is designed to solve a the letterboxed puzzle game from the NYTimes website in 2 words. If it can't solve the puzzle in 2 words, it will try to solve it in 3.

The game works as follows:
12 letters are placed on the sides of a square, 3 to each side, and the player must try to form words by connecting letters.
The game is done when the player has used all of the letters on the outside of the box to form words.

Restrictions:
Letters from the same side of the box cannot be used next to one another in the same word. For Example: if ['M', 'X', 'A'] are on the same side of a box, The player cannot form the word 'MARK'. They could form the word 'AIM' assuming 'I' is available on another side.
While the first word can begin with any letter, all other words must begin with the last letter of the words before them. For Example: if the first word is 'MARK', the second word must begin with a 'K'.

Right now the program works, but there are a couple of issues it may have.
1. I may not be using the exact list of words the NYTimes finds acceptable. So far this has meant that the program will occasionally produce solutions with proper nouns that the puzzle will not accept. I don't really care about this bug, however.
2. The program runs very slowly owing to the way I eliminate words that violate the above conditions. I find it very hard to run loops that eliminate items in a list using relatively complicated conditions like the ones above. If anyone could point me to a better way to perform this task, it would help me with other projects.

SAMPLE BOX:

  ---V---L---I---
  
 |.................|
 
 N...............G
 
 |.................|
 
 H...............E
 
 |.................|
 
 R...............X
 
 |.................|
 
 ---M---W---O---

#Thanks and enjoy! Any feedback is welcome.
