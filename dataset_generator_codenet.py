import os
import time
import argparse
import logging
import random
import json
from pathlib import Path
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("codenet_with_ia.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Définition des templates de prompts pour différentes variations
PROMPT_TEMPLATES = {
    # Styles de programmation
    "style_functional": "Réécris ce code Python en utilisant un style fonctionnel sans effets secondaires. Évite les variables mutables et privilégie les fonctions pures. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "style_oop": "Réécris ce code Python en utilisant une approche orientée objet avec des classes appropriées. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "style_procedural": "Réécris ce code Python en utilisant une approche procédurale, étape par étape. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "style_recursive": "Réécris ce code Python en utilisant une approche récursive lorsque c'est possible. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Niveau d'expertise simulé
    "expertise_beginner": "Réécris ce code Python comme si tu étais un programmeur débutant, avec une structure simple mais fonctionnelle. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "expertise_advanced": "Réécris ce code Python comme si tu étais un expert Python, en utilisant des fonctionnalités avancées du langage et des optimisations. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Documentation et commentaires
    "docs_none": "Réécris ce code Python sans aucun commentaire ni docstring. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "docs_detailed": "Réécris ce code Python avec des commentaires détaillés expliquant chaque section et des docstrings complètes pour toutes les fonctions. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Structure et formatage
    "format_oneline": "Réécris ce code Python en réduisant au maximum le nombre de lignes (utilise des one-liners, des opérateurs ternaires, etc.). Renvoie uniquement le code brut sans délimiteurs markdown.",
    "format_verbose": "Réécris ce code Python avec des noms de variables très explicites et une structure espacée pour maximiser la lisibilité. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Approches algorithmiques
    "algo_simple": "Réécris ce code Python de la manière la plus simple possible, même si ce n'est pas optimal en termes de performance. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "algo_optimized": "Réécris ce code Python en l'optimisant pour la performance, avec des algorithmes plus efficaces si possible. Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Simulation de code "humain"
    "human_like": "Réécris ce code Python comme si tu étais un humain qui fait des erreurs courantes, avec quelques inconsistances de style et peut-être une ou deux inefficacités mineures (mais le code doit rester fonctionnel). Renvoie uniquement le code brut sans délimiteurs markdown.",
    "human_tired": "Réécris ce code Python comme si tu étais un développeur fatigué travaillant tard le soir, avec quelques inconsistances et imperfections mineures (mais le code doit rester fonctionnel). Renvoie uniquement le code brut sans délimiteurs markdown.",
    
    # Spécifique au langage Python
    "python_modern": "Réécris ce code Python en utilisant les fonctionnalités modernes de Python 3.9+ (f-strings, walrus operator, type hints, etc.). Renvoie uniquement le code brut sans délimiteurs markdown.",
    "python_pep8": "Réécris ce code Python en suivant strictement les conventions PEP 8 pour le style et le formatage. Renvoie uniquement le code brut sans délimiteurs markdown.",
}

# Prompts pour générer du code depuis zéro à partir d'un énoncé
GENERATION_TEMPLATES = {
    "standard": "Crée une solution complète en Python pour ce problème. Sois concis et efficace. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "detailed": "Crée une solution complète en Python pour ce problème avec des commentaires détaillés expliquant ton approche. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "optimized": "Crée la solution la plus optimisée possible en Python pour ce problème, en tenant compte de la complexité temporelle et spatiale. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "readable": "Crée une solution en Python pour ce problème en priorisant la lisibilité et la maintenabilité plutôt que la concision. Renvoie uniquement le code brut sans délimiteurs markdown.",
    "creative": "Crée une solution originale et créative en Python pour ce problème, en utilisant des approches qui ne sont peut-être pas conventionnelles. Renvoie uniquement le code brut sans délimiteurs markdown.",
}

class DetectorDatasetGenerator:
    def __init__(self, input_path, output_path, api_key=None, max_workers=3):
        """
        Initialise le générateur de dataset pour le détecteur de code IA.
        
        Args:
            input_path (str): Chemin vers le dataset CodeNet
            output_path (str): Chemin de sortie pour les fichiers générés
            api_key (str, optional): Clé API OpenAI. Par défaut, utilise la variable d'environnement.
            max_workers (int, optional): Nombre maximum de workers pour le traitement parallèle.
        """
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.max_workers = max_workers
        
        # Initialiser le client OpenAI
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
        
        # Vérifier que la clé API est configurée
        if not self.client.api_key:
            raise ValueError("La clé API OpenAI n'est pas configurée. Définissez la variable d'environnement OPENAI_API_KEY ou passez-la en paramètre.")
            
        # Statistiques
        self.stats = {
            "problems_processed": 0,
            "variations_generated": 0,
            "solutions_from_scratch": 0,
            "api_errors": 0,
            "file_errors": 0
        }
        
        # Créer le répertoire des métadonnées
        self.metadata_dir = self.output_path / "metadata"
        self.metadata_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialiser le fichier de métadonnées global
        self.global_metadata_file = self.metadata_dir / "dataset_metadata.jsonl"
        if not self.global_metadata_file.exists():
            with open(self.global_metadata_file, 'w') as f:
                f.write('')

    def create_directories(self, path):
        """Crée les répertoires nécessaires s'ils n'existent pas déjà."""
        path.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Répertoire vérifié: {path}")

    def read_file(self, file_path):
        """Lit le contenu d'un fichier."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # Essayer avec une autre encodage si utf-8 échoue
            try:
                with open(file_path, 'r', encoding='latin-1') as file:
                    return file.read()
            except Exception as e:
                logger.error(f"Erreur lors de la lecture du fichier {file_path} avec l'encodage latin-1: {e}")
                self.stats["file_errors"] += 1
                return None
        except Exception as e:
            logger.error(f"Erreur lors de la lecture du fichier {file_path}: {e}")
            self.stats["file_errors"] += 1
            return None

    def write_file(self, file_path, content):
        """Écrit le contenu dans un fichier."""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            logger.debug(f"Fichier écrit: {file_path}")
            return True
        except Exception as e:
            logger.error(f"Erreur lors de l'écriture du fichier {file_path}: {e}")
            self.stats["file_errors"] += 1
            return False

    def append_metadata(self, metadata):
        """Ajoute une entrée de métadonnées au fichier global."""
        try:
            with open(self.global_metadata_file, 'a') as f:
                f.write(json.dumps(metadata) + '\n')
            return True
        except Exception as e:
            logger.error(f"Erreur lors de l'écriture des métadonnées: {e}")
            return False

    def api_call_with_backoff(self, func, *args, **kwargs):
        """
        Effectue un appel API avec backoff exponentiel en cas d'erreur.
        
        Args:
            func: Fonction à appeler
            *args, **kwargs: Arguments de la fonction
            
        Returns:
            Le résultat de la fonction ou None en cas d'erreur
        """
        max_retries = 5
        base_delay = 1
        
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Gestion simplifiée des erreurs - adapter selon les types d'erreurs spécifiques d'OpenAI
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                logger.warning(f"Erreur API, attente de {delay:.2f}s avant de réessayer... ({e})")
                time.sleep(delay)
        
        logger.error(f"Échec après {max_retries} tentatives")
        self.stats["api_errors"] += 1
        return None

    def clean_code_response(self, response):
        """
        Nettoie la réponse de l'API en retirant les délimiteurs de code Markdown.
        
        Args:
            response (str): Réponse de l'API
            
        Returns:
            str: Code nettoyé
        """
        if not response:
            return response
            
        # Supprimer les délimiteurs Markdown ```python et ```
        response = response.strip()
        
        # Cas 1: Code entouré de ```python ... ```
        if response.startswith("```python") and response.endswith("```"):
            response = response[len("```python"):].strip()
            response = response[:-3].strip()
        # Cas 2: Code entouré simplement de ``` ... ```
        elif response.startswith("```") and response.endswith("```"):
            response = response[3:].strip()
            response = response[:-3].strip()
        # Cas 3: Vérifier si le code commence par ```python mais ne se termine pas exactement par ```
        elif response.startswith("```python"):
            lines = response.split("\n")
            if len(lines) > 1:
                lines = lines[1:]  # Supprimer la première ligne contenant ```python
                # Rechercher la dernière ligne contenant ``` et la supprimer
                for i in range(len(lines)-1, -1, -1):
                    if lines[i].strip() == "```":
                        lines.pop(i)
                        break
                response = "\n".join(lines)
        # Cas 4: Vérifier si le code commence par ``` mais ne se termine pas exactement par ```
        elif response.startswith("```"):
            lines = response.split("\n")
            if len(lines) > 1:
                lines = lines[1:]  # Supprimer la première ligne contenant ```
                # Rechercher la dernière ligne contenant ``` et la supprimer
                for i in range(len(lines)-1, -1, -1):
                    if lines[i].strip() == "```":
                        lines.pop(i)
                        break
                response = "\n".join(lines)
            
        return response

    def generate_variation(self, code, problem_id, variation_key, solution_id=None):
        """
        Génère une variation de code à partir du code existant.
        
        Args:
            code (str): Code à reformuler
            problem_id (str): Identifiant du problème
            variation_key (str): Clé du template de variation à utiliser
            solution_id (str, optional): Identifiant de la solution originale
            
        Returns:
            tuple: (code_reformulé, métadonnées) ou (None, None) en cas d'erreur
        """
        prompt_template = PROMPT_TEMPLATES.get(variation_key)
        if not prompt_template:
            logger.error(f"Template de variation inconnu: {variation_key}")
            return None, None
            
        logger.info(f"Génération de la variation '{variation_key}' pour le problème {problem_id}...")
        
        def call_api():
            return self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Tu es un expert en Python chargé de reformuler du code selon des instructions spécifiques. Le code généré doit être fonctionnel et respecter les contraintes demandées."},
                    {"role": "user", "content": f"{prompt_template}\n\n{code}"}
                ],
                max_tokens=4096
            )
        
        response = self.api_call_with_backoff(call_api)
        if response:
            content = self.clean_code_response(response.choices[0].message.content)
            
            # Créer les métadonnées
            metadata = {
                "problem_id": problem_id,
                "variation_type": variation_key,
                "prompt_used": prompt_template,
                "original_solution_id": solution_id,
                "is_variation": True,
                "source": "gpt-4o",
                "timestamp": time.time()
            }
            
            return content, metadata
        
        return None, None

    def generate_from_prompt(self, prompt, problem_id, template_key):
        """
        Génère une solution Python à partir d'un énoncé.
        
        Args:
            prompt (str): Énoncé du problème
            problem_id (str): Identifiant du problème
            template_key (str): Clé du template de génération à utiliser
            
        Returns:
            tuple: (solution_générée, métadonnées) ou (None, None) en cas d'erreur
        """
        generation_template = GENERATION_TEMPLATES.get(template_key)
        if not generation_template:
            logger.error(f"Template de génération inconnu: {template_key}")
            return None, None
            
        logger.info(f"Génération d'une solution '{template_key}' pour le problème {problem_id}...")
        
        def call_api():
            return self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Tu es un expert en programmation Python chargé de résoudre des problèmes algorithmiques."},
                    {"role": "user", "content": f"{generation_template}\n\n{prompt}"}
                ],
                max_tokens=4096
            )
        
        response = self.api_call_with_backoff(call_api)
        if response:
            content = self.clean_code_response(response.choices[0].message.content)
            
            # Créer les métadonnées
            metadata = {
                "problem_id": problem_id,
                "generation_type": template_key,
                "prompt_used": generation_template,
                "is_variation": False,
                "source": "gpt-4o",
                "timestamp": time.time()
            }
            
            return content, metadata
        
        return None, None

    def process_human_solution(self, problem_id, solution_file, selected_variations):
        """
        Traite une solution humaine et génère des variations.
        
        Args:
            problem_id (str): Identifiant du problème
            solution_file (Path): Chemin vers le fichier de solution
            selected_variations (list): Liste des variations à générer
            
        Returns:
            int: Nombre de variations générées avec succès
        """
        variations_generated = 0
        
        try:
            solution_id = solution_file.name
            solution_code = self.read_file(solution_file)
            
            if not solution_code:
                return variations_generated
            
            # Créer le répertoire de sortie pour ce problème
            problem_output_dir = self.output_path / problem_id
            self.create_directories(problem_output_dir)
            
            # Créer le sous-répertoire pour la solution originale
            solution_dir = problem_output_dir / f"original_{solution_id}"
            self.create_directories(solution_dir)
            
            # Sauvegarder la solution humaine originale
            human_solution_path = solution_dir / "human_original.py"
            if self.write_file(human_solution_path, solution_code):
                # Enregistrer les métadonnées pour la solution humaine
                human_metadata = {
                    "problem_id": problem_id,
                    "solution_id": solution_id,
                    "file_path": str(human_solution_path.relative_to(self.output_path)),
                    "is_human": True,
                    "source": "codenet",
                    "timestamp": time.time()
                }
                self.append_metadata(human_metadata)
            
            # Générer les variations
            for variation_key in selected_variations:
                # Générer la variation
                variation_code, metadata = self.generate_variation(
                    solution_code, problem_id, variation_key, solution_id
                )
                
                if variation_code and metadata:
                    # Sauvegarder la variation
                    variation_file = solution_dir / f"ai_{variation_key}.py"
                    if self.write_file(variation_file, variation_code):
                        # Ajouter le chemin du fichier aux métadonnées
                        metadata["file_path"] = str(variation_file.relative_to(self.output_path))
                        # Enregistrer les métadonnées
                        self.append_metadata(metadata)
                        variations_generated += 1
            
            return variations_generated
                
        except Exception as e:
            logger.error(f"Erreur lors du traitement de la solution {solution_file}: {e}")
            return variations_generated

    def process_problem(self, problem_id, variation_limit=5, generation_limit=3, test_mode=False):
        """
        Traite un problème individuel en générant des variations et des solutions depuis zéro.
        
        Args:
            problem_id (str): Identifiant du problème
            variation_limit (int): Nombre maximum de variations à générer par solution
            generation_limit (int): Nombre maximum de solutions à générer depuis zéro
            test_mode (bool): Indique si le script est en mode test
            
        Returns:
            dict: Statistiques pour ce problème
        """
        problem_stats = {
            "variations_generated": 0,
            "solutions_from_scratch": 0
        }
        
        try:
            problem_dir = self.input_path / problem_id
            prompt_path = problem_dir / 'prompt.txt'
            
            if not prompt_path.exists():
                logger.warning(f"L'énoncé du problème {problem_id} n'existe pas: {prompt_path}")
                return problem_stats
                
            # Lire l'énoncé du problème
            prompt = self.read_file(prompt_path)
            if not prompt:
                logger.warning(f"L'énoncé du problème {problem_id} n'a pas pu être lu.")
                return problem_stats
                
            # Créer le répertoire de sortie pour ce problème
            problem_output_dir = self.output_path / problem_id
            self.create_directories(problem_output_dir)
            
            # Rechercher toutes les solutions Python existantes
            solutions = list(problem_dir.glob('*.py'))
            solutions = [s for s in solutions if s.name != 'prompt.py']
            logger.info(f"Trouvé {len(solutions)} solutions humaines pour le problème {problem_id}")
            
            # En mode test, limiter le nombre de solutions
            if test_mode:
                if len(solutions) > 2:
                    solutions = solutions[:2]
                    logger.info(f"Mode test: limitation à 2 solutions pour le problème {problem_id}")
                variation_limit = min(variation_limit, 2)
                generation_limit = min(generation_limit, 2)
            
            # Sélectionner aléatoirement un sous-ensemble de variations pour chaque solution
            available_variations = list(PROMPT_TEMPLATES.keys())
            if len(available_variations) > variation_limit:
                selected_variations = random.sample(available_variations, variation_limit)
            else:
                selected_variations = available_variations
            
            # Traiter chaque solution humaine en parallèle
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = [executor.submit(
                    self.process_human_solution, 
                    problem_id, 
                    solution_file,
                    selected_variations
                ) for solution_file in solutions]
                
                for future in as_completed(futures):
                    try:
                        variations = future.result()
                        problem_stats["variations_generated"] += variations
                        self.stats["variations_generated"] += variations
                    except Exception as e:
                        logger.error(f"Erreur lors du traitement d'une solution: {e}")
            
            # Générer des solutions depuis zéro
            from_scratch_dir = problem_output_dir / "from_scratch"
            self.create_directories(from_scratch_dir)
            
            # Sélectionner aléatoirement un sous-ensemble de templates de génération
            available_templates = list(GENERATION_TEMPLATES.keys())
            if len(available_templates) > generation_limit:
                selected_templates = random.sample(available_templates, generation_limit)
            else:
                selected_templates = available_templates
                
            # Générer les solutions depuis zéro
            for template_key in selected_templates:
                solution_code, metadata = self.generate_from_prompt(
                    prompt, problem_id, template_key
                )
                
                if solution_code and metadata:
                    # Sauvegarder la solution
                    solution_file = from_scratch_dir / f"ai_generated_{template_key}.py"
                    if self.write_file(solution_file, solution_code):
                        # Ajouter le chemin du fichier aux métadonnées
                        metadata["file_path"] = str(solution_file.relative_to(self.output_path))
                        # Enregistrer les métadonnées
                        self.append_metadata(metadata)
                        problem_stats["solutions_from_scratch"] += 1
                        self.stats["solutions_from_scratch"] += 1
            
            self.stats["problems_processed"] += 1
            return problem_stats
        
        except Exception as e:
            logger.error(f"Erreur lors du traitement du problème {problem_id}: {e}")
            return problem_stats

    def process_dataset(self, variation_limit=5, generation_limit=3, test_mode=False, problem_limit=None):
        """
        Traite l'ensemble du dataset CodeNet pour générer un dataset de détection.
        
        Args:
            variation_limit (int): Nombre maximum de variations à générer par solution
            generation_limit (int): Nombre maximum de solutions à générer depuis zéro
            test_mode (bool): Indique si le script est en mode test
            problem_limit (int, optional): Limite le nombre de problèmes à traiter
            
        Returns:
            dict: Statistiques de traitement
        """
        # Créer le répertoire de sortie principal
        self.create_directories(self.output_path)
        
        # Obtenir la liste des problèmes (dossiers commençant par 'p')
        problems = [d.name for d in self.input_path.iterdir() 
                  if d.is_dir() and d.name.startswith('p')]
        
        # Trier les problèmes pour un traitement ordonné
        problems.sort()
        
        # En mode test, ne traiter qu'un nombre limité de problèmes
        if test_mode:
            if 'p00000' in problems:
                problems = ['p00000']
                logger.info(f"Mode test activé, traitement uniquement du problème: {problems[0]}")
            elif len(problems) > 0:
                problems = [problems[0]]
                logger.info(f"Mode test activé, traitement uniquement du problème: {problems[0]}")
            else:
                logger.error(f"Aucun problème trouvé. Vérifiez votre dataset.")
                return self.stats
        
        # Limiter le nombre de problèmes si demandé
        if problem_limit and len(problems) > problem_limit:
            problems = problems[:problem_limit]
            logger.info(f"Limitation à {problem_limit} problèmes.")
        
        logger.info(f"Début du traitement de {len(problems)} problèmes...")
        
        # Traiter chaque problème
        for problem in problems:
            stats = self.process_problem(problem, variation_limit, generation_limit, test_mode)
            
            # Afficher les statistiques intermédiaires
            logger.info(f"Problème {problem} traité: {stats['variations_generated']} variations, {stats['solutions_from_scratch']} solutions depuis zéro")
            logger.info(f"Statistiques globales: {self.stats}")
        
        return self.stats


def main():
    """Fonction principale."""
    parser = argparse.ArgumentParser(description='Génération de dataset pour détection de code IA à partir de CodeNet.')
    parser.add_argument('--input', type=str, default='codenet', help='Chemin vers le dataset CodeNet')
    parser.add_argument('--output', type=str, default='codenet_with_ia', help='Chemin de sortie pour les fichiers générés')
    parser.add_argument('--test', action='store_true', help='Activer le mode test (traiter uniquement le premier problème)')
    parser.add_argument('--workers', type=int, default=3, help='Nombre de workers pour le traitement parallèle')
    parser.add_argument('--api-key', type=str, help='Clé API OpenAI (par défaut: variable d\'environnement OPENAI_API_KEY)')
    parser.add_argument('--variations', type=int, default=5, help='Nombre de variations à générer par solution')
    parser.add_argument('--generations', type=int, default=3, help='Nombre de solutions à générer depuis zéro par problème')
    parser.add_argument('--problems', type=int, help='Limite le nombre de problèmes à traiter')
    
    args = parser.parse_args()
    
    logger.info("=== Démarrage du processus de génération de dataset pour détection ===")
    logger.info(f"Mode test: {'Activé' if args.test else 'Désactivé'}")
    logger.info(f"Chemin d'entrée: {args.input}")
    logger.info(f"Chemin de sortie: {args.output}")
    logger.info(f"Nombre de workers: {args.workers}")
    logger.info(f"Variations par solution: {args.variations}")
    logger.info(f"Générations par problème: {args.generations}")
    
    try:
        generator = DetectorDatasetGenerator(
            input_path=args.input,
            output_path=args.output,
            api_key=args.api_key,
            max_workers=args.workers
        )
        
        stats = generator.process_dataset(
            variation_limit=args.variations,
            generation_limit=args.generations,
            test_mode=args.test,
            problem_limit=args.problems
        )
        
        logger.info("=== Processus terminé ===")
        logger.info(f"Statistiques finales:")
        logger.info(f"  - Problèmes traités: {stats['problems_processed']}")
        logger.info(f"  - Variations générées: {stats['variations_generated']}")
        logger.info(f"  - Solutions générées depuis zéro: {stats['solutions_from_scratch']}")
        logger.info(f"  - Erreurs API: {stats['api_errors']}")
        logger.info(f"  - Erreurs fichier: {stats['file_errors']}")
        
    except Exception as e:
        logger.error(f"Erreur critique: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())