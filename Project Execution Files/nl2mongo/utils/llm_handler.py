import logging


class LLMHandler:
    def __init__(self, *args, **kwargs):
        """
        Initialize a simple rule-based handler instead of OpenAI.
        """
        logging.info("Rule-based query handler initialized.")
        self.conversation_history = []

    def chat_with_llm(self, user_input: str) -> dict:
        """
        Convert natural language input into a MongoDB query.
        """

        try:
            user_input_lower = user_input.lower()

            # Query 1: Show all students
            if "all students" in user_input_lower or "show students" in user_input_lower:
                return {
                    "query": {},
                    "explanation": "Showing all students"
                }

            # Query 2: CGPA greater than
            if "cgpa greater than" in user_input_lower:
                return {
                    "query": {"cgpa": {"$gt": 8}},
                    "explanation": "Finding students with CGPA greater than 8"
                }

            # Query 3: CSE department
            if "cse" in user_input_lower:
                return {
                    "query": {"department": "CSE"},
                    "explanation": "Showing students from CSE department"
                }

            # Query 4: ECE department
            if "ece" in user_input_lower:
                return {
                    "query": {"department": "ECE"},
                    "explanation": "Showing students from ECE department"
                }

            # Query 5: Age greater than
            if "age greater than" in user_input_lower:
                return {
                    "query": {"age": {"$gt": 20}},
                    "explanation": "Finding students with age greater than 20"
                }

            # Default case
            return {
                "query": {},
                "explanation": "Query not recognized. Showing all students."
            }

        except Exception as e:
            logging.error(f"Error processing user query: {e}")
            raise