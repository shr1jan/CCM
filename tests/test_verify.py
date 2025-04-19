import pytest
from app.verify import verify_output, verify_citation
from app.extractor import extract_citations

def test_extract_citations():
    text = "This is a reference to Section 88(1)(a) and also Article 45 of the National Civil Code 2074."
    citations = extract_citations(text)
    assert "Section 88(1)(a)" in citations
    assert "Article 45" in citations

def test_verify_citation():
    text = "According to Section 88, this is allowed."
    result = verify_citation(text)
    assert isinstance(result, dict)
    assert "Section 88" in result

# Updated to use the test_corpus fixture
def test_verify_output_with_valid_citation(test_corpus):
    text = "According to Section 88, this is allowed."
    result = verify_output(text, test_corpus)
    assert "Section 88" in result  # Citation should remain unchanged

def test_verify_output_with_invalid_citation(test_corpus):
    text = "According to Section 999, this is allowed."
    result = verify_output(text, test_corpus)
    assert "Section 999" not in result  # Citation should be rewritten
    assert "the relevant legal provision" in result

def test_verify_output_no_citations(test_corpus):
    text = "This text has no legal citations."
    result = verify_output(text, test_corpus)
    assert result == text  # Text should remain unchanged

# New test using the sample_texts fixture
def test_with_sample_texts(test_corpus, sample_texts):
    # Test with valid citation
    result = verify_output(sample_texts["with_valid"], test_corpus)
    assert "Section 88" in result
    
    # Test with invalid citation
    result = verify_output(sample_texts["with_invalid"], test_corpus)
    assert "Section 999" not in result
    assert "the relevant legal provision" in result
    
    # Test with no citations
    result = verify_output(sample_texts["without"], test_corpus)
    assert result == sample_texts["without"]
