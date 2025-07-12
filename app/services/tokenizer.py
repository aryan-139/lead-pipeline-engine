import re

# name parser 
def process_lead(raw_item):
    # Filter for Linkedin View 
    raw_item= clean_raw_item(raw_item)

    # Normalize
    raw_item = raw_item.strip()
    parts = raw_item.split()
    raw_item = raw_item.lower()

    # Rejection logic, if parts is more than 3 
    if not parts or len(parts) > 3:
        return {
            "error": "invalid_name_format",
            "raw_item_log": raw_item
        }
    
    # Assign based on number of tokens
    first_name = parts[0]
    middle_name = parts[1] if len(parts) == 3 else ""
    last_name = parts[-1] if len(parts) >= 2 else ""

    return {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "raw_item_log": raw_item
    }

def clean_raw_item(raw_item: str) -> str:
    raw_item = re.sub(r'View\s+.+?profile', '', raw_item, flags=re.IGNORECASE)
    raw_item = raw_item.replace("linkedin view", "").replace("View", "")
    raw_item = re.sub(r'\b(\w+\s\w+)\1\b', r'\1', raw_item, flags=re.IGNORECASE)
    raw_item = raw_item.strip()

    return raw_item
