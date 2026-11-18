import http.client
import json
import tempfile
import threading
import unittest
from pathlib import Path
from http.server import ThreadingHTTPServer

from analyse import lire, valider, DOSSIER
from build import construire, HEADERS, PUBLIC
from preview import Handler


class PortfolioTest(unittest.TestCase):
    def test_journal_invalide(self):
        ligne = ["1", "atlas", "192.0.2.1", "2026-10-01T12:00:00Z", "succes"]
        for index, mauvais in enumerate(["1.5", "", "999.1.1.1", "2026-02-31T01:00:00Z", "ok"]):
            with self.subTest(index=index), self.assertRaises(ValueError):
                valider([ligne[:index] + [mauvais] + ligne[index + 1:]])
        with self.assertRaises(ValueError):
            valider([ligne, ligne])
        with tempfile.TemporaryDirectory() as dossier:
            path = Path(dossier) / "journal.csv"
            path.write_text("mauvais,en-tete\n")
            with self.assertRaises(ValueError):
                lire(path)

    def test_livraison(self):
        with tempfile.TemporaryDirectory() as dossier:
            out = Path(dossier)
            construire(out)
            self.assertEqual({p.name for p in out.iterdir()}, {*PUBLIC, "_headers"})
            data = json.loads((out / "alertes.json").read_text())
            self.assertEqual([(a["compte"], a["echecs"]) for a in data], [("atlas", 5), ("boreal", 5)])
            self.assertIn("Strict-Transport-Security: max-age=", (out / "_headers").read_text())
            (out / "ancien.bak").touch()
            with self.assertRaises(ValueError):
                construire(out)

    def test_http(self):
        construire(DOSSIER / "dist")
        with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as serveur:
            thread = threading.Thread(target=serveur.serve_forever)
            thread.start()
            try:
                for methode, path, statut in [("GET", "/", 200), ("HEAD", "/alertes.json", 200),
                                              ("GET", "/.env", 404), ("GET", "/analyse.py", 404),
                                              ("GET", "/../README.md", 404), ("POST", "/", 501)]:
                    with self.subTest(path=path, methode=methode):
                        conn = http.client.HTTPConnection(*serveur.server_address, timeout=3)
                        conn.request(methode, path)
                        response = conn.getresponse()
                        self.assertEqual(response.status, statut)
                        for key, value in HEADERS.items():
                            self.assertEqual(response.getheader(key), value)
                        self.assertIsNone(response.getheader("Set-Cookie"))
                        self.assertIsNone(response.getheader("Access-Control-Allow-Origin"))
                        if methode == "HEAD":
                            self.assertEqual(response.read(), b"")
                        conn.close()
            finally:
                serveur.shutdown()
                thread.join()
