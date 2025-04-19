import os
import json
import logging

# Corpus configuration
CORPUS_PATH = "path/to/your/legal_corpus"
ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_INDEX = "legal_corpus"

# Verification settings
FUZZY_MATCH_THRESHOLD = 90
USE_ELASTICSEARCH = False  # Set to True to use Elasticsearch instead of local corpus

# Add to your existing config.py
TEST_MODE = False  # Set to True for testing

# Update your load_corpus function
def load_corpus():
    """
    Loads the legal corpus from the configured source
    
    Returns:
        dict: A dictionary of citations and their content
    """
    corpus = {}
    
    if USE_ELASTICSEARCH:
        # Placeholder for Elasticsearch integration
        logging.info("Elasticsearch corpus loading not implemented yet")
        return {}
    
    # Load from local file
    try:
        if os.path.exists(CORPUS_PATH):
            if CORPUS_PATH.endswith('.json'):
                with open(CORPUS_PATH, 'r', encoding='utf-8') as f:
                    corpus = json.load(f)
            else:
                # Simple directory-based corpus
                for filename in os.listdir(CORPUS_PATH):
                    if filename.endswith('.txt'):
                        citation_key = filename.replace('.txt', '')
                        corpus[citation_key] = True
        else:
            logging.warning(f"Corpus path not found: {CORPUS_PATH}")
            # For testing, create a sample corpus
            if TEST_MODE:
                return {"Section 88": True, "Article 45": True, "National Civil Code 2074": True}
            
            # For testing, create a sample corpus
            corpus = {"Section 88": True, "Article 45": True, "National Civil Code 2074": True}
    except Exception as e:
        logging.error(f"Error loading corpus: {str(e)}")
        corpus = {}
    
    logging.info(f"Loaded corpus with {len(corpus)} citations")
    return corpus
