# Projet-Informatique-ML
IA QUI COLORE LES MAILS

**Première réu avec Valoche**
- Quitter la chaine de caractère, trouver une nouvelle représentation
- Qu'est ce qu'on met dans nos vecteur?
- Réseaux pré-entrainé, comment s'en servir?
- 2pbs:
  * Extraire la mise en forme d'un texte
  * Formater un texte vierge
- Représentation vectorielle et distance entre les mots
- Apprentissage simple au début
- Proximité dans le texte + même fomat = faible distance?

**Prise en main de biblio python-docx**
https://python-docx.readthedocs.io/en/latest/#
Docx -> Paragraphes -> runs -> fonts
Dans un font:
* couleur (color)
* surlignage (highlight_color)
* taille (size)
* gras (bold)
* italic
* souligné (underline)
* police (name)
* barré (strike)
* CAST (all_caps)

*Seuls certaines couleurs du package word sont récupérables/utilisables*

**Différentes méthodes de Word-embending**
-TFID
- Réseau de neuronne de Bengio (http://www.scholarpedia.org/article/Neural_net_language_models)
  * Proba d'un mot sachant les mots avant dans la phrase
  * Utilisé pour compléter une phrase...
  
- Skip-gram et Continuous Bag of Word (CBOW)
  * Réseau de neuronne pour entrainer une matrice de vecteurs en utilisant les mots autour (contexte)

- GloVe:
  * Matrice de coapparition puis fonction cout --> entrainement en 1 fois
  * Prend en compte le contexte proche (les mots autour) et le contexte général (est-ce qu'ils apparaissent souvent ensemble?)


*Proposition*
Utiliser des tenseurs d'ordre 2 et 3 pour ajouter la mise en forme dans la représentation vectorielle (tensorielle maintenant) dans les réseaux de neuronnes

**Avant entrainement il faut au préablable:**
- pre-process / résuire les infos inutiles --> prise en main de regex (expressions regulières)
- Choisir la mise en forme à garder et comment on la stocke --> prise en main de python-docx
