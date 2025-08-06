# alix-agent-demo
# 🧠 Estate Document Classification & Compliance Agent

This Python application provides a modular system to **classify** and **validate** estate-related documents using AI-driven logic or rule-based checks.

## 🔍 What It Does

1. **Classifies** incoming documents into categories like:
   - **Death Certificate**
   - **Will or Trust**
   - **Other**
2. **Validates** content based on strict compliance rules:
   - ✅ *Death Certificate* must contain both `"Certificate of Death"` **and** `"Date of death"`
   - ✅ *Will or Trust* must contain either `"Last Will and Testament"` **or** `"Trust Agreement"`
   - ✅ *Other* documents are always considered valid
3. **Returns** a structured result with classification and validation status.

## 🏗 Architecture

- **`MasterRoutingAgent`**  
  Coordinates classification and validation steps.
  
- **`ClassificationAgent`**  
  Determines the document category based on its content.
  
- **`ComplianceAgent`**  
  Validates the content based on predefined business rules for that category.

## 🧪 Example
  Requires python3.11+

  Running the application:

```bash
pip install -r requirements.txt

python master_routing_agent.py


### Sample Input Document
```json
{
  "documentId": "doc-001",
  "content": "This is the Certificate of Death for John Doe. Date of death: 2023-01-01."
}

### Sample Responses
```json
'documentId': 'doc-001', 'category': 'Miscellaneous', 'categoryCode': '00.0000-00', 'valid': True, 'reason': 'Valid'}
{'documentId': 'doc-002', 'category': 'Will or Trust', 'categoryCode': '02.0300-50', 'valid': False, 'reason': "Invalid due to missing content: 'Last Will and Testament'"}
{'documentId': 'doc-003', 'category': 'Tax Document', 'categoryCode': '05.5000-70', 'valid': True, 'reason': 'Valid'}
{'documentId': 'doc-004', 'category': 'Will or Trust', 'categoryCode': '02.0300-50', 'valid': True, 'reason': 'Valid'}
{'documentId': 'doc-005', 'category': 'Death Certificate', 'categoryCode': '01.0000-50', 'valid': True, 'reason': 'Valid'}
{'documentId': 'doc-006', 'category': 'Miscellaneous', 'categoryCode': '00.0000-00', 'valid': True, 'reason': 'Valid'}
