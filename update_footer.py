import re

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Hero section
hero_pattern = re.compile(r'<div class="hero-content">.*?</div>', re.DOTALL)
new_hero = '''<div class="hero-content">
                <h1 class="hero-title">cea mai frumoasa poveste de dragoste 💗</h1>
            </div>'''
html = hero_pattern.sub(new_hero, html)

# 2. Add Footer before the closing </div> of main-content
footer_html = '''        <!-- Footer Message -->
        <footer class="site-footer">
            <p>un mesaj pentru invidiosi, nu o sa aveti niciodata o relatie ca a noastra 😉</p>
        </footer>
    </div>
    <script src="netflix.js"></script>'''

# Try to replace the exact ending
import traceback
try:
    if '    </div>\n\n    <script src="netflix.js"></script>' in html:
        html = html.replace('    </div>\n\n    <script src="netflix.js"></script>', footer_html)
    elif '    </div>\r\n\r\n    <script src="netflix.js"></script>' in html:
        html = html.replace('    </div>\r\n\r\n    <script src="netflix.js"></script>', footer_html)
    elif '    </div>\n    <script src="netflix.js"></script>' in html:
        html = html.replace('    </div>\n    <script src="netflix.js"></script>', footer_html)
    elif '    </div>\r\n    <script src="netflix.js"></script>' in html:
        html = html.replace('    </div>\r\n    <script src="netflix.js"></script>', footer_html)
    else:
        # Fallback regex if exact string misses due to whitespace
        html = re.sub(r'\s*</div>\s*<script src="netflix.js"></script>', '\n' + footer_html, html)
except Exception as e:
    print(e)
    
with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.css', 'a', encoding='utf-8') as f:
    f.write('''\n.site-footer {
  text-align: center;
  padding: 60px 20px 20px 20px;
  font-size: 0.85rem;
  color: #888;
  font-style: italic;
}\n''')

print("Done")
