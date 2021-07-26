from _text import text
import data
import numpy as np
import random


def make_pairs(txt):
    for i in range(len(txt)-1):
        yield txt[i], txt[i+1]


pairs = make_pairs(text)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = np.random.choice(text)
while first_word.islower():
    first_word = np.random.choice(text)

chain = [first_word]
cnt = random.randrange(4, 7, 1)
for i in range(30):
    chain.append(np.random.choice(word_dict[chain[-1]]))
    """if np.random.choice(word_dict[chain[-1]]).count("!") >0:
        chain.append('!')
        cnt -= 1
        break
    if np.random.choice(word_dict[chain[-1]]).count(".") >0:
        chain.append('.')
        cnt -= 1
        break"""


def generate(pers, txt):
    final = "Уважаем"
    if pers.gender == "m":
        final += "ый "
    else:
        final += "ая "
    final += pers.name + ", поздравляю Вас с "
    if pers.is_anniversary():
        final += "Юбилеем! "
    else:
        final += "Днём Рождения! "
    final += ' '.join(chain)

    return final


print(generate(data.Yubilyar, text))
