import re

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<div class="nav-logo">S</div>', '<a href="book1.html" class="nav-logo">S</a>')

start_marker = '<!-- Cards Section -->'

new_rows = """        <!-- Row 2024 -->
        <div class="row">
            <h2 class="row-title">2024</h2>
            <div class="cards-container">
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
                </div>
            </div>
        </div>

        <!-- Row 2025 -->
        <div class="row">
            <h2 class="row-title">2025</h2>
            <div class="cards-container">
                <div class="movie-card">
                    <img src="poza5.jpg" alt="19.XII.2025" class="card-img">
                    <div class="card-info">
                        <h3>Primul Craciun</h3>
                        <p class="match-score">19.XII.2025</p>
                        <p class="memory-text">Încă de la început am simțit că între noi e ceva ce nu se întâlnește la tot pasul. Ne-am învățat unul pe altul cu răbdare, trecând prin toate...</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Row 2026 -->
        <div class="row">
            <h2 class="row-title">2026</h2>
            <div class="cards-container">
                <div class="movie-card">
                    <img src="poza1.jpg" alt="23.I.2026" class="card-img">
                    <div class="card-info">
                        <h3>Un nou inceput</h3>
                        <p class="match-score">23.I.2026</p>
                        <p class="memory-text">Îmi aduc aminte cu drag și acum de momentele astea minunate ale noastre. Mă uit la pozele noastre și realizez cât de mult contează clipele astea mici pentru mine care imi amintesc ca locul meu preferat este langa tine.</p>
                    </div>
                </div>
                <div class="movie-card">
                    <img src="poza2.jpg" alt="12.II.2026" class="card-img">
                    <div class="card-info">
                        <h3>Locul meu preferat</h3>
                        <p class="match-score">12.II.2026</p>
                        <p class="memory-text">Nu contează neapărat unde suntem sau ce facem, ci faptul că suntem împreună. Tu ești "acasă" pentru mine.</p>
                    </div>
                </div>
                <div class="movie-card">
                    <img src="poza3.jpg" alt="13.II.2026" class="card-img">
                    <div class="card-info">
                        <h3>Doar noi doi</h3>
                        <p class="match-score">13.II.2026</p>
                        <p class="memory-text">Te iubesc, Sonia! Mai mult ca ieri, dar clar mai puțin ca mâine! ❤️</p>
                    </div>
                </div>
                <div class="movie-card">
                    <img src="poza4.jpg" alt="20.II.2026" class="card-img">
                    <div class="card-info">
                        <h3>Viitorul nostru</h3>
                        <p class="match-score">20.II.2026</p>
                        <p class="memory-text">Și povestea continuă... Abia aștept să umplem cartea cu amintiri.</p>
                    </div>
                </div>
                
                <div class="movie-card va-urma-card">
                    <div class="card-info va-urma-info">
                        <h3 class="va-urma-text">Va urma..</h3>
                    </div>
                </div>
            </div>
        </div>"""

old_block = re.search(r'<!-- Cards Section -->.*?<div class="row">.*?</div>\s*</div>\s*', text, re.DOTALL)
if old_block:
    text = text[:old_block.start()] + start_marker + '\n' + new_rows + text[old_block.end():]
else:
    print("Could not find old block")

with open(r'c:\Users\Costinel\OneDrive\Desktop\siteiub1\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done index.html updates")
