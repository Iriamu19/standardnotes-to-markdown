# Standard Notes to Markdown Converter

This script is designed to convert a JSON file, exported from the note taking app Standard Notes, into multiple Markdown files. 

The JSON file can be exported from the Standard Notes desktop app :
***Preferences -> Backups -> Data backups -> select "decrypted" -> Download backup***

Each Markdown file will have a YAML header with specific metadata (especially created_at timestamp) from the JSON file. The script filters out notes with the `"trashed": true` attribute.

## Requirements

- Python 3.x
- `pyyaml` package

## Usage

Run the script with the following command:

```bash
python json_to_markdown.py input.json export_folder
```

Replace `input.json` with the path to your input JSON file, and `export_folder` with the desired path for exporting the Markdown files.

## Script Details

The script reads the JSON file, processes the data, and creates individual Markdown files for each note. It extracts the following fields from the JSON data and includes them in the YAML header of each Markdown file:

- `title`
- `created_at`
- `created_at_timestamp`
- `uuid`
- `protected`
- `tags`
