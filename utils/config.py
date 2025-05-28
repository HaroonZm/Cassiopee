#!/usr/bin/env python3
"""Configuration centralisée pour l'application"""

import os
from pathlib import Path

# Configuration de l'API
OPENAI_API_KEY = "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"

# Structure des dossiers
DEFAULT_OUTPUT_DIR = "data"
BATCH_DIR = "batches"
TBATCH_DIR = "tbatch"
IABATCH_DIR = "iabatch"
METADATA_DIR = "metadata"
TEMP_DIR = "temp"

# Préfixes standards
TBATCH_PREFIX = "tbatch_"
IABATCH_PREFIX = "iabatch_"

# Paramètres par défaut
DEFAULT_BATCH_SIZE = 5000
DEFAULT_POLL_INTERVAL = 20
DEFAULT_MAX_BATCHES = 10
DEFAULT_MODEL = "gpt-4.1-mini"

# Format des fichiers
METADATA_FORMAT = "jsonl"
RESULTS_FORMAT = "json"

class Config:
    """Classe de configuration avec gestion des chemins"""
    
    def __init__(self, base_dir=None):
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.setup_directories()
    
    def setup_directories(self):
        """Crée la structure de dossiers nécessaire"""
        # Dossiers principaux
        self.output_dir = self.base_dir / DEFAULT_OUTPUT_DIR
        self.batch_dir = self.output_dir / BATCH_DIR
        self.metadata_dir = self.output_dir / METADATA_DIR
        self.temp_dir = self.output_dir / TEMP_DIR
        
        # Sous-dossiers pour les batchs
        self.tbatch_dir = self.batch_dir / TBATCH_DIR
        self.iabatch_dir = self.batch_dir / IABATCH_DIR
        
        # Créer tous les dossiers
        for directory in [self.output_dir, self.batch_dir, self.metadata_dir, 
                         self.temp_dir, self.tbatch_dir, self.iabatch_dir]:
            directory.mkdir(parents=True, exist_ok=True)
    
    def get_batch_path(self, batch_id):
        """Retourne le chemin approprié pour un batch donné"""
        if batch_id.startswith(TBATCH_PREFIX):
            return self.tbatch_dir
        elif batch_id.startswith(IABATCH_PREFIX):
            return self.iabatch_dir
        return self.batch_dir
    
    def get_metadata_path(self, batch_id):
        """Retourne le chemin pour les métadonnées d'un batch"""
        return self.metadata_dir / f"{batch_id}.{METADATA_FORMAT}"
    
    def get_results_path(self, batch_id):
        """Retourne le chemin pour les résultats d'un batch"""
        batch_dir = self.get_batch_path(batch_id)
        return batch_dir / f"{batch_id}_results.{RESULTS_FORMAT}"
    
    def get_temp_path(self):
        """Retourne un chemin temporaire unique"""
        import uuid
        return self.temp_dir / f"temp_{uuid.uuid4().hex}"

# Instance globale de configuration
config = Config() 