"""Construit exclusivement les ressources publiques du portfolio."""
import json
from pathlib import Path
from shutil import copyfile

from analyse import DOSSIER, detecter, lire

ASSETS = ("index.html", "style.css", "app.js")
PUBLIC = (*ASSETS, "alertes.json")
HEADERS = {
    "Content-Security-Policy": "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
}


def construire(destination: Path) -> None:
    destination.mkdir(exist_ok=True)
    if any(p.name not in (*PUBLIC, "_headers") or p.is_symlink() or not p.is_file()
           for p in destination.iterdir()) or destination.is_symlink():
        raise ValueError("Le dossier de livraison doit être dédié au portfolio.")
    alertes = detecter(lire(DOSSIER / "evenements.csv"))
    for name in ASSETS:
        copyfile(DOSSIER / "web" / name, destination / name)
    champs = ("id", "compte", "ip", "instant", "echecs")
    (destination / "alertes.json").write_text(json.dumps([dict(zip(champs, a)) for a in alertes]))
    headers = {**HEADERS, "Strict-Transport-Security": "max-age=31536000", "Access-Control-Allow-Origin": None}
    rules = [f"  {k}: {v}" if v is not None else f"  ! {k}" for k, v in headers.items()]
    (destination / "_headers").write_text("/*\n" + "\n".join(rules) + "\n")


if __name__ == "__main__":
    construire(DOSSIER / "dist")
