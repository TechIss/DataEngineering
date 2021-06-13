import json

with open("gras_blok.json") as x:
    blok = json.load(x)

blok['block']['snow'] = True
blok['block']['coordinates']['y'] += 66
blok['block']['coordinates']['z'] *= 3
print(blok)

with open("sneeuw_blok.json", 'w') as outfile:
    json.dump(blok, outfile)
