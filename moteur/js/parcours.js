/* Le comparateur de parcours.
 *
 * Il ne calcule rien : il met en regard deux listes d'étapes écrites dans
 * `src/immigration/pages/parcours.py` et déposées dans la page en JSON. Le
 * script ne connaît donc aucun chiffre — c'est ce qui garantit que la page et
 * le module Python ne peuvent pas diverger.
 *
 * Pas de dépendance, pas de requête réseau : le site ne demande rien à un
 * tiers, et une page politique lue depuis un téléphone n'a pas à charger
 * trois cents kilo-octets de bibliothèque pour afficher des barres.
 */

const source = document.getElementById("donnees-parcours");
const choix = document.getElementById("cas");
const sortie = document.getElementById("resultat");
const resume = document.getElementById("resume-cas");

if (source && choix && sortie) {
  const { cas, dureeMax } = JSON.parse(source.textContent);

  /* Le total d'un parcours : la somme des étapes, arrondie au demi-mois. Les
     étapes se succèdent, elles ne se chevauchent pas — c'est une hypothèse,
     et elle est favorable au droit actuel, qui superpose parfois deux
     démarches. */
  const total = (etapes) => etapes.reduce((somme, [, mois]) => somme + mois, 0);

  const enClair = (mois) => {
    if (mois < 1) return "moins d'un mois";
    if (mois < 2) return "environ un mois";
    if (mois < 12) return `environ ${Math.round(mois)} mois`;
    const annees = mois / 12;
    return `environ ${annees.toFixed(annees < 2 ? 1 : 0).replace(".", ",")} an${annees >= 2 ? "s" : ""}`;
  };

  /* Une colonne : le total en gros, la barre à l'échelle commune, puis les
     étapes. L'échelle est la même à gauche et à droite — deux barres qui ne
     partagent pas leur échelle ne se comparent pas, et c'est précisément ce
     qu'on demande au lecteur de faire ici. */
  const colonne = (titre, etapes, classe) => {
    const somme = total(etapes);
    const largeur = Math.min(100, (somme / dureeMax) * 100);
    const lignes = etapes
      .map(([libelle, mois]) => {
        const part = Math.min(100, (mois / dureeMax) * 100);
        const duree = mois === 0 ? "immédiat" : enClair(mois);
        return `<li><span class="etape">${libelle}</span>
          <span class="duree">${duree}</span>
          <span class="barre ${classe}"><span style="width:${part}%"></span></span></li>`;
      })
      .join("");
    return `<div class="colonne">
      <h3>${titre}</h3>
      <p class="total"><strong>${enClair(somme)}</strong> avant de travailler légalement</p>
      <span class="barre ${classe}" aria-hidden="true"><span style="width:${largeur}%"></span></span>
      <ol class="etapes">${lignes}</ol>
    </div>`;
  };

  const rendre = (cle) => {
    const c = cas.find((c) => c.cle === cle) || cas[0];
    if (resume) resume.textContent = c.resume;
    const ecart = total(c.actuel) - total(c.propose);
    sortie.innerHTML = `
      <div class="parcours">
        ${colonne("Aujourd'hui", c.actuel, "actuel")}
        ${colonne("Avec le programme", c.propose, "liberal")}
      </div>
      <p class="ecart"><strong>${enClair(Math.max(ecart, 0))}</strong> de gagné, à
      contrôles identiques : identité vérifiée, casier consulté, contrat
      contrôlé dans les deux colonnes.</p>
      <p class="apropos">${c.note}</p>`;
  };

  choix.addEventListener("change", () => rendre(choix.value));
  /* L'adresse porte le cas choisi : un militant qui partage un lien partage
     le parcours dont il parle, et non la page par défaut. */
  const demande = new URLSearchParams(location.search).get("cas");
  if (demande && cas.some((c) => c.cle === demande)) choix.value = demande;
  choix.addEventListener("change", () => {
    const url = new URL(location.href);
    url.searchParams.set("cas", choix.value);
    history.replaceState(null, "", url);
  });
  rendre(choix.value);
}
