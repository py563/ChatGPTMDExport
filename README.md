# ChatGPTMDExport

**ChatGPTMDExport** is a utility to extract ChatGPT conversations from HTML exports and convert them into clean, readable Markdown files. It supports full conversation exports, filtered responses by prompt keywords, and exact prompt-response matching.

**Export** your chats from ChatGPT to get started. I built this tool to help me create notes from questions I asked ChatGPT.

## 📦 Features

* ✅ Extract all conversations from an HTML file
* 🔍 Filter prompt-response pairs by a list of keywords
* 🎯 Find exact match prompts and get their responses
* 📝 Save outputs as structured Markdown files
* 💬 Works with multiple `<div class="conversation">` blocks per HTML

## 📂 Folder Structure

```
ChatGPTMDExport/
│
├── output/                 # Output markdown files
├── parser.py               # Core logic (the code you wrote)
├── playw_render.py         # Core logic (the code you wrote)
├── test-all.py             # tests all methods
├── tes1/chat.html          # Sample HTML (exported from ChatGPT)
└── README.md
```

## 🚀 Usage

### 1. Extract all conversations to Markdown

```python
from parser import process_all_conversations

process_all_conversations("chat.html")
```

### 2. Extract only specific prompts

```python
from parser import extract_specific_prompt

process_specific_prompt("test1/ChatGPT1.html", "dp", "dp_charges")
```

### 3. Filter with prompt list

```python
from parser import process_all_conversations

process_all_conversations("chat.html", prompt_list=["DP", "Demat"])
```

## Requirements

* Python 3.7+
* `beautifulsoup4`
* `playwright`
* `lxml` (optional but faster)

Check attached requirements.txt file

```bash
pip install -r requirements.txt
```

## HTML Format

The tool expects exported ChatGPT history with this structure:

```html
<div class="conversation">
  <div class="author">user</div>
  <div>Prompt text</div>
  <pre class="message">...</pre>
  <div class="author">ChatGPT</div>
  <pre class="message">...</pre>
</div>
```

## 🛠 TODO

* [ ] Add CLI support
* [ ] Regex / case-insensitive matching
* [ ] Merge all responses into a single notebook-style markdown file

## License

MIT License.
