#!/usr/bin/env python3
"""Bangun aplikasi dari src/: menyisipkan file data, lalu menulis
   - index.html            : versi PWA untuk GitHub Pages
   - dist/artifact.html    : versi satu file untuk claude.ai
   Pakai: python3 build.py"""
import pathlib, re
root = pathlib.Path(__file__).parent
src = (root / "src/app.html").read_text(encoding="utf-8")
def inline(m):
    return "<script>\n" + (root / "src" / m.group(1)).read_text(encoding="utf-8") + "\n</script>"
app = re.sub(r'<script src="(data/[^"]+)"></script>', inline, src)
(root / "dist").mkdir(exist_ok=True)
(root / "dist/artifact.html").write_text(app, encoding="utf-8")
head = ('<!doctype html>\n<html lang="id"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<link rel="manifest" href="manifest.webmanifest"><meta name="theme-color" content="#22427A">'
        '<link rel="icon" href="icon.svg"><link rel="apple-touch-icon" href="icon.svg">\n'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}</style>'
        '</head><body>\n')
tail = '\n<script>if("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(()=>{});</script>\n</body></html>\n'
(root / "index.html").write_text(head + app + tail, encoding="utf-8")
print("index.html dan dist/artifact.html dibuat")
