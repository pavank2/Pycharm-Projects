#Given a string s and a dictionary of strings wordDict, return true
# if s can be segmented into a space-separated sequence of one or more dictionary words.

#Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Not working
def breakWord(s,wordDict):
    flag = []
    slist = list(s)
    for word in wordDict:

      if s.rfind(word) >= 0:
          i = s.rfind(word) # start index
          print(i)
          end = i + len(word)
          while  i < end:
              flag[i] = 1
              i += 1
          print(flag)



s = "leetcodeleet"
wordDict = ["code","leet","ten"]
breakWord(s,wordDict)