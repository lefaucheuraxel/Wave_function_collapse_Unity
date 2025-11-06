# Modifications pour le support 3D du WaveFunctionCollapse

## Problème résolu
Les tiles 3D (murs, etc.) étaient générés à plat sur le plan XY (vertical) au lieu du plan XZ (horizontal).

## Modifications apportées

### 1. **OverlapWFC.cs** - Génération des tiles
- **Ligne 131** : Position changée de `new Vector3(x*gridsize, y*gridsize, 0f)` vers `new Vector3(x*gridsize, 0f, y*gridsize)`
  - Les tiles sont maintenant placés sur le plan XZ (sol horizontal)
  
- **Ligne 139** : Rotation changée de `new Vector3(0, 0, 360 - (rot * 90))` vers `new Vector3(0, 360 - (rot * 90), 0)`
  - La rotation se fait maintenant autour de l'axe Y (vertical) au lieu de Z

- **Lignes 105-106** : Gizmo de visualisation ajusté pour le plan XZ
  - Le cube de prévisualisation s'affiche maintenant horizontalement

### 2. **Training.cs** - Lecture du pattern d'entrée
- **Ligne 113** : Vérification des limites changée pour utiliser `tilepos.z` au lieu de `tilepos.y`
  - Le script lit maintenant les positions sur le plan XZ
  
- **Ligne 131** : Calcul de Y changé de `(int)(tilepos.y) / gridsize` vers `(int)(tilepos.z) / gridsize`
  - La profondeur est maintenant lue depuis l'axe Z
  
- **Ligne 132** : Rotation changée de `tile.transform.localEulerAngles.z` vers `tile.transform.localEulerAngles.y`
  - La rotation des tiles d'entrée est maintenant lue depuis l'axe Y

- **Lignes 152-153** : Gizmo de visualisation ajusté pour le plan XZ
  - Le cube de prévisualisation du Training s'affiche horizontalement

- **Ligne 159** : Vérification des limites dans OnDrawGizmos ajustée pour l'axe Z

## Comment utiliser

### Configuration du Training (Input)
1. Placez vos cubes/tiles de pattern dans le GameObject avec le component **Training**
2. Positionnez-les sur le plan XZ (horizontal) :
   - X : largeur
   - Z : profondeur  
   - Y : hauteur (généralement 0)
3. Faites pivoter vos tiles autour de l'axe Y (rotation verticale)
4. Cliquez sur **"compile"** puis **"record neighbors"** dans l'inspecteur

### Configuration de l'Output
1. Dans le GameObject avec le component **OverlapWFC** :
   - Assignez le Training dans le champ `training`
   - Définissez `width` et `depth` pour la taille de sortie
   - Ajustez `N` (taille du pattern, généralement 2 ou 3)
2. Lancez la scène ou cliquez sur **"generate"** puis **"RUN"** dans l'éditeur

## Résultat
Les tiles 3D sont maintenant générés correctement sur le plan horizontal (XZ), avec les rotations appropriées autour de l'axe Y, ce qui est parfait pour des murs, des sols, et autres objets architecturaux 3D.
