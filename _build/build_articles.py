#!/usr/bin/env python3
"""Генерує сторінки статей TradFi8: /statti/<slug>/index.html і /statti/index.html.

Запуск з кореня сайту:  python3 _build/build_articles.py
Папка _build не публікується на GitHub Pages (Jekyll пропускає папки з «_»).
Щоб додати статтю — допишіть словник у ARTICLES і запустіть скрипт.
Кожен текст перед публікацією — через чекліст tradfi8-perevirka.
"""
import html
import json
import os

SITE = "https://tradfi8.com.ua"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPDATED = "2026-11-25"
DISC_INVEST = ("Матеріал має освітній характер і не є фінансовою чи інвестиційною порадою. "
               "Ухвалюйте рішення самостійно або з ліцензованим консультантом.")

ARTICLES = [
    {
        "slug": "bank-zbankrutuvav-depozyt",
        "tag": "Депозити",
        "title": "Банк збанкрутував. Що буде з вашим депозитом?",
        "desc": "Як працює Фонд гарантування вкладів, які гроші він повертає і що перевірити у своєму банку вже зараз.",
        "date": "2026-11-24", "minutes": 5,
        "body": """
<p>Банки іноді виходять з ринку: через збитки, порушення чи рішення Національного банку. Для вкладника це неприємно, але не катастрофа, якщо знати правила гри заздалегідь.</p>

<h2>Хто повертає гроші</h2>
<p>В Україні вклади людей у банках захищає <strong>Фонд гарантування вкладів фізичних осіб (ФГВФО)</strong>. Коли банк виводять з ринку, Фонд виплачує вкладникам гарантоване відшкодування зі своїх коштів.</p>
<p>За даними Фонду, від початку роботи він виплатив вкладникам <span class="num">105,1 млрд грн</span>, а гроші отримали понад 2 млн людей — 96,1% вкладників банків, що ліквідуються (станом на жовтень 2026 року).</p>

<h2>Які гроші під захистом</h2>
<ul>
<li>Вклади <strong>фізичних осіб</strong> у банках — учасниках Фонду: депозити, поточні та карткові рахунки.</li>
<li>Захист діє <strong>в межах гарантованої суми</strong>. Її розмір і тимчасові правила на час воєнного стану змінювалися, тому актуальну суму завжди перевіряйте на офіційному сайті Фонду <a href="https://www.fg.gov.ua" rel="noopener">fg.gov.ua</a>.</li>
</ul>
<p>Фонд <strong>не</strong> відшкодовує гроші, які ви тримаєте поза банками: у кредитних спілках, фінансових і інвестиційних компаніях, на криптобіржах.</p>

<h2>Як отримати відшкодування</h2>
<ol>
<li>Після рішення про ліквідацію банку Фонд публікує на своєму сайті, який <strong>банк-агент</strong> виплачує гроші і з якої дати.</li>
<li>Перевірте себе в переліку вкладників і зверніться до банку-агента. Зазвичай потрібні паспорт та ідентифікаційний код.</li>
<li>Якщо вас немає в переліку або сума інша — звертайтеся до Фонду з договором і випискою.</li>
</ol>

<div class="box"><h3>Що перевірити вже зараз</h3><ul>
<li>Чи є ваш банк учасником Фонду — перелік є на fg.gov.ua.</li>
<li>Чи не тримаєте ви в одному банку більше за гарантовану суму. Якщо так — подумайте про розподіл між кількома банками.</li>
<li>Чи оформлений вклад саме на вас як фізичну особу.</li>
<li>Чи збережені договір і виписки — вони знадобляться, якщо виникне спір.</li>
</ul></div>
""",
    },
    {
        "slug": "skladnyi-vidsotok",
        "tag": "Інвестиції",
        "title": "Відсотки на відсотки: як 10 000 ₴ стають 174 494 ₴",
        "desc": "Складний відсоток на простих прикладах і з калькулятором. Чому час важить більше за суму.",
        "date": "2026-11-23", "minutes": 4,
        "body": """
<p>Складний відсоток — це коли відсотки нараховуються не тільки на ваш внесок, а й на вже нараховані відсотки. Гроші починають «працювати» самі на себе, і з роками ефект стає дедалі помітнішим.</p>

<h2>Приклад: одна сума і 30 років</h2>
<p>Припустимо, ви вклали <strong>10 000 ₴</strong> під умовні <strong>10% річних</strong>, і відсотки щороку додаються до суми вкладу:</p>
<table>
<tr><th>Через</th><th class="r">Зі складним відсотком</th><th class="r">Без капіталізації</th></tr>
<tr><td>1 рік</td><td class="r">11 000 ₴</td><td class="r">11 000 ₴</td></tr>
<tr><td>10 років</td><td class="r">25 937 ₴</td><td class="r">20 000 ₴</td></tr>
<tr><td>20 років</td><td class="r">67 275 ₴</td><td class="r">30 000 ₴</td></tr>
<tr><td>30 років</td><td class="r"><span class="num">174 494 ₴</span></td><td class="r">40 000 ₴</td></tr>
</table>
<p>Перші роки різниця майже непомітна. Але далі крива різко йде вгору: за останні 10 років сума зростає більше, ніж за перші 20.</p>

<h2>Чому важливо почати раніше</h2>
<p>Візьмімо регулярні внески: <strong>2 000 ₴ щомісяця</strong> під умовні <strong>12% річних</strong> з нарахуванням щомісяця.</p>
<table>
<tr><th>Строк</th><th class="r">Внесено</th><th class="r">Накопичено</th></tr>
<tr><td>10 років</td><td class="r">240 000 ₴</td><td class="r">≈ 460 077 ₴</td></tr>
<tr><td>20 років</td><td class="r">480 000 ₴</td><td class="r">≈ 1 978 511 ₴</td></tr>
<tr><td>30 років</td><td class="r">720 000 ₴</td><td class="r">≈ 6 989 928 ₴</td></tr>
</table>
<p>Внески за 30 років лише втричі більші, ніж за 10, а накопичення — у 15 разів. Це і є головна сила складного відсотка: <strong>час</strong>.</p>

<div class="box"><h3>Важливо пам'ятати</h3><ul>
<li>Ставки 10% і 12% у прикладах умовні. Реальна дохідність депозитів, облігацій чи фондів змінюється і не гарантована.</li>
<li>Інфляція зменшує купівельну спроможність грошей, тож через 30 років 174 494 ₴ купуватимуть менше, ніж сьогодні.</li>
<li>Податки та комісії теж зменшують результат.</li>
</ul></div>
<p>Порахуйте свій варіант у калькуляторі на головній сторінці — змінюйте суму, ставку і строк.</p>
""",
        "cta": ("/#calc", "Відкрити калькулятор"),
        "disc": True,
    },
    {
        "slug": "seed-fraza",
        "tag": "Крипто",
        "title": "Seed-фраза: 12 слів, важливіших за пароль",
        "desc": "Що таке seed-фраза, де її зберігати і 5 помилок, через які люди втрачають криптовалюту.",
        "date": "2026-11-22", "minutes": 6,
        "body": """
<p>Якщо ви тримаєте криптовалюту у власному гаманці, а не на біржі, у вас є <strong>seed-фраза</strong> — 12 або 24 слова, які гаманець показав під час створення. Саме вона, а не пароль від застосунку, дає повний доступ до ваших коштів.</p>

<h2>Що таке seed-фраза</h2>
<p>Це резервна копія гаманця. З неї можна відновити гаманець на будь-якому пристрої. Звідси два правила:</p>
<ul>
<li>Втратили фразу і пристрій — <strong>втратили доступ</strong> до коштів. Відновити його ніхто не допоможе.</li>
<li>Хтось дізнався фразу — він може <strong>вивести все</strong>, і скасувати переказ не вийде.</li>
</ul>

<h2>Де її зберігати</h2>
<ul>
<li>Запишіть від руки на папері або вигравіюйте на металевій пластині.</li>
<li>Тримайте <strong>офлайн</strong>, у надійному місці, захищеному від води й вогню.</li>
<li>Майте дві копії в різних місцях, щоб не втратити все через один випадок.</li>
</ul>

<h2>5 помилок, через які втрачають криптовалюту</h2>
<ol>
<li><strong>Фото або скриншот фрази.</strong> Галерея синхронізується з хмарою, а хмару можуть зламати.</li>
<li><strong>Зберігання в нотатках, пошті чи месенджері.</strong> Це ті самі онлайн-сервіси, до яких можна отримати доступ.</li>
<li><strong>Введення фрази на сайті чи у формі «перевірки гаманця».</strong> Це класичний фішинг: справжньому сервісу ваша фраза не потрібна.</li>
<li><strong>Повідомлення фрази «підтримці».</strong> Жодна справжня служба підтримки ніколи не просить seed-фразу.</li>
<li><strong>Одна копія.</strong> Папірець можна загубити, а пристрій — зламати.</li>
</ol>

<div class="box"><h3>Біржа чи власний гаманець?</h3>
<p style="margin:0">На біржі ключі тримає сама біржа, а ви входите за логіном і паролем. Це зручно, але ви залежите від біржі. У власному гаманці всі ключі у вас — і вся відповідальність теж. Обирайте свідомо.</p></div>
""",
        "disc": True,
    },
    {
        "slug": "ovdp",
        "tag": "Облігації",
        "title": "Як працюють ОВДП і чи варто їх купувати",
        "desc": "Що таке облігації внутрішньої державної позики, як на них отримують дохід, які ризики і де їх купити.",
        "date": "2026-11-21", "minutes": 7,
        "body": """
<p>ОВДП — облігації внутрішньої державної позики. Купуючи їх, ви позичаєте гроші державі на певний строк, а вона зобов'язується повернути борг і заплатити дохід.</p>

<h2>Як це працює</h2>
<ul>
<li>ОВДП випускає Міністерство фінансів. Номінал однієї облігації зазвичай становить 1 000 одиниць валюти випуску.</li>
<li>Бувають <strong>гривневі</strong> і <strong>валютні</strong> (у доларах чи євро) облігації.</li>
<li>Дохід ви отримуєте як <strong>купон</strong> (періодичну виплату відсотків) або як <strong>дисконт</strong> — різницю між ціною купівлі та номіналом, який повертають у дату погашення.</li>
</ul>
<p>ОВДП популярні серед українців: станом на кінець лютого 2026 року фізичні особи тримали в цих облігаціях понад <span class="num">121,8 млрд грн</span>.</p>

<h2>Яка дохідність</h2>
<p>Вона залежить від строку, валюти та умов конкретного випуску і змінюється з часом. Актуальні ставки дивіться в пропозиціях банків і брокерів та на сайті Мінфіну <a href="https://mof.gov.ua" rel="noopener">mof.gov.ua</a>. Порівнюйте дохідність саме «на руки» — з урахуванням комісій.</p>

<h2>Ризики</h2>
<ul>
<li><strong>Інфляція.</strong> Якщо вона вища за дохідність, реальна вартість грошей падає.</li>
<li><strong>Продаж до погашення.</strong> Ціну диктує ринок, і вона може бути нижчою, ніж ви заплатили.</li>
<li><strong>Валютний ризик</strong> — для валютних облігацій під час перерахунку в гривню.</li>
<li><strong>Кредитний ризик держави.</strong> Він вважається низьким, але не нульовим.</li>
</ul>

<h2>Податки</h2>
<p>Правила оподаткування доходу від ОВДП для фізичних осіб варто перевіряти перед покупкою: вони можуть змінюватися. Актуальні правила — на сайті Державної податкової служби <a href="https://tax.gov.ua" rel="noopener">tax.gov.ua</a>.</p>

<h2>Де купити</h2>
<p>ОВДП купують через банки та брокерів, що мають ліцензію Національної комісії з цінних паперів та фондового ринку. Частина банків продає їх прямо в мобільному застосунку, також є можливість купити облігації через «Дію».</p>

<div class="box"><h3>Перед покупкою</h3><ul>
<li>Визначте строк, на який гроші вам точно не знадобляться.</li>
<li>Порівняйте дохідність і комісії кількох банків і брокерів.</li>
<li>Не вкладайте фінансову подушку, яка може знадобитися раптово.</li>
</ul></div>
""",
        "disc": True,
    },
    {
        "slug": "odna-moneta-z-desiaty",
        "tag": "Бюджет",
        "title": "Правило «одна монета з десяти — собі»",
        "desc": "Проста система, щоб почати відкладати навіть із невеликої зарплати.",
        "date": "2026-11-20", "minutes": 3,
        "body": """
<p>Одне з найстаріших правил особистих фінансів звучить так: <strong>з кожних десяти зароблених гривень одну залиште собі</strong>. Не на покупки, а на майбутнє.</p>

<h2>У чому ідея</h2>
<p>Більшість людей відкладає «те, що залишилось наприкінці місяця». Зазвичай не залишається нічого. Правило перевертає порядок: спершу відкладаєте 10%, а живете на решту. Цей принцип ще називають «спершу заплати собі».</p>

<h2>Як почати вже з наступної зарплати</h2>
<ol>
<li><strong>Відкрийте окремий рахунок</strong> чи «банку» для накопичень, щоб ці гроші не змішувалися з повсякденними.</li>
<li><strong>Налаштуйте автопереказ</strong> на день зарплати. Тоді не доведеться щоразу ухвалювати рішення.</li>
<li><strong>Почніть з меншого</strong>, якщо 10% зараз забагато: 3–5% теж працюють. Збільшуйте частку з кожним підвищенням доходу.</li>
<li><strong>Місяць записуйте витрати.</strong> Так легше знайти, звідки взяти ці 10%.</li>
</ol>

<h2>Приклад</h2>
<p>Дохід 20 000 ₴ на місяць → 2 000 ₴ відкладаєте одразу. За рік це <span class="num">24 000 ₴</span> — навіть без жодних відсотків.</p>

<div class="box"><h3>Куди спрямувати відкладене</h3><ul>
<li>Спершу — <strong>фінансова подушка</strong> на кілька місяців звичайних витрат. Вона має бути доступною.</li>
<li>Потім — довші цілі: навчання, житло, пенсія. Для них уже можна розглядати депозити чи облігації.</li>
</ul></div>
<p>Порахуйте, скільки дасть ваша сума з роками, у калькуляторі на головній.</p>
""",
        "cta": ("/#calc", "Порахувати накопичення"),
    },
    {
        "slug": "oblikova-stavka",
        "tag": "Економіка",
        "title": "Облікова ставка за 2 хвилини",
        "desc": "Хто керує ціною грошей і як рішення НБУ впливають на ваш кредит і депозит.",
        "date": "2026-11-19", "minutes": 4,
        "body": """
<p>Облікова ставка — головний інструмент, яким Національний банк України впливає на ціну грошей в економіці. Від неї залежать ставки за кредитами й депозитами, а отже — ваш гаманець.</p>

<h2>Що це таке</h2>
<p>Це базова ставка, за якою НБУ залучає і надає гроші банкам. Змінюючи її, Нацбанк стримує або підштовхує інфляцію. Головна ціль НБУ — стабільно низька інфляція.</p>

<h2>Яка ставка зараз</h2>
<p>З <strong>30 жовтня 2026 року</strong> облікова ставка становить <span class="num">16,5%</span> — Правління НБУ підвищило її 29 жовтня. Наступне засідання з монетарної політики заплановане на <strong>17 грудня 2026 року</strong>. Актуальне значення завжди є на сайті НБУ <a href="https://bank.gov.ua" rel="noopener">bank.gov.ua</a>.</p>

<h2>Як вона впливає на вас</h2>
<table>
<tr><th></th><th>Ставку підвищують</th><th>Ставку знижують</th></tr>
<tr><td>Кредити</td><td>дорожчають</td><td>дешевшають</td></tr>
<tr><td>Депозити</td><td>ставки зростають</td><td>ставки падають</td></tr>
<tr><td>Інфляція</td><td>стримується</td><td>може пришвидшитися</td></tr>
</table>
<p>Зміни відбуваються не миттєво: банки підлаштовують свої ставки протягом тижнів і місяців.</p>

<div class="box"><h3>Що це означає на практиці</h3><ul>
<li>Кредит з <strong>плаваючою</strong> ставкою може подорожчати після підвищення облікової. З фіксованою — ні.</li>
<li>Строковий депозит фіксує ставку на весь строк. Коли ставки ростуть, короткі строки дають змогу швидше переоформити вклад на кращих умовах.</li>
<li>Стежте за датами засідань НБУ: рішення публікують на bank.gov.ua.</li>
</ul></div>
""",
        "disc": True,
    },
]


