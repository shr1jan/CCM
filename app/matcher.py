from fuzzywuzzy import fuzz
from elasticsearch import Elasticsearch
import logging

# Initialize Elasticsearch client (make sure Elasticsearch is running)
try:
    es = Elasticsearch("http://localhost:9200")
    if not es.ping():
        raise ValueError("Elasticsearch server not available")
except Exception as e:
    es = None
    logging.error(f"Elasticsearch connection error: {e}")

# Function to check if the citation exists in the legal corpus
def is_valid_citation(citation, corpus_index="nepali_laws"):
    """
    Validate citation using fuzzy matching and Elasticsearch.
    """
    if es is None:
        logging.error("Elasticsearch client is not initialized.")
        return False
    # Fuzzy matching score threshold (adjust as needed)
    fuzzy_threshold = 80
    try:
        # Check Elasticsearch for the exact citation match
        search_result = es.search(index=corpus_index, body={
            "query": {
                "match": {
                    "citation": citation
                }
            }
        })
        # If found in Elasticsearch, return valid
        if search_result['hits']['total']['value'] > 0:
            return True
        # Fuzzy match the citation with existing entries
        corpus_citations = [hit['_source']['citation'] for hit in search_result['hits']['hits']]
        for corp_citation in corpus_citations:
            if fuzz.partial_ratio(corp_citation, citation) > fuzzy_threshold:
                return True
        return False
    except Exception as e:
        logging.error(f"Error during citation validation: {e}")
        return False


import logging
from fuzzywuzzy import fuzz

def is_valid_citation(citation, corpus_index=None):
    """
    Checks if a citation is valid against the corpus.
    
    Args:
        citation (str): The citation to verify
        corpus_index (dict, optional): The corpus index to check against
        
    Returns:
        bool: True if citation is valid, False otherwise
    """
    # If no corpus is provided, return False (or True for testing)
    if corpus_index is None or not corpus_index:
        logging.warning("No corpus index provided for validation")
        return False
    
    # Exact match
    if citation in corpus_index:
        return True
    
    # Fuzzy match (if exact match fails)
    threshold = 90  # Minimum similarity score
    for corpus_citation in corpus_index:
        similarity = fuzz.ratio(citation.lower(), corpus_citation.lower())
        if similarity >= threshold:
            logging.info(f"Fuzzy match found: {citation} -> {corpus_citation} ({similarity}%)")
            return True
    
    logging.warning(f"Citation not found in corpus: {citation}")
    return False
