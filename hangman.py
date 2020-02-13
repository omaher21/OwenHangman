from __future__ import print_function
 
lives = 6
word = ""
updatedSpaces = []
letter = ""
  
def check():
   ''' find the index of the word and replace it with the correct index from the list'''
   global word
   global updatedSpaces
   global lives
   lives = 6
   if letter in word:
      i = (word.find(letter))
      del (updatedSpaces[i])
      updatedSpaces.insert(i,letter)
      if i != len(word)-1:
         e = word.find(letter, i+1, len(word)+ 1)
         if e != -1:
            del (updatedSpaces[e])
            updatedSpaces.insert(e,letter)
            if e != len(word)-1:
               a = word.find(letter, e+1, len(word)+1)
               if a != -1:
                  del (updatedSpaces[a])
                  updatedSpaces.insert(a,letter)
            else:
               won()
      else:
         won()
      
   if letter not in word:
       print ('Sorry not the right letter, try again')
       lives-=1
       print ('You have',lives, 'lives left')
       won()
   if word in word:
       won()

main()
 
 
 