def esc(s):
    return html.escape(s, quote=True)


def fmt_date(d):
    y, m, dd = d.split("-")
    return f"{dd}.{m}.{y}"


NAV = """<nav class="nav"><div class="in">
  <a class="logo" href="/">Trad<b>Fi</b>8</a>
  <div class="links"><a href="/statti/">Статті</a><a href="/#calc">Калькулятор</a><a class="hide-m" href="/#products">Курси й гайди</a><a class="hide-m" href="/#video">Відео</a></div>
</div></nav>"""

FOOTER = """<footer><div class="in">
Матеріали TradFi8 мають освітній характер і не є фінансовою чи інвестиційною порадою.<br>
© 2026 TradFi8 · <a href="/">Головна</a> · <a href="/statti/">Статті</a> · <a href="https://youtube.com/@TradFi8">YouTube</a> · <a href="https://t.me/tradfi8">Telegram</a>
</div></footer>"""


def head(title, desc, url, ld):
    return f"""<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#fbfbfd">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="TradFi8">
<meta property="og:locale" content="uk_UA">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/og-image.png">
<link rel="stylesheet" href="/assets/article.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
{NAV}
"""


def card(a):
    return (f'<a class="card" href="/statti/{a["slug"]}/"><span class="tag">{esc(a["tag"])}</span>'
            f'<h3>{esc(a["title"])}</h3><p>{esc(a["desc"])}</p></a>')


