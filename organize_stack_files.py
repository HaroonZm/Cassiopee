import os
import json
from collections import defaultdict
from datetime import datetime
from datasets import load_dataset
from tqdm import tqdm
import sys

# ===========================
# Configuration principale
# ===========================
OUTPUT_DIR = "the_stack_organized"
TARGET_REPOS = 1000         # Nombre de dépôts à collecter
MIN_FILES_PER_REPO = 5      # Nombre mini de fichiers par dépôt
MIN_STARS = 100             # Seuil minimal d'étoiles
MAX_FILE_SIZE = 1_000_000   # Taille max d'un fichier (1MB)
MIN_CODE_LENGTH = 2000      # Longueur min de code (caractères) - pour environ 50 lignes
MIN_ALPHANUM = 0.3          # Fraction min alphanumérique
PERMISSIVE_LICENSES = ["mit", "apache", "bsd", "isc", "zlib", "cc0"]

# Coupe date – on veut tout avant le 1er janvier 2020
CUTOFF_DATE = datetime(2020, 1, 1)

# ===========================
# Préparation du dossier de sortie
# ===========================
os.makedirs(OUTPUT_DIR, exist_ok=True)
global_metadata_path = os.path.join(OUTPUT_DIR, "metadata.json")

# ===========================
# Configuration des logs debug
# ===========================
def debug_print(msg):
    print(f"DEBUG: {msg}")

# ===========================
# Chargement en streaming (ajout du split)
# ===========================
print("Chargement du dataset The Stack en streaming...")
try:
    dataset = load_dataset(
        "bigcode/the-stack",
        data_dir="data/python",
        split="train",
        streaming=True
    )
    print("Dataset chargé avec succès!")
except Exception as e:
    print(f"ERREUR lors du chargement du dataset: {str(e)}")
    print("Vérifiez que vous avez bien installé la bibliothèque datasets: pip install datasets")
    sys.exit(1)

# ===========================
# Structures de suivi
# ===========================
repo_counts = defaultdict(int)
selected_repos = set()
repo_files = defaultdict(list)
repo_meta = defaultdict(list)
repo_stars = defaultdict(int)       # Pour stocker le nombre d'étoiles par dépôt
repo_licenses = defaultdict(list)   # Pour stocker les licences par dépôt
repo_first_star_dates = {}          # Pour stocker les dates de première étoile
saved_count = 0
file_counter = 0                    # simple compteur global pour nommer les fichiers
debug_samples = []                  # pour stocker quelques exemples pour debug

# Métadonnées globales
global_metadata = {
    "target_repos": TARGET_REPOS,
    "min_files_per_repo": MIN_FILES_PER_REPO,
    "min_stars": MIN_STARS,
    "permissive_licenses": PERMISSIVE_LICENSES,
    "cutoff_date": CUTOFF_DATE.isoformat(),
    "repos": []
}

# ===========================
# Fonction de filtrage
# ===========================
def is_valid(example):
    """Vérifie si un exemple répond aux critères de filtrage."""
    # Enregistrer quelques exemples pour debug
    if len(debug_samples) < 3:
        debug_samples.append(example)
    
    # 1) Taille minimale
    content = example.get("content") or ""
    if len(content) < MIN_CODE_LENGTH:
        return False
    if example.get("size", 0) > MAX_FILE_SIZE:
        return False
    if example.get("alphanum_fraction", 0.0) < MIN_ALPHANUM:
        return False

    # 2) Licence permissive
    lic = example.get("max_stars_repo_licenses") or []
    lic_str = " ".join(lic).lower() if isinstance(lic, list) else str(lic).lower()
    if not any(l in lic_str for l in PERMISSIVE_LICENSES):
        return False

    # 3) Popularité
    stars = example.get("max_stars_count") or 0
    if stars < MIN_STARS:
        return False

    # 4) Date du premier star (si présente)
    date_str = example.get("max_stars_repo_stars_min_datetime") or ""
    if date_str:
        try:
            d = datetime.fromisoformat(date_str.rstrip("Z"))
            if d >= CUTOFF_DATE:
                return False
        except Exception:
            # date invalide ou manquante → on ignore ce filtre
            pass

    return True

