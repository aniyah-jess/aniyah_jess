# A function for next movie suggestion

import spacy
nlp = spacy.load('en_core_web_md')

movie_watched = """Planet Hulk: Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati 
trick Hulk into a shuttle and launch him into space to a planet 
where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# storing movie names and descriptions in separate lists
movie_descrip = []
movie_title = []
with open("movies.txt", "r") as f:
    for line in f:
        split = line.split(":")
        movie_title.append(split[0])
        movie_descrip.append(split[1])

# comparing the movie watched with the other movie descriptions
# storing all similarity values in a list
comparisons = []
movie_watched = nlp(movie_watched)
for x in movie_descrip:
    similarity = nlp(x).similarity(movie_watched)
    comparisons.append(similarity)

# finding the index of the highest similarity 
x = comparisons.index(max(comparisons))

# matching the index of the most similar description with the movie name and printing
print(f"Based on previous viewing, you should watch {movie_title[x]}next.")
print("Description: " + movie_descrip[x])