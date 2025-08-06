from typing import Dict

from classification_agent import ClassificationAgent
from compliance_agent import ComplianceAgent



class MasterRoutingAgent:
    def __init__(self):
        self.classifier = ClassificationAgent()
        self.compliance = ComplianceAgent()

    def process_document(self, document: Dict[str, str]) -> Dict[str, str]:
        classification = self.classifier.classify(document)
        compliance = self.compliance.validate(document, classification["category"])

        return {
            "documentId": classification["documentId"],
            "category": classification["category"],
            "categoryCode": classification["categoryCode"],
            "valid": compliance["valid"],
            "reason": compliance["reason"]
        }


# 🧪 Example Usage
if __name__ == "__main__":
    documents = [
        {
            "documentId": "doc-001",
            "content": "This is the Certificate of Death for John Doe. Date of death: 2023-01-01."
        },
        {
            "documentId": "doc-002",
            "content": "Will of Jane Doe."
        },
        {
            "documentId": "doc-003",
            "content": "IRS Tax Form 1040 for John Doe."
        },
        {
            "documentId": "doc-004",
            "content": "Trust Agreement regarding Jane Doe’s estate."
        },
        {
            "documentId": "doc-005",
            "content": "Certificate of Death for John Smith."
        },
        {
            "documentId": "doc-006",
            "content": "Random note from a family member."
        }
    ]

    master_agent = MasterRoutingAgent()

    for doc in documents:
        result = master_agent.process_document(doc)
        print(result)
