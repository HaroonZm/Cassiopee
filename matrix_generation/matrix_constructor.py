import json
import os
import shutil
import numpy as np
from typing import Dict, List, Tuple, Optional
import pandas as pd
import logging
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TokenMatrixConstructor:
    def __init__(self, input_directory: str):
        """
        Constructeur de matrices basé sur les fichiers JSON de tokens
        Inspiré de la logique du script d'analyse OpenAI
        
        Args:
            input_directory: Dossier contenant les fichiers JSON des tokens
        """
        self.input_directory = Path(input_directory)
        self.token_data = {}
        self.vocabulary = set()
        self.scripts_info = {}
        
    def load_token_files(self) -> Dict[str, Tuple[List[Dict], Path]]:
        """
        Charge tous les fichiers JSON de tokens depuis le dossier d'entrée
        
        Returns:
            Dict avec nom_fichier -> (données des tokens, chemin du fichier)
        """
        token_files = {}
        
        if not self.input_directory.exists():
            raise ValueError(f"Le dossier {self.input_directory} n'existe pas")
            
        for filepath in self.input_directory.glob("*_tokens.json"):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Extraire les informations du nom de fichier
                script_name = filepath.stem.replace('_tokens', '')
                token_files[script_name] = (data, filepath)
                
                # Construire le vocabulaire
                self._build_vocabulary(data)
                
                logger.info(f"Chargé: {filepath.name} ({len(data)} tokens)")
                
            except Exception as e:
                logger.error(f"Erreur lors du chargement de {filepath.name}: {e}")
                
        # Sauvegarder les données pour usage ultérieur, mais garder aussi les chemins
        self.token_data = {name: data for name, (data, _) in token_files.items()}
        return token_files
    
    def _build_vocabulary(self, token_data: List[Dict]):
        """
        Construit le vocabulaire à partir des données de tokens
        """
        for token_info in token_data:
            # Ajouter le token principal
            if token_info.get('token'):
                self.vocabulary.add(token_info['token'])
            
            # Ajouter les alternatives
            for alt in token_info.get('alternatives', []):
                if alt.get('token'):
                    self.vocabulary.add(alt['token'])

    def _reconstruct_text_and_get_structure(self, tokens: List[str]) -> Tuple[List[str], List[int], List[Tuple[int, int]]]:
        """
        Reconstruit le texte et analyse sa structure en lignes
        Inspiré de la fonction construire_matrice_logprob du script original
        
        Args:
            tokens: Liste des tokens à analyser
            
        Returns:
            Tuple (lignes_texte, tokens_par_ligne, position_tokens)
        """
        # 1) Reconstituer le texte complet et découper en lignes
        texte_complet = ''.join(tokens)
        lignes_texte = texte_complet.split('\n')
        
        # Ajuster les lignes pour gérer les cas spéciaux
        if tokens and tokens[-1] != '\n':
            # Le dernier token n'est pas un saut de ligne
            pass
        else:
            # Ajouter une ligne vide si le texte se termine par \n
            lignes_texte.append('')
        
        # Supprimer la dernière ligne vide si elle existe
        if lignes_texte and lignes_texte[-1] == '':
            lignes_texte = lignes_texte[:-1]
        
        n_lignes = len(lignes_texte)
        
        # 2) Parcourir les tokens pour déterminer tokens_par_ligne et positions
        tokens_par_ligne = []
        position_tokens = []
        ligne_courante = 0
        position_dans_ligne = 0
        
        for i, token in enumerate(tokens):
            # Enregistrer la position
            position_tokens.append((ligne_courante, position_dans_ligne))
            position_dans_ligne += 1
            
            # Si le token contient un saut de ligne, on change de ligne
            if '\n' in token:
                tokens_par_ligne.append(position_dans_ligne)
                ligne_courante += 1
                position_dans_ligne = 0
                if ligne_courante >= n_lignes:
                    break
        
        # Ajouter la dernière ligne si nécessaire
        if ligne_courante < n_lignes and position_dans_ligne > 0:
            tokens_par_ligne.append(position_dans_ligne)
        
        return lignes_texte, tokens_par_ligne, position_tokens

    def construire_matrice_logprob(self, script_name: str, top_k: int = 10) -> Tuple[np.ndarray, Dict]:
        """
        Construit une matrice 2D de log probabilités avec la même logique que le script original
        
        Args:
            script_name: Nom du script à traiter
            top_k: Nombre d'alternatives à considérer
            
        Returns:
            Tuple (matrice, structure_info)
        """
        if script_name not in self.token_data:
            raise ValueError(f"Script {script_name} non trouvé dans les données")
        
        data = self.token_data[script_name]
        
        # Extraire les tokens de référence
        tokens_reference = []
        for token_info in data:
            token = token_info.get('token', '')
            tokens_reference.append(token)
        
        # Analyser la structure du texte
        lignes_texte, tokens_par_ligne, position_tokens = self._reconstruct_text_and_get_structure(tokens_reference)
        
        # Calculer les dimensions de la matrice
        n_lignes = len(lignes_texte)
        max_tokens = max(tokens_par_ligne) if tokens_par_ligne else 0
        
        logger.info(f"Structure du code pour {script_name}: {n_lignes} lignes, {max_tokens} tokens max par ligne")
        
        # Initialiser la matrice de padding avec les dimensions dynamiques
        # Valeur 100.0 pour le padding comme dans le script original
        matrice = np.full((n_lignes, max_tokens), 100.0)
        
        structure = {
            "script_name": script_name,
            "lignes": n_lignes,
            "max_tokens": max_tokens,
            "tokens_par_ligne": tokens_par_ligne,
            "position_tokens": position_tokens,
            "lignes_texte": lignes_texte
        }
        
        # Remplir la matrice avec log-probabilités ou valeurs spéciales
        for idx, (i, j) in enumerate(position_tokens):
            if i < n_lignes and j < max_tokens:
                token_info = data[idx] if idx < len(data) else None
                
                if not token_info:
                    # Pas d'information pour ce token -> anomalie
                    matrice[i, j] = -50.0
                    continue
                
                token_attendu = token_info.get('token', '')
                alternatives = token_info.get('alternatives', [])
                
                # Si pas d'alternatives, c'est probablement un token d'amorce
                if not alternatives:
                    matrice[i, j] = -10.0  # Valeur pour l'amorce
                    continue
                
                # Valeur par défaut pour anomalie
                val = -50.0
                
                # Chercher le token attendu dans les alternatives
                for alt in alternatives:
                    if alt.get("token") == token_attendu:
                        val = alt.get("logprob", -50.0)
                        break
                
                # Si le token attendu n'est pas dans les alternatives, garder -50.0
                matrice[i, j] = val
        
        return matrice, structure

    def afficher_matrice_brute(self, matrice: np.ndarray, structure: Dict):
        """
        Affiche la matrice 2D de log probabilités brute dans la console
        Reproduit la fonction du script original
        """
        print(f"\nMATRICE BRUTE DE LOG PROBABILITÉS - {structure['script_name']}:")
        print(f"Dimensions: {matrice.shape[0]} lignes x {matrice.shape[1]} colonnes")
        
        # Calculer la largeur maximale pour l'affichage
        max_w = 10  # Largeur par défaut pour chaque valeur
        
        # Créer une ligne de séparation
        sep = "-" * (max_w * matrice.shape[1] + 10)
        print(sep)
        
        # Afficher les indices de colonnes
        print("     ", end="")
        for j in range(matrice.shape[1]):
            print(f"{j:^{max_w}}", end="")
        print()  # Nouvelle ligne
        
        # Ligne de séparation après les indices de colonnes
        print("     " + "-" * (max_w * matrice.shape[1]))
        
        # Afficher chaque ligne avec son indice
        for i in range(matrice.shape[0]):
            print(f"{i:3d} |", end="")
            for j in range(matrice.shape[1]):
                val = matrice[i, j]
                if val == 100:
                    # Padding
                    cell = "PAD"
                elif val == -50:
                    # Anomalie
                    cell = "ANOM"
                elif val == -10:
                    # Amorce
                    cell = "AMOR"
                else:
                    # Log probabilité normale
                    cell = f"{val:.4f}"
                print(f"{cell:^{max_w}}", end="")
            print()  # Nouvelle ligne
        
        # Ligne de séparation finale
        print(sep)
        
        # Légende
        print("Légende:")
        print("  - PAD  : Padding (valeur 100)")
        print("  - ANOM : Anomalie (valeur -50)")
        print("  - AMOR : Amorce (valeur -10)")
        print("  - Autres valeurs : Log probabilités réelles")
        print(sep)

    def sauvegarder_matrice_numpy(self, matrice: np.ndarray, nom_fichier: str):
        """
        Sauvegarde la matrice au format numpy pour une utilisation ultérieure.
        """
        np.save(nom_fichier, matrice)
        logger.info(f"Matrice sauvegardée dans {nom_fichier}")

    def analyser_script_statistiques(self, script_name: str) -> Dict:
        """
        Analyse statistique d'un script avec la logique adaptée
        """
        if script_name not in self.token_data:
            raise ValueError(f"Script {script_name} non trouvé")
        
        data = self.token_data[script_name]
        matrice, structure = self.construire_matrice_logprob(script_name)
        
        stats = {
            'script_name': script_name,
            'total_positions': len(data),
            'lignes_code': structure['lignes'],
            'max_tokens_par_ligne': structure['max_tokens'],
            'tokens_par_ligne': structure['tokens_par_ligne'],
            'positions_with_alternatives': 0,
            'positions_amorce': 0,
            'positions_anomalie': 0,
            'total_alternatives': 0,
            'avg_alternatives_per_position': 0,
            'max_alternatives': 0,
            'min_logprob': float('inf'),
            'max_logprob': float('-inf'),
            'reconstructed_code': ''
        }
        
        all_logprobs = []
        reconstructed_tokens = []
        
        for token_info in data:
            token = token_info.get('token', '')
            reconstructed_tokens.append(token)
            alternatives = token_info.get('alternatives', [])
            
            if not alternatives:
                stats['positions_amorce'] += 1
            else:
                stats['positions_with_alternatives'] += 1
                stats['total_alternatives'] += len(alternatives)
                stats['max_alternatives'] = max(stats['max_alternatives'], len(alternatives))
                
                # Analyser les log-probabilités
                for alt in alternatives:
                    logprob = alt.get('logprob', float('-inf'))
                    if logprob != float('-inf'):
                        all_logprobs.append(logprob)
                        stats['min_logprob'] = min(stats['min_logprob'], logprob)
                        stats['max_logprob'] = max(stats['max_logprob'], logprob)
                
                # Vérifier si le token attendu est dans les alternatives
                token_found = any(alt.get('token') == token for alt in alternatives)
                if not token_found:
                    stats['positions_anomalie'] += 1
        
        if stats['positions_with_alternatives'] > 0:
            stats['avg_alternatives_per_position'] = stats['total_alternatives'] / stats['positions_with_alternatives']
        
        # Reconstruire le code
        stats['reconstructed_code'] = ''.join(reconstructed_tokens)
        
        # Statistiques de la matrice
        unique_values, counts = np.unique(matrice, return_counts=True)
        matrix_stats = dict(zip(unique_values, counts))
        stats['matrix_stats'] = {
            'padding_cells': matrix_stats.get(100.0, 0),
            'anomaly_cells': matrix_stats.get(-50.0, 0),
            'amorce_cells': matrix_stats.get(-10.0, 0),
            'logprob_cells': sum(counts) - matrix_stats.get(100.0, 0) - matrix_stats.get(-50.0, 0) - matrix_stats.get(-10.0, 0)
        }
        
        return stats

    def generer_rapport_detaille(self, script_name: str, output_file: str = None):
        """
        Génère un rapport détaillé similaire au script original
        """
        if script_name not in self.token_data:
            raise ValueError(f"Script {script_name} non trouvé")
        
        data = self.token_data[script_name]
        matrice, structure = self.construire_matrice_logprob(script_name)
        stats = self.analyser_script_statistiques(script_name)
        
        if output_file is None:
            output_file = f"rapport_{script_name}.txt"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # Écrire l'en-tête
            f.write("="*80 + f"\nRAPPORT D'ANALYSE - {script_name}\n" + "="*80 + "\n\n")
            
            # Écrire le script reconstruit
            f.write("SCRIPT RECONSTRUIT:\n" + "-"*80 + "\n")
            f.write(stats['reconstructed_code'] + "\n" + "-"*80 + "\n\n")
            
            # Écrire la matrice 2D
            f.write("MATRICE 2D:\n" + "-"*80 + "\n")
            for i in range(matrice.shape[0]):
                row = []
                for j in range(matrice.shape[1]):
                    v = matrice[i, j]
                    if v == 100:
                        row.append("PAD")
                    elif v == -50:
                        row.append("ANOM")
                    elif v == -10:
                        row.append("AMOR")
                    else:
                        row.append(f"{v:.2f}")
                f.write("[ " + ", ".join(row) + " ]\n")
            f.write("\n")
            
            # Écrire l'analyse token par token
            f.write("ANALYSE TOKEN PAR TOKEN:\n" + "-"*80 + "\n")
            for idx, token_info in enumerate(data):
                token = token_info.get('token', '')
                alternatives = token_info.get('alternatives', [])
                
                f.write(f"Position {idx}: '{repr(token)[1:-1]}'\n")
                
                if not alternatives:
                    f.write("  -> Token d'amorce (pas d'alternatives)\n\n")
                    continue
                
                # Vérifier si le token est dans les alternatives
                token_found = False
                token_logprob = -50.0
                
                for alt in alternatives:
                    if alt.get('token') == token:
                        token_found = True
                        token_logprob = alt.get('logprob', -50.0)
                        break
                
                status = "✓" if token_found else "✗"
                f.write(f"  -> Status: {status} (logprob: {token_logprob:.4f})\n")
                
                # Afficher les alternatives
                f.write("  -> Alternatives:\n")
                for i, alt in enumerate(alternatives[:10]):  # Top 10
                    alt_token = alt.get('token', '')
                    alt_logprob = alt.get('logprob', -100)
                    marker = " [TOKEN ATTENDU]" if alt_token == token else ""
                    f.write(f"    {i+1}. '{repr(alt_token)[1:-1]}' (logprob: {alt_logprob:.4f}){marker}\n")
                f.write("\n")
            
            # Ajouter les statistiques
            f.write("STATISTIQUES:\n" + "-"*80 + "\n")
            f.write(f"Script: {stats['script_name']}\n")
            f.write(f"Total des positions: {stats['total_positions']}\n")
            f.write(f"Lignes de code: {stats['lignes_code']}\n")
            f.write(f"Tokens max par ligne: {stats['max_tokens_par_ligne']}\n")
            f.write(f"Positions avec alternatives: {stats['positions_with_alternatives']}\n")
            f.write(f"Positions d'amorce: {stats['positions_amorce']}\n")
            f.write(f"Positions d'anomalie: {stats['positions_anomalie']}\n")
            f.write(f"Alternatives moyennes par position: {stats['avg_alternatives_per_position']:.2f}\n")
            f.write(f"Max alternatives: {stats['max_alternatives']}\n")
            if stats['min_logprob'] != float('inf'):
                f.write(f"Log-prob min: {stats['min_logprob']:.4f}\n")
                f.write(f"Log-prob max: {stats['max_logprob']:.4f}\n")
            
            # Statistiques de la matrice
            f.write(f"\nSTATISTIQUES DE LA MATRICE:\n")
            f.write(f"Cellules de padding: {stats['matrix_stats']['padding_cells']}\n")
            f.write(f"Cellules d'anomalie: {stats['matrix_stats']['anomaly_cells']}\n")
            f.write(f"Cellules d'amorce: {stats['matrix_stats']['amorce_cells']}\n")
            f.write(f"Cellules avec log-prob: {stats['matrix_stats']['logprob_cells']}\n")
            
            f.write("\n" + "="*80 + "\n")
        
        logger.info(f"Rapport détaillé sauvegardé dans {output_file}")
        return output_file

    def archive_token_file(self, script_name: str, token_files_dict: Dict[str, Tuple[List[Dict], Path]], archive_dir: str):
        """
        Déplace le fichier JSON de tokens vers le dossier d'archive après traitement réussi
        
        Args:
            script_name: Nom du script traité
            token_files_dict: Dictionnaire des fichiers de tokens avec leurs chemins
            archive_dir: Dossier de destination pour l'archivage
        """
        if script_name not in token_files_dict:
            logger.warning(f"Impossible d'archiver {script_name}: fichier non trouvé dans le dictionnaire")
            return False
        
        try:
            _, source_path = token_files_dict[script_name]
            archive_path = Path(archive_dir)
            archive_path.mkdir(parents=True, exist_ok=True)
            
            destination_path = archive_path / source_path.name
            
            # Déplacer le fichier (pas copier)
            shutil.move(str(source_path), str(destination_path))
            logger.info(f"Fichier JSON archivé: {source_path.name} -> {destination_path}")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors de l'archivage de {script_name}: {e}")
            return False

