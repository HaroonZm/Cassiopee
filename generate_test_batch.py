#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import tempfile
from pathlib import Path
import shutil

# Ajouter le répertoire actuel au chemin de recherche
sys.path.append('.')

# Créer un répertoire temporaire pour le test
temp_dir = Path("./temp_test")
temp_dir.mkdir(exist_ok=True)
scripts_dir = temp_dir / "scripts"
scripts_dir.mkdir(exist_ok=True)
output_dir = temp_dir / "output"
output_dir.mkdir(exist_ok=True)

# Créer un fichier Python simple pour tester
test_script = scripts_dir / "hello.py"
with open(test_script, "w", encoding="utf-8") as f:
    f.write("""
def hello():
    print("Hello, World!")

if __name__ == "__main__":
    hello()
""")

print(f"Script créé dans {test_script}")
print(f"Répertoire de sortie: {output_dir}")

# Importer uniquement les classes nécessaires
from matrix_generation.matrix_batch_sender import BatchAnalyzer, tokeniser_avec_tiktoken
from pathlib import Path
import json, datetime, time, os

# Fonction simplifiée pour soumettre un batch
def submit_batch_simple(script_path, output_dir):
    """Version simplifiée de envoyer_batches qui ne traite qu'un seul fichier"""
    # Lire le contenu du script
    with open(script_path, "r", encoding="utf-8") as f:
        script_content = f.read()
    
    # Tokeniser le script
    token_ids, tokens = tokeniser_avec_tiktoken(script_content, "gpt-4o-mini")
    print(f"Script {script_path.name} tokenisé en {len(tokens)} tokens")
    
    # Créer l'objet BatchAnalyzer
    analyzer = BatchAnalyzer(batch_size=10, poll_interval=5)
    
    # Créer une requête simple pour test
    from matrix_generation.matrix_batch_sender import BatchRequestItem
    items = []
    for i in range(5):  # Juste 5 tokens pour tester
        item = BatchRequestItem(
            script_name=script_path.name,
            token_index=i,
            token_content=tokens[i] if i < len(tokens) else "test",
            context="".join(tokens[:i]) if i > 0 else "",
            model="gpt-4o-mini"
        )
        items.append(item)
    
    # Soumettre le batch
    print("Soumission du batch...")
    batch_id = analyzer.submit_batch(items)
    
    # Préfixer l'ID du batch
    prefixed_batch_id = f"tbatch_{batch_id[6:]}" if batch_id.startswith("batch_") else batch_id
    
    # Enregistrer les informations du batch
    batch_info = {
        "original_batch_id": batch_id,
        "prefixed_batch_id": prefixed_batch_id,
        "status": "submitted",
        "timestamp": datetime.datetime.now().isoformat(),
        "script": script_path.name,
        "tokens_count": len(tokens)
    }
    
    # Sauvegarder les informations
    batch_info_file = output_dir / f"tbatch_info_{batch_id}.json"
    with open(batch_info_file, "w", encoding="utf-8") as f:
        json.dump(batch_info, f, ensure_ascii=False, indent=2)
    
    return prefixed_batch_id

print("Génération du batch...")
try:
    # Appeler notre fonction simplifiée
    batch_id = submit_batch_simple(test_script, output_dir)
    
    print(f"\nBatch généré: {batch_id}")
    
    # Vérifier le préfixe
    if batch_id.startswith("tbatch_"):
        print(f"✅ Préfixe correct: {batch_id}")
    else:
        print(f"❌ Préfixe incorrect: {batch_id} (attendu: tbatch_)")
    
    # Liste des fichiers créés
    print("\nFichiers créés:")
    for file in output_dir.glob("*"):
        print(f"- {file.name}")
    
except Exception as e:
    print(f"Erreur: {e}")
    import traceback
    print(traceback.format_exc()) 