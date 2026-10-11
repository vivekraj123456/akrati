import re

with open('index.html.bak', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<section class="deck-slide" id="10"[^>]*>(.*?)</section>', c, re.DOTALL)
if m:
    s = re.sub(r'data:image/[^;]+;base64,[a-zA-Z0-9+/=]+', 'B64', m.group(1))
    with open('orig_s10_node0.html', 'w', encoding='utf-8') as out:
        out.write(s)
    print("Written to orig_s10_node0.html")
