#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
import re

def main():
    # Analyse des arguments de la ligne de commande
    parser = argparse.ArgumentParser(description='Intégration de fichiers sources Python depuis un dataset de référence')
    parser.add_argument('batch_path', help='Chemin vers le dossier batch à traiter')
   
    args = parser.parse_args()
   
    # Chemins des datasets
    codenet_path = './original_datasets/codenet'
    thestack_path = './original_datasets/the_stack_organized'
   
    # Vérification de l'existence du dossier batch
    if not os.path.isdir(args.batch_path):
        print(f"Erreur: Le dossier batch '{args.batch_path}' n'existe pas")
        sys.exit(1)
   
    # Vérification de l'existence des dossiers datasets
    if not os.path.isdir(codenet_path):
        print(f"Avertissement: Le dossier dataset '{codenet_path}' n'existe pas. Les samples CodeNet seront ignorés.")
    
    if not os.path.isdir(thestack_path):
        print(f"Avertissement: Le dossier dataset '{thestack_path}' n'existe pas. Les samples The Stack seront ignorés.")
    
    if not os.path.isdir(codenet_path) and not os.path.isdir(thestack_path):
        print("Erreur: Aucun dossier dataset n'existe. Impossible de continuer.")
        sys.exit(1)
   
    # Récupération de tous les fichiers dans le dossier batch
    batch_files = os.listdir(args.batch_path)
    
    # Extraction des identifiants des samples à partir des noms de fichiers
    sample_ids = set()
    for filename in batch_files:
        # Extraction de la partie après le premier underscore
        match = re.match(r'^[^_]+_([^_]+)_', filename)
        if match:
            sample_id = match.group(1)
            sample_ids.add(sample_id)
   
    print(f"Trouvé {len(sample_ids)} identifiants de samples uniques")
   
    # Traitement de chaque identifiant de sample
    total_copied = 0
    for sample_id in sample_ids:
        sample_found = False
        
        # Essayer de trouver dans CodeNet
        if os.path.isdir(codenet_path):
            sample_path = os.path.join(codenet_path, sample_id)
            
            if os.path.isdir(sample_path):
                sample_found = True
                print(f"Traitement du sample CodeNet: {sample_id}")
                
                # Récupération de tous les fichiers Python dans le sous-dossier
                py_files = [f for f in os.listdir(sample_path) if f.endswith('.py')]
                
                if not py_files:
                    print(f"Avertissement: Aucun fichier Python trouvé dans le sous-dossier CodeNet '{sample_id}'")
                else:
                    # Copie et renommage de chaque fichier Python
                    for py_file in py_files:
                        src_path = os.path.join(sample_path, py_file)
                        new_filename = f"human_{sample_id}_{py_file}"
                        dst_path = os.path.join(args.batch_path, new_filename)
                        
                        shutil.copy2(src_path, dst_path)
                        total_copied += 1
                        print(f"Copié (CodeNet): {py_file} -> {new_filename}")
        
        # Essayer de trouver dans The Stack si pas déjà trouvé dans CodeNet
        if not sample_found and os.path.isdir(thestack_path):
            # Chercher le premier sous-dossier qui contient l'identifiant
            found = False
            for subdir in os.listdir(thestack_path):
                if sample_id in subdir:
                    sample_path = os.path.join(thestack_path, subdir)
                    found = True
                    print(f"Trouvé: sous-dossier '{subdir}' pour l'identifiant '{sample_id}' dans The Stack")
                    
                    # Récupération de tous les fichiers Python dans le sous-dossier
                    py_files = [f for f in os.listdir(sample_path) if f.endswith('.py')]
                    
                    if not py_files:
                        print(f"Avertissement: Aucun fichier Python trouvé dans le sous-dossier The Stack '{subdir}'")
                    else:
                        # Copie et renommage de chaque fichier Python
                        for py_file in py_files:
                            src_path = os.path.join(sample_path, py_file)
                            new_filename = f"human_{sample_id}_{py_file}"
                            dst_path = os.path.join(args.batch_path, new_filename)
                            
                            shutil.copy2(src_path, dst_path)
                            total_copied += 1
                            print(f"Copié (The Stack): {py_file} -> {new_filename}")
                    
                    break
            
            if not found:
                print(f"Avertissement: L'identifiant '{sample_id}' n'a pas été trouvé dans The Stack")
        
        # Si l'identifiant n'a été trouvé dans aucun dataset
        if not sample_found and (not os.path.isdir(thestack_path) or not found):
            print(f"Avertissement: L'identifiant '{sample_id}' n'a été trouvé dans aucun dataset")
   
    print(f"Terminé! {total_copied} nouveaux fichiers ont été copiés dans le dossier batch.")

if __name__ == '__main__':
    main()