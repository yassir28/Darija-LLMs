## what can be proven?

translateration > arabic letters ?

semantics evaluation?

syntatics evaluation?

gpt4 > gpt 3.5 ?


## constructions, idioms
Since I did A year of intensive studies in Morocco I collected and translated Moroccan cultural expressions with a great deal of help from my instructor. Proverbs, expressions and idioms in dialect are great for demonstrating knowledge of the culture. If your target audience, doesn't understand Darija this is no problem. You can take a chunk out of a word count pretty quickly explaining some of these expressions.


# what could be next?
 see what's lacking in the ouput in the model's output.

# work on idioms:


# what to do
recheck papers for the idioms how they went all the way for a very specific culture or equivalence.


# How to evaluate a dialect on an LLM like gpt?


i's basically getting influenced but in a way that you treat all cases.


# how to make the paper/work systematic:
- understand the api
- we need to classify the evaluation: when do we say okay, when do we say not okay, when do we say perhaps.
- Use with not just not the roles user and system roles but other roles and dictionary (few shot) = gloassary?
- scrape the 14 idioms and play with them (qualitative descreptive work).
- I should make sure that rather than getting influenced by the empirical tries(bias), to come up with a list of all things a prompt should have.



# Evaluation:
- synsets for words
- 



# fewshot
The upgrade:

 1
- Multi-turn dialogue and single turn translation
- Fake CoT: revision


 2:
- What is the purpose of the translation? 
- Who is the intended audience for the target sentence? 
- What is the locale of the target language? 
- What is the register? 
- Is a style guide available? 
+
- Whether there will be a designated glossary?


An actual chain of tought COT


Please fulfill the following conditions when translating."+

     "The translation must contain only the lemma of the translated verb"+

     "Purpose of the translation: To study the accuracy of LLMs on Low resource languages, particularly Darija." + 

     "Target audience: Computational linguists"

would probably work better on few inputs like idioms analysis


# metrics for word similarity:

- Word Similarity Metrics: 
Methods such as cosine similarity between word embeddings (vectors representing words) from models like Word2Vec, GloVe, or BERT can be used. These models capture semantic properties of words, so similar words have similar vectors.


- WordNet-Based Similarity: 
WordNet is a lexical database for the English language that groups words into sets of synonyms (synsets) and captures various semantic relations between these sets. Libraries like NLTK in Python provide access to WordNet and functions to compute semantic similarity scores between words based on their synsets' relationships within the WordNet hierarchy. Metrics like path similarity, Wu-Palmer similarity, and Leacock-Chodorow similarity are examples of WordNet-based measures.

- Edit Distance: 
For a more syntactic comparison, edit distance (Levenshtein distance) measures how many single-character edits (insertions, deletions, substitutions) are required to change one word into another. While not a measure of semantic similarity, it's useful for evaluating spelling or typing errors and morphological similarity.


###  >> chosen here: wornet synsets, cosine?



# metrics for sentence similarity (semantic comparison)

- BLEU Score (Bilingual Evaluation Understudy): 
A standard metric for evaluating a generated text to reference texts. BLEU measures the similarity of the machine translations to one or more reference translations, considering precision of n-grams (sequences of n words).

- ROUGE Score (Recall-Oriented Understudy for Gisting Evaluation): 
Especially useful for evaluating summarization tasks, ROUGE measures overlap between the generated text and the reference texts, including n-gram overlap, word sequence overlap, and word pair overlap.

- METEOR Score (Metric for Evaluation of Translation with Explicit ORdering): 
Attempts to improve upon BLEU by considering synonyms, stemming, and paraphrase matching, as well as sequence alignment for translation evaluation. It balances precision and recall, and it's designed to address some of BLEU's shortcomings.

- TER (Translation Edit Rate): 
Measures the number of edits required to change a system output into one of the references. TER is an error metric where lower scores are better, indicating fewer modifications needed for the translation to match a reference.

- BERTScore: 
Leverages the pre-trained contextual embeddings from BERT (or other transformers) and matches words in candidate and reference sentences by cosine similarity. It's robust against paraphrases since it considers the context of words.

- ChrF (Character n-gram F-score): 
Focuses on character n-grams rather than word n-grams, which can be particularly useful for languages with rich morphology or when dealing with agglutinative languages. It's also useful for languages with less training data available.

### >> Metrics chosen: BLEU, METEOR, TER, BERTScore, ChrF (few data)



## Synsets concept
why synsets and not synonyms?
- Synsets: These are groups of synonyms that share a common meaning. Each synset represents a unique concept and includes a set of synonyms (lemmas) that are interchangeable in some context. Synsets are interconnected by various semantic relations, including hypernyms (more general concepts), hyponyms (more specific concepts), antonyms (opposites), and more.


check metrics ipynb (1)


- exit, go_out: lemmas of the synset
- v: verb, n: noun, a: adjective, s: satellite adj, r: adverb.
- 01/02..: a seperate meaning of that lemma.



## path similarity
How it work in WordNet?

The path_similarity function returns a score between 0 and 1, where 1 means the synsets are identical, and a lower score indicates less similarity.

The similarity is calculated as follows:

similarity = 1 / (path length + 1) ​
 
Path length : is the number of edges between the two synsets in the WordNet graph. 

### examples of path similarity between words to determine threshold:



#### Similarity looks right subjectively =>0.5
#### >> instances from the verbs csv file


#### >> phrasal verbs need further cleaning  from "go out" to "go_out"

# Next steps:
Can work on a different ipynb if this is not showing.
- phrasal verbs in results.cv turned into verbs with tirets 8: "_"
- cleaning to .. verbs. >> must redo the instruction for openai to more clear not including to + verb.
- applying the path similarity function on the synsets.
- checks on True percentage of correct match and draw it in a py chart with plotly.
- compare another csv containing sentences.
- evaluate with cosine similarity, words? if I have time or if I asked professor.


# how does path similarity work
ChatGPT
Path similarity is a concept used in graph theory and various applications like natural language processing (NLP) and semantic networks to measure the closeness or relatedness of two nodes in a graph. Here’s a simplified explanation of how it works:

Graph Representation: Nodes represent entities, and edges represent the relationships between these entities.

Path: A path is a sequence of nodes and edges connecting two nodes.

Path Length: The length of a path is the number of edges in the path.

Path Similarity Calculation:

Shortest Path Method: Path similarity often uses the shortest path between two nodes. The shorter the path, the higher the similarity. For instance, in a semantic network, closely related concepts will have a shorter path.
Formula: One common formula for path similarity is 1 / (1 + shortest path length). This formula ensures that similarity is higher for shorter paths.
Applications:

NLP: In WordNet (a lexical database), path similarity measures how closely two words are related based on their positions in the taxonomy.
Recommendation Systems: Path similarity can help in suggesting similar items or users.
Example:

In a simple graph where nodes A, B, and C are connected as A - B - C:
The path length between A and C is 2.
The path similarity would be 1 / (1 + 2) = 1/3.
Path similarity is useful in various fields for determining relatedness or similarity between entities represented as nodes in a graph.


# WordNet only contains "open-class words": 
nouns, verbs, adjectives, and adverbs. Thus, excluded words include determiners, prepositions, pronouns, conjunctions, and particles.

