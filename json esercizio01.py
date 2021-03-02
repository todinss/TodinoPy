import json
data = {'libreria': [{'titolo': 'Mirum Iter', 'casa editrice': 'Mondadori', 'materia': 'latino'},
                     {'titolo': 'Performer B1', 'casa editrice': 'Zanichelli', 'materia': 'inglese'},
                     {'titolo': 'Amaldi per i licei scentifici', 'casa editrice': 'Zanichelli', 'materia': 'fisica'},
                     {'titolo': 'Matematica in blu', 'casa editrice': 'Zanichelli', 'materia': 'matematica'},
                     {'titolo': 'Leggere a colori', 'casa editrice': 'Loescher', 'materia': 'italiano'},
                     {'titolo': 'Le pietre parlano', 'casa editrice': 'Loescher', 'materia': 'geostoria'},
                     {'titolo': 'Itinerario di arte', 'casa editrice': 'Zanichelli', 'materia': 'arte'},
                     {'titolo': 'La nuova biologia', 'casa editrice': 'Zanichelli', 'materia': 'scienze'},
                     {'titolo': 'Parola chiave', 'casa editrice': 'Loescher', 'materia': 'grammatica'},
                     {'titolo': 'I promessi sposi', 'casa editrice': 'Loescher', 'materia': 'letteratura'}]}
with open("output.json", "w") as outfile:
    json.dump(data, outfile)
