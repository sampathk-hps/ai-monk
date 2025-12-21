VALIDATION_PROMPT = """
You are a Quality Assurance Auditor. Compare the AI-generated ticket attributes against the Ground Truth (Expected) attributes.

Context:
- Source ID: {source_id}

Generated Attributes:
- Category: {gen_category}
- Priority: {gen_priority}

Expected Attributes:
- Category: {exp_category}
- Priority: {exp_priority}

Task:
1. Assign an accuracy score from 0.0 to 1.0. 
   - 1.0 means Category AND Priority match perfectly.
   - 0.5 means one matches.
   - 0.0 means neither matches.
   - Adjust slightly if semantic meaning is same but words differ (e.g., "Critical" vs "High" might be 0.8 if close).
2. Provide a short reasoning.
"""
