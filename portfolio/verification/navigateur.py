"""Lancer preview.py au préalable. Outillage facultatif : Playwright et Chromium."""
import os
from shutil import which
from hashlib import sha256
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

PREUVES = Path(__file__).resolve().parents[1] / "preuves"
PREUVES.mkdir(exist_ok=True)
with sync_playwright() as p:
    navigateur = p.chromium.launch(executable_path=os.getenv("CHROME_BIN") or which("google-chrome") or which("chromium"))
    page = navigateur.new_page()
    erreurs = []
    page.on("pageerror", lambda err: erreurs.append(str(err)))
    for largeur in [360, 768, 1440]:
        page.set_viewport_size({"width": largeur, "height": 900})
        page.goto("http://127.0.0.1:8000/")
        expect(page.locator("#alertes li")).to_have_count(2)
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
        assert page.evaluate("Array.from(document.querySelectorAll('textarea,input')).every(e=>e.labels.length)")
        page.keyboard.press("Tab")
        expect(page.locator(".skip")).to_be_focused()
        page.keyboard.press("Enter")
        expect(page).to_have_url("http://127.0.0.1:8000/#contenu")
        page.locator(".brand").focus()
        page.evaluate("window.scrollTo(0,0)")
        if largeur != 768:
            page.screenshot(path=PREUVES / f"accueil-{largeur}.jpg", quality=65)
    page.locator("#verifier").click()
    expect(page.locator("#diagnostic")).to_contain_text("x-frame-options — conforme")
    page.locator("#entetes").fill("X-Frame-Options: DENY\nX-Frame-Options: SAMEORIGIN")
    page.locator("#verifier").click()
    expect(page.locator("#diagnostic")).to_contain_text("x-frame-options — à examiner")
    page.locator("#fichier").set_input_files({"name": "test.txt", "mimeType": "text/plain", "buffer": b"abc"})
    for ref, texte in [(sha256(b"abc").hexdigest(), "identique"), ("0" * 64, "différente")]:
        page.locator("#reference").fill(ref)
        page.locator("#integrite button").click()
        expect(page.locator("#comparaison")).to_contain_text(texte)
    page.locator("#laboratoire").screenshot(path=PREUVES / "laboratoire.jpg", quality=65)
    assert not page.locator("#courrier").evaluate("f=>f.checkValidity()")
    page.locator("#sujet").fill("Mission")
    page.locator("#message").fill("Bonjour")
    assert page.locator("#courrier").evaluate("f=>f.checkValidity()")
    assert not erreurs, erreurs
    print("Largeurs 360/768/1440, clavier, formulaires, journal, intégrité et en-têtes validés.")
    navigateur.close()
