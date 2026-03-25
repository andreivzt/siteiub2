import re

# 1. Update netflix.js
with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Change back to 5000 to allow the full zoom animation to complete
js = re.sub(r'setTimeout\(\(\) => \{\n        // Start fading out the intro.*?\}, \d+\); // Wait', 
            '''setTimeout(() => {
        // Start fading out the intro
        introContainer.style.opacity = '0';

        // Wait for the fade out transition (1s as defined in CSS) to complete before hiding it completely
        setTimeout(() => {
            introContainer.classList.add('hidden');
            mainContent.classList.remove('hidden');

            // Small semantic animation for the main content entry
            mainContent.style.opacity = '0';
            mainContent.style.transition = 'opacity 1s ease-in';
            // Force reflow
            void mainContent.offsetWidth;
            mainContent.style.opacity = '1';
        }, 1000);

    }, 4500); // Wait''', js, flags=re.DOTALL)

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Update netflix.css
with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Revert row styling to be closer
css = re.sub(r'\.row\s*\{.*?margin-top:\s*40px;.*?\}', 
    '''.row {
  padding: 10px 40px;
  position: relative;
  z-index: 20;
  margin-bottom: 20px;
}
.row:first-of-type {
  margin-top: -100px;
}''', css, flags=re.DOTALL)

# Netflix gap is usually very small (around 8-10px)
css = re.sub(r'\.cards-container\s*\{.*?padding-bottom:\s*60px;.*?\}',
    '''.cards-container {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding-bottom: 40px;
  padding-top: 20px;
  scrollbar-width: none;
}''', css, flags=re.DOTALL)

# Revert sizing
css = re.sub(r'\.movie-card\s*\{.*?min-width:\s*320px;\s*max-width:\s*380px;.*?\}',
    '''.movie-card {
  position: relative;
  min-width: 250px;
  max-width: 300px;
  flex: 1;
  border-radius: 4px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  background-color: #2f2f2f;
}''', css, flags=re.DOTALL)

css = re.sub(r'\.row-title\s*\{.*?letter-spacing:\s*1px;.*?\}',
    '''.row-title {
  font-size: 1.4rem;
  margin-bottom: 10px;
  font-weight: 500;
}''', css, flags=re.DOTALL)

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\netflix.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update index.html
with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_cards = '''
                <div class="movie-card">
                    <img src="poza8.jpg" alt="Poza 8" class="card-img">
                    <div class="card-info">
                        <h3>Amintire noua</h3>
                        <p class="match-score">2026</p>
                        <p class="memory-text">Momente de neuitat...</p>
                    </div>
                </div>
                <div class="movie-card">
                    <img src="poza9.jpg" alt="Poza 9" class="card-img">
                    <div class="card-info">
                        <h3>Amintire noua</h3>
                        <p class="match-score">2026</p>
                        <p class="memory-text">Cea mai recentă amintire adăugată pentru povestea noastră.</p>
                    </div>
                </div>
                <div class="movie-card va-urma-card">'''

html = html.replace('<div class="movie-card va-urma-card">', new_cards)

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS and HTML reverted correctly")
