import json

def convert_file_to_json(input_file, output_file):
    post_list = []
    
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split("\n")

        # Accumulate lines for a post
        post_text = ""
        for line in lines:
            # If the line contains '|', it indicates the end of the post text with engagement
            if '|' in line:
                # Combine the current accumulated text and this line
                post_text += " " + line.strip()
                
                try:
                    # Safely split the post text and engagement value
                    text, engagement = post_text.strip().rsplit('|', 1)
                    post_data = {
                        "text": text.strip(),
                        "engagement": int(engagement.strip())
                    }
                    post_list.append(post_data)
                except ValueError:
                    print(f"Error processing post, skipping: {post_text}")
                
                # Reset accumulator for next post
                post_text = ""
            else:
                # Accumulate text lines until the delimiter is found
                post_text += " " + line.strip()

        # Handle the last accumulated post (if any)
        if post_text.strip():
            try:
                text, engagement = post_text.strip().rsplit('|', 1)
                post_data = {
                    "text": text.strip(),
                    "engagement": int(engagement.strip())
                }
                post_list.append(post_data)
            except ValueError:
                print(f"Error processing final post, skipping: {post_text}")

    # Convert the list of posts to JSON format
    json_data = json.dumps(post_list, indent=4)
    
    # Write the JSON data to the output file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

# File paths
input_file = 'raw_data.txt'
output_file = 'posts.json'

# Convert the input file to JSON
convert_file_to_json(input_file, output_file)

print(f"Data has been converted to JSON and saved in '{output_file}'.")


