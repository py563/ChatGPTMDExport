from bs4 import BeautifulSoup
from typing import List, Tuple

def parse_conversation_html(html_content: str) -> List[List[Tuple[str, str]]]:
    """Parses entire HTML with multiple <div class='conversation'> sections and extracts user/ChatGPT message pairs."""
    soup = BeautifulSoup(html_content, 'html.parser')
    all_conversations = []

    for conv_div in soup.select('div.conversation'):
        messages = conv_div.select('pre.message')
        conversation = []
        current_prompt = None

        for msg in messages:
            author_tag = msg.select_one('.author')
            content_divs = msg.find_all('div')
            if not author_tag or not content_divs:
                continue

            author = author_tag.text.strip()
            content = content_divs[-1].get_text(separator="\n").strip()

            if author.lower() == "user":
                current_prompt = content
            elif author.lower() == "chatgpt" and current_prompt:
                conversation.append((current_prompt, content))
                current_prompt = None

        if conversation:
            all_conversations.append(conversation)

    return all_conversations


def extract_to_markdown(conversation: List[Tuple[str, str]], prompts: List[str], output_file: str):
    """Writes selected user prompts and ChatGPT responses from a single conversation to a markdown file."""
    filtered = [(u, r) for u, r in conversation if any(p.lower() in u.lower() for p in prompts)]

    if not filtered:
        print(f"No matching prompts found for {output_file}")
        return

    with open(output_file, "w", encoding="utf-8") as md:
        for user, reply in filtered:
            md.write(f"### 🧑 User Prompt: `{user}`\n\n")
            md.write(f"**ChatGPT Response:**\n\n```\n{reply}\n```\n\n---\n")

    print(f"Extracted {len(filtered)} responses to: {output_file}")


def extract_conversation_to_markdown(conversation: List[Tuple[str, str]], output_file: str):
    """Writes an entire conversation to markdown file."""
    with open(output_file, "w", encoding="utf-8") as md:
        for user, reply in conversation:
            md.write(f"### 🧑 User Prompt: `{user}`\n\n")
            md.write(f"**ChatGPT Response:**\n\n```\n{reply}\n```\n\n---\n")

    print(f"Full conversation saved to: {output_file}")


def process_all_conversations(html_path: str, prompts: List[str] = None):
    """Processes all conversations and writes each to a separate markdown file."""
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    all_conversations = parse_conversation_html(html_content)

    for idx, conv in enumerate(all_conversations):
        if prompts:
            output_file = f"output/conversation_{idx+1}_filtered.md"
            extract_to_markdown(conv, prompts, output_file)
        else:
            output_file = f"output/conversation_{idx+1}_full.md"
            extract_conversation_to_markdown(conv, output_file)

def extract_by_prompt_exact_to_markdown(conversation: List[Tuple[str, str]], prompt: str, output_file: str):
    '''
    Extracts messages by exact user prompt match.
    '''
    filtered = [(u, r) for u, r in conversation if (prompt.lower() == u.lower())]
    # print(f"Filtered: {filtered}")
    
    if not filtered:
        print(f"No matching prompts found for {prompt}")
        return

    with open(output_file, "w", encoding="utf-8") as md:
        for user, reply in filtered:
            md.write(f"### 🧑 User Prompt: `{user}`\n\n")
            md.write(f"**ChatGPT Response:**\n\n```\n{reply}\n```\n\n---\n")

    print(f"Extracted {len(filtered)} responses to: {output_file}")
        
def process_specific_prompt(html_path: str, prompt: str, prefix_file_name: str):
    """Processes all conversations and writes each to a separate markdown file."""
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    all_conversations = parse_conversation_html(html_content)

    for idx, conv in enumerate(all_conversations):
        """Writes selected user prompts and ChatGPT responses from a single conversation to a markdown file."""
        if prompt:
            output_file = f"output/{prefix_file_name}_conversation_{idx+1}.md"
            extract_by_prompt_exact_to_markdown(conv, prompt, output_file)
        else:
            output_file = f"output/conversation_{idx+1}_full.md"
            extract_conversation_to_markdown(conv, output_file)