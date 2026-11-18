const test = require("node:test");
const assert = require("node:assert/strict");
const {readFileSync} = require("node:fs");
const {runInNewContext} = require("node:vm");
const {webcrypto} = require("node:crypto");

test("Parcours du laboratoire sur un DOM simulé", async () => {
  const elements = new Map();
  function champ(id) {
    if (!elements.has(id)) elements.set(id, {
      enfants: [], append(x) { this.enfants.push(x); },
      addEventListener(nom, fn) { this[nom] = fn; }
    });
    return elements.get(id);
  }
  const location = {};
  const document = {getElementById: champ, createElement: () => ({})};
  const json = JSON.parse(readFileSync("dist/alertes.json"));
  const fetch = async () => ({ok: true, json: async () => json});
  runInNewContext(readFileSync("web/app.js", "utf8"), {document, location, fetch, crypto: webcrypto});
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(champ("alertes").enfants.length, 2);
  champ("entetes").value = "X-Frame-Options: DENY";
  champ("verifier").click();
  assert.match(champ("diagnostic").textContent, /x-frame-options — conforme/);
  champ("entetes").value += "\nX-Frame-Options: DENY";
  champ("verifier").click();
  assert.match(champ("diagnostic").textContent, /x-frame-options — à examiner/);
  const event = {preventDefault() {}};
  champ("fichier").files = [new Blob(["abc"])];
  champ("reference").value = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad";
  await champ("integrite").submit(event);
  assert.equal(champ("comparaison").textContent, "Empreinte identique.");
  champ("reference").value = "0".repeat(64);
  await champ("integrite").submit(event);
  assert.equal(champ("comparaison").textContent, "Empreinte différente.");
  champ("fichier").files = [{size: 6 * 1024 * 1024}];
  await champ("integrite").submit(event);
  assert.match(champ("comparaison").textContent, /maximum/);
  champ("sujet").value = "Mission & recrutement";
  champ("message").value = "Bonjour";
  champ("courrier").submit(event);
  assert.match(location.href, /subject=Mission%20%26%20recrutement&body=Bonjour$/);
});
