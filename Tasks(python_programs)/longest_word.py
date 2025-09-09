sentence = "Python makes coding easier and fun"
words = sentence.split()
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)