## Пункт В

import random
k = 3
y = []
total = 0
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

while k != 0:
  random_song = random.choice(list(my_favorite_songs_dict))
  random_length = my_favorite_songs_dict.get(random_song)
  k -= 1
  y.append(random_length)
# print(y)

for i in y:
  total += i

totalr = round(total, 2)

print("Три песни звучат", totalr, "минут")