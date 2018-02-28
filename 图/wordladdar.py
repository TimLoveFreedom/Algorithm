'''

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence frombeginWord toendWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note thatbeginWord isnot a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''
import queue

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

q=[[beginWord,1]]  #队列用
while q:
    ele,steps=q.pop(0)
    for i in range(len(ele)):
        left=ele[:i]
        right=ele[i+1:]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if ele[i]!=c:
                newstr=left+c+right  #替换一个字符后的字符串
                if newstr in wordList:
                    if newstr==endWord:
                        print(steps+1)

                    else:
                        q.append([newstr,steps+1])
                        wordList.remove(newstr)
