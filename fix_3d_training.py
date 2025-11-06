#!/usr/bin/env python3
"""
Script pour corriger le Training.cs pour qu'il fonctionne avec des objets 3D sur le plan XZ
"""

import re

# Lire le fichier
with open('/home/matheo/PROJET_GenerativeWorld/Assets/unity-wave-function-collapse/Training.cs', 'r') as f:
    content = f.read()

# Remplacer les vérifications de position Y par Z (ligne 113-114)
content = re.sub(
    r'if \(\(tilepos\.x > -0\.55f\) && \(tilepos\.x <= width\*gridsize-0\.55f\) &&\n\t\t\t\t  \(tilepos\.y > -0\.55f\) && \(tilepos\.y <= depth\*gridsize-0\.55f\)\){',
    'if ((tilepos.x > -0.55f) && (tilepos.x <= width*gridsize-0.55f) &&\n\t\t\t\t  (tilepos.z > -0.55f) && (tilepos.z <= depth*gridsize-0.55f)){',
    content
)

# Remplacer Y par Z pour la position (ligne 131)
content = re.sub(
    r'int Y = \(int\)\(tilepos\.y\) / gridsize;',
    'int Y = (int)(tilepos.z) / gridsize; // Utiliser Z pour la profondeur',
    content
)

# Remplacer la rotation Z par Y (ligne 132)
content = re.sub(
    r'int R = \(int\)\(\(360 - tile\.transform\.localEulerAngles\.z\)/90\);',
    'int R = (int)((360 - tile.transform.localEulerAngles.y)/90); // Rotation Y pour 3D',
    content
)

# Remplacer dans OnDrawGizmos aussi (ligne 158-159)
content = re.sub(
    r'if \(\(tilepos\.x > -0\.55f\) && \(tilepos\.x <= width\*gridsize-0\.55f\) &&\n\t\t\t\t\(tilepos\.y > -0\.55f\) && \(tilepos\.y <= depth\*gridsize-0\.55f\)\){',
    'if ((tilepos.x > -0.55f) && (tilepos.x <= width*gridsize-0.55f) &&\n\t\t\t\t(tilepos.z > -0.55f) && (tilepos.z <= depth*gridsize-0.55f)){',
    content
)

# Écrire le fichier modifié
with open('/home/matheo/PROJET_GenerativeWorld/Assets/unity-wave-function-collapse/Training.cs', 'w') as f:
    f.write(content)

print("✓ Training.cs modifié pour utiliser le plan XZ (3D)")
