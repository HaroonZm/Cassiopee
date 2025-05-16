import os
import statistics
import argparse
from datetime import datetime

def analyze_python_files(root_dir):
    """
    Analyse tous les fichiers Python dans le répertoire root_dir et ses sous-dossiers.
    Calcule des statistiques sur la longueur (nombre de lignes) et la largeur (longueur des lignes) des fichiers.
    """
    # Pour stocker les résultats
    results = []
    
    # Parcourir tous les fichiers du dossier et sous-dossiers
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                
                try:
                    # Ouvrir et analyser le fichier
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        
                        # Ignorer les lignes vides
                        non_empty_lines = [line for line in lines if line.strip()]
                        
                        # Statistiques sur le fichier
                        if non_empty_lines:
                            line_count = len(non_empty_lines)
                            line_lengths = [len(line.rstrip('\n')) for line in non_empty_lines]
                            max_line_length = max(line_lengths) if line_lengths else 0
                            avg_line_length = sum(line_lengths) / len(line_lengths) if line_lengths else 0
                            
                            results.append({
                                'file': file_path,
                                'line_count': line_count,
                                'max_line_length': max_line_length,
                                'avg_line_length': avg_line_length
                            })
                except Exception as e:
                    print(f"Erreur lors de l'analyse du fichier {file_path}: {e}")
    
    return results

def calculate_statistics(results):
    """
    Calcule les statistiques globales à partir des résultats individuels des fichiers.
    """
    if not results:
        return None
    
    # Extraire les données pour les statistiques
    line_counts = [r['line_count'] for r in results]
    max_line_lengths = [r['max_line_length'] for r in results]
    avg_line_lengths = [r['avg_line_length'] for r in results]
    
    # Calculer les statistiques
    stats = {
        'nombre_de_fichiers': len(results),
        'longueur': {
            'moyenne': statistics.mean(line_counts),
            'médiane': statistics.median(line_counts),
            'min': min(line_counts),
            'max': max(line_counts)
        },
        'largeur_max': {
            'moyenne': statistics.mean(max_line_lengths),
            'médiane': statistics.median(max_line_lengths),
            'min': min(max_line_lengths),
            'max': max(max_line_lengths)
        },
        'largeur_moyenne': {
            'moyenne': statistics.mean(avg_line_lengths),
            'médiane': statistics.median(avg_line_lengths),
            'min': min(avg_line_lengths),
            'max': max(avg_line_lengths)
        }
    }
    
    return stats

def write_results_to_file(results, stats, output_file):
    """
    Écrit les résultats dans un fichier texte.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        # Écrire l'en-tête
        f.write(f"Rapport d'analyse des fichiers Python - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        if not results:
            f.write("Aucun fichier Python trouvé dans le dataset spécifié.\n")
            return
        
        # Écrire les statistiques globales
        f.write("STATISTIQUES GLOBALES\n")
        f.write("-" * 80 + "\n")
        f.write(f"Nombre total de fichiers Python: {stats['nombre_de_fichiers']}\n\n")
        
        f.write("Longueur (nombre de lignes):\n")
        f.write(f"  Moyenne: {stats['longueur']['moyenne']:.2f}\n")
        f.write(f"  Médiane: {stats['longueur']['médiane']:.2f}\n")
        f.write(f"  Min: {stats['longueur']['min']}\n")
        f.write(f"  Max: {stats['longueur']['max']}\n\n")
        
        f.write("Largeur maximale (caractères par ligne):\n")
        f.write(f"  Moyenne: {stats['largeur_max']['moyenne']:.2f}\n")
        f.write(f"  Médiane: {stats['largeur_max']['médiane']:.2f}\n")
        f.write(f"  Min: {stats['largeur_max']['min']}\n")
        f.write(f"  Max: {stats['largeur_max']['max']}\n\n")
        
        f.write("Largeur moyenne (caractères par ligne):\n")
        f.write(f"  Moyenne: {stats['largeur_moyenne']['moyenne']:.2f}\n")
        f.write(f"  Médiane: {stats['largeur_moyenne']['médiane']:.2f}\n")
        f.write(f"  Min: {stats['largeur_moyenne']['min']:.2f}\n")
        f.write(f"  Max: {stats['largeur_moyenne']['max']:.2f}\n\n")
        
        # Écrire les résultats détaillés
        f.write("RÉSULTATS DÉTAILLÉS PAR FICHIER\n")
        f.write("-" * 80 + "\n")
        f.write(f"{'Fichier':<60} {'Lignes':<10} {'Largeur Max':<15} {'Largeur Moyenne':<15}\n")
        f.write("-" * 80 + "\n")
        
        # Trier les résultats par nombre de lignes (décroissant)
        for r in sorted(results, key=lambda x: x['line_count'], reverse=True):
            f.write(f"{r['file']:<60} {r['line_count']:<10} {int(r['max_line_length']):<15} {r['avg_line_length']:<15.2f}\n")

def parse_arguments():
    """
    Analyse les arguments de la ligne de commande.
    """
    parser = argparse.ArgumentParser(description='Analyse la taille des fichiers Python dans un dataset.')
    parser.add_argument('-d', '--dataset', 
                        default='dataset',
                        help='Chemin vers le dossier dataset à analyser (par défaut: "dataset")')
    parser.add_argument('-o', '--output', 
                        default='python_stats_results.txt',
                        help='Nom du fichier de sortie (par défaut: "python_stats_results.txt")')
    return parser.parse_args()

def main():
    # Récupérer les arguments
    args = parse_arguments()
    dataset_path = args.dataset
    output_file = args.output
    
    # Vérifier que le dossier existe
    if not os.path.isdir(dataset_path):
        print(f"Erreur: Le dossier '{dataset_path}' n'existe pas ou n'est pas accessible.")
        return
    
    # Analyser les fichiers
    print(f"Analyse des fichiers Python dans '{dataset_path}' en cours...")
    results = analyze_python_files(dataset_path)
    
    if not results:
        print(f"Aucun fichier Python trouvé dans '{dataset_path}'.")
        write_results_to_file(results, None, output_file)
        print(f"Un rapport vide a été généré dans '{output_file}'.")
        return
    
    # Calculer les statistiques
    print("Calcul des statistiques...")
    stats = calculate_statistics(results)
    
    # Écrire les résultats dans un fichier
    print(f"Écriture des résultats dans '{output_file}'...")
    write_results_to_file(results, stats, output_file)
    
    print(f"\nAnalyse terminée. {len(results)} fichiers Python analysés.")
    print(f"Les résultats ont été enregistrés dans '{output_file}'.")

if __name__ == "__main__":
    main()