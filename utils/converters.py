from datetime import datetime
import re

def timestamp_to_date(ts):
    return datetime.fromtimestamp(ts).date()

def timestamp_to_datetime(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime('%H:%M')

def item_to_wowhead_link(item, wow_data_url):

    # Regex pattern to capture the id and name
    pattern = r'\|Hitem:(\d+):.*?\|h\[(.*?)\]\|h\|r'
    match = re.search(pattern, item)
    
    if match:
        item_id = match.group(1)  # Extracted id
        item_name = match.group(2)  # Extracted name
        return '[' + item_name + '](' + wow_data_url + '/?item=' + item_id + ')'
    
    else:
        print(f"Error: Item string '{item}' does not match expected format.")
        return "Error: Item string did not match expected format"