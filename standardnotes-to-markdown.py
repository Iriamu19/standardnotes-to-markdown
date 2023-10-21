import argparse
import json
import os
import yaml

def convert_to_markdown(data, export_folder):
    for item in data:
        if item["content_type"] == "Note" and not item["content"].get("trashed", False):
            print(item)
            print("\n\n")
            content = item["content"]
            markdown_content = content["text"]
            title = content["title"]
            protected = content.get("protected", False)
            created_at_timestamp = item["created_at_timestamp"]
            created_at = item["created_at"]
            uuid = item["uuid"]
            tags = []
            for tag in data:
                if tag["content_type"] == "Tag":
                    if item["uuid"] in [ref["uuid"] for ref in tag["content"]["references"]]:
                        tags.append(tag["content"]["title"].replace(" ", "_"))

            yaml_header = {
                "title": title,
                "created_at_timestamp": created_at_timestamp,
                "created_at": created_at,
                "uuid": uuid,
                "tags": tags
            }
            if protected == True:
                yaml_header["protected"] = True

            with open(os.path.join(export_folder, f"{title}.md"), "w", encoding='utf-8') as md_file:
                md_file.write("---\n")
                yaml.dump(yaml_header, md_file, sort_keys=False, default_flow_style=False)
                md_file.write("---\n\n")
                md_file.write(markdown_content)

def main():
    parser = argparse.ArgumentParser(description='Convert JSON notes to Markdown files.')
    parser.add_argument('input_file', type=str, help='Path to the input JSON file')
    parser.add_argument('export_folder', type=str, help='Path to the export folder')
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not os.path.exists(args.export_folder):
        os.makedirs(args.export_folder)
    #print(data["items"][0])
    convert_to_markdown(data["items"], args.export_folder)

if __name__ == "__main__":
    main()