# ===========================
# Fonction pour créer un nom de fichier sécurisé
# ===========================
def safe_filename(original_path):
    """Crée un nom de fichier sécurisé à partir du chemin d'origine."""
    if not original_path:
        return f"file_{file_counter}.py"
    
    # Extraire le nom du fichier du chemin complet
    basename = os.path.basename(original_path)
    
    # S'assurer que le fichier a une extension .py
    if not basename.lower().endswith('.py'):
        basename += '.py'
    
    # Remplacer les caractères non valides
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        basename = basename.replace(char, '_')
    
    return basename

# ===========================
# Parcours et extraction
# ===========================
print("Démarrage du traitement...")
processed_count = 0
try:
    for example in tqdm(dataset, desc="Streaming Python files"):
        processed_count += 1
        
        # Vérification de métadonnées minimales
        repo = example.get("max_stars_repo_name")
        if not repo:
            continue
            
        # Vérifier si l'exemple est valide selon nos critères
        if not is_valid(example):
            continue

        # Afficher quelques exemples acceptés pour debug
        if saved_count < 3:
            debug_print(f"Exemple accepté {saved_count}: repo={repo}, stars={example.get('max_stars_count')}, license={example.get('max_stars_repo_licenses')}")

        # 1) Sélection initiale des repos
        if repo not in selected_repos:
            if len(selected_repos) < TARGET_REPOS:
                selected_repos.add(repo)
            else:
                # tous nos repos ont au moins le min de fichiers ? alors on arrête
                if all(repo_counts[r] >= MIN_FILES_PER_REPO for r in selected_repos):
                    print(f"Tous les {len(selected_repos)} dépôts ont au moins {MIN_FILES_PER_REPO} fichiers. Arrêt du traitement.")
                    break

        # 2) Extraction des fichiers pour chaque repo choisi
        if repo in selected_repos and repo_counts[repo] < MIN_FILES_PER_REPO:
            file_counter += 1
            
            # Obtenir un nom de fichier sécurisé basé sur le chemin d'origine
            original_path = example.get("max_stars_repo_path", "")
            filename = safe_filename(original_path)
            
            # Éviter les collisions de noms de fichiers dans le même dépôt
            if filename in repo_files[repo]:
                basename, ext = os.path.splitext(filename)
                filename = f"{basename}_{file_counter}{ext}"
            
            # Créer le dossier du dépôt s'il n'existe pas
            safe_repo_name = repo.replace("/", "_")
            repo_dir = os.path.join(OUTPUT_DIR, safe_repo_name)
            os.makedirs(repo_dir, exist_ok=True)
            
            # Chemin complet du fichier
            filepath = os.path.join(repo_dir, filename)
            
            # Sauvegarde du code
            with open(filepath, "w", encoding="utf-8") as f:
                content = example.get("content") or ""
                f.write(content)
            
            # Suivre les fichiers de ce dépôt
            repo_files[repo].append(filename)
            
            # Mettre à jour les métadonnées du dépôt
            # 1. Étoiles
            stars = example.get("max_stars_count") or 0
            repo_stars[repo] = max(repo_stars[repo], stars)
            
            # 2. Licences
            licenses = example.get("max_stars_repo_licenses") or []
            if licenses and isinstance(licenses, list):
                if repo not in repo_licenses or not repo_licenses[repo]:
                    repo_licenses[repo] = licenses
            
            # 3. Date de première étoile
            date_str = example.get("max_stars_repo_stars_min_datetime") or ""
            if date_str and repo not in repo_first_star_dates:
                repo_first_star_dates[repo] = date_str
            
            # Préparer les métadonnées du fichier
            file_meta = {
                "file": filename,
                "original_path": original_path,
                "size": example.get("size", 0),
                "alphanum_fraction": example.get("alphanum_fraction", 0),
                "line_count": len(content.splitlines()),
                "character_count": len(content),
            }
            
            # Ajouter aux métadonnées du dépôt
            repo_meta[repo].append(file_meta)
            
            repo_counts[repo] += 1
            saved_count += 1
            
        # Afficher la progression toutes les 1000 entrées
        if processed_count % 1000 == 0:
            print(f"Traités: {processed_count}, Sauvegardés: {saved_count}, Dépôts: {len(selected_repos)}")

