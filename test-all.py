from playw_render import renders_html_with_playwright
from gpthtmlparser import process_all_conversations, process_specific_prompt

# Example usage
# Uncomment the following line to render HTML with Playwright
rendered_html_path = renders_html_with_playwright()
# Uncomment the following line to process all conversations
process_all_conversations(rendered_html_path, prompts=["Coding standards", "git"])
# Example call for all conversations with filters
process_specific_prompt("tes1/ChatGPT1.htm", "dp charges", "dp_charges")
# process_specific_prompt("tes1/ChatGPT1.htm", "Coding standards", "coding_standards")
# process_specific_prompt("tes1/ChatGPT1.htm","how to activate venv in git bash on windows","venv_git_bash")
# process_all_conversations("tes1/ChatGPT1.htm", prompts=["Coding standards", "git"])
# process_all_conversations("tes1/ChatGPT1.htm", prompts=["Coding standards"])
# process_all_conversations("output_path", prompts=["Coding standards"])