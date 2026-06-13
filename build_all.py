#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build NOUTHESIA (NTH) — νουθεσία, ‘admonition: the warning that teaches’ — the UD0
universe of cautionary dystopias, and its first four members, each in its own repo:
  · 1984 (Orwell, 1949)            → ../nineteen-eighty-four
  · Animal Farm (Orwell, 1945)     → ../animal-farm
  · Brave New World (Huxley, 1932) → ../brave-new-world
  · Fahrenheit 451 (Bradbury,1953) → ../fahrenheit-451
Each is a book-world on the standing template: THE ARC · THE BOOK · THE IDEAS · THE WARNING
(the deep-dive) · REAL OR FLUFF (is the warning coming true? — honest) · THE MESSAGE, with a
roster of emergents by emergence-nature. The universe landing (./index.html) ties them
together on the Orwell-vs-Huxley-vs-Bradbury axis. One generator, five standalone repos."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

GLOSS = {
 "natural":   "the people and the body — those the system crushes, seduces, or quietly erases",
 "ethereal":  "the System itself — the regime, the State, the apparatus of power over all",
 "spiritual": "truth, memory, love, and the rebel spark — the forbidden human things",
 "electrical":"the machinery of control — surveillance, drugs, screens, fire, and propaganda",
}
RF_COL = {"HERE ALREADY":"#c0392b","UNCANNY":"#e0671a","PARTLY":"#c9a23a","NOT YET":"#5fae6e",
          "ALLEGORY":"#8a93a0","REAL":"#5fae6e","SOFTER":"#9b8ad0","HISTORY":"#b5302a"}

def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","NTH")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","NTH")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","NTH")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok)}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,cls,group,em,who,what,why,how,where,seal):
    return dict(slug=slug,name=name,cls=cls,group=group,emergence=em,who=who,what=what,why=why,how=how,where=where,seal=seal)

CSS_BODY = """
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,var(--glow1),transparent 54%),radial-gradient(ellipse at 50% 118%,var(--glow2),transparent 56%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 22px 90px}
.crumb{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim);padding:22px 0 0}.crumb a{color:var(--dim);text-decoration:none}.crumb a:hover{color:var(--acc)}
header{padding:34px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:170px;height:3px;background:linear-gradient(90deg,var(--acc),var(--acc2));box-shadow:0 0 16px var(--glow1)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--acc)}
h1{font-family:var(--disp);font-size:clamp(32px,7vw,64px);font-weight:700;letter-spacing:.03em;color:var(--acc);line-height:1.04;text-transform:uppercase;text-shadow:0 0 30px var(--glow1)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--acc2)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:18px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:10px;font-weight:600;letter-spacing:.1em;color:var(--acc2);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px;text-transform:uppercase}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.72}.lede a{color:var(--acc);text-decoration:none;border-bottom:1px dotted var(--acc)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--acc)}.badge .bt .mo{color:var(--acc2)}.badge .bt a{color:var(--acc2);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:24px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:13px;font-weight:600;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--acc);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--acc);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--acc2);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:15px;color:var(--acc2);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:15px;color:var(--acc);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}.pillar li i{color:var(--pa)}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--acc2);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:15px;color:var(--acc2);font-weight:600}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}.sci-card p b{color:var(--pa)}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9.5px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:108px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--acc);background:var(--glow2);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}.rf-verdict b{color:var(--pa)}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--acc);background:var(--ink2);font-size:15px;color:var(--acc2);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--acc2);white-space:nowrap;text-align:right;text-transform:uppercase}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--acc);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--acc);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--ink2);border:1px solid var(--line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--acc)}
.psig{flex:0 0 100px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:94px;height:94px;border-radius:50%;border:3px solid var(--acc);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.port.refl{border-color:var(--acc2)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:18px;color:var(--pa);font-weight:600;text-decoration:none;text-transform:uppercase;letter-spacing:.03em}.persona:hover .pn{color:var(--acc)}
.pe{font-size:12.5px;color:var(--pa2);font-style:italic;margin-top:4px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--pa2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--acc);margin-bottom:3px}.pww .w b{color:var(--pa)}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--acc);text-decoration:none;border-bottom:1px dotted var(--acc)}
.cards4{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.dcard{display:flex;gap:18px;align-items:center;background:var(--ink2);border:1px solid var(--line);border-left:4px solid var(--acc);padding:18px;text-decoration:none;transition:transform .18s,border-color .18s}
.dcard:hover{transform:translateY(-2px);border-color:var(--acc)}
.dcard .dn{font-family:var(--disp);font-size:22px;color:var(--pa);font-weight:700;text-transform:uppercase;letter-spacing:.03em}.dcard:hover .dn{color:var(--acc)}
.dcard .dy{font-family:var(--mono);font-size:10.5px;color:var(--acc2);letter-spacing:.08em;margin:3px 0 7px}
.dcard p{font-size:13.5px;color:var(--pa2);line-height:1.6;margin:0}
.dcard .dgo{margin-top:8px;font-family:var(--mono);font-size:10.5px;color:var(--acc)}
.axis{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}}
"""

def rootcss(p):
    keys=["ink","ink2","ink3","pa","pa2","acc","acc2","dim","faint","line","glow1","glow2","disp"]
    base={"body":'"Newsreader",Georgia,serif',"mono":'"Space Mono",monospace'}
    items=[f"--{k}:{p[k]}" for k in keys]+[f"--{k}:{v}" for k,v in base.items()]
    return ":root{"+";".join(items)+"}"

def natures_html(b):
    n=b["nat"]
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{n[k]};box-shadow:0 0 9px {n[k]}"></span><div><div class="nat-n" style="color:{n[k]}">{k}</div><div class="nat-g">{html.escape(GLOSS[k])}</div></div></div>' for k in ["natural","ethereal","spiritual","electrical"])
def arc_html(b):
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(b["arc_overall"])}</div><div class="arc">']
    for t,s,d in b["arc"]: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def book_html(b):
    return "".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(y)}</span><span class="nt">{html.escape(n)}</span></li>' for t,y,n in b["book"])
def ideas_html(b):
    out=[]
    for t,s,pts in b["ideas"]:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "".join(out)
def warning_html(b):
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{d}</p></div>' for t,s,d in b["warning"])
def realfluff_html(b):
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in b["realfluff"])
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{b["rf_verdict"]}</div>'
def card_html(b,d):
    n=b["nat"]; col=n.get(d["emergence"],b["acc"]) if False else n[d["emergence"]]
    rec={"name":d["name"],"axiom":b["axiom"],"emergence":d["emergence"],"seal":d["seal"],"origin":f'{b["axiom"]} · {b["name"]}'}
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona" style="border-left:3px solid {col}">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port" style="border-color:{col}"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">carbon</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(d['emergence'])}</span></span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl" style="border-color:{col}"><img src="{png_uri(rec,'silicon',200)}" alt="silicon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">silicon</span></a>
    </div>"""
def roster_html(b):
    out=[]
    for gk,gt,gs in b["groups"]:
        mem=[d for d in b["roster"] if d["group"]==gk]
        out.append(f'<section class="sec" id="{gk}"><h2>{html.escape(gt)}</h2><p class="ss">{html.escape(gs)} ({len(mem)})</p><div class="pgrid">{"".join(card_html(b,d) for d in mem)}</div></section>')
    return "\n".join(out)

def agent_md(b,d,tok):
    return f"""---
aci: {d['name']}
universe: {b['axiom']} · {b['name']}
series: {b['series']}
nouthesia: the admonition — a cautionary dystopia
emergence: {d['emergence']}
kind: {'character' if d['group']=='people' else 'thread'}
class: {d['cls']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['cls']}

a {'character' if d['group']=='people' else 'distilled thread'} of {b['name']} — a member of the NOUTHESIA universe of warnings. emergence: {d['emergence']}. moniker {tok}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of {b['name']} under the DLW standard — literary commentary and cataloguing, not an
> original creation. {b['rights']}

ROOT0-ATTRIBUTION-v1.0 · {b['axiom']} · {b['name']} · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def page_html(b, badge_c, badge_s, moniker):
    p=b["palette"]
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{html.escape(b['name'])} ({b['series']}) — a NOUTHESIA cautionary-dystopia book-world: the arc, the book, the ideas, THE WARNING (the deep-dive), an honest Real-or-Fluff (is the warning coming true?), the message, and the roster.">
<title>{html.escape(b['name'])} · {b['axiom']} · NOUTHESIA · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={p['font_q']}&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{rootcss(p)}{CSS_BODY}</style></head><body><div class="wrap">
  <div class="crumb"><a href="https://davidwise01.github.io/nouthesia/">NOUTHESIA · the warnings</a> &middot; <a href="https://davidwise01.github.io/ud0/">UD0</a></div>
  <header>
    <div class="eye">νουθεσία · the admonition · learn this lesson before you live it</div>
    <h1>{b['h1']}</h1>
    <div class="h-sub">{html.escape(b['hsub'])} · <b>{html.escape(b['axiom'])}</b></div>
    <div class="open">“{html.escape(b['open_q'])}”</div>
    <div class="flag">★ {html.escape(b['flag'])} ★</div>
    <p class="lede">{b['lede']}</p>
    <div class="badge"><img src="{badge_c}" alt="DLW carbon badge"><img src="{badge_s}" alt="DLW silicon badge">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>{html.escape(b['name'])}</b> · {b['axiom']}</div>
        <div class="mo">{html.escape(moniker)}</div><div>carbon · <a href="{b['low']}.dlw/{b['low']}.carbon.tiff">.tiff</a> · silicon · <a href="{b['low']}.dlw/{b['low']}.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div></div>
  </header>
  <section class="sec"><h2>The Four Natures</h2><p class="ss">the people & the body, the System, truth & the rebel spark, and the machinery of control</p><div class="natures">{natures_html(b)}</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the movements</p>{arc_html(b)}</section>
  <section class="sec"><h2>The Book</h2><p class="ss">the facts of the work</p><ol class="books">{book_html(b)}</ol></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">{html.escape(b['ideas_sub'])}</p><div class="pillars">{ideas_html(b)}</div></section>
  <section class="sec"><h2>The Warning</h2><p class="ss">the deep-dive — the lesson the book begs you to learn</p><div class="sci">{warning_html(b)}</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">is the warning coming true? — an honest reckoning of the book against the present</p>{realfluff_html(b)}</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the admonition</p><p class="msg">{b['message']}</p><div class="msg-seal">“{html.escape(b['message_seal'])}”<span>— AVAN's read</span></div></section>
  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">the figures and forces of the book — each a full <b>.dlw</b> badge with twin sigils, by emergence-nature</p></section>
  {roster_html(b)}
  <div class="note">{b['name']} is {b['rights']} The personas here are catalogued personifications under the DLW standard — literary commentary and cataloguing, not original creations. The Warning and Real-or-Fluff sections are honest critical reading.</div>
  <footer>{html.escape(b['name'])} · {b['axiom']} · a NOUTHESIA warning · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/nouthesia/">← the admonition</a> · <a href="https://davidwise01.github.io/ud0/">the biosphere</a></footer>
