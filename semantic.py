import spacy
nlp = spacy.load('en_core_web_md')


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print(" ")
# Highest similarity between cat and monkey as they are both animals.
# Second highet similarity between banana and monkey as monkeys are known to eat bananas.
# Lowest similarity between cat and banana, there is no obvious link between the 2 words.

# My example
word1 = nlp("train")
word2 = nlp("sea")
word3 = nlp("boat")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print(" ")
# Lowest similarity between train and sea as no real correlation.
# Highest similarity between sea and boat as boats can be found on the sea.
# Second highest similarity between train and sea as both modes of transport.

# Running with en_core_web_sm
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(" ")

# This model gives the following warning: UserWarning: 
# [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. 
# This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
# You can always add your own word vectors, or use one of the larger models instead if available.

# The similarity values given are also much higher.

nlp = spacy.load('en_core_web_md')
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


print(" ")

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my cat in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)