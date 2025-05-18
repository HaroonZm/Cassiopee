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
        dataset_path = './codenet'
    else:  # args.thestack
        dataset_path = './the_stack_organized'
    
    # Vérification de l'existence du dossier batch
    if not os.path.isdir(args.batch_path):
        print(f"Erreur: Le dossier batch '{args.batch_path}' n'existe pas")
        sys.exit(1)
    
    # Vérification de l'existence du dossier dataset
    if not os.path.isdir(dataset_path):
        print(f"Erreur: Le dossier dataset '{dataset_path}' n'existe pas")
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
            dst_path = os.path.join(args.batch_path, new_filename)
            
            shutil.copy2(src_path, dst_path)
            total_copied += 1
            print(f"Copié: {py_file} -> {new_filename}")
    
    print(f"Terminé! {total_copied} fichiers ont été copiés au total.")

if __name__ == '__main__':
    main()