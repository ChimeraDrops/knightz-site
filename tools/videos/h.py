import html

def esc(s):
    return html.escape(s, quote=False)

def fig(src, alt, cap):
    return f'''<figure><a href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{html.escape(alt, quote=True)}" loading="lazy"></a><figcaption>{cap}</figcaption></figure>'''

def prompt(label, text, why=None):
    w = f'<div class="why">{why}</div>' if why else ""
    return f'''<div class="prompt"><div class="prompt-head"><span>{label}</span><button type="button" class="copy">Copy</button></div><pre>{esc(text)}</pre>{w}</div>'''

def table(head, rows, num_cols=()):
    th = "".join(f'<th{" class=\"num\"" if i in num_cols else ""}>{c}</th>' for i, c in enumerate(head))
    trs = []
    for r in rows:
        trs.append("<tr>" + "".join(f'<td{" class=\"num\"" if i in num_cols else ""}>{c}</td>' for i, c in enumerate(r)) + "</tr>")
    return f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'

def stats(items):
    return '<div class="stat-row">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items) + "</div>"

def script(blocks, title):
    inner = "".join(f"<p><b>{esc(k)}</b>{esc(v)}</p>" for k, v in blocks)
    return f'<details class="script"><summary>{title}</summary><div class="inner">{inner}</div></details>'

def section(sid, title, content):
    return f'<section id="{sid}">\n<h2>{title}</h2>\n{content}\n</section>\n'

def step(n, title, sid=None):
    i = f' id="{sid}"' if sid else ""
    return f'<h3{i}><span class="stepno">{n}</span>{title}</h3>'
