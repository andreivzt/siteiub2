import glob, re

html_files = glob.glob(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert meta description if it doesn't exist
    if '<meta name="description"' not in content.lower():
        content = re.sub(
            r'(<meta name="viewport"[^>]*>)',
            r'\1\n    <meta name="description" content="O colecție de amintiri prețioase.">',
            content,
            flags=re.IGNORECASE
        )
    
    # Prevent the hidden overlay from being used as a search snippet by adding data-nosnippet
    content = content.replace(
        '<div id="surprise-overlay" class="surprise-overlay hidden">',
        '<div id="surprise-overlay" class="surprise-overlay hidden" data-nosnippet="true">'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Updated {len(html_files)} files.')
