print("Alien Translate (v1.0.1)")
AlienDictionary = {"we": "vorag", "come": "thang", "in": "zon", "peace": "argh", "hello": "kodar", "can": "znak", "i": "az", "borrow": "liftit", "some": "zum", "rocket": "upgoman", "fuel": "kakboom", "please": "selpin", "don't": "baaaaaaaaarn", "shoot": "flabil", "welcome": "unkip", "our": "mandig", "new": "brang", "alien": "marangin", "overlords": "bap", "earth": "Picom", "planet": "bumpis", "hello": "wregaxez", "toilet": "tarrg", "came": "cig", "a": "iv", "an": "ivin", "to": "tiik", "lawn": "lavyurn", "cut": "tivun", "lawnmower": "lavyurnamin", "mover": "min", "earmuffs": "vroomaprow"}
EnglishPhrase = input("Please enter something in English to translate: ")
EnglishWords = EnglishPhrase.lower().split()
AlienWords = []
for word in EnglishWords:
    if word in AlienDictionary:
        AlienWords.append(AlienDictionary[word])
    else:
        AlienWords.append(word)
print("In Alien, say:", " ".join(AlienWords))
