""" Code snippet to recursively generate all-possible anagrams of a word.
    Though it says 'word', it works on any string. However words are more ideal.
"""

#Recursive function
def anagram(block):
   if (len(block) <= 2):
      permu=list()
      permu.append(block[0]+block[1])
      permu.append(block[1]+block[0])
   else:
      permu=list()
      lowerpermu=anagram(block[1:]) 			# anag(sd)
      for blocklet in lowerpermu:  			# sd, ds are blocklets
         for each in rotate(block[0],blocklet): 	# each in ['asd', 'sad', 'sda'] and ['ads', 'das', 'dsa']
            permu.append(each)
   return permu
             
#function to generate a list with 'letter' occupying all possible positions inside 'word'

def rotate(letter, word):
   rotatedlist=list()
   for i in range(len(word)+1):
      rotatedlist.append(word[:i]+letter+word[i:])
   return rotatedlist

#main function         
def main():
   word=raw_input('Enter the word to be anagrammed: ')	#for example: 'asd'
   print "\nAnagrams:" 
   for anagrammed_word in anagram(word):
      print anagrammed_word
   
if __name__ == '__main__':
    main()
