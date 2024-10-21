meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    anlam = meme_dict[word]
    print(anlam)
else:
    print("Yazdığınız kelime sözlükte bulunmamaktadır.")