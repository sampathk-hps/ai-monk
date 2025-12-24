import pandas as pd
from schema.feedback import FeedbackItem
from constants.constants import INPUT_REVIEWS_PATH, INPUT_EMAILS_PATH, EXPECTED_CLASSIFICATIONS_PATH
from functools import lru_cache

def load_and_normalize_data() -> list[FeedbackItem]:
    items = []
    
    # Process Reviews
    try:
        reviews_df = pd.read_csv(INPUT_REVIEWS_PATH)
        for _, row in reviews_df.iterrows():
            meta = {
                "platform": row.get("platform"), 
                "rating": row.get("rating"), 
                "version": row.get("app_version"),
                "user": row.get("user_name")
            }
            items.append(FeedbackItem(
                source_id=str(row["review_id"]),
                source_type="app_store",
                text_content=str(row["review_text"]),
                metadata=meta
            ))
    except FileNotFoundError:
        print(f"Warning: {INPUT_REVIEWS_PATH} not found.")

    # Process Emails
    try:
        emails_df = pd.read_csv(INPUT_EMAILS_PATH)
        for _, row in emails_df.iterrows():
            content = f"Subject: {row['subject']}\nBody: {row['body']}"
            meta = {
                "sender": row.get("sender_email"), 
                "priority_claimed": row.get("priority")
            }
            items.append(FeedbackItem(
                source_id=str(row["email_id"]),
                source_type="support_email",
                text_content=content,
                metadata=meta
            ))
    except FileNotFoundError:
        print(f"Warning: {INPUT_EMAILS_PATH} not found.")
        
    return items

# Cache the expected data so we don't read CSV every time
@lru_cache(maxsize=1)
def get_expected_data():
    try:
        df = pd.read_csv(EXPECTED_CLASSIFICATIONS_PATH)
        # Convert to dictionary for O(1) lookup: { "SR001": {row_data} }
        return df.set_index("source_id").to_dict(orient="index")
    except Exception as e:
        print(f"Error loading expected data: {e}")
        return {}

if __name__ == "__main__":
    items = load_and_normalize_data()
    print(f"Loaded {len(items)} feedback items.")
