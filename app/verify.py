import logging
from app.extractor import extract_citations
from app.matcher import is_valid_citation
from app.rewriter import rewrite_sentence
import re

# Configure logging
logging.basicConfig(level=logging.INFO)

def verify_citation(text):
    try:
        # Extract citations from the text
        citations = extract_citations(text)
        logging.info(f"Extracted citations: {citations}")

        if not citations:
            logging.warning("No citations found in the text.")
            return {"status": "No citations found"}

        # Verify each citation
        results = {}
        for citation in citations:
            is_valid = is_valid_citation(citation)
            results[citation] = "Verified" if is_valid else "Misrepresented"
        return results
    except Exception as e:
        logging.error(f"Error verifying citation: {str(e)}")
        return {"status": "Error", "message": str(e)}

def verify_output(text, corpus_index):
    """
    Verifies legal citations in AI-generated text and rewrites unverified citations.
    
    Args:
        text (str): The AI-generated text to verify
        corpus_index (dict): The legal corpus index to check against
        
    Returns:
        str: The cleaned/verified text
    """
    logging.info("Starting verification of AI output")
    
    # Extract all citations
    citations = extract_citations(text)
    
    if not citations:
        logging.info("No citations found in text")
        return text
    
    # Split text into sentences (simple split by period for now)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Process each sentence
    cleaned_sentences = []
    for sentence in sentences:
        # Check if sentence contains any citation
        sentence_citations = [c for c in citations if c in sentence]
        
        if not sentence_citations:
            cleaned_sentences.append(sentence)
            continue
            
        # Verify citations in this sentence
        all_verified = True
        for citation in sentence_citations:
            # Use the corpus_index to verify
            is_valid = is_valid_citation(citation, corpus_index)
            if not is_valid:
                all_verified = False
                break
        
        # Rewrite sentence if needed
        status = "verified" if all_verified else "unverified"
        cleaned_sentence = rewrite_sentence(sentence, status)
        cleaned_sentences.append(cleaned_sentence)
    
    # Join sentences back together
    cleaned_text = " ".join(cleaned_sentences)
    logging.info("Verification complete")
    
    return cleaned_text

# Example usage
if __name__ == "__main__":
    text = "This is a reference to Section 88(1)(a), which is cited correctly."
    verification_result = verify_citation(text)
    print(verification_result)
