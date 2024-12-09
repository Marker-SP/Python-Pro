meme_dict = {
            "CRINGE": "Weird or embarassing",
            "LOL": "Funny",
            "ROFL": "Rolling On Floor Laughing",
            "SHEESH": "Agree",
            "CREEPY": "Scary",
            "AGGRO": "Angry/Annoyed"
            }

word = input("Write a word that you dont know (with capital letters): ")

if word in meme_dict.keys():
    meaning = meme_dict[word]
    print(meaning)
else:
    print("The word you entered does not exist in the dictionary.")