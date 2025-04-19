def rewrite_sentence(sentence, status):
    """
    Rewrites sentences containing unverified citations.
    
    Args:
        sentence (str): The sentence to potentially rewrite
        status (str): 'verified' or 'unverified'
        
    Returns:
        str: The original or rewritten sentence
    """
    if status == "unverified":
        # Extract citations from the sentence
        from app.extractor import extract_citations
        citations = extract_citations(sentence)
        
        # Replace each citation with a generic phrase
        rewritten = sentence
        for citation in citations:
            rewritten = rewritten.replace(citation, "the relevant legal provision")
        return rewritten
    return sentence
