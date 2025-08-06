import re
from typing import Dict
from llama_cpp import Llama
import json


class DocumentClassifier:
    def __init__(self, model_path: str, n_ctx: int = 512, verbose: bool = False):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            verbose=verbose
        )

    def classify(self, content: str) -> str:
        """
        Classify a document using a localized LLM.

        Args:
            content (str): Document text content.

        Returns:
            str: Classified category (e.g., 'Death Certificate', 'Will or Trust', etc.)
        """
        prompt = f"""You are a classification agent. Categorize the following estate-related document. Return one of:
- Death Certificate
- Will or Trust
- Tax Document
- Property Deed
- Financial Statement
- Miscellaneous

Document:
\"\"\"{content}\"\"\"

Category:"""

        output = self.llm(prompt, stop=["\n"], max_tokens=10)
        category = output["choices"][0]["text"].strip()
        return category

    def validate_document_with_llm(self, content: str, category: str) -> Dict[str, str]:
        """
        Validate a document using a localized LLM based on business rules.

        Args:
            content (str): Document text content.
            category (str): Classified category.

        Returns:
            Dict[str, str]: A dictionary with 'valid' (bool) and 'reason' (str).
        """
        prompt = f"""
You are a compliance validation agent for estate-related documents.

You will be given:
- A document category
- The content of the document

Your task:
- Determine if the content satisfies the validation rules for the given category.
- DO NOT reclassify the document or question the category.
- Only validate the content based on the Validation Rules below.

Validation Rules:
- Category "Death Certificate": content must contain AT LEAST ONE of the following strings:
    - "Certificate of Death"
    - "Date of death"
- Category "Will or Trust": content must contain AT LEAST ONE of the following strings:
    - "Last Will and Testament"
    - "Trust Agreement"
- Any other category other than "Death Certificate" or "Will or Trust" will always be valid.
  Do not run any validation rules against those categories.

Output:
- Return ONLY a valid JSON object, with no extra explanation or formatting.
- No additional text before or after the JSON object.
- The JSON must be in this format:
{{
  "valid": true or false,
  "reason": "Explanation of why the document is valid or not."
}}

Example:
{{
  "valid": true,
  "reason": "Valid"
}}

This is the category: "{category}"

This is the content:
\"\"\"{content}\"\"\"
"""


        output = self.llm(prompt, stop=["}"], max_tokens=100)
        response_text = output["choices"][0]["text"].strip() + "}"
        # print(f"response_text = {response_text}")

        try:
            match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if match:
                return json.loads(match.group())
            else:
                return {
                    "valid": False,
                    "reason": "No JSON found in response from LLM. Can't validate document."
                }

        except json.JSONDecodeError:
            return {
                "valid": False,
                "reason": "Validation LLM Model returned malformed JSON"
            }
