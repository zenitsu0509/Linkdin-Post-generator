import json

# Load the JSON data
with open('processed_posts.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Function to decode Unicode escape sequences
def decode_unicode(text):
    return text.encode('utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')

# Process the text in each post
for post in data:
    if 'text' in post:
        post['text'] = decode_unicode(post['text'])


with open('cleaned_posts.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Data has been cleaned and saved in 'cleaned_posts.json'.")