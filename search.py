import json
from collections import defaultdict
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def extract_sentences(text):
    return sent_tokenize(text)

def semantic_search(query, data, top_n=5):
    sentences = [sentence for document in data.values() for sentence in extract_sentences(document)]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    query_vector = tfidf_vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    related_indices = cosine_similarities.argsort()[::-1]
    top_related_indices = related_indices[:top_n]
    top_related_sentences = [sentences[index] for index in top_related_indices]
    return top_related_sentences

def main():
    # Load data from JSON file
    data = load_data('final_all_cases.json')
    
    # Perform semantic search based on keyword
    keyword = input("Enter your keyword: ")
    relevant_sentences = semantic_search(keyword, data)
    
    # Print relevant sentences
    print("\nRelevant sentences:")
    for i, sentence in enumerate(relevant_sentences, 1):
        print(f"{i}. {sentence}")

if __name__ == "__main__":
    main()
