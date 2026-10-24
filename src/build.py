import re, urllib.parse, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root/'src/home.template.html').read_text()
logo = (root/'assets/logo-stacked.svg').read_text()
logo = re.sub(r'<svg[^>]*>', '<svg viewBox="0 0 206 211" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">', logo, count=1).strip()
swirl = re.search(r'<path class="swirl"[^>]*/>', logo).group(0)
WA = 'https://wa.me/966507701166?text='
waicon = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.5-.3Z"/></svg>'
def wa(text): return WA + urllib.parse.quote(text)

blends = [
  dict(n='١', name='شاي عمران', img='assets/img/omran.webp', alt='أوراق شاي عمران السوداء الكاملة على خلفية حمراء', level=3, label='ثقيلة', notes=['جريئة','عميقة','لون عسلي'], when='لكل وقت',
       text='نكهة ثقيلة ولون عسلي، تُشرب بلا سكر أو بقليل منه. لمن يحب الشاي الذي «يدنّق الراس».'),
  dict(n='٢', name='شاي الأصدقاء', img='assets/img/asdiqaa.webp', light=True, alt='أوراق شاي الأصدقاء مع خيوط الزعفران على خلفية بلون الخوخ', level=2, label='متوسطة', notes=['زعفران نفّاذ','حلوة بلا مرارة','سريعة التخدير'], when='المساء، وأي وقت',
       text='أوراق سيلانية كاملة ومكسورة مع زعفران قوي. طعمها حلو بلا مرارة، يشجعك على شربها بلا سكر.'),
  dict(n='٣', name='شاي العصاري', img='assets/img/asari.webp', alt='أوراق شاي العصاري على خلفية حمراء', level=2, label='متوسطة', notes=['متوازنة','ناعمة','زعفران موزون'], when='لكل الأوقات',
       text='شاي فاخر مع مقدار موزون من شعيرات الزعفران، يوازن النكهة ويحفظ لون الشاي.'),
  dict(n='٤', name='شاي الضحى', img='assets/img/duha.webp', alt='أوراق شاي الضحى مع خيوط الزعفران على خلفية حمراء', level=1, label='خفيفة', notes=['خفيفة','منعشة','أربعة أنواع'], when='الصباح واستراحة العمل',
       text='أربعة أنواع من الشاي الهندي والسيلاني والإنجليزي مع طشّة خيوط زعفران.'),
]
def ph(b):
    if b.get('img'):
        return f'<div class="ph has-img"><img src="{b["img"]}" alt="{b["alt"]}" loading="lazy" width="1200" height="1200"><span class="ph-num{' on-light' if b.get('light') else ''}">{b["n"]}</span></div>'
    return f'<div class="ph" role="img" aria-label="صورة {b["name"]}"><span class="num">{b["n"]}</span><span class="ph-label">الصورة قريباً</span></div>'
cards = []
for b in blends:
    dots = ''.join(f'<b class="{"on" if i < b["level"] else ""}"></b>' for i in range(3))
    notes = ''.join(f'<li>{x}</li>' for x in b['notes'])
    cards.append(f'''<article class="blend">
          {ph(b)}
          <div class="blend-body">
            <div class="blend-top"><h3>{b["name"]}</h3><span class="idx">{b["n"]}</span></div>
            <div class="strength"><span class="dots" aria-hidden="true">{dots}</span>{b["label"]}</div>
            <ul class="notes">{notes}</ul>
            <p>{b["text"]}</p>
            <div class="when">الوقت: <strong>{b["when"]}</strong></div>
            <a class="btn btn-red" href="{wa("السلام عليكم، أود طلب توليفة " + b["name"])}" target="_blank" rel="noopener">{waicon}اطلب {b["name"]}</a>
          </div>
        </article>''')

ig = [  # newest first
  dict(img='assets/img/ig/post-6.webp', url='https://www.instagram.com/p/Dew6ZxziKmk/', title='كلمة الشاي في عناوين الكتب، الجزء الثاني'),
  dict(img='assets/img/ig/post-5.webp', url='https://www.instagram.com/p/DeUplfjjHSY/', title='كلمة الشاي في عناوين الكتب'),
  dict(img='assets/img/ig/post-4.webp', url='https://www.instagram.com/p/DU_QZjajKsa/', title='الزعفران، الذهب الأحمر'),
  dict(img='assets/img/ig/post-3.webp', url='https://www.instagram.com/p/DPQTTaoDG8m/', title='محاورة بين القهوة والشاي'),
  dict(img='assets/img/ig/post-2.webp', url='https://www.instagram.com/p/DN3JEhI2I2-/', title='كيف أشتري الشاي المناسب لمزاجي؟'),
  dict(img='assets/img/ig/post-1.webp', url='https://www.instagram.com/p/DNYmseRMz7g/', title='كلمة الشاي'),
]
def igtile(x):
    if x.get('img'):
        return f'<a class="ig ig-img" href="{x["url"]}" target="_blank" rel="noopener"><img src="{x["img"]}" alt="منشور: {x["title"]}" loading="lazy" width="720" height="960"></a>'
    return f'<a class="ig" href="https://www.instagram.com/shayowrq/" target="_blank" rel="noopener"><small>{x["sub"]}</small><strong>{x["title"]}</strong></a>'
igh = '\n        '.join(igtile(x) for x in ig)

out = tpl.replace('{{LOGO}}', logo).replace('{{SWIRL}}', swirl).replace('{{BLENDS}}', '\n        '.join(cards)).replace('{{IG}}', igh).replace('{{WAICON}}', waicon)
out = re.sub(r'\{\{WA:(.*?)\}\}', lambda m: wa(m.group(1)), out)
assert '{{' not in out
(root/'preview.html').write_text(out)
print('preview', len(out))

# ---------- deployable site ----------
import shutil, html
dist = root/'dist'
if dist.exists(): shutil.rmtree(dist)
(dist/'assets/img/ig').mkdir(parents=True)
for f in (root/'assets/img').rglob('*.webp'):
    dst = dist/f.relative_to(root); dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy(f, dst)
shutil.copy(root/'assets/logo-stacked.svg', dist/'favicon.svg')
for name in ['og-image.jpg','apple-touch-icon.png','favicon-32.png']:
    shutil.copy(root/'assets'/name, dist/name)

body = out
style_start = body.index('<style>'); style_end = body.index('</style>') + len('</style>')
style = body[style_start:style_end].replace('body {\n  direction: rtl;', 'body {\n  margin: 0;\n  direction: rtl;', 1)
fonts = '\n'.join(l for l in body[:style_start].splitlines() if 'fonts.g' in l)
rest = body[style_end:].replace('<script>document.documentElement.lang="ar";document.documentElement.dir="rtl";</script>\n', '')
SITE = 'https://shayowrq.com/'
desc = 'شاي وورق: مشروع عائلي لتوليفات الشاي بالزعفران. أربع توليفات لكل مزاج ولكل وقت، والطلب عبر واتساب.'
head = f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>شاي وورق | توليفات شاي بالزعفران</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}">
<meta name="theme-color" content="#F0CAA9">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="ar_SA">
<meta property="og:site_name" content="شاي وورق">
<meta property="og:title" content="شاي وورق | توليفات شاي بالزعفران">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{fonts}
{style}
</head>
<body>"""
(dist/'index.html').write_text(head + rest + '\n</body>\n</html>\n')
(dist/'robots.txt').write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
(dist/'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>{SITE}</loc></url>\n</urlset>\n')
print('dist ok')
