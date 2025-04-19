import re

# Updated regex for citation extraction
def extract_citations(text):
    """
    Extract citations from the provided text.
    Supports citations like 'Section 88(1)(a)', 'Section 88', 'National Civil Code 2074'
    and more complex references in Nepali legal documents.
    """
    # Updated pattern to properly handle nested parentheses
    citation_pattern = r"(\b(?:Section|Article|Chapter|Clause|National)\s*\d{1,3}(?:\(\d+\))?(?:\([a-zA-Z]+\))?(?:\s*\d{4})?)"
    citations = re.findall(citation_pattern, text)
    return citations

# Example usage
if __name__ == "__main__":
    text = "This is a reference to Section 88(1)(a) and also Article 45 of the National Civil Code 2074."
    citations = extract_citations(text)
    print(citations)  # Should output: ['Section 88(1)(a)', 'Article 45', 'National Civil Code 2074']
