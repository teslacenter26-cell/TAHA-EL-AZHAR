"""Prévisualisation locale en lecture seule."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

from build import DOSSIER, HEADERS, construire

TYPES = {"index.html": "text/html; charset=utf-8", "app.js": "text/javascript",
         "style.css": "text/css", "alertes.json": "application/json"}


class Handler(BaseHTTPRequestHandler):
    def end_headers(self):
        for key, value in HEADERS.items():
            self.send_header(key, value)
        super().end_headers()

    def do_HEAD(self):
        self.servir(False)

    def do_GET(self):
        self.servir(True)

    def servir(self, corps: bool):
        path = urlsplit(self.path).path
        name = "index.html" if path == "/" else path[1:]
        if name not in TYPES:
            self.send_error(404)
            return
        try:
            data = (DOSSIER / "dist" / name).read_bytes()
        except OSError:
            self.send_error(503)
            return
        self.send_response(200)
        self.send_header("Content-Type", TYPES[name])
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if corps:
            self.wfile.write(data)


if __name__ == "__main__":
    construire(DOSSIER / "dist")
    print("Portfolio disponible sur http://127.0.0.1:8000", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