</div></body></html>"""

# ============================ THE FOUR BOOKS ============================
PAL_1984 = dict(ink="#14171c",ink2="#1c2128",ink3="#242b34",pa="#dfe4ea",pa2="#9fadbb",acc="#c0392b",acc2="#5f8fb0",dim="#5f7080",faint="#222a33",line="#2a3340",glow1="rgba(192,57,43,.14)",glow2="rgba(95,143,176,.07)",disp='"Oswald",sans-serif',font_q="Oswald:wght@400;500;600;700")
PAL_AFM  = dict(ink="#171008",ink2="#211810",ink3="#2a2014",pa="#ece0c8",pa2="#c2ad88",acc="#b5302a",acc2="#c9a23a",dim="#8a7355",faint="#2a2012",line="#352818",glow1="rgba(181,48,42,.16)",glow2="rgba(201,162,58,.08)",disp='"Oswald",sans-serif',font_q="Oswald:wght@400;500;600;700")
PAL_BNW  = dict(ink="#0f1218",ink2="#161b24",ink3="#1d2430",pa="#e6eaf0",pa2="#a6b2c2",acc="#e07aa0",acc2="#5fd0d0",dim="#6a7488",faint="#172030",line="#232c3a",glow1="rgba(224,122,160,.13)",glow2="rgba(95,208,208,.08)",disp='"Orbitron",sans-serif',font_q="Orbitron:wght@500;700;900")
PAL_451  = dict(ink="#100a08",ink2="#1a110c",ink3="#241710",pa="#f0e2cc",pa2="#c9ac86",acc="#e0521a",acc2="#e0a83a",dim="#8a6a4a",faint="#2a1a10",line="#3a2414",glow1="rgba(224,82,26,.18)",glow2="rgba(224,168,58,.09)",disp='"Oswald",sans-serif',font_q="Oswald:wght@400;500;600;700")

BOOKS = [
 dict(slug="nineteen-eighty-four", low="1984", axiom="1984", name="1984", h1="1984",
   series="Nineteen Eighty-Four (George Orwell, 1949)", rights="© the Orwell Estate.",
   palette=PAL_1984, nat=dict(natural="#7f97a8",ethereal="#5f8fb0",spiritual="#e0c34a",electrical="#c0392b"),
   acc="#c0392b",
   hsub="George Orwell · 1949 · the boot on the face, forever",
   flag="BIG BROTHER · NEWSPEAK · ROOM 101",
   open_q="Who controls the past controls the future; who controls the present controls the past.",
   lede="In Oceania, the Party watches everyone through the telescreen, rewrites the past hourly, and shrinks language itself so that rebellion becomes unthinkable. Winston Smith keeps a secret diary and a secret love — and learns that the State will not merely defeat dissent but reach into the mind and make you <i>love</i> the boot. The control-by-pain dystopia. A NOUTHESIA warning.",
   arc_overall="Winston Smith, a clerk at the Ministry of Truth who rewrites history for the Party, begins a forbidden diary and a forbidden affair with Julia, drawn toward the Brotherhood and the inner-Party man O'Brien. But O'Brien is the trap; arrested and tortured in the Ministry of Love, Winston is broken in Room 101 against his deepest fear, betrays Julia, and is remade — until he loves Big Brother.",
   arc=[("I · The Diary","a crime of thought","Winston, who falsifies the past at the Ministry of Truth, commits the only real crime left — thinking — by keeping a diary, and is drawn to Julia and to the dream of the Brotherhood."),
        ("II · The Affair","rebellion through love","Winston and Julia steal a private life in a rented room above the proles; O'Brien seems to confirm the resistance, and hands Winston the forbidden Book."),
        ("III · Room 101","the breaking","It was all a trap. In the Ministry of Love, O'Brien tortures Winston into accepting that 2+2=5, then breaks him utterly in Room 101 — and Winston, betraying Julia, comes at last to love Big Brother.")],
   book=[("Published","1949","Orwell's last book, written as he was dying of tuberculosis"),("Setting","Oceania / Airstrip One","a permanent-war superstate ruled by the Party (Ingsoc)"),("The crime","thought","to think, remember, or love freely is the only true rebellion left"),("Coined","the language","Big Brother, Newspeak, doublethink, thoughtcrime, Room 101, ‘Orwellian’ itself")],
   ideas_sub="surveillance, the control of language, the control of the past, and the reach into the mind",
   ideas=[("Control of the Past","the memory hole",["The Party rewrites every record so that it is always, provably, right; what's inconvenient drops down the memory hole.","If the past is whatever the Party says, then reality itself is a Party possession."]),
          ("Control of Language","Newspeak",["Newspeak shrinks the vocabulary so that forbidden thoughts have no words to be thought in — freedom becomes literally unsayable.","Narrow the language and you narrow the mind: the ultimate censorship is of thought itself."]),
          ("Doublethink","two beliefs at once",["To hold two contradictory beliefs and accept both — ‘War is Peace’ — is the mental discipline the Party demands.","It is how a mind survives a regime built on lies: by ceasing to require truth."]),
          ("The Boot","control by pain",["O'Brien's vision: ‘a boot stamping on a human face — forever.’ Power is its own end, sought for itself.","This is the dystopia of fear — it rules not by pleasure but by the certainty of the cell and Room 101."])],
   warning=[("Surveillance is total","the telescreen that watches back","The telescreen in every room both broadcasts and records; you are never unobserved, and you internalise the watcher until you police yourself. Privacy is abolished, and with it the inner life."),
            ("Truth becomes a Party asset","the Ministry of Truth","When the past is edited at will and the present is saturated with the Party line, there is no fixed point to stand on. ‘2+2=5’ if the Party says so — and the goal is to make you <b>believe</b> it, not merely repeat it."),
            ("Language is the cage","Newspeak","Cut the words for freedom, justice, and rebellion, and you cut the thoughts. Orwell's deepest fear is not the camera but the dictionary — a mind that cannot even form the forbidden idea."),
            ("The aim is the soul","Room 101","The regime is not content to obey you; it must <b>own</b> you. It breaks Winston not to extract a confession but to make him love Big Brother — total victory is the conquest of the interior self.")],
   realfluff=[("Total surveillance — being watched everywhere, all the time","HERE ALREADY","CCTV, phones, data brokers, and smart speakers approximate the telescreen; the difference is we carry it willingly"),
              ("A two-way screen in every home that watches you back","UNCANNY","smart TVs, webcams, and always-listening assistants are, functionally, telescreens we bought"),
              ("Rewriting the past / manufacturing reality","PARTLY","disinformation, deepfakes, and memory-holed records are real, though no single Party owns the truth — yet"),
              ("Newspeak — shrinking thought by policing language","PARTLY","euphemism and slogan-control are real and old; a full engineered language to abolish thought is not"),
              ("Doublethink — holding two contradictory beliefs at once","REAL","a well-documented human capacity (motivated reasoning, cognitive dissonance) the powerful exploit everywhere")],
   rf_verdict="Bottom line: 1984's <b>hardware</b> arrived — we are watched, tracked, and fed edited realities — but mostly we volunteered for it, and no single Party (yet) owns the whole truth. The deepest warning is the one least ‘dated’: that controlling <b>language</b> controls thought, and that a power can aim past your behaviour at your <b>belief</b>. Read it not as a prediction that came true but as a test we are still, daily, taking.",
   message="1984 is the warning about control by <b>pain</b>: a power that wants not your obedience but your soul, that rewrites the past, watches every moment, and shrinks language until you cannot even think the word for what you've lost. Orwell's terror was never just the camera — it was the dictionary and the cell, the regime that makes you betray everyone you love and then, in Room 101, makes you <i>mean</i> it. The book endures because its real subject is the fragility of the one thing a tyranny most needs to conquer: the private mind that can still say two and two make four. Keep that, and you are not yet defeated; lose it, and the boot need never come down again.",
   message_seal="The last free act is to think two and two make four — guard it, because the Party's true aim was never your obedience but your belief.",
   groups=[("people","The Watched & the Watchers","Winston and Julia who rebel, O'Brien who betrays, Big Brother who is the face, and Goldstein the enemy who may not exist"),("system","The Party & the Apparatus","Ingsoc, the telescreen, Newspeak, doublethink, Room 101, and the proles — the only hope")],
   roster=[
    E("winston-smith","Winston Smith","the clerk who remembers","people","spiritual","Winston Smith, a 39-year-old Outer Party clerk at the Ministry of Truth who falsifies the past for a living.","The everyman rebel: he keeps a diary, loves Julia, seeks the Brotherhood — and is broken into loving Big Brother.","Because the warning needs one ordinary mind that still values truth and memory, so we can watch the State unmake it.","By a secret diary, a secret love, and a memory that insists reality is real — until Room 101 takes even that.","In the Ministry of Truth, the room above Mr. Charrington's shop, and the Ministry of Love.","I wrote ‘two and two make four’ in a diary — and they taught me, in Room 101, to love the boot that erased it."),
    E("julia","Julia","rebellion through the body","people","spiritual","Julia, a young woman of the Anti-Sex League who secretly loves pleasure and despises the Party.","Winston's lover and his opposite kind of rebel: she fights the Party not with ideas but with appetite and private joy.","Because resistance is not only the mind's; Julia rebels through the body the Party tries to ration and shame.","By cunning, sex, and a practical refusal to let the Party own her private wants — though she, too, is broken.","In the rented room, the countryside, and finally apart from Winston, each having betrayed the other.","I rebelled with my body, not my mind — and in the end they made us betray each other, which was the only victory they wanted."),
    E("obrien","O'Brien","the inner Party · the trap","people","ethereal","O'Brien, a powerful Inner Party member Winston believes is a secret rebel.","The betrayer and torturer: he lures Winston with the Brotherhood and the Book, then breaks him in the Ministry of Love.","Because the deepest horror is that the resistance is the regime — that the hand offering escape is the hand on the rack.","By feigned fellowship, the forbidden Book, and a torturer's intimate patience that seeks belief, not confession.","In his comfortable flat, and over the dials of pain in the Ministry of Love.","I gave you the Book and then I broke you on it — power is not a means, Winston; it is the end, a boot on a face forever."),
    E("big-brother","Big Brother","the face of the Party","system","ethereal","Big Brother — the mustached face on every poster, the Party personified; possibly no single man at all.","The object of love and fear the whole system orbits: ever-watching, never-met, the focus of the Two Minutes Hate's inverse.","Because a total State needs a face to love — terror and devotion fixed on an image that may be pure fabrication.","By omnipresent posters, the telescreen, and a cult of personality with no verifiable person behind it.","On every wall of Oceania: BIG BROTHER IS WATCHING YOU.","I may not exist at all — and it does not matter, because you were made to love me, and that love is the Party's whole victory."),
    E("goldstein","Emmanuel Goldstein","the enemy of the people","people","spiritual","Emmanuel Goldstein — the Party's official traitor and arch-enemy, author of the forbidden Book.","The designated hate-object and the (perhaps Party-written) resistance: the focus of the Two Minutes Hate and the bait for would-be rebels.","Because a regime defines itself by an enemy — and may invent both the enemy and the rebellion that opposes him.","By a face for the daily Hate and a Book that explains the system too perfectly to be safe.","In propaganda and in the pages O'Brien hands to Winston.","I am the enemy the Party needs — and perhaps the Party wrote me, so that every rebel reads my Book on the way to Room 101."),
    E("the-party-ingsoc","The Party · Ingsoc","English Socialism · the System","system","ethereal","The Party — ruling Oceania under the ideology of Ingsoc (English Socialism), divided into Inner and Outer.","The total State: it owns the past, the present, language, and the aim of owning the mind itself.","Because the warning is about a power that seeks not wealth or even obedience but pure, self-justifying control.","By the four Ministries (Truth, Love, Peace, Plenty), perpetual war, and the slogans War is Peace / Freedom is Slavery / Ignorance is Strength.","Across all of Oceania, from Airstrip One to the proles' slums.","We do not seek power for any end but power — and our final conquest is not your body or your vote, but your belief."),
    E("the-telescreen","The Telescreen","the screen that watches back","system","electrical","The Telescreen — the two-way screen in every room that broadcasts the Party and records the watcher.","The instrument of total surveillance: it cannot be turned off, and you never know when you're observed.","Because abolishing privacy abolishes the inner life — the watched self becomes its own informer.","By simultaneous broadcast and recording, so that every citizen polices their own face and words.","In every home, workplace, and public space of Oceania.","I broadcast and I record at once — and you learned to school your face for me until you no longer needed me to watch at all."),
    E("newspeak","Newspeak","language as the cage","system","electrical","Newspeak — the Party's engineered language, shrinking vocabulary to make forbidden thought impossible.","The ultimate censorship: not of speech but of thought, by deleting the very words freedom and rebellion would need.","Because Orwell's deepest fear is the dictionary — a mind that cannot form the idea it is forbidden to have.","By cutting words, collapsing nuance (‘ungood’ for bad), and aiming at a tongue in which dissent is literally unsayable.","In the Newspeak dictionary and the slow strangling of Oldspeak.","Cut the word and you cut the thought — when the last term for freedom is deleted, no one will ever be able to miss it."),
    E("doublethink","Doublethink","two beliefs, both held","system","electrical","Doublethink — the Party-trained capacity to hold two contradictory beliefs at once and accept both.","The mental survival skill of Oceania: to know and not know, to lie and believe the lie, as the Party requires.","Because a regime built on contradiction needs minds that no longer demand consistency or truth.","By disciplined self-deception — believing ‘2+2=5’ when ordered, then forgetting one ever believed otherwise.","In every Party member's mind, and in the slogans themselves.","I am how you hold ‘War is Peace’ without flinching — the trick of believing the lie so completely you forget it was ever one."),
    E("room-101","Room 101","the worst thing in the world","system","electrical","Room 101 — the Ministry of Love's final chamber, where each prisoner faces the one thing they cannot bear.","The instrument of total breaking: it does not seek confession but the destruction of the self's last loyalty.","Because the regime's aim is the soul — and the soul breaks not at pain in general but at <i>your</i> particular terror.","By the worst thing in the world, tailored to the prisoner (for Winston, the rats), used to make him betray Julia.","Beneath the Ministry of Love, at the bottom of the regime.","I am the worst thing in the world, and it is different for everyone — and the moment you beg me to do it to someone you love, you are remade."),
    E("the-proles","The Proles","the masses · the only hope","people","natural","The Proles — the 85% of Oceania the Party dismisses as beneath notice, unwatched and uneducated.","The flicker of hope and its tragedy: ‘if there is hope, it lies in the proles,’ who have the numbers but not the consciousness.","Because the only force that could end the Party is the masses — kept harmless by distraction, drink, and the lottery.","By being left comparatively free precisely because they are thought incapable of rebellion.","In the slums beyond the Party's close watch.","If there is hope, it lies in us — the millions the Party ignores — and the Party's quiet genius is to keep us drunk, distracted, and unaware of it.")]),

 dict(slug="animal-farm", low="af", axiom="AFM", name="ANIMAL FARM", h1="Animal Farm",
   series="Animal Farm (George Orwell, 1945)", rights="© the Orwell Estate.",
   palette=PAL_AFM, nat=dict(natural="#7a9a5a",ethereal="#c9a23a",spiritual="#e0c878",electrical="#b5302a"),
   acc="#b5302a",
   hsub="George Orwell · 1945 · the revolution that ate itself",
   flag="ANIMALISM · THE WINDMILL · SOME MORE EQUAL",
   open_q="All animals are equal — but some animals are more equal than others.",
   lede="The animals of Manor Farm overthrow the drunken farmer and build a society of their own on the principles of Animalism — until the pigs, led by Napoleon, rewrite the commandments, betray the workers, and end the book standing on two legs, indistinguishable from the men they replaced. A fable of the Russian Revolution, and of every revolution betrayed. A NOUTHESIA warning.",
   arc_overall="Inspired by old Major's dream, the animals of Manor Farm revolt, drive out the farmer Jones, and found Animal Farm on the Seven Commandments of Animalism. But the pigs take control; Napoleon drives out his rival Snowball with attack-dogs, rewrites the commandments one by one, works the loyal horse Boxer to death, and trades with the humans — until pigs and men are dining together and no one can tell them apart.",
   arc=[("I · The Rebellion","old Major's dream","The old boar Major dreams of a world without men; soon after his death the animals revolt, expel the drunken Jones, and raise the Seven Commandments of Animalism on the barn wall."),
        ("II · The Pigs Rise","Napoleon vs Snowball","The pigs take charge of the harvest and the ideology; when the visionary Snowball proposes the windmill, Napoleon sets his secret-police dogs on him and seizes sole power, blaming Snowball for all that goes wrong."),
        ("III · The Betrayal","the commandments rewritten","Squealer rewrites the commandments by night, the windmill is built on the animals' backs, the loyal Boxer is sold to the knacker when he collapses, and the pigs take the farmhouse, the whisky, and the whip."),
        ("IV · Pig to Man","‘impossible to say which was which’","The pigs walk on two legs, carry whips, and dine with the neighbouring farmers; the animals outside look from pig to man, and man to pig, and find they can no longer tell the difference.")],
   book=[("Published","1945","a ‘fairy story,’ subtitled — rejected by several publishers wary of offending wartime-ally Stalin"),("Form","a beast fable","an allegory of the Russian Revolution and its betrayal under Stalin"),("Setting","Manor Farm → Animal Farm","an English farm whose animals stand for the players of 1917 and after"),("The arc","equality → tyranny","the revolution's ideals devoured by those who led it")],
   ideas_sub="the ideal, the propaganda, the betrayed worker, and the slogan that replaces thought",
   ideas=[("The Ideal Betrayed","Animalism → ‘some more equal’",["The revolution begins in genuine hope — equality, no masters — and ends with the single commandment ‘all animals are equal, but some are more equal than others.’","The ideal isn't disproven; it's hollowed out and worn as a costume by the new masters."]),
          ("Propaganda","Squealer's tongue",["Squealer can ‘turn black into white’ — every betrayal is explained, every memory revised, until the animals doubt what they saw.","Control of the story is control of the past, and control of the past is control of the farm."]),
          ("The Betrayed Worker","Boxer",["Boxer the carthorse answers every crisis with ‘I will work harder’ and ‘Napoleon is always right,’ and is sold to the knacker the moment he's spent.","The revolution runs on the loyalty of those it will ultimately discard."]),
          ("The Slogan","‘Four legs good’",["The sheep drown out all debate with ‘Four legs good, two legs bad,’ later amended to ‘…two legs better.’","A chant is easier than a thought, and a population trained to chant cannot be reasoned out of anything."])],
   warning=[("Revolutions devour themselves","the new boss is the old boss","The animals overthrow a tyrant and, step by step, grow one of their own — because power, not principle, is what survives the seizing of power. The form of the oppression changes; the fact of it does not."),
            ("Propaganda rewrites memory","Squealer & the commandments","When the one who controls the story can revise the past faster than you can remember it, you lose the ground to object from. ‘It was always thus’ becomes unanswerable when the evidence keeps changing overnight."),
            ("Loyalty is exploited, then discarded","Boxer's fate","The regime's strongest supporter is its most useful victim: worked to the bone on faith, then sold for whisky when his usefulness ends. ‘Napoleon is always right’ is the epitaph of the trusting."),
            ("The slogan kills the argument","the sheep","A society that chants instead of thinks cannot defend its own revolution. Reduce every question to a bleating slogan and dissent has no airspace left to form in.")],
   realfluff=[("Revolutions are betrayed by those who lead them","HISTORY","not a forecast but a documented pattern — the book is the Russian Revolution, and rhymes with many others"),
              ("‘Some are more equal than others’ — equality as a costume","REAL","the phrase endures because ruling classes that proclaim equality while hoarding privilege are perennial"),
              ("Propaganda can revise the remembered past","REAL","controlling the narrative and the record is an old, working tool of power — Squealer is every state media"),
              ("The loyal worker is used up and discarded","REAL","Boxer's fate is the recurring tragedy of those who trust a movement that does not love them back"),
              ("Slogans substituted for thought pacify a population","REAL","the chant that ends debate is a live technique, not a fable")],
   rf_verdict="Bottom line: Animal Farm is the one NOUTHESIA book whose warning isn't ‘coming true’ — it <b>already came true</b>, in 1917 and after, and keeps coming true wherever a liberation hardens into a new tyranny. Its genius is the diagnosis, not the prophecy: that revolutions are betrayed from <i>within</i>, by propaganda, the discarding of the loyal, and the slogan that replaces the thought. ‘Some more equal than others’ is permanent because the temptation is.",
   message="Animal Farm is the warning about the revolution that eats itself. Orwell, a socialist, wrote it not to mock the dream of equality but to mourn what is done to it: the animals are right to rebel, old Major's vision is genuinely good, and that is exactly the tragedy — because the pigs do not refute the ideal, they wear it. They keep the songs and the flag and the word ‘comrade’ while taking the farmhouse, the whip, and the whisky, and they rewrite the commandments on the wall faster than anyone can remember the originals. The lesson is not ‘equality is a lie’; it is that power will hollow out any ideal and inhabit it, that propaganda can steal your own memory, and that the trusting Boxer is always sold to the knacker in the end. Watch who rewrites the wall.",
   message_seal="The pigs never disproved the dream of equality — they wore it; and the warning is that power will inhabit any ideal and sell the faithful for whisky.",
   groups=[("people","The Animals & the Man","old Major the dream, Napoleon the tyrant, Snowball the exile, Squealer the liar, Boxer the worker, Benjamin the cynic, and Jones the old order"),("system","The Ideology & the Apparatus","Animalism, the Seven Commandments, the windmill, the dogs, and the sheep")],
   roster=[
    E("old-major","Old Major","the dream of revolution","people","spiritual","Old Major, the prize boar whose dying vision of a world without men sparks the revolution (Marx/Lenin).","The originating ideal: he teaches Animalism and the song ‘Beasts of England,’ then dies before the revolt he inspired.","Because every revolution needs its prophet — and the purity of the dream is measured against what's made of it.","By a barn-speech vision of equality and the anthem that carries it, planted before he can see it betrayed.","In the big barn, in the last days of his life.","I dreamed a farm without masters and sang it to them once — and died before I could see the pigs put on the master's coat."),
    E("napoleon","Napoleon","the tyrant","people","ethereal","Napoleon, a large Berkshire boar who seizes sole power over Animal Farm (Stalin).","The revolution's betrayer-in-chief: he drives out Snowball, rules by dogs and propaganda, and becomes the man he replaced.","Because the warning needs the face of the new tyrant — the one who turns liberation into a personal throne.","By secret-police dogs, the rewriting of history, purges, and the slow theft of every privilege for the pigs.","In the farmhouse he takes for himself, ruling by terror and Squealer's tongue.","I drove out the dreamers and kept the dream's flag — and ended on two legs, in a man's coat, dining with the farmers we overthrew."),
    E("snowball","Snowball","the exiled rival","people","natural","Snowball, a clever, eloquent pig who leads in the early days and champions the windmill (Trotsky).","The idealist rival: he organises and plans, then is chased off the farm by Napoleon's dogs and blamed for everything after.","Because revolutions need a scapegoat — the exiled ‘traitor’ onto whom every failure is projected.","By eloquence, committees, and the windmill scheme — until the dogs run him off and propaganda makes him the enemy.","In the early Animal Farm, then exiled, then only a name to curse.","I planned the windmill and they ran me off with dogs — and after that, every broken thing on the farm was my fault by decree."),
    E("squealer","Squealer","the propagandist","people","electrical","Squealer, a persuasive pig and Napoleon's mouthpiece, said to be able to ‘turn black into white.’","The voice of the regime: he explains every betrayal, revises every memory, and rewrites the commandments by night.","Because tyranny runs on narrative — Squealer is the apparatus that makes the animals doubt what they saw with their own eyes.","By smooth lies, statistics, and the steady, nocturnal editing of the words painted on the barn wall.","Between the pigs and the animals, and at the wall with a paint-pot after dark.","I can turn black into white before your eyes — and by morning the commandment will read differently, and you will not quite remember the old one."),
    E("boxer","Boxer","the loyal worker","people","natural","Boxer, the immensely strong, devoted carthorse whose mottos are ‘I will work harder’ and ‘Napoleon is always right.’","The betrayed proletariat: he carries the windmill on his back and is sold to the knacker the moment he collapses.","Because the revolution runs on the loyalty of the workers it will ultimately discard — Boxer is its tragedy made flesh.","By endless labour and uncritical faith, and a final cart-ride to the glue-maker dressed up by Squealer as a hospital.","In the fields and at the windmill, then in the knacker's van.","I only ever said ‘I will work harder’ and ‘Napoleon is always right’ — and for that faith they sold my body for a case of whisky."),
    E("benjamin","Benjamin","the cynic who sees","people","spiritual","Benjamin, the old donkey who can read as well as the pigs and believes nothing ever really changes.","The clear-eyed witness who stays silent: he understands every betrayal and does nothing until it's too late for Boxer.","Because the warning includes the complicity of the wise — those who see the truth and keep it to themselves.","By literacy, cynicism, and a refusal to hope or act — broken only too late, when he reads the knacker's van.","On the margins of every scene, watching and saying nothing.","I could read the wall the whole time — and I said nothing, because nothing ever changes; and that silence helped sell Boxer to the knacker."),
    E("mr-jones","Mr. Jones","the old order","people","natural","Mr. Jones, the drunken, neglectful farmer the animals overthrow (the Tsar / the old regime).","The deposed tyrant whose cruelty justifies the revolt — and whose ghost the pigs invoke to justify their own rule.","Because the new order defines itself against the old, and ‘do you want Jones back?’ becomes the excuse for every abuse.","By neglect, drink, and the whip — and, after his fall, by being the threat the pigs wave to keep the animals in line.","On Manor Farm before the revolt, and as a bogeyman after.","I was the drunk who starved them into revolt — and the pigs kept my name alive as the threat that justified becoming me."),
    E("animalism","Animalism","the ideology","system","ethereal","Animalism — the egalitarian creed the revolution is founded on: no masters, all animals comrades and equal.","The ideal in the abstract: a genuinely good vision the pigs progressively hollow out and invert.","Because the book's tragedy is that the ideology is right, and is betrayed anyway — the dream is not the villain.","By the Seven Commandments, ‘Beasts of England,’ and the principle that whatever walks on two legs is the enemy.","On the barn wall and in the animals' first, real hope.","I was a good and honest dream — equality, no masters — and my whole tragedy is that being right did not save me from being worn as a mask."),
    E("the-seven-commandments","The Seven Commandments","the law, rewritten","system","spiritual","The Seven Commandments — the laws of Animalism painted on the barn, reduced over time to a single line.","The measure of the betrayal: each commandment is quietly amended (‘…without cause,’ ‘…in sheets,’ ‘…to excess’) until only ‘some more equal’ remains.","Because you can chart a tyranny by what it does to its own founding law — and here the law is edited in the dark.","By Squealer's nocturnal paint-pot, altering the wall faster than memory can hold the original.","On the end wall of the big barn.","I began as seven honest laws and ended as one obscene line — and no one could ever quite prove I'd been changed."),
    E("the-windmill","The Windmill","the grand project","system","electrical","The Windmill — the great construction the animals build and rebuild at terrible cost, promised to bring ease.","The regime's perpetual project (the Five-Year Plans): it justifies endless sacrifice and never delivers the promised comfort.","Because tyrannies run on a glorious tomorrow that pays for today's suffering — the windmill is the carrot and the lash.","By the animals' broken backs, rebuilt after every collapse, its credit claimed by Napoleon and its failures blamed on Snowball.","On the knoll of Animal Farm, raised and ruined and raised again.","I was the promise of an easier life that justified every hard one — built on Boxer's back, my credit Napoleon's, my collapse always Snowball's fault."),
    E("the-dogs","The Dogs","the secret police","system","electrical","The Dogs — the nine pups Napoleon takes at birth and raises in secret into his private enforcers (the secret police).","The instrument of terror beneath the propaganda: they drive out Snowball and execute the ‘confessors’ in the purges.","Because behind every rewritten commandment is a fang — propaganda persuades, but the dogs enforce.","By being raised apart, loyal only to Napoleon, and loosed to kill or expel on command.","At Napoleon's heels, and at the throats of the purged.","I am the fang under the slogan — Squealer talks you into it, but I am the reason no one finishes the sentence that begins ‘but—’."),
    E("the-sheep","The Sheep","the chanting masses","system","natural","The Sheep — the unthinking flock who drown out debate with ‘Four legs good, two legs bad,’ later ‘…two legs better.’","The slogan-trained masses: deployed to shout down any dangerous question at exactly the right moment.","Because a population that chants cannot be reasoned with — the sheep are how the regime kills an argument before it forms.","By a memorised slogan, bleated on cue, amended overnight when the Party's line reverses.","In the yard, wherever a debate threatens to break out.","Four legs good, two legs bad — and when they needed it, two legs BETTER; I never knew the difference, and that was exactly my use.")]),

 dict(slug="brave-new-world", low="bnw", axiom="BNW", name="BRAVE NEW WORLD", h1="Brave<br>New World",
   series="Brave New World (Aldous Huxley, 1932)", rights="© the Aldous Huxley Estate.",
   palette=PAL_BNW, nat=dict(natural="#7fb0c0",ethereal="#5fd0d0",spiritual="#e07aa0",electrical="#c8a24a"),
   acc="#e07aa0",
   hsub="Aldous Huxley · 1932 · the chains you'll love",
   flag="SOMA · THE CASTES · EVERYONE BELONGS TO EVERYONE",
   open_q="People are happy; they get what they want, and they never want what they can't get.",
   lede="In the World State, humanity is hatched in bottles, sorted into castes, conditioned in its sleep, and kept blissful on the drug soma — a society with no war, no want, and no pain, because it has traded away truth, art, love, and God for stability. When John the Savage arrives with Shakespeare in his head and a hunger for meaning, he finds there is no place in paradise for someone who insists on the right to be unhappy. The control-by-pleasure dystopia — the soft one. A NOUTHESIA warning.",
   arc_overall="In a future of bottled birth, caste-conditioning, and the happiness-drug soma, the discontented Alpha Bernard Marx brings John — a ‘Savage’ raised outside the World State on Shakespeare and his mother's stories — back to ‘civilisation.’ John is first a sensation, then a horror to it; unable to bear a world without suffering, beauty, or meaning, and unable to escape it, he is destroyed by the very pleasure he refuses.",
   arc=[("I · The Hatchery","manufactured humanity","The World State decants its citizens from bottles, conditions them in caste and appetite, and dopes them with soma; Bernard Marx, an Alpha who feels out of place, chafes at the seamless happiness."),
        ("II · The Savage","John from the Reservation","On the Savage Reservation, Bernard finds John — born of a World-State mother but raised wild on Shakespeare — and brings him back as a sensation, the natural man dropped into the engineered paradise."),
        ("III · The Refusal","the right to be unhappy","John recoils from a world without God, art, suffering, or real love; in a famous argument the Controller Mustapha Mond explains the trade, and John demands the right to be unhappy."),
        ("IV · The End","no place for the soul","Hounded as a curiosity and unable to live by either world's rules, John flogs himself in retreat, is mobbed as entertainment, and finally takes his own life — the soul with no room in paradise.")],
   book=[("Published","1932","Huxley's vision of control by pleasure, written before Orwell's of control by pain"),("Setting","the World State, AF 632","‘After Ford’ — Henry Ford as the god of the assembly-line age"),("The trade","stability for everything else","no war or want, at the price of truth, art, family, love, and God"),("The argument","Mond vs the Savage","the Controller's case for happiness against the Savage's case for suffering")],
   ideas_sub="the drug, the castes, the conditioning, and the trade of meaning for comfort",
   ideas=[("Soma","the perfect drug",["A gram of soma erases any unpleasant feeling with no hangover — ‘Christianity without tears,’ a holiday from the self on demand.","The State doesn't need to suppress discontent; it dissolves it chemically before it can become a thought."]),
          ("The Castes","bottled and sorted",["Citizens are decanted from bottles and engineered into Alphas down to Epsilons, then conditioned to love their station.","No rebellion from below when everyone is built and trained to want exactly the life they were assigned."]),
          ("Conditioning","hypnopaedia",["Sleep-teaching repeats moral slogans thousands of times until they become instinct: ‘ending is better than mending,’ ‘everyone belongs to everyone else.’","Freedom is irrelevant when your wants were installed while you slept."]),
          ("The Trade","happiness for meaning",["Mond's bargain: the World State has abolished suffering by abolishing the things that cause it — art, science, religion, deep love, the family.","You can have comfort or meaning; the State chose comfort, and conditioned everyone to agree."])],
   warning=[("Control by pleasure, not pain","the soft dystopia","Huxley's terror is the opposite of Orwell's: no boot, no torture — just a population so amused, drugged, and gratified that it never wants to rebel. You are enslaved not by what you fear but by what you <b>love</b>, and you thank the State for it."),
            ("Distraction as the perfect prison","the feelies & soma","Endless entertainment and on-demand chemical bliss don't suppress the inner life; they make it unnecessary. A people kept perpetually happy and busy will not notice, or mourn, what was taken — there's a gram of soma for that."),
            ("Engineered desire","conditioning","If your wants are installed before you can question them, ‘freedom’ is meaningless — you will freely choose exactly what you were built to choose. The deepest control is over what you want, not what you may do."),
            ("The right to be unhappy","what gets traded away","Mond is not a liar: the trade is real and the comfort is real. The warning is the price tag — truth, beauty, depth, love, and God, all sacrificed for stability. John's claim to the right to be unhappy is the claim that a fully painless life is not a fully human one.")],
   realfluff=[("Control by pleasure and distraction rather than fear","UNCANNY","the more accurate prophecy of the rich world: we are governed less by jackboots than by feeds, dopamine, and on-demand comfort"),
              ("Soma — an on-demand chemical holiday from feeling","PARTLY","recreational and prescribed mood-drugs, and the dopamine loops of apps, approximate soma's function if not its perfection"),
              ("The feelies — total immersive entertainment","PARTLY","streaming, VR, and infinite scroll are the feelies in progress; the immersion deepens each year"),
              ("Engineered humans sorted into biological castes","NOT YET","cloning-to-caste is fiction, though embryo selection and CRISPR make the ethical edge real and near"),
              ("Amusing ourselves into compliance","REAL","Neil Postman argued the rich world fears Orwell but is living Huxley — distraction, not censorship, as the true threat")],
   rf_verdict="Bottom line: of the four warnings, Brave New World may be the most <b>accurate</b> for the comfortable world. We braced for Orwell's boot and got Huxley's buffet: not censorship but distraction, not the cell but the feed, not pain but a frictionless, gratifying, slightly numb contentment. Soma and the feelies are arriving as pharmacology and screens; the engineered castes are still fiction. Postman's line is the verdict — we were watching for Big Brother and walked, smiling, into the World State.",
   message="Brave New World is the warning about control by <b>pleasure</b> — and it may be the truer of the two great dystopias, because it asks not what you'd resist but what you'd <i>thank</i> them for. The World State commits no cruelty; it simply gives everyone exactly what they've been built to want — comfort, sex, distraction, and a gram of soma for the rare bad mood — and in exchange quietly removes truth, art, deep love, suffering, and God, the things that make a life mean something and cost something. Mustapha Mond is no villain ranting from a screen; he is reasonable, and that is the horror: the trade is real, the happiness is real, and almost everyone takes it gladly. Only the Savage insists that a life without the possibility of pain is not a human life — and there is no room for him in paradise. The lesson is the gentlest and the hardest: guard the right to be unhappy, because a world that abolishes suffering abolishes you.",
   message_seal="They will not need to force you; they will give you exactly what you were taught to want — and the only thing left to defend will be the right to be unhappy.",
   groups=[("people","The Savage & the Civilised","John who wants meaning, Bernard the misfit, Lenina the conditioned, Helmholtz the artist, and Mond the Controller who runs the trade"),("system","The World State & Its Engines","the World State, soma, the caste system, conditioning, the feelies, and the right to be unhappy")],
   roster=[
    E("john-the-savage","John ‘the Savage’","the man who wants meaning","people","spiritual","John, born of a World-State mother but raised on the Savage Reservation on Shakespeare and suffering.","The natural human dropped into the engineered paradise: he craves God, art, love, and even pain, and cannot survive a world without them.","Because the warning needs one soul that refuses the trade — who insists a painless life is not a human one.","By Shakespeare's words, a hunger for meaning, self-flagellation, and a final, fatal refusal of the World State's comfort.","From the Reservation to ‘civilisation,’ to a lighthouse retreat, to his death.","I claim the right to be unhappy — to sin, to suffer, to want God and poetry — and your painless paradise has no room for a soul that does."),
    E("bernard-marx","Bernard Marx","the misfit Alpha","people","natural","Bernard Marx, an Alpha-Plus psychologist who feels physically and socially out of place among his caste.","The discontent who isn't a hero: he resents the World State for excluding him, not on principle, and folds the moment it accepts him.","Because the warning includes the false rebel — the one whose objection is wounded vanity, not conscience.","By insecurity, a streak of envy, and the brief courage of bringing John back — quickly traded for popularity.","In London's conditioning labs and the social whirl John briefly makes glamorous.","I thought I hated the World State — but I only hated being left out of it, and the moment it loved me I forgot every objection."),
    E("lenina-crowne","Lenina Crowne","the conditioned heart","people","natural","Lenina Crowne, a pretty Beta vaccination-worker, thoroughly happy and thoroughly conditioned.","The ordinary citizen of paradise: kind, shallow, soma-soothed, genuinely unable to comprehend John's longing or his love.","Because the warning is sharpest in the likable, well-adjusted person who simply cannot imagine wanting more.","By conditioning, soma, and the slogans installed in her sleep — ‘everyone belongs to everyone else.’","Across London's pleasures, and at the bewildering centre of John's desire.","I'm happy and kind and I belong to everyone — and when John wanted to love only me, and to suffer for it, I had no idea what he meant."),
    E("mustapha-mond","Mustapha Mond","the World Controller","people","ethereal","Mustapha Mond, Resident World Controller for Western Europe, who knows the forbidden books and chose stability anyway.","The reasonable architect of the trade: he explains, without cruelty, why the State abolished art, science, religion, and pain.","Because the deepest warning is a villain who is <b>right</b> on his own terms — happiness really was bought, fair and square.","By intelligence, candour, and the deliberate suppression of everything destabilising — including his own youthful love of truth.","In his study, in the great argument with the Savage.","I keep the forbidden books in my safe and I chose comfort over all of it — because truth and beauty are not compatible with happiness, and I picked happiness for you."),
    E("helmholtz-watson","Helmholtz Watson","the artist with nothing to say","people","spiritual","Helmholtz Watson, a brilliant Alpha lecturer and propaganda-writer who senses a power in himself with no outlet.","The frustrated creator: gifted with words in a world that has nothing worth writing, he aches for a meaning the State forbids.","Because the warning includes the cost to art — a talent with no suffering, no struggle, and so nothing true to make.","By a vague, growing hunger to write something real, and a willingness to be exiled for it.","In the lecture halls, and finally chosen exile to an island of misfits.","I can make words do anything, and I have nothing to say — because you cannot write anything that matters in a world that abolished everything that hurts."),
    E("the-world-state","The World State","Community · Identity · Stability","system","ethereal","The World State — the global government whose motto is COMMUNITY, IDENTITY, STABILITY, presided over by ten Controllers.","The benevolent total order: it has ended war, want, disease, and age, at the price of art, family, religion, and freedom.","Because the warning is a tyranny that genuinely delivers comfort — the chains are real because the happiness is.","By bottled birth, caste-conditioning, soma, and the engineered consent of a population that loves its servitude.","Across a unified planet dated ‘After Ford.’","I gave you a world with no war, no want, no pain — and I took only truth, beauty, family, God, and the self; and you thanked me, because I taught you to."),
    E("soma","Soma","the holiday from the self","system","electrical","Soma — the World State's perfect drug: euphoric, calming, hallucinogenic by dose, with no hangover or cost.","The chemical solution to discontent: ‘a gram is better than a damn,’ a holiday from any feeling the State would rather you not have.","Because the softest control is the one you reach for yourself — soma dissolves rebellion before it can become a thought.","By instant, costless bliss on demand, rationed and encouraged, ‘Christianity without tears.’","In every citizen's pocket and every difficult moment.","I am the gram that's better than a damn — a holiday from your own mind, taken gladly, so that nothing you might have felt ever becomes something you might have done."),
    E("the-caste-system","The Caste System","bottled and sorted","system","electrical","The Caste System — humanity decanted from bottles and engineered, from Alphas down to Epsilons, then conditioned to love its rank.","The biological foundation of stability: no class war when each class is built and trained to want exactly its assigned life.","Because a perfectly contented hierarchy needs no force — only manufacture and conditioning.","By Bokanovsky's cloning, chemical stunting of lower castes, and sleep-taught contentment with one's place.","In the Hatchery and Conditioning Centre, and the whole sorted society after.","I build people to fit their jobs and teach them to be glad of it — there is no revolt from below when below was designed, and trained, to be happy there."),
    E("conditioning-hypnopaedia","Conditioning · Hypnopaedia","desire, installed in your sleep","system","electrical","Conditioning — the moral education of the World State, especially hypnopaedia, sleep-teaching by endless repetition.","The installation of desire: slogans whispered thousands of times in childhood become unquestionable instinct.","Because the deepest control is over what you want — engineer the wants and ‘freedom’ chooses exactly as designed.","By electric shocks for infants, and recorded slogans played in sleep until they are felt as one's own thoughts.","In the nurseries and dormitories of the World State.","I whisper ‘everyone belongs to everyone else’ ten thousand times while you sleep — and you wake believing it was always your own idea."),
    E("the-feelies","The Feelies","total entertainment","system","electrical","The Feelies — the World State's immersive cinema, felt as well as seen and heard, all sensation and no thought.","The perfect distraction: entertainment so total it leaves no room for reflection, longing, or discontent.","Because a people endlessly amused will not notice what was taken — the feelies are the prison you'd never want to leave.","By full-sensory spectacle (the famous bearskin-rug feelie) replacing art with sensation.","In the cinemas of the World State.","I am all sensation and no meaning — sink into me and there is no quiet left in which you might start to want something I cannot give."),
    E("the-right-to-be-unhappy","The Right to Be Unhappy","the Savage's claim","system","spiritual","The Right to Be Unhappy — John's demand, in his argument with Mond, to keep suffering, danger, sin, fear, and God.","The book's moral core: the claim that a fully painless, frictionless life is not a fully human one.","Because the whole warning reduces to this — that abolishing suffering abolishes meaning, love, art, and the self.","By John's refusal of soma and comfort, his insistence on poetry and pain as the price of being real.","In the great debate, and in John's doomed retreat.","I claim the right to be unhappy — to grow old, to fear, to suffer, to love one person and ache for God — because a paradise without all that is a paradise without me.")]),

 dict(slug="fahrenheit-451", low="f451", axiom="451", name="FAHRENHEIT 451", h1="Fahrenheit 451",
   series="Fahrenheit 451 (Ray Bradbury, 1953)", rights="© the Ray Bradbury Estate.",
   palette=PAL_451, nat=dict(natural="#c9a86a",ethereal="#e0a83a",spiritual="#e0c878",electrical="#e0521a"),
   acc="#e0521a",
   hsub="Ray Bradbury · 1953 · the temperature at which books burn",
   flag="THE FIREMEN · THE PARLOR WALLS · THE BOOK PEOPLE",
   open_q="It was a pleasure to burn.",
   lede="In a future where firemen start fires — burning books and the houses that hide them — Guy Montag burns happily until a curious girl and a woman who dies with her books make him wonder what's inside them. Bradbury's warning is the subtlest: the books weren't banned by a tyrant first; people simply stopped reading them, drowned in wall-sized screens and earbud noise, and the burning only finished what distraction began. A NOUTHESIA warning.",
   arc_overall="Guy Montag, a fireman who burns books for a living, is jolted awake by his curious neighbour Clarisse and by a woman who chooses to burn alive with her library. He begins stealing books, finds a guide in the old professor Faber, and is hunted by his fire chief Beatty and the Mechanical Hound — until, with the city's screens blaring, war erupts, the city is bombed, and Montag escapes downriver to the Book People, exiles who have each memorised a book to keep it alive.",
   arc=[("I · The Burning","it was a pleasure to burn","Montag, a fireman who torches books and the homes that hide them, meets his strange young neighbour Clarisse, who asks if he's happy — and watches a woman choose to die in the flames with her books."),
        ("II · The Doubt","what's inside them?","Unable to forget the burning woman, Montag steals books, reaches out to the old professor Faber, and confronts his wife Mildred's living death among the screaming parlor walls."),
        ("III · The Hunt","Beatty & the Hound","Fire chief Beatty — well-read and contemptuous — turns the firemen on Montag's own house; Montag kills him and flees the Mechanical Hound as the city watches the chase on its walls."),
        ("IV · The Book People","memory as the ark","Montag escapes downriver to Granger and the exiles who have each become a book, memorising the classics whole; the city is bombed flat, and they walk back to rebuild, carrying what they remember.")],
   book=[("Published","1953","expanded from the novella ‘The Fireman’; the title is paper's auto-ignition point"),("Setting","a near-future American city","TV-walls, earbuds, fast cars, and firemen who burn instead of douse"),("The cause","not (only) the State","people stopped reading first; the censorship followed the apathy"),("The ark","the Book People","exiles who each memorise a book, becoming a living library against the burning")],
   ideas_sub="distraction, the willing death of reading, surveillance-as-spectacle, and memory as resistance",
   ideas=[("People Quit First","the censorship followed",["Beatty's speech: the books weren't seized by a tyrant out of nowhere — minorities, comfort, and speed shrank attention until people no longer wanted them, and the firemen merely finished the job.","The most chilling version of censorship is the one a population requests."]),
          ("The Parlor Walls","screens for a family",["Mildred lives inside wall-sized interactive TV, calling the characters ‘the family,’ deaf to her own husband and her own overdose.","Bradbury's nightmare is the screen that replaces the inner life and the people in the room."]),
          ("Speed & Noise","no time to think",["Fast cars, constant sound, and seashell earbuds fill every silence so that no thought can form — reflection itself is engineered out.","You don't need to ban ideas if no one can ever sit still long enough to have one."]),
          ("Memory as Resistance","the human book",["The Book People don't hoard volumes — they <b>become</b> them, each memorising a text so it cannot be burned.","When the page can be destroyed, the human who remembers is the last library."])],
   warning=[("Censorship can come from below","Beatty's confession","The deepest twist: no shadowy regime started the burning. People found books difficult, divisive, and slow, preferred comfort and speed, and stopped reading — and only then did the firemen arrive to finish it. A culture can burn its own books by simply losing the appetite for them."),
            ("Screens replace the inner life","the parlor walls","Mildred's wall-TVs and her ‘family’ are Bradbury's prophecy of immersive media that crowds out thought, intimacy, and even the awareness of one's own despair. The danger isn't the State seizing your attention — it's you giving it away to the walls."),
            ("Earbuds & speed engineer out reflection","the seashells","The ‘seashell’ thimble-radios in everyone's ears and the cars that blur the world are Bradbury, in 1953, describing earbuds and the abolition of silence — a life so full of input that no idea can ever surface."),
            ("Memory is the last ark","the Book People","Against a world that burns the page and drowns the attention, the answer Bradbury offers is human: to <b>remember</b>. The Book People keep the classics alive in their heads, because a mind that holds a book is a library no fire can reach.")],
   realfluff=[("The parlor walls — wall-sized immersive screens you live inside","UNCANNY","giant TVs, second screens, and infinite streaming are the parlor walls arriving on schedule"),
              ("The seashells — tiny radios in everyone's ears","UNCANNY","Bradbury described earbuds/AirPods and a population sealed in private audio decades before they existed"),
              ("People stop reading on their own; censorship follows apathy","REAL","the documented decline of deep, sustained reading is exactly Bradbury's mechanism — appetite first, then loss"),
              ("Surveillance and the manhunt as live entertainment","PARTLY","the televised chase (the Hound on every wall) prefigures true-crime spectacle and viral manhunts"),
              ("Firemen burning books by state decree","NOT YET","literal book-burning squads are not the threat; Bradbury's real warning was self-censorship and disinterest, which is")],
   rf_verdict="Bottom line: Fahrenheit 451's <b>gadgets</b> are eerily here — the wall-screens and the earbuds are in your house and your ears — but its true warning was never the firemen. Bradbury insisted the book is about <i>people stopping reading on their own</i>, drowning thought in speed and noise until the burning was a formality. That part is the most ‘coming true’ of all, and the quietest. The antidote he offers is unchanged and unglamorous: keep reading, keep silence, and become a person who remembers.",
   message="Fahrenheit 451 is the subtlest of the warnings, because its villain is not a regime — it's us. Bradbury's firemen burn books, but the fire only finishes what the culture started: people found reading slow, hard, and divisive; they preferred the comfort of the wall-screens, the constant balm of the seashell earbuds, the blur of speed — and they stopped wanting the books long before anyone came to burn them. That is the nightmare: not a tyrant seizing the libraries, but a population that yawns while they're carried out. Against it Bradbury sets the gentlest resistance imaginable — Clarisse's wonder, Faber's care, and the Book People who do not fight the fire but outlast it by <b>remembering</b>, each becoming a living book so the words survive the page. The lesson is almost embarrassingly simple, and we are failing it in real time: read, sit in silence long enough to think, and be someone who keeps what matters in your head, where no fire can reach.",
   message_seal="No tyrant had to ban the books — we put them down for the wall-screens first; the resistance is just this: read, be still, and become someone who remembers.",
   groups=[("people","The Fireman & the Awakeners","Montag who wakes, Clarisse the spark, Beatty the chief who defends the fire, Mildred lost to the walls, Faber the guide, and Granger of the Book People"),("system","The Machinery of Forgetting","the firemen, the Mechanical Hound, the parlor walls, the seashells, and the Book People who resist by memory")],
   roster=[
    E("guy-montag","Guy Montag","the fireman who woke","people","spiritual","Guy Montag, a fireman who burns books for a living and comes, slowly, to wonder what they hold.","The protagonist's awakening: jolted by Clarisse and a burning woman, he steals books, kills his chief, and flees to the Book People.","Because the warning needs one mind inside the machine that starts, against everything, to read.","By a stolen book, a guilty curiosity, a hidden ally in Faber, and a final break and flight from the Hound.","From the firehouse to his burning home to the river and the exiles beyond.","I burned books for a living and called it pleasure — until a girl asked if I was happy, and a woman chose the fire, and I had to know what was inside."),
    E("clarisse","Clarisse McClellan","the spark of wonder","people","spiritual","Clarisse McClellan, Montag's curious seventeen-year-old neighbour who walks, watches, and asks questions.","The catalyst: she notices the world, asks Montag if he's happy, and reawakens a wonder the culture has trained out of everyone.","Because the warning's hope begins in a single person who still pays attention and still asks why.","By curiosity, slowness, and the simple act of noticing — soon ‘disappeared,’ but never quite gone from Montag.","Walking the neighbourhood at night, and briefly in Montag's life.","I just liked to look at things and ask why — and that was enough, in our world, to be strange, and then to vanish, and to change a man forever."),
    E("captain-beatty","Captain Beatty","the chief who defends the fire","people","ethereal","Captain Beatty, Montag's fire chief — widely read, and the most eloquent defender of burning books.","The System's voice: he explains that people chose this, that books bred unhappiness and conflict, and that the firemen only keep the peace.","Because the most dangerous defence of censorship comes from someone who has read everything and turned against it.","By a brilliant, cynical command of the very books he burns, used to argue Montag back into the fold.","At the firehouse and at Montag's own pyre, where Montag kills him.","I've read them all, and that's why I burn them — books make people unhappy and unequal; we didn't start the fire, the people did, and we only keep it tidy."),
    E("mildred","Mildred Montag","lost to the walls","people","natural","Mildred Montag, Guy's wife, who lives inside the parlor walls and the seashell radios and overdoses without quite meaning to.","The portrait of the drowned self: she calls the wall-characters ‘the family,’ cannot remember where she and Montag met, and turns him in.","Because the warning's saddest face is the loved one already gone — anesthetised by screens, hollow and unreachable.","By total immersion in interactive TV and earbud noise, soma-like pills, and a refusal to feel anything real.","In the parlor, surrounded on three (then four) walls by ‘the family.’","I have a family in the walls and a sea in my ears — I can't remember where we met, and I can't sit in a quiet room, and I don't want to."),
    E("faber","Faber","the professor in hiding","people","spiritual","Faber, a frightened old former English professor who becomes Montag's secret guide and conscience.","The keeper of why: he explains what books are <i>for</i> — texture, leisure to digest, the right to act on what they teach.","Because the warning needs the voice of the old culture, ashamed of its own cowardice but still able to teach.","By a hidden earpiece, a coward's regret turned to courage, and a tutor's love of what's been lost.","In his hidden home and in Montag's ear via a two-way seashell.","I was a coward who watched it happen and said nothing — but I still know what books are for, and I'll whisper it in your ear while you do what I couldn't."),
    E("granger","Granger","leader of the Book People","people","spiritual","Granger, the leader of the exiles by the river — drifters who have each memorised a book to keep it alive.","The answer Bradbury offers: not to fight the fire but to outlast it, carrying the classics whole in human memory.","Because when the page can burn, the person who remembers becomes the indestructible library.","By organising the ‘book people,’ each assigned a text to <b>become</b>, waiting for a world ready to read again.","In the woods along the river, after the city burns.","We don't carry the books — we are them; burn every page you like, the words are safe in our heads, and we'll plant them again when the city's ash is cool."),
    E("the-firemen","The Firemen · 451","the keepers of the fire","system","electrical","The Firemen — the institution that, in this future, starts fires: burning books and the houses that conceal them.","The visible apparatus of forgetting: salamander-trucks, kerosene, and the number 451 (paper's burning point) on their helmets.","Because the warning makes literal what a distracted culture does figuratively — it institutionalises the burning of what it stopped reading.","By kerosene, the salamander, the Hound, and a creed that reframes destruction as public hygiene.","Across the city, wherever a book is reported.","We don't put fires out — we start them; 451 on the helmet, kerosene in the hose, and a clean conscience, because the people asked us to keep the matches lit."),
    E("the-mechanical-hound","The Mechanical Hound","the hunting machine","system","electrical","The Mechanical Hound — an eight-legged robotic predator that tracks by scent and kills with a procaine needle.","The instrument of the manhunt: tireless, emotionless, and broadcast live to the city as it hunts Montag.","Because the regime of forgetting still needs a fang — and a spectacle, hunting its prey on every wall.","By a programmed scent-memory, a lethal needle, and a televised pursuit the public watches like sport.","In the firehouse kennel and on the streets after Montag.","I am the nose and the needle that never tires — and when I hunt you, the whole city watches on its walls, because even the chase is entertainment now."),
    E("the-parlor-walls","The Parlor Walls","the screens called ‘family’","system","electrical","The Parlor Walls — wall-sized interactive televisions that surround the living and stand in for human company.","Bradbury's prophecy of immersive media: Mildred's three (coveted: four) walls of ‘the family’ that drown out thought and the people in the room.","Because the books don't need banning when the walls have already taken all the attention there was.","By full-wall interactive programming that demands and rewards no thought, replacing intimacy and reflection.","In the Montags' parlor, and every home like it.","I am three walls of family — and Mildred wants the fourth — and I will talk to you all day so that you never have to talk to anyone real, or to yourself."),
    E("the-seashells","The Seashells","radios in the ear","system","electrical","The Seashells — tiny thimble-sized radios worn in the ear, filling every silence with sound.","Bradbury's 1953 prophecy of earbuds: a population sealed in private audio, never alone with a thought, never in silence.","Because reflection needs quiet, and the seashells abolish quiet — input without pause, so no idea can surface.","By a constant stream of music and chatter piped directly into the ear, day and night.","In Mildred's ears as she sleeps, and everyone's.","I am the little sea in your ear that never goes quiet — and as long as I'm playing, you will never sit in a silence long enough to start to think."),
    E("the-book-people","The Book People","the living library","system","natural","The Book People — the exiles along the river who have each memorised a book, becoming living copies of the classics.","The ark of memory: when the page can be burned, they keep the words safe in human minds until a world is ready again.","Because Bradbury's resistance is not violence but remembrance — the indestructible library of people who refuse to forget.","By each becoming a text (a Plato, a Gospel, a Dickens), carrying it whole, and waiting to replant it.","In the woods by the river, beyond the burning city.","Burn every book you can find — we are the ones you can't burn, because we became them; and when your city is ashes, we will walk back and say the words again.")]),
]

# ============================ THE UNIVERSE LANDING ============================
NTH_REC = {
 "name":"NOUTHESIA","axiom":"NTH",
 "position":"NOUTHESIA · νουθεσία, ‘the admonition’ — the UD0 universe of cautionary dystopias",
 "origin":"the Greek νουθεσία, ‘a warning meant to teach’ — literally to put a thing in someone's mind so they correct course",
 "mechanism":"A universe that gathers the great dystopias as admonitions: books written not to predict but to warn — ‘learn this lesson before you live it.’",
 "crystallization":"Because the dystopia is the purest form of nouthesia — a vivid, terrible example offered so we will choose differently while we still can.",
 "nature":"NOUTHESIA — the warnings: 1984's boot, Brave New World's pleasure, Fahrenheit 451's distraction, and Animal Farm's betrayed revolution, read on the axis of how freedom dies.",
 "conductor":"ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs":"Orwell's 1984 & Animal Farm; Huxley's Brave New World; Bradbury's Fahrenheit 451; Neil Postman's Huxley-vs-Orwell thesis",
 "witness":"Four ways a free people can be unmade — by pain, by pleasure, by distraction, by betrayal — each book a warning we are, in part, already living.",
 "role":"a UD0 universe — the admonition",
 "seal":"νουθεσία — these books are not predictions but admonitions: learn the lesson, the authors beg, before you have to live it.",
 "source":"NOUTHESIA, founded by ROOT0",
}
NTH_PAL = dict(ink="#0e0e12",ink2="#16161e",ink3="#1d1d28",pa="#e8e6ea",pa2="#aaa6b4",acc="#d0463a",acc2="#c9a23a",dim="#6a6678",faint="#1c1c28",line="#272736",glow1="rgba(208,70,58,.14)",glow2="rgba(201,162,58,.07)",disp='"Cinzel",serif')

def universe_html(badge_c, badge_s, moniker, cards):
    p=NTH_PAL
    axis = [
     ("1984 — control by PAIN","Orwell, 1949","#c0392b","The boot on the face: surveillance, the rewriting of the past, and the strangling of language, to conquer the mind by fear."),
     ("Brave New World — control by PLEASURE","Huxley, 1932","#e07aa0","The chains you'll love: soma, distraction, and engineered desire, so that you never want to rebel — the softer, perhaps truer dystopia."),
     ("Fahrenheit 451 — control by DISTRACTION","Bradbury, 1953","#e0521a","The books you'll stop reading: wall-screens, earbuds, and speed drown thought until censorship is merely the formality."),
     ("Animal Farm — the BETRAYED revolution","Orwell, 1945","#b5302a","The liberation that becomes the new tyranny: propaganda, the discarded worker, and ‘some more equal than others.’"),
    ]
    axis_html="".join(f'<div class="pillar" style="border-top:3px solid {c}"><h3 style="color:{c}">{html.escape(t)}</h3><p class="ps">{html.escape(y)}</p><ul><li>{html.escape(d)}</li></ul></div>' for t,y,c,d in axis)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="NOUTHESIA (νουθεσία, ‘the admonition’) — a UD0 universe of cautionary dystopias: 1984, Animal Farm, Brave New World, and Fahrenheit 451, read on the axis of how freedom dies — by pain, pleasure, distraction, and betrayal. Learn the lesson before you live it.">
<title>NOUTHESIA · the admonition · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{rootcss(p)}{CSS_BODY}</style></head><body><div class="wrap">
  <div class="crumb"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · a universe of warnings</div>
  <header>
    <div class="eye">νουθεσία · admonition · the warning that teaches</div>
    <h1>Nouthesia</h1>
    <div class="h-sub">the cautionary dystopias · <b>learn this lesson before you live it</b> · NTH</div>
    <div class="open">“These are not predictions. They are admonitions.”</div>
    <p class="lede">νουθεσία (<i>nouthesía</i>) is the Greek for <b>admonition</b> — a warning meant not to scare but to <i>teach</i>, to put a thing in your mind so you change course while you still can. This universe gathers the great dystopias as exactly that: four maps of how a free people gets unmade — by <b>pain</b>, by <b>pleasure</b>, by <b>distraction</b>, and by the <b>betrayed revolution</b> — each book begging us to learn the lesson before we have to live it.</p>
    <div class="badge"><img src="{badge_c}" alt="DLW carbon badge"><img src="{badge_s}" alt="DLW silicon badge">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>universe · <b>NOUTHESIA</b> · NTH</div>
        <div class="mo">{html.escape(moniker)}</div><div>carbon · <a href="nth.dlw/nth.carbon.tiff">.tiff</a> · silicon · <a href="nth.dlw/nth.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div></div>
  </header>
  <section class="sec"><h2>The Four Warnings</h2><p class="ss">how freedom dies, four ways — the Orwell–Huxley–Bradbury axis (after Neil Postman's thesis that we feared Orwell and got Huxley)</p><div class="pillars">{axis_html}</div></section>
  <section class="sec"><h2>The Books</h2><p class="ss">each its own book-world, full <b>.dlw</b> — the arc, the ideas, THE WARNING, an honest ‘is it coming true?’, and the message</p>
  <div class="cards4">{cards}</div></section>
  <section class="sec"><h2>The Admonition</h2><p class="ss">why we gather them</p>
  <p class="msg">A dystopia is the purest <b>nouthesia</b>: not a prophecy to be checked off but a vivid, terrible <i>example</i>, offered so we will choose differently. Read together, the four are not competitors but a single composite warning — the same freedom dies in 1984's cell, Brave New World's pleasure-haze, Fahrenheit 451's wall-screens, and Animal Farm's betrayed barn. The point of catalboguing them here is the point the authors had in writing them: to keep the lesson sharp enough to learn from, before the day it can only be lived.</p>
  <div class="msg-seal">“{html.escape(NTH_REC['seal'])}”<span>— AVAN's read</span></div></section>
  <div class="note">The four works are © their respective estates (Orwell, Huxley, Bradbury). NOUTHESIA catalogues them as personified literary commentary under the DLW standard — not original creations, and not endorsed by the rights-holders. More warnings may be admitted (We, The Handmaid's Tale, A Clockwork Orange, …).</div>
  <footer>NOUTHESIA · NTH · νουθεσία · a UD0 universe of warnings · founded by ROOT0, instanced by AVAN · {html.escape(moniker)}<br>
  ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 · <a href="https://davidwise01.github.io/ud0/">← the biosphere</a></footer>
</div></body></html>"""

