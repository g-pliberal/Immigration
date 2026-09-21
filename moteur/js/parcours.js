/* Le comparateur de parcours.
 *
 * Il ne calcule rien : il met en regard trois listes d'étapes écrites dans
 * `src/immigration/pages/parcours.py` et déposées dans la page en JSON. Le
 * script ne connaît donc aucun chiffre — c'est ce qui garantit que la page et
 * le module Python ne peuvent pas diverger.
 *
 * Trois colonnes et non deux : ce qui se passe aujourd'hui (mesuré), ce que
 * la loi garantit aujourd'hui (promis, et le plus souvent indéfini), et ce
 * qu'elle garantirait sous le programme (promis). Les deux dernières sont
 * hachurées : une promesse et une mesure ne se comparent pas sans qu'on le
 * dise, et la version précédente de ce comparateur les mettait côte à côte
 * dans la même couleur pleine.
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

  /* Une étape dont la durée est `null` n'a pas de terme : c'est le cas général
     de la colonne du milieu, où la loi ne promet rien. Elle ne s'additionne
     pas — on ne somme pas l'indéfini —, elle rend le total indéfini. */
  const indefini = (etapes) => etapes.some(([, mois]) => mois === null);

  /* Le total d'un parcours : la somme des étapes bornées. Les étapes se
     succèdent, elles ne se chevauchent pas — c'est une hypothèse, et elle est
     favorable au droit actuel, qui superpose parfois deux démarches. */
  const total = (etapes) =>
    etapes.reduce((somme, [, mois]) => somme + (mois || 0), 0);

  const enClair = (mois) => {
    if (mois < 1) return "moins d'un mois";
    if (mois < 2) return "environ un mois";
    if (mois < 12) return `environ ${Math.round(mois)} mois`;
    const annees = mois / 12;
    return `environ ${annees.toFixed(annees < 2 ? 1 : 0).replace(".", ",")} an${annees >= 2 ? "s" : ""}`;
  };

  /* L'échelle est la même dans les trois colonnes — trois barres dont les
     échelles diffèrent ne se comparent pas, et c'est précisément ce qu'on
     demande au lecteur de faire ici. `dureeMax` est choisi dans le module
     Python pour dépasser le plus long parcours : aucune barre n'est écrêtée,
     et aucun total affiché ne contredit donc sa propre barre. */
  const largeur = (mois) => Math.min(100, (mois / dureeMax) * 100);

  const colonne = ({ titre, genre, etapes }) => {
    const ouvert = indefini(etapes);
    const somme = total(etapes);
    const lignes = etapes
      .map(([libelle, mois]) => {
        if (mois === null) {
          return `<li class="sans-terme"><span class="etape">${libelle}</span>
            <span class="duree">sans terme</span>
            <span class="barre ${genre} sans-terme"><span style="width:100%"></span></span></li>`;
        }
        const duree = mois === 0 ? "immédiat" : enClair(mois);
        return `<li><span class="etape">${libelle}</span>
          <span class="duree">${duree}</span>
          <span class="barre ${genre}"><span style="width:${largeur(mois)}%"></span></span></li>`;
      })
      .join("");
    const resume = ouvert
      ? `<strong>aucun délai garanti</strong>`
      : `<strong>${enClair(somme)}</strong>`;
    return `<div class="colonne">
      <h3>${titre}</h3>
      <p class="total">${resume} avant de travailler légalement</p>
      <span class="barre ${genre}${ouvert ? " sans-terme" : ""}" aria-hidden="true"><span style="width:${ouvert ? 100 : largeur(somme)}%"></span></span>
      <ol class="etapes">${lignes}</ol>
    </div>`;
  };

  const rendre = (cle) => {
    const c = cas.find((c) => c.cle === cle) || cas[0];
    if (resume) resume.textContent = c.resume;
    const constate = c.colonnes.find((col) => col.genre === "constate");
    const promesse = c.colonnes.find((col) => col.genre === "promesse");
    const ecart = total(constate.etapes) - total(promesse.etapes);
    sortie.innerHTML = `
      <div class="parcours trois">
        ${c.colonnes.map(colonne).join("")}
      </div>
      <p class="ecart"><strong>${enClair(Math.max(ecart, 0))}</strong> entre le
      délai constaté aujourd'hui et le délai que la loi garantirait — à
      contrôles identiques : identité vérifiée, casier consulté, contrat
      contrôlé, étape consulaire maintenue.</p>
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