def build_article(a, others):
    url = f"{SITE}/statti/{a['slug']}/"
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Article", "headline": a["title"], "description": a["desc"], "inLanguage": "uk",
             "datePublished": a["date"], "dateModified": UPDATED, "mainEntityOfPage": url,
             "image": f"{SITE}/og-image.png",
             "author": {"@type": "Organization", "name": "TradFi8", "url": SITE + "/"},
             "publisher": {"@type": "Organization", "name": "TradFi8",
                           "logo": {"@type": "ImageObject", "url": f"{SITE}/apple-touch-icon.png"}}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Головна", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Статті", "item": SITE + "/statti/"},
                {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
        ],
    }
    cta_href, cta_text = a.get("cta", ("/statti/", "Усі статті"))
    disc = f'<p class="disc">{DISC_INVEST}</p>' if a.get("disc") else \
        '<p class="disc">Матеріал має освітній характер і не є фінансовою порадою.</p>'
    out = head(f"{a['title']} — TradFi8", a["desc"], url, ld)
    out += f"""<main>
<div class="wrap">
  <div class="crumbs"><a href="/">Головна</a> › <a href="/statti/">Статті</a> › {esc(a['tag'])}</div>
  <header class="art">
    <span class="tag">{esc(a['tag'])}</span>
    <h1>{esc(a['title'])}</h1>
    <p class="lead">{esc(a['desc'])}</p>
    <p class="meta">{a['minutes']} хв читання · {fmt_date(a['date'])} · оновлено {fmt_date(UPDATED)}</p>
  </header>
  <article class="body">
{a['body'].strip()}
  </article>
  <div class="cta"><a class="btn" href="{cta_href}">{cta_text}</a><a class="btn light" href="https://youtube.com/@TradFi8">Відео на YouTube</a></div>
  {disc}
</div>
<section class="more"><h2>Читайте також</h2><div class="cards">
{''.join(card(o) for o in others)}
</div></section>
</main>
{FOOTER}
</body>
</html>
"""
    d = os.path.join(ROOT, "statti", a["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


def build_index():
    url = f"{SITE}/statti/"
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Статті TradFi8",
          "url": url, "inLanguage": "uk",
          "hasPart": [{"@type": "Article", "headline": a["title"], "url": f"{SITE}/statti/{a['slug']}/"}
                      for a in ARTICLES]}
    desc = "Статті TradFi8 про гроші простими словами: депозити, складний відсоток, ОВДП, бюджет, крипто й економіка."
    out = head("Статті — TradFi8", desc, url, ld)
    items = "\n".join(
        f'<a class="card" href="/statti/{a["slug"]}/"><span class="tag">{esc(a["tag"])} · {a["minutes"]} хв</span>'
        f'<h3>{esc(a["title"])}</h3><p>{esc(a["desc"])}</p></a>' for a in ARTICLES)
    out += f"""<main>
<div class="wrap">
  <div class="crumbs"><a href="/">Головна</a> › Статті</div>
  <header class="art"><h1>Статті.</h1><p class="lead">Гроші простими словами — українською. Нові матеріали щодня.</p></header>
  <div class="list">
{items}
  </div>
</div>
</main>
{FOOTER}
</body>
</html>
"""
    os.makedirs(os.path.join(ROOT, "statti"), exist_ok=True)
    with open(os.path.join(ROOT, "statti", "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


def build_sitemap():
    urls = [(SITE + "/", "1.0", "daily"), (SITE + "/statti/", "0.9", "daily")]
    urls += [(f"{SITE}/statti/{a['slug']}/", "0.8", "weekly") for a in ARTICLES]
    body = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{UPDATED}</lastmod>\n    <changefreq>{c}</changefreq>\n    <priority>{p}</priority>\n  </url>"
        for u, p, c in urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + body + "\n</urlset>\n")


if __name__ == "__main__":
    for i, a in enumerate(ARTICLES):
        others = [ARTICLES[(i + k) % len(ARTICLES)] for k in (1, 2, 3)]
        build_article(a, others)
    build_index()
    build_sitemap()
    print(f"Готово: {len(ARTICLES)} статей, /statti/, sitemap.xml")
