#!/usr/bin/env python3
"""
Script pour corriger le OverlapWFC.cs pour les Gizmos 3D
"""

import re

# Lire le fichier
with open('/home/matheo/PROJET_GenerativeWorld/Assets/unity-wave-function-collapse/OverlapWFC.cs', 'r') as f:
    content = f.read()

# Remplacer le Gizmo dans OnDrawGizmos
content = re.sub(
    r'Gizmos\.DrawWireCube\(new Vector3\(width\*gridsize/2f-gridsize\*0\.5f, depth\*gridsize/2f-gridsize\*0\.5f, 0f\),\n\t\t\t\t\t\t\tnew Vector3\(width\*gridsize, depth\*gridsize, gridsize\)\);',
    'Gizmos.DrawWireCube(new Vector3(width*gridsize/2f-gridsize*0.5f, 0f, depth*gridsize/2f-gridsize*0.5f),\n\t\t\t\t\t\t\tnew Vector3(width*gridsize, gridsize, depth*gridsize));',
    content
)

# Écrire le fichier modifié
with open('/home/matheo/PROJET_GenerativeWorld/Assets/unity-wave-function-collapse/OverlapWFC.cs', 'w') as f:
    f.write(content)

print("✓ OverlapWFC.cs modifié pour les Gizmos 3D")