def main():
    """
    Fonction principale avec gestion des arguments de ligne de commande
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Constructeur de matrices à partir de fichiers JSON de tokens",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  %(prog)s --input-dir ./tokens_json --output-dir ./matrices_output
  %(prog)s -i ./data/tokens -o ./results --script gen_p00000_optimized.py__12
  %(prog)s --input-dir ./tokens --output-dir ./output --archive-dir ./processed
  %(prog)s -i ./tokens -o ./output -a ./archive --display-matrix --verbose
        """
    )
    
    # Arguments obligatoires
    parser.add_argument(
        '--input-dir', '-i', 
        type=str, 
        required=True,
        help='Dossier contenant les fichiers JSON de tokens (*_tokens.json)'
    )
    
    parser.add_argument(
        '--output-dir', '-o', 
        type=str, 
        required=True,
        help='Dossier de sortie pour les matrices et rapports'
    )
    
    # Arguments optionnels
    parser.add_argument(
        '--script', '-s',
        type=str,
        default=None,
        help='Nom spécifique du script à traiter (sans extension). Si non spécifié, traite tous les scripts.'
    )
    
    parser.add_argument(
        '--display-matrix', '-d',
        action='store_true',
        help='Afficher les matrices dans la console'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Mode verbeux (affichage détaillé)'
    )
    
    parser.add_argument(
        '--top-k',
        type=int,
        default=10,
        help='Nombre maximum d\'alternatives à considérer (défaut: 10)'
    )
    
    parser.add_argument(
        '--archive-dir', '-a',
        type=str,
        default=None,
        help='Dossier d\'archive où déplacer les fichiers JSON après traitement réussi (optionnel)'
    )
    
    args = parser.parse_args()
    
    # Configuration du logging selon le mode verbeux
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        # Vérifier que le dossier d'entrée existe
        input_path = Path(args.input_dir)
        if not input_path.exists():
            logger.error(f"Le dossier d'entrée n'existe pas: {input_path}")
            return 1
            
        # Créer le dossier de sortie s'il n'existe pas
        output_path = Path(args.output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Dossier d'entrée: {input_path}")
        logger.info(f"Dossier de sortie: {output_path}")
        if args.archive_dir:
            logger.info(f"Dossier d'archive: {args.archive_dir}")
        
        # Initialiser le constructeur
        constructor = TokenMatrixConstructor(str(input_path))
        
        # Charger les fichiers
        token_files = constructor.load_token_files()
        
        if not token_files:
            logger.warning("Aucun fichier *_tokens.json trouvé dans le dossier d'entrée")
            return 1
        
        logger.info(f"Nombre de scripts trouvés: {len(token_files)}")
        
        # Déterminer quels scripts traiter
        scripts_to_process = []
        if args.script:
            if args.script in token_files:
                scripts_to_process = [args.script]
                logger.info(f"Traitement du script spécifique: {args.script}")
            else:
                logger.error(f"Script '{args.script}' non trouvé. Scripts disponibles: {list(token_files.keys())}")
                return 1
        else:
            scripts_to_process = list(token_files.keys())
            logger.info("Traitement de tous les scripts disponibles")
        
        # Créer les dossiers de sortie
        rapports_dir = output_path / "rapports"
        rapports_dir.mkdir(parents=True, exist_ok=True)
        
        # Traiter chaque script
        processed_count = 0
        for script_name in scripts_to_process:
            logger.info(f"Traitement de {script_name}...")
            
            try:
                # Construire la matrice
                matrice, structure = constructor.construire_matrice_logprob(script_name, top_k=args.top_k)
                
                # Afficher la matrice si demandé
                if args.display_matrix:
                    constructor.afficher_matrice_brute(matrice, structure)
                
                # Sauvegarder la matrice directement dans output_path
                matrix_file = output_path / f"matrix_{script_name}.npy"
                constructor.sauvegarder_matrice_numpy(matrice, str(matrix_file))
                
                # Générer le rapport détaillé
                rapport_file = rapports_dir / f"rapport_{script_name}.txt"
                constructor.generer_rapport_detaille(script_name, str(rapport_file))
                
                # Archiver le fichier JSON si un dossier d'archive est spécifié
                if args.archive_dir:
                    archive_success = constructor.archive_token_file(script_name, token_files, args.archive_dir)
                    if not archive_success:
                        logger.warning(f"Échec de l'archivage pour {script_name}, mais traitement réussi")
                
                # Générer les statistiques si mode verbeux
                if args.verbose:
                    stats = constructor.analyser_script_statistiques(script_name)
                    logger.info(f"Statistiques pour {script_name}:")
                    logger.info(f"  - Lignes de code: {stats['lignes_code']}")
                    logger.info(f"  - Positions avec alternatives: {stats['positions_with_alternatives']}")
                    logger.info(f"  - Positions d'amorce: {stats['positions_amorce']}")
                    logger.info(f"  - Positions d'anomalie: {stats['positions_anomalie']}")
                    logger.info(f"  - Max alternatives par position: {stats['max_alternatives']}")
                
                processed_count += 1
                logger.info(f"✓ {script_name} traité avec succès")
                
            except Exception as e:
                logger.error(f"✗ Erreur lors du traitement de {script_name}: {e}")
                if args.verbose:
                    import traceback
                    logger.error(traceback.format_exc())
        
        # Résumé final
        logger.info(f"\nTraitement terminé:")
        logger.info(f"  - Scripts traités avec succès: {processed_count}/{len(scripts_to_process)}")
        logger.info(f"  - Matrices sauvegardées dans: {output_path}")
        logger.info(f"  - Rapports sauvegardés dans: {rapports_dir}")
        if args.archive_dir:
            logger.info(f"  - Fichiers JSON archivés dans: {args.archive_dir}")
        
        if processed_count == len(scripts_to_process):
            logger.info("✓ Tous les scripts ont été traités avec succès")
            return 0
        else:
            logger.warning(f"⚠ {len(scripts_to_process) - processed_count} scripts n'ont pas pu être traités")
            return 1
            
    except KeyboardInterrupt:
        logger.info("Traitement interrompu par l'utilisateur")
        return 1
    except Exception as e:
        logger.error(f"Erreur générale: {e}")
        if args.verbose:
            import traceback
            logger.error(traceback.format_exc())
        return 1

if __name__ == "__main__":
    exit(main())