except Exception as e:
    print(f"ERREUR pendant le traitement: {str(e)}")
    import traceback
    traceback.print_exc()

# ===========================
# Debug des premiers exemples
# ===========================
if debug_samples:
    print("\nExemples d'entrées du dataset pour debug:")
    for i, sample in enumerate(debug_samples[:3]):
        print(f"\nExemple {i+1}:")
        print(f"  Repo: {sample.get('max_stars_repo_name')}")
        print(f"  Stars: {sample.get('max_stars_count')}")
        print(f"  Licenses: {sample.get('max_stars_repo_licenses')}")
        print(f"  Date première étoile: {sample.get('max_stars_repo_stars_min_datetime')}")
        print(f"  Taille: {sample.get('size')}")
        print(f"  Alphanum: {sample.get('alphanum_fraction')}")

# ===========================
# Debug des dépôts retenus
# ===========================
print("\nInformations sur les dépôts retenus:")
for i, repo in enumerate(list(selected_repos)[:5]):
    print(f"\nDépôt {i+1}: {repo}")
    print(f"  Stars: {repo_stars.get(repo, 'NON TROUVÉ!')}")
    print(f"  Licenses: {repo_licenses.get(repo, 'NON TROUVÉ!')}")
    print(f"  Première étoile: {repo_first_star_dates.get(repo, 'NON TROUVÉ!')}")
    print(f"  Nombre de fichiers: {repo_counts.get(repo, 0)}")

# ===========================
# Finalisation
# ===========================
print("\nGénération des fichiers metadata.json...")

# Génère un metadata.json par dépôt et mise à jour des métadonnées globales
for repo, files_meta in repo_meta.items():
    safe_repo_name = repo.replace("/", "_")
    repo_dir = os.path.join(OUTPUT_DIR, safe_repo_name)
    
    # Création du metadata.json du dépôt
    repo_metadata = {
        "repo_name": repo,
        "stars": repo_stars.get(repo, 0),
        "license": repo_licenses.get(repo, []),
        "first_star_date": repo_first_star_dates.get(repo, None),
        "total_files": len(files_meta),
        "files": files_meta
    }
    
    # Écrire le fichier metadata.json du dépôt
    with open(os.path.join(repo_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(repo_metadata, f, indent=2, ensure_ascii=False)
    
    # Ajouter aux métadonnées globales
    global_metadata["repos"].append({
        "repo_name": repo,
        "safe_name": safe_repo_name,
        "stars": repo_stars.get(repo, 0),
        "license": repo_licenses.get(repo, []),
        "total_files": len(files_meta)
    })

# Écrire le fichier de métadonnées globales
with open(global_metadata_path, "w", encoding="utf-8") as f:
    json.dump(global_metadata, f, indent=2, ensure_ascii=False)

print(f"\n✅ Extraction terminée :")
print(f"- Entrées traitées    : {processed_count}")
print(f"- Dépôts retenus      : {len(selected_repos)}")
print(f"- Fichiers extraits   : {saved_count}")
print(f"- Metadata global     : {global_metadata_path}")
print(f"- Dossiers par dépôt  : {OUTPUT_DIR}/<repo_safe>/")
print(f"- Taille minimum      : {MIN_CODE_LENGTH} caractères (~50 lignes)")
print(f"- Étoiles minimum     : {MIN_STARS}")
print(f"- Licences permissives: {', '.join(PERMISSIVE_LICENSES)}")
print(f"- Date limite         : avant {CUTOFF_DATE.isoformat()}")
