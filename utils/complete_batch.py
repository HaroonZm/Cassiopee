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
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--codenet', action='store_true', help='Utiliser le dataset CodeNet')
    group.add_argument('--thestack', action='store_true', help='Utiliser le dataset The Stack')
   
    args = parser.parse_args()
   
    # Définition du chemin du dataset en fonction de l'option choisie
    if args.codenet:
        dataset_path = './original_datasets/codenet'
    else:  # args.thestack
        dataset_path = './original_datasets/the_stack_organized'
   
    # Vérification de l'existence du dossier batch
    if not os.path.isdir(args.batch_path):
        print(f"Erreur: Le dossier batch '{args.batch_path}' n'existe pas")
        sys.exit(1)
   
    # Vérification de l'existence du dossier dataset
    if not os.path.isdir(dataset_path):
        print(f"Erreur: Le dossier dataset '{dataset_path}' n'existe pas")
        sys.exit(1)
    
    # Création du sous-dossier scripts s'il n'existe pas
    scripts_dir = os.path.join(args.batch_path, "scripts")
    if not os.path.exists(scripts_dir):
        os.makedirs(scripts_dir)
        print(f"Dossier '{scripts_dir}' créé")
   
    # Récupération de tous les fichiers dans le dossier batch
    batch_files = os.listdir(args.batch_path)
    
    # Déplacer tous les fichiers Python existants du dossier batch vers scripts
    python_files_moved = 0
    for filename in batch_files:
        if filename.endswith('.py'):
            src_path = os.path.join(args.batch_path, filename)
            dst_path = os.path.join(scripts_dir, filename)
            
            # Ne pas déplacer le dossier scripts lui-même s'il est un fichier .py (cas peu probable)
            if filename != "scripts":
                shutil.move(src_path, dst_path)
                python_files_moved += 1
                print(f"Déplacé: {filename} -> scripts/{filename}")
    
    print(f"{python_files_moved} fichiers Python existants ont été déplacés vers le dossier 'scripts'")
   
    # Extraction des identifiants des samples à partir des noms de fichiers restants ou déplacés
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
        # Construction du chemin vers le sous-dossier dans le dataset
        sample_path = os.path.join(dataset_path, sample_id)
       
        # Vérification de l'existence du sous-dossier
        if not os.path.isdir(sample_path):
            print(f"Avertissement: Le sous-dossier '{sample_id}' n'a pas été trouvé dans le dataset")
            continue
       
        print(f"Traitement du sample: {sample_id}")
       
        # Récupération de tous les fichiers Python dans le sous-dossier
        py_files = [f for f in os.listdir(sample_path) if f.endswith('.py')]
       
        if not py_files:
            print(f"Avertissement: Aucun fichier Python trouvé dans le sous-dossier '{sample_id}'")
            continue
       
        # Copie et renommage de chaque fichier Python
        for py_file in py_files:
            src_path = os.path.join(sample_path, py_file)
            new_filename = f"human_{sample_id}_{py_file}"
            # Utilisation du sous-dossier scripts comme destination
            dst_path = os.path.join(scripts_dir, new_filename)
           
            shutil.copy2(src_path, dst_path)
            total_copied += 1
            print(f"Copié: {py_file} -> scripts/{new_filename}")
   
    print(f"Terminé! {total_copied} nouveaux fichiers ont été copiés dans le dossier 'scripts'.")

if __name__ == '__main__':
    main()