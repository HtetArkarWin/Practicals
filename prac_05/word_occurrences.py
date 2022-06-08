word_file=open("words.txt","r")
text=word_file.read()

print("Text:",text)

words=text.split()

word_to_count={}
for word in words:
    if word in word_to_count:
        word_to_count[word]+=1
    else:
        word_to_count[word]=1

sorted_words=[]

max_char_count=0
for w in word_to_count:
    sorted_words.append(w)
    if len(w)>max_char_count:
        max_char_count=len(w)

sorted_words.sort()
for word in sorted_words:
    print(f"{word:<{max_char_count}}: {word_to_count[word]:>}")