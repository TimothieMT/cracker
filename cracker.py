password_hash = "5e6757e6529d863099dd9939b3bb88f398ec390defeafe141e77f9901ca651bd"

import hashlib

extra_chars = "!$%&/()=?"

with open("assets/dictionary.txt", "r") as file:
    for line in file:
        word = line.strip()

        for char in extra_chars:
            for char2 in extra_chars:
                w = word + char + char2

                if hashlib.sha256(w.encode()).hexdigest() == password_hash:
                    print(w)

print("Programm fertig!")
