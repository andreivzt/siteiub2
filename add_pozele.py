import re

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

poze_html = '''
                <div class="movie-card">
                    <img src="poza6.jpeg" alt="09.IX.2024" class="card-img">
                    <div class="card-info">
                        <h3>Așa am început</h3>
                        <p class="match-score">09.IX.2024</p>
                        <p class="memory-text">Totul a inceput simplu, si usor, nu a fost nimic fortat ceea ce m a facut sa ma indragostesc pana peste cap de tine de la inceput</p>
                    </div>
                </div>
                <div class="movie-card">
                    <img src="poza7.jpeg" alt="09.IX.2024" class="card-img">
                    <div class="card-info">
                        <h3>Așa am început</h3>
                        <p class="match-score">09.IX.2024</p>
                        <p class="memory-text">Când mă uit la pozele astea din prima zi, văd cât de mult am crescut amândoi și cât de frumoasa este povestea noastră.</p>
                    </div>
                </div>'''

html = re.sub(r'(<h2 class="row-title">2025</h2>\s*<div class="cards-container">)', r'\g<1>' + poze_html, html)

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done inserting pozele")
