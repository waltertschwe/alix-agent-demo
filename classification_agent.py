from typing import Dict

from mistral_model import DocumentClassifier

class ClassificationAgent:
    """
    Classification Agent
    """
    def __init__(self):
        self.category_to_code = {
            "Death Certificate": "01.0000-50",
            "Will or Trust": "02.0300-50",
            "Property Deed": "03.0090-00",
            "Financial Statement": "04.5000-00",
            "Tax Document": "05.5000-70",
            "Miscellaneous": "00.0000-00",
        }

        self.document_classifier = DocumentClassifier(
            model_path="/home/walterschweitzer/projects/alix/mistral-7b-instruct-v0.1.Q8_0.gguf"
        )

    def classify(self, document: Dict[str, str]) -> Dict[str, str]:
        content = document["content"]
        category = self.document_classifier.classify(content)

        # Fallback for unrecognized categories
        category_code = self.category_to_code.get(category, "00.0000-00")
        normalized_category = category if category in self.category_to_code else "Miscellaneous"

        return {
            "documentId": document["documentId"],
            "category": normalized_category,
            "categoryCode": category_code
        }
