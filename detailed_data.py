# import json
# import re

# # Load the JSON file
# with open('cases.json', 'r') as f:
#     data = json.load(f)

# # Define a function to extract date and court name from content or name
# def extract_info(content, name):
#     # Extract date from content
#     date_match = re.search(r'\b(\d{1,2}\s+\w+\s+\d{4})\b', content)
#     if date_match:
#         date = date_match.group(1)
#     else:
#         # If not found in content, try to extract from name
#         date_match = re.search(r'(\d+\s+\w+\s+\d{4})', name)
#         if date_match:
#             date = date_match.group(1)
#         else:
#             date = None

#     # Extract court name from content
#     court_match = re.search(r'(?:Supreme Court of India|THE\s+HIGH\s+COURT\s+OF\s+JUDICATURE(?:\s+\w+)*|High Court of \w+)(?=\W)', content, re.IGNORECASE)
#     if court_match:
#         court = court_match.group(0)
#     else:
#         # If not found in content, set default as "High Court"
#         court = "High Court"

#     return date, court

# # Iterate over each JSON object, extract information, and add new columns
# for item in data:
#     date, court = extract_info(item['content'], item['name'])
#     item['date'] = date
#     item['court'] = court

#     # Extract link from content
#     link_match = re.search(r'(?<=Indian Kanoon - )http[^\s]+', item['content'])
#     if link_match:
#         item['link'] = link_match.group(0)
#     else:
#         item['link'] = None

# # Write the updated data back to the JSON file
# with open('all_cases6.json', 'w') as f:
#     json.dump(data, f, indent=4)




import json
import re

# Load the JSON file
with open('all_cases4.json', 'r') as f:
    data = json.load(f)

# Define a function to extract links from content
def extract_links(content):
    # Extract link from content
    link_match = re.search(r'(?<=Indian Kanoon - )http[^\s]+', content)
    if link_match:
        return link_match.group(0)
    else:
        return None

# Iterate over each JSON object, extract links, and add a new column
for item in data:
    link = extract_links(item['content'])
    item['link'] = link

# Write the updated data back to the JSON file
with open('final_ll_cases.json', 'w') as f:
    json.dump(data, f, indent=4)

