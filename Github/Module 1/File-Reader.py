


#reads the text
f = open('file path here', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

#rewrites the text
f = open('file path here', 'w', encoding='utf-8')
the_new_text = 'new text'
f.write(the_new_text)
print(the_new_text)
f.close()

#the new text will be saved so lets change it again
f = open('file path here', 'w', encoding='utf-8')
the_new_text = 'text'
f.write(the_new_text)
print(the_new_text)
f.close()

#Shorter version of the reading code
with open('file path here', 'r', encoding='utf-8') as f:
    print(f.read())