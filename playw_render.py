from playwright.sync_api import sync_playwright
import os

def renders_html_with_playwright():
    """Renders HTML using Playwright to execute JavaScript and save the output."""
    
    # Absolute path to your local HTML file
    local_file = os.path.abspath("tes1/chat.html")
    file_url = "file://" + local_file

    # Output path
    output_path = "tes1/rendered_output.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # You can use .launch(headless=False) to see it
        page = browser.new_page()
        page.goto(file_url, wait_until="load")

        # Get rendered HTML after JavaScript execution
        rendered_html = page.content()

        # Save to local file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)

        print(f"Rendered HTML saved to {output_path}")
        browser.close()
    
        return output_path
    return None