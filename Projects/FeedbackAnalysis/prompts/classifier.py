CLASSIFIER_PROMPT = """
You are a Product Manager Assistant. Analyze the incoming feedback.
Classify it into exactly one category: [Bug, Feature Request, Praise, Complaint, Spam].
Provide a confidence score (0.0 to 1.0).
Feedback: {text}
"""
