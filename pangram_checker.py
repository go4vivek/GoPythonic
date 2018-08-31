'''
Author:      Vivek Srivastava
Description: A pangram is a sentence that contains all the letters of the English alphabet at least once.
For example: The quick brown fox jumps over the lazy dog.

'''

def pangram_checker(s):
  flag="False"
  alp_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  low_str=s.lower().replace(',','').replace('.','').replace('!','')
  for alp in alp_list:
    if alp in low_str:
      flag="True"
    else:
      flag="False"
  if flag=="True":
    print("Sentence- \"%s\" : is a Pangram Sentence" % (s))

if __name__=="__main__":
  pangram_checker("The quick brown fox, jumps over the lazy dog!.")
