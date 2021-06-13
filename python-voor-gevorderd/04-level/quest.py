bezittingen = {
    'goud' : 500,
    'buidel' : ['touw', 'vuursteen', 'zakmes'],
    'rugzak' : ['panfluit', 'dolk', 'slaapzak','appel']
}

bezittingen['zilver'] = 12
bezittingen.update({ 'buidel': ['touw', 'vuursteen']})
rugzak = bezittingen['rugzak']
rugzak.sort()

print(bezittingen)
