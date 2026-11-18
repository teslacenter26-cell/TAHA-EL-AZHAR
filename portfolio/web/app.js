"use strict";
const element = (id) => document.getElementById(id);

async function afficherAlertes() {
  try {
    const response = await fetch("alertes.json", {credentials: "omit"});
    if (!response.ok) throw new Error("journal");
    const alertes = await response.json();
    for (const alerte of alertes) {
      const ligne = document.createElement("li");
      ligne.textContent = [alerte.compte, alerte.ip, alerte.instant, alerte.echecs + " échecs"].join(" · ");
      element("alertes").append(ligne);
    }
    element("statut").textContent = alertes.length + " alertes dans le scénario fictif.";
  } catch {
    element("statut").textContent = "Journal indisponible. Rechargez la page ou consultez la note de triage.";
  }
}
afficherAlertes();

element("verifier").addEventListener("click", () => {
  const lignes = element("entetes").value.split(/\r?\n/);
  const regles = {"x-content-type-options": "nosniff", "referrer-policy": "no-referrer", "x-frame-options": "deny"};
  const resultats = Object.entries(regles).map(([nom, attendu]) => {
    const valeurs = lignes.filter(l => l.split(":")[0].trim().toLowerCase() === nom)
      .map(l => l.slice(l.indexOf(":") + 1).trim().toLowerCase());
    return nom + " — " + (valeurs.length === 1 && valeurs[0] === attendu ? "conforme" : "à examiner");
  });
  element("diagnostic").textContent = resultats.join(" / ");
});

element("integrite").addEventListener("submit", async (event) => {
  event.preventDefault();
  const fichier = element("fichier").files[0];
  const reference = element("reference").value.toLowerCase();
  const sortie = element("comparaison");
  if (!fichier || fichier.size > 5 * 1024 * 1024) {
    sortie.textContent = "Choisissez un fichier de 5 Mio maximum.";
    return;
  }
  try {
    const digest = await crypto.subtle.digest("SHA-256", await fichier.arrayBuffer());
    const hex = Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2, "0")).join("");
    sortie.textContent = hex === reference ? "Empreinte identique." : "Empreinte différente.";
  } catch {
    sortie.textContent = "Calcul indisponible. Ouvrez le laboratoire en HTTPS ou sur localhost.";
  }
});
element("courrier").addEventListener("submit", event => {
  event.preventDefault();
  const sujet = element("sujet").value.replace(/[\r\n]/g, " ").trim();
  const corps = element("message").value.trim();
  if (sujet && corps) location.href = "mailto:tahaelazhar0@gmail.com?subject=" +
    encodeURIComponent(sujet) + "&body=" + encodeURIComponent(corps);
});
