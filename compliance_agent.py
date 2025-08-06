from typing import Dict, List

from mistral_model import DocumentClassifier



class ComplianceAgent:
    """
    Validate the Document
    """
    def __init__(self):
        self.document_classifier = DocumentClassifier(
            model_path="/home/walterschweitzer/projects/alix/mistral-7b-instruct-v0.1.Q8_0.gguf"
        )

    def validate(self, document: Dict[str, str], category: str) -> Dict[str, str]:
        result = self.document_classifier.validate_document_with_llm(document["content"], category)

        return result
      