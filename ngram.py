import nltk
import random


ngram_dict = {}

def create_trigram_dict(corpus):
    n = 3
    ngrams = nltk.ngrams(corpus, n)
    
    for grams in ngrams:
        dict_key = grams[:-1][0] + " " + grams[:-1][1]
        if dict_key in ngram_dict:
            ngram_dict[dict_key].append(grams[-1])
        else:
            ngram_dict[dict_key] = []
            ngram_dict[dict_key].append(grams[-1])
            
def generate_trigram(seed, samples = 15):
    output = seed
    for _ in range(samples):
        try:
            new_sample = random.choice(ngram_dict[seed])
        except:
            return output
        output += " " + new_sample
        seed = seed.split(" ")[1] + " " + new_sample
        
    return output

word_corpus = 'am I a gram or am I a markov chain am I a gram only ... maybe I am both'
ngram_dict = {}
create_trigram_dict(word_corpus.split(" "))
ngram_dict

print(generate_trigram("chain am", 30))