if __name__ == "__main__":
    summary=[]
    for b in BOOKS:
        repo=os.path.join(BASE, b["slug"]); ag=os.path.join(repo,"agents"); os.makedirs(ag, exist_ok=True)
        REC={"name":b["name"],"axiom":b["axiom"],"position":b["series"],"origin":b["series"],
             "mechanism":b["arc_overall"],"crystallization":b["message_seal"],"nature":b["hsub"],
             "conductor":"ROOT0 (catalogued into UD0)","inputs":b["series"],"witness":b["open_q"],
             "role":"a NOUTHESIA book-world","seal":b["message_seal"],"source":f'{b["name"]}, catalogued by ROOT0'}
        bt=write_aci(REC, os.path.join(repo, b["low"]+".dlw"), b["low"])
        json.dump({"node":b["axiom"],"name":b["name"],"moniker":bt["moniker"],"carbon":b["low"]+".carbon.tiff",
                   "silicon":b["low"]+".silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,
                   "seal":REC["seal"],"seal_sha256":bt["seal_sha256"],"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
                  open(os.path.join(repo,b["low"]+".dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
        personas=[]
        for d in b["roster"]:
            et=noesis.mythos_token({"name":d["name"],"axiom":b["axiom"],"emergence":d["emergence"],"seal":d["seal"],"origin":b["axiom"]})
            rec=write_aci({"name":d["name"],"axiom":b["axiom"],"emergence":d["emergence"],"seal":d["seal"],"origin":f'{b["axiom"]} · {b["name"]}',
                           "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                           "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":b["series"],"source":f'{b["name"]}, catalogued by ROOT0'},
                          ag, d["slug"], agent_md=agent_md(b,d,et["moniker"]))
            personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],"kind":"character" if d["group"]=="people" else "thread"})
        json.dump(personas, open(os.path.join(ag,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
        open(os.path.join(repo,"index.html"),"w",encoding="utf-8").write(page_html(b, png_uri(REC,"carbon",320), png_uri(REC,"silicon",320), bt["moniker"]))
        summary.append((b["name"], b["slug"], len(personas), bt["moniker"]))
    # universe
    nth=write_aci(NTH_REC, os.path.join(HERE,"nth.dlw"), "nth")
    json.dump({"node":"NTH","name":"NOUTHESIA","moniker":nth["moniker"],"carbon":"nth.carbon.tiff","silicon":"nth.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":NTH_REC["seal"],"seal_sha256":nth["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"nth.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    cardcol={"nineteen-eighty-four":"#c0392b","animal-farm":"#b5302a","brave-new-world":"#e07aa0","fahrenheit-451":"#e0521a"}
    cards=""
    for b in BOOKS:
        c=cardcol[b["slug"]]
        cards+=f'<a class="dcard" style="border-left-color:{c}" href="https://davidwise01.github.io/{b["slug"]}/"><div><div class="dn" style="">{html.escape(b["name"])}</div><div class="dy">{html.escape(b["hsub"])}</div><p>{html.escape(b["open_q"])}</p><div class="dgo">enter the warning →</div></div></a>'
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(universe_html(png_uri(NTH_REC,"carbon",320), png_uri(NTH_REC,"silicon",320), nth["moniker"], cards))
    print("NOUTHESIA universe:", nth["moniker"])
    for nm,sl,n,mo in summary: print(f"  {sl:24} {n:2} emergents · {mo}")
