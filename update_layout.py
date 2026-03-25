import re

# 1. Update index.html
with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the 2024 row completely
html = re.sub(r'        <!-- Row 2024 -->.*?<!-- Row 2025 -->', r'        <!-- Row 2025 -->', html, flags=re.DOTALL)

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update netflix.js
with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Change 5500 to 4200 to fade earlier and hide the red stripe
js = js.replace('5500', '4200')

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Update netflix.css
with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'\.row\s*\{.*?margin-top:\s*-100px;.*?\}',
    r'''.row {
  padding: 40px 60px 80px 60px;
  position: relative;
  z-index: 20;
  margin-top: 40px;
}

.row:first-of-type {
  margin-top: -100px;
}''', css, flags=re.DOTALL
)

css = re.sub(
    r'\.row-title\s*\{.*?\}',
    r'''.row-title {
  font-size: 2.2rem;
  margin-bottom: 30px;
  font-weight: 700;
  letter-spacing: 1px;
}''', css, flags=re.DOTALL
)

css = re.sub(
    r'\.cards-container\s*\{.*?padding-bottom:\s*40px;.*?\}',
    r'''.cards-container {
  display: flex;
  gap: 40px;
  overflow-x: auto;
  padding-bottom: 60px;
  padding-top: 20px;
  scrollbar-width: none;
}''', css, flags=re.DOTALL
)

css = re.sub(
    r'\.movie-card\s*\{.*?min-width:\s*250px;\s*max-width:\s*300px;.*?\}',
    r'''.movie-card {
  position: relative;
  min-width: 320px;
  max-width: 380px;
  flex: 1;
  border-radius: 4px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  background-color: #2f2f2f;
}''', css, flags=re.DOTALL
)

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates successful")
