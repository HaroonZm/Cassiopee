import os
import json
from collections import defaultdict
from datasets import load_dataset
from tqdm import tqdm

# Configuration
OUTPUT_DIR = "the_stack_repos"
TARGET_REPOS = 1000        # Nombre de dépôts à collecter
MIN_FILES_PER_REPO = 5     # Nombre minimum de fichiers par dépôt
MIN_STARS = 150             # Seuil minimal d'étoiles du dépôt
MAX_FILE_SIZE = 1_000_000  # Taille max d'un fichier (1MB)
MIN_CODE_LENGTH = 200      # Longueur minimale du code
MIN_ALPHANUM = 0.3         # Fraction minimale de caractères alphanumériques
PERMISSIVE_LICENSES = ["mit", "apache", "bsd", "isc", "zlib", "cc0"]

# Prépare le dossier de sortie
os.makedirs(OUTPUT_DIR, exist_ok=True)
global_metadata_path = os.path.join(OUTPUT_DIR, "metadata.jsonl")
meta_file = open(global_metadata_path, "w", encoding="utf-8")

# Charger en streaming le sous-dataset Python de The Stack
dataset = load_dataset(
    "bigcode/the-stack",
    data_dir="data/python",
    streaming=True,
    split="train"
)

# Structures de suivi
repo_counts = defaultdict(int)
selected_repos = set()
repo_meta = defaultdict(list)
saved_count = 0

# Fonction de filtrage améliorée
def is_valid(example):
    content = example.get("content", "") or ""
    if len(content) < MIN_CODE_LENGTH:
        return False
    if example.get("size", 0) > MAX_FILE_SIZE:
        return False
    if example.get("alphanum_fraction", 0.0) < MIN_ALPHANUM:
        return False

    # Filtrage sur licence permissive
    lic = example.get("max_stars_repo_licenses") or []
    lic_str = " ".join(lic).lower() if isinstance(lic, list) else str(lic).lower()
    if not any(l in lic_str for l in PERMISSIVE_LICENSES):
        return False

    # Filtrage sur le nombre d'étoiles (peut être None)
    stars = example.get("max_stars_count") or 0
    if stars < MIN_STARS:
        return False

    return True

# Parcours et extraction
for example in tqdm(dataset, desc="Streaming Python files"):
    repo = example.get("max_stars_repo_name")
    if not repo or not is_valid(example):
        continue

    # Sélection initiale des dépôts
    if repo not in selected_repos:
        if len(selected_repos) < TARGET_REPOS:
            selected_repos.add(repo)
        else:
            # Si on a nos repos et tous ont assez de fichiers, on arrête
            if all(repo_counts[r] >= MIN_FILES_PER_REPO for r in selected_repos):
                break

    # Extraction des fichiers pour les dépôts sélectionnés
    if repo in selected_repos and repo_counts[repo] < MIN_FILES_PER_REPO:
        safe_repo = repo.replace("/", "_")
        file_index = repo_counts[repo] + 1
        filename = f"{safe_repo}_{file_index}.py"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Sauvegarde du code
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(example["content"] or "")

        # Construction des métadonnées
        meta = {
            "repo": repo,
            "file": filename,
            "path": example.get("max_stars_repo_path"),
            "license": example.get("max_stars_repo_licenses"),
            "size": example.get("size"),
            "alphanum_fraction": example.get("alphanum_fraction"),
            "stars": example.get("max_stars_count") or 0
        }

        # Écriture dans l'index global
        meta_file.write(json.dumps(meta, ensure_ascii=False) + "\n")
        # Ajout aux métadonnées par dépôt
        repo_meta[repo].append(meta)

        repo_counts[repo] += 1
        saved_count += 1

# Fermeture du fichier global
meta_file.close()

# Génération d'un metadata.json par dépôt
for repo, entries in repo_meta.items():
    safe_repo = repo.replace("/", "_")
    repo_dir = os.path.join(OUTPUT_DIR, safe_repo)
    os.makedirs(repo_dir, exist_ok=True)
    with open(os.path.join(repo_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"\n✅ Extraction terminée :")
print(f"- Dépôts sélectionnés : {len(selected_repos)}")
print(f"- Fichiers extraits : {saved_count}")
print(f"- Métadonnées globales : {global_metadata_path}")
print(f"- Métadonnées par dépôt dans : {OUTPUT_DIR}/<repo>")  
