import sys
import os
import subprocess
import tempfile
import glob
import json

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFileDialog, QProgressBar, QSpinBox, QCheckBox,
    QComboBox, QListWidget, QMessageBox, QLineEdit,
    QGroupBox, QRadioButton, QTextEdit, QScrollArea,
    QListWidgetItem, QSizePolicy
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QMimeData, QTimer
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Import des modules de visualisation
sys.path.append('visualization')
try:
    import visualize_matrix
    import visualize_activation
    import visualize_tilespy
except ImportError:
    print("Warning: Modules de visualisation non trouvés. Certaines fonctionnalités seront désactivées.")


class ProcessThread(QThread):
    """Thread pour exécuter des commandes système en arrière-plan"""
    update_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)
    
    def __init__(self, command):
        super().__init__()
        self.command = command
    
    def run(self):
        try:
            # Exécuter la commande avec capture de sortie en temps réel
            process = subprocess.Popen(
                self.command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            # Lire la sortie ligne par ligne
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.update_signal.emit(output.strip())
            
            # Attendre la fin du processus
            return_code = process.poll()
            
            if return_code == 0:
                self.finished_signal.emit(True, "Processus terminé avec succès")
            else:
                self.finished_signal.emit(False, f"Processus terminé avec erreur (code: {return_code})")
                
        except Exception as e:
            self.finished_signal.emit(False, f"Erreur lors de l'exécution: {str(e)}")


class ScriptGenerationTab(QWidget):
    """Onglet pour la génération de code IA"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Sélection du dataset d'entrée
        input_group = QGroupBox("Dataset d'entrée")
        input_layout = QHBoxLayout()
        
        self.input_path = QLineEdit()
        self.input_path.setPlaceholderText("Chemin vers le dataset (CodeNet ou The Stack)")
        input_button = QPushButton("Parcourir...")
        input_button.clicked.connect(self.browse_input)
        
        input_layout.addWidget(self.input_path)
        input_layout.addWidget(input_button)
        input_group.setLayout(input_layout)
        
        # Dossier de sortie
        output_group = QGroupBox("Dossier de sortie")
        output_layout = QHBoxLayout()
        
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Chemin de sortie pour les scripts générés (obligatoire)")
        output_button = QPushButton("Parcourir...")
        output_button.clicked.connect(self.browse_output)
        
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(output_button)
        output_group.setLayout(output_layout)
        
        # Configuration de génération
        config_group = QGroupBox("Configuration")
        config_layout = QVBoxLayout()
        
        # Mode API
        api_layout = QHBoxLayout()
        self.batch_mode_checkbox = QCheckBox("Utiliser l'API Batch (50% moins cher)")
        self.batch_mode_checkbox.setChecked(True)
        api_layout.addWidget(self.batch_mode_checkbox)
        
        # Modèle
        model_layout = QHBoxLayout()
        model_layout.addWidget(QLabel("Modèle:"))
        self.model_combo = QComboBox()
        self.model_combo.addItems(["gpt-4.1-mini", "gpt-4o-mini", "gpt-4o", "gpt-4.1"])
        model_layout.addWidget(self.model_combo)
        
        # Variations et générations
        variations_layout = QHBoxLayout()
        variations_layout.addWidget(QLabel("Variations par fichier/problème:"))
        self.variations_spinbox = QSpinBox()
        self.variations_spinbox.setRange(1, 10)
        self.variations_spinbox.setValue(3)
        variations_layout.addWidget(self.variations_spinbox)
        
        generations_layout = QHBoxLayout()
        generations_layout.addWidget(QLabel("Générations depuis zéro (CodeNet):"))
        self.generations_spinbox = QSpinBox()
        self.generations_spinbox.setRange(0, 5)
        self.generations_spinbox.setValue(2)
        generations_layout.addWidget(self.generations_spinbox)
        
        # Taille des batches (seulement pour mode batch)
        batch_size_layout = QHBoxLayout()
        batch_size_layout.addWidget(QLabel("Taille des batches:"))
        self.batch_size_spinbox = QSpinBox()
        self.batch_size_spinbox.setRange(100, 50000)
        self.batch_size_spinbox.setValue(1000)
        batch_size_layout.addWidget(self.batch_size_spinbox)
        
        # Limite de dossiers/problèmes
        folders_layout = QHBoxLayout()
        folders_layout.addWidget(QLabel("Limite de dossiers/problèmes:"))
        self.folders_spinbox = QSpinBox()
        self.folders_spinbox.setRange(0, 10000)
        self.folders_spinbox.setValue(0)  # 0 = pas de limite
        self.folders_spinbox.setSpecialValueText("Pas de limite")
        folders_layout.addWidget(self.folders_spinbox)
        
        # Contrôle du volume de génération
        volume_group = QGroupBox("Contrôle du volume de génération")
        volume_layout = QVBoxLayout()
        
        # Nombre maximum de batches
        max_batches_layout = QHBoxLayout()
        max_batches_layout.addWidget(QLabel("Nombre max de batches:"))
        self.max_batches_spinbox = QSpinBox()
        self.max_batches_spinbox.setRange(0, 100)
        self.max_batches_spinbox.setValue(0)  # 0 = pas de limite
        self.max_batches_spinbox.setSpecialValueText("Pas de limite")
        max_batches_layout.addWidget(self.max_batches_spinbox)
        
        # Estimation du volume
        estimate_button = QPushButton("Estimer le volume de génération")
        estimate_button.clicked.connect(self.estimate_volume)
        
        self.volume_info = QLabel("Sélectionnez un dataset pour voir l'estimation")
        self.volume_info.setStyleSheet("color: blue; font-style: italic;")
        
        volume_layout.addLayout(max_batches_layout)
        volume_layout.addWidget(estimate_button)
        volume_layout.addWidget(self.volume_info)
        
        # Options avancées
        advanced_group = QGroupBox("Options avancées")
        advanced_layout = QVBoxLayout()
        
        self.test_mode_checkbox = QCheckBox("Mode test (petit échantillon)")
        self.validate_first_only_checkbox = QCheckBox("Valider seulement le premier batch (pour tester)")
        self.wait_completion_checkbox = QCheckBox("Attendre la complétion (mode batch)")
        
        advanced_layout.addWidget(self.test_mode_checkbox)
        advanced_layout.addWidget(self.validate_first_only_checkbox)
        advanced_layout.addWidget(self.wait_completion_checkbox)
        
        config_layout.addLayout(api_layout)
        config_layout.addLayout(model_layout)
        config_layout.addLayout(variations_layout)
        config_layout.addLayout(generations_layout)
        config_layout.addLayout(batch_size_layout)
        config_layout.addLayout(folders_layout)
        config_layout.addWidget(volume_group)
        config_layout.addWidget(advanced_group)
        
        # Fermer les groupes de layout
        volume_group.setLayout(volume_layout)
        advanced_group.setLayout(advanced_layout)
        config_group.setLayout(config_layout)
        
        # Bouton de génération
        self.generate_button = QPushButton("Générer les scripts IA")
        self.generate_button.clicked.connect(self.generate_scripts)
        
        # Console de sortie
        console_group = QGroupBox("Sortie du processus")
        console_layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        console_layout.addWidget(self.console)
        console_group.setLayout(console_layout)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addWidget(input_group)
        layout.addWidget(output_group)
        layout.addWidget(config_group)
        layout.addWidget(self.generate_button)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
    
    def browse_input(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dataset d'entrée")
        if folder:
            self.input_path.setText(folder)
    
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sortie")
        if folder:
            self.output_path.setText(folder)
    
    def estimate_volume(self):
        """Estime le volume de génération basé sur les paramètres actuels"""
        if not self.input_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord sélectionner un dataset d'entrée.")
            return
        
        if not os.path.exists(self.input_path.text()):
            QMessageBox.warning(self, "Erreur", "Le chemin du dataset n'existe pas.")
            return
        
        try:
            import pathlib
            dataset_path = pathlib.Path(self.input_path.text())
            
            # Compter les sous-dossiers
            subfolders = [f for f in dataset_path.iterdir() if f.is_dir()]
            total_subfolders = len(subfolders)
            
            # Appliquer la limite de dossiers si spécifiée
            folders_limit = self.folders_spinbox.value() if self.folders_spinbox.value() > 0 else total_subfolders
            effective_folders = min(folders_limit, total_subfolders)
            
            # Estimer le nombre de requêtes
            variations = self.variations_spinbox.value()
            generations = self.generations_spinbox.value()
            
            # Estimation grossière (à adapter selon le type de dataset)
            estimated_requests_per_folder = variations + generations
            total_estimated_requests = effective_folders * estimated_requests_per_folder
            
            # Calculer le nombre de batches
            batch_size = self.batch_size_spinbox.value()
            estimated_batches = max(1, (total_estimated_requests + batch_size - 1) // batch_size)
            
            # Appliquer la limite de batches si spécifiée
            max_batches = self.max_batches_spinbox.value()
            if max_batches > 0:
                effective_batches = min(max_batches, estimated_batches)
                effective_requests = effective_batches * batch_size
            else:
                effective_batches = estimated_batches
                effective_requests = total_estimated_requests
            
            # Estimation du coût (approximatif)
            cost_per_request = 0.0001  # Estimation en dollars
            estimated_cost = effective_requests * cost_per_request
            
            # Mise à jour du label d'information
            info_text = f"""📊 Estimation du volume:
• Dossiers trouvés: {total_subfolders} (limite: {folders_limit})
• Dossiers effectifs: {effective_folders}
• Requêtes estimées: {effective_requests:,}
• Batches estimés: {effective_batches}
• Coût approximatif: ${estimated_cost:.2f}
• Mode test: {'Activé' if self.test_mode_checkbox.isChecked() else 'Désactivé'}"""
            
            self.volume_info.setText(info_text)
            self.volume_info.setStyleSheet("color: green; font-family: monospace;")
            
        except Exception as e:
            self.volume_info.setText(f"Erreur lors de l'estimation: {str(e)}")
            self.volume_info.setStyleSheet("color: red;")
    
    def generate_scripts(self):
        # Vérifier les entrées
        if not self.input_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dataset d'entrée.")
            return
        
        if not self.output_path.text():
            QMessageBox.warning(self, "Erreur", "Un dossier de sortie est requis.")
            return
        
        # Construire la commande
        cmd = ['python', 'scripts_generation/ia_scripts_generator.py']
        cmd.extend(['--input', self.input_path.text()])
        cmd.extend(['--output', self.output_path.text()])  # Toujours inclure le dossier de sortie
        
        if self.batch_mode_checkbox.isChecked():
            cmd.extend(['--batch-size', str(self.batch_size_spinbox.value())])
            if self.wait_completion_checkbox.isChecked():
                cmd.append('--wait-completion')
        else:
            cmd.append('--no-batch')
        
        cmd.extend(['--model', self.model_combo.currentText()])
        cmd.extend(['--variations', str(self.variations_spinbox.value())])
        cmd.extend(['--generations', str(self.generations_spinbox.value())])
        
        if self.folders_spinbox.value() > 0:
            cmd.extend(['--folders', str(self.folders_spinbox.value())])
        
        if self.max_batches_spinbox.value() > 0:
            cmd.extend(['--max-batches', str(self.max_batches_spinbox.value())])
        
        if self.test_mode_checkbox.isChecked():
            cmd.append('--test')
        
        if self.validate_first_only_checkbox.isChecked():
            cmd.append('--validate-first-only')
        
        # Préparer l'interface
        self.console.clear()
        self.progress_bar.show()
        self.generate_button.setEnabled(False)
        
        # Afficher les informations de volume si disponibles
        if "Estimation du volume" in self.volume_info.text():
            self.console.append("=== ESTIMATION DU VOLUME ===")
            self.console.append(self.volume_info.text().replace("📊 ", ""))
            self.console.append("=" * 40 + "\n")
        
        # Afficher la commande
        command_str = ' '.join(cmd)
        self.console.append(f"Exécution de la commande: {command_str}\n")
        
        # Exécuter dans un thread
        self.thread = ProcessThread(command_str)
        self.thread.update_signal.connect(self.update_console)
        self.thread.finished_signal.connect(self.process_finished)
        self.thread.start()
    
    def update_console(self, text):
        self.console.append(text)
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def process_finished(self, success, message):
        self.progress_bar.hide()
        self.generate_button.setEnabled(True)
        status = "Succès" if success else "Échec"
        QMessageBox.information(self, status, message)


class MatrixGenerationTab(QWidget):
    """Onglet pour la génération des matrices"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Méthode de génération
        method_group = QGroupBox("Méthode de génération")
        method_layout = QVBoxLayout()
        
        self.batch_method_radio = QRadioButton("Méthode par batch (recommandée)")
        self.direct_method_radio = QRadioButton("Méthode directe (pour petits fichiers)")
        self.batch_method_radio.setChecked(True)
        self.batch_method_radio.toggled.connect(self.toggle_method)
        self.direct_method_radio.toggled.connect(self.toggle_method)
        
        method_layout.addWidget(self.batch_method_radio)
        method_layout.addWidget(self.direct_method_radio)
        method_group.setLayout(method_layout)
        
        # Mode de sélection (fichier unique ou dossier batch)
        mode_group = QGroupBox("Mode de génération")
        mode_layout = QVBoxLayout()
        
        self.file_mode_radio = QRadioButton("Analyser un fichier unique")
        self.dir_mode_radio = QRadioButton("Analyser un dossier complet")
        self.batch_id_mode_radio = QRadioButton("Reprendre un batch existant")
        self.file_mode_radio.setChecked(True)
        self.file_mode_radio.toggled.connect(self.toggle_mode)
        self.dir_mode_radio.toggled.connect(self.toggle_mode)
        self.batch_id_mode_radio.toggled.connect(self.toggle_mode)
        
        mode_layout.addWidget(self.file_mode_radio)
        mode_layout.addWidget(self.dir_mode_radio)
        mode_layout.addWidget(self.batch_id_mode_radio)
        mode_group.setLayout(mode_layout)
        
        # Sélection du fichier
        self.file_group = QGroupBox("Sélection du script")
        file_layout = QHBoxLayout()
        
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText("Chemin du script à analyser")
        file_button = QPushButton("Parcourir...")
        file_button.clicked.connect(self.browse_file)
        
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(file_button)
        self.file_group.setLayout(file_layout)
        
        # Sélection du dossier
        self.dir_group = QGroupBox("Sélection du dossier")
        dir_layout = QVBoxLayout()
        
        dir_select_layout = QHBoxLayout()
        self.dir_path = QLineEdit()
        self.dir_path.setPlaceholderText("Chemin du dossier contenant les scripts Python")
        dir_button = QPushButton("Parcourir...")
        dir_button.clicked.connect(self.browse_directory)
        dir_select_layout.addWidget(self.dir_path)
        dir_select_layout.addWidget(dir_button)
        
        # Option pour la récursivité
        self.recursive_checkbox = QCheckBox("Analyser également les sous-dossiers")
        self.recursive_checkbox.setChecked(True)
        
        info_label = QLabel("Le script analysera tous les fichiers Python dans le dossier")
        info_label.setStyleSheet("color: gray;")
        
        dir_layout.addLayout(dir_select_layout)
        dir_layout.addWidget(self.recursive_checkbox)
        dir_layout.addWidget(info_label)
        self.dir_group.setLayout(dir_layout)
        self.dir_group.hide()  # Caché par défaut
        
        # ID de batch
        self.batch_id_group = QGroupBox("ID de batch existant")
        batch_id_layout = QVBoxLayout()
        
        self.batch_id = QLineEdit()
        self.batch_id.setPlaceholderText("Entrez l'ID du batch à reprendre (ex: batch_xyz123)")
        
        info_batch_id = QLabel("Permet de reprendre l'analyse d'un batch existant interrompu")
        info_batch_id.setStyleSheet("color: gray;")
        
        batch_id_layout.addWidget(self.batch_id)
        batch_id_layout.addWidget(info_batch_id)
        self.batch_id_group.setLayout(batch_id_layout)
        self.batch_id_group.hide()  # Caché par défaut
        
        # Modèles utilisés
        models_group = QGroupBox("Modèles")
        models_layout = QVBoxLayout()
        
        token_layout = QHBoxLayout()
        token_layout.addWidget(QLabel("Modèle de tokenisation:"))
        self.token_model = QComboBox()
        self.token_model.addItems(["gpt-4o-mini", "gpt-4o", "gpt-4.1", "gpt-4.1-mini"])
        token_layout.addWidget(self.token_model)
        
        pred_layout = QHBoxLayout()
        pred_layout.addWidget(QLabel("Modèle de prédiction:"))
        self.pred_model = QComboBox()
        self.pred_model.addItems(["gpt-4o-mini", "gpt-4o", "gpt-4.1", "gpt-4.1-mini"])
        pred_layout.addWidget(self.pred_model)
        
        models_layout.addLayout(token_layout)
        models_layout.addLayout(pred_layout)
        models_group.setLayout(models_layout)
        
        # Type d'API (pour matrix_generator_classic.py)
        self.api_group = QGroupBox("Type d'API")
        api_layout = QVBoxLayout()
        
        self.completions_api_radio = QRadioButton("API Completions (traditionnel)")
        self.chat_api_radio = QRadioButton("API Chat (avec prompt spécifique)")
        self.completions_api_radio.setChecked(True)
        
        api_layout.addWidget(self.completions_api_radio)
        api_layout.addWidget(self.chat_api_radio)
        self.api_group.setLayout(api_layout)
        
        # Options de batch (seulement pour méthode batch)
        self.batch_group = QGroupBox("Options de batch")
        batch_layout = QVBoxLayout()
        
        batch_size_layout = QHBoxLayout()
        batch_size_layout.addWidget(QLabel("Taille du batch:"))
        self.batch_size = QSpinBox()
        self.batch_size.setRange(100, 50000)
        self.batch_size.setValue(5000)
        self.batch_size.setSingleStep(100)
        batch_size_layout.addWidget(self.batch_size)
        
        poll_layout = QHBoxLayout()
        poll_layout.addWidget(QLabel("Intervalle de sondage (s):"))
        self.poll_interval = QSpinBox()
        self.poll_interval.setRange(5, 300)
        self.poll_interval.setValue(20)
        poll_layout.addWidget(self.poll_interval)
        
        max_batches_layout = QHBoxLayout()
        max_batches_layout.addWidget(QLabel("Nombre max de batches:"))
        self.max_batches = QSpinBox()
        self.max_batches.setRange(1, 100)
        self.max_batches.setValue(1)
        max_batches_layout.addWidget(self.max_batches)
        
        wait_unlimited_layout = QHBoxLayout()
        self.wait_unlimited = QCheckBox("Attente illimitée (recommandé)")
        self.wait_unlimited.setChecked(True)
        wait_unlimited_layout.addWidget(self.wait_unlimited)
        
        # Option de tentatives de reconnexion
        connection_retries_layout = QHBoxLayout()
        connection_retries_layout.addWidget(QLabel("Tentatives de reconnexion:"))
        self.connection_retries = QSpinBox()
        self.connection_retries.setRange(1, 20)
        self.connection_retries.setValue(5)
        self.connection_retries.setToolTip("Nombre de tentatives de reconnexion en cas d'erreur réseau")
        connection_retries_layout.addWidget(self.connection_retries)
        
        # Option pour continuer en cas d'erreur
        continue_on_error_layout = QHBoxLayout()
        self.continue_on_error = QCheckBox("Continuer en cas d'erreur")
        self.continue_on_error.setChecked(True)
        self.continue_on_error.setToolTip("Si coché, le traitement continue même si un fichier échoue")
        continue_on_error_layout.addWidget(self.continue_on_error)
        
        batch_layout.addLayout(batch_size_layout)
        batch_layout.addLayout(poll_layout)
        batch_layout.addLayout(max_batches_layout)
        batch_layout.addLayout(wait_unlimited_layout)
        batch_layout.addLayout(connection_retries_layout)
        batch_layout.addLayout(continue_on_error_layout)
        self.batch_group.setLayout(batch_layout)
        
        # Répertoires de sortie et d'archivage
        paths_group = QGroupBox("Répertoires")
        paths_layout = QVBoxLayout()
        
        # Dossier de sortie
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel("Dossier de sortie:"))
        self.output_dir = QLineEdit()
        self.output_dir.setPlaceholderText("Dossier pour les résultats (tokens, matrices)")
        output_button = QPushButton("Parcourir...")
        output_button.clicked.connect(self.browse_output)
        output_layout.addWidget(self.output_dir)
        output_layout.addWidget(output_button)
        
        # Dossier d'archivage (seulement pour méthode batch)
        archive_layout = QHBoxLayout()
        archive_layout.addWidget(QLabel("Dossier d'archivage:"))
        self.archive_dir = QLineEdit()
        self.archive_dir.setPlaceholderText("Dossier pour archiver les scripts traités")
        archive_button = QPushButton("Parcourir...")
        archive_button.clicked.connect(self.browse_archive)
        archive_layout.addWidget(self.archive_dir)
        archive_layout.addWidget(archive_button)
        
        paths_layout.addLayout(output_layout)
        paths_layout.addLayout(archive_layout)
        paths_group.setLayout(paths_layout)
        
        # Bouton d'exécution
        self.execute_button = QPushButton("Générer les matrices")
        self.execute_button.clicked.connect(self.execute_generation)
        
        # Console de sortie
        console_group = QGroupBox("Sortie")
        console_layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        console_layout.addWidget(self.console)
        console_group.setLayout(console_layout)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addWidget(method_group)
        layout.addWidget(mode_group)
        layout.addWidget(self.file_group)
        layout.addWidget(self.dir_group)
        layout.addWidget(self.batch_id_group)
        layout.addWidget(models_group)
        layout.addWidget(self.api_group)
        layout.addWidget(self.batch_group)
        layout.addWidget(paths_group)
        layout.addWidget(self.execute_button)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
    
    def toggle_method(self):
        """Change l'interface en fonction de la méthode sélectionnée"""
        is_batch_method = self.batch_method_radio.isChecked()
        
        # Avec matrix_batch_generator.py, on peut analyser un fichier unique en mode batch
        # On n'a plus besoin de désactiver le groupe de fichiers en mode batch
        self.batch_group.setEnabled(is_batch_method)
        
        # Les options d'API sont uniquement pour la méthode directe
        self.api_group.setEnabled(not is_batch_method)
        
        # Le dossier d'archivage est moins important avec le nouveau générateur de matrices
        archive_widgets = self.findChildren(QWidget)
        for widget in archive_widgets:
            if hasattr(widget, 'parent') and "archivage" in str(widget.parent()):
                widget.setEnabled(not is_batch_method)  # Désactiver pour matrix_batch_generator
                if is_batch_method:
                    widget.hide()  # Cacher les widgets d'archivage en mode batch
                else:
                    widget.show()  # Les montrer en mode direct
    
    def toggle_mode(self):
        """Change l'interface en fonction du mode sélectionné"""
        is_file_mode = self.file_mode_radio.isChecked()
        is_dir_mode = self.dir_mode_radio.isChecked()
        is_batch_id_mode = self.batch_id_mode_radio.isChecked()
        is_batch_method = self.batch_method_radio.isChecked()
        
        # Montrer/cacher les groupes appropriés
        self.file_group.setVisible(is_file_mode)
        self.dir_group.setVisible(is_dir_mode)
        self.batch_id_group.setVisible(is_batch_id_mode)
        
        # Rendre certains éléments visibles ou invisibles en fonction du mode
        self.token_model.setEnabled(not is_batch_id_mode)
        self.pred_model.setEnabled(not is_batch_id_mode)
        
        # Dans le mode batch_id, seul le dossier de sortie est nécessaire
        if is_batch_id_mode:
            self.batch_group.setEnabled(False)
        else:
            self.batch_group.setEnabled(is_batch_method)
    
    def browse_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Sélectionner un script Python", "", "Fichiers Python (*.py)")
        if file:
            self.file_path.setText(file)
    
    def browse_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier")
        if folder:
            self.dir_path.setText(folder)
    
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le répertoire de sortie")
        if folder:
            self.output_dir.setText(folder)
    
    def browse_archive(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le répertoire d'archivage")
        if folder:
            self.archive_dir.setText(folder)
    
    def execute_generation(self):
        # Vérifier que les chemins requis sont fournis
        if self.file_mode_radio.isChecked() and not self.file_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un script Python.")
            return
        elif self.dir_mode_radio.isChecked() and not self.dir_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier.")
            return
        elif self.batch_id_mode_radio.isChecked() and not self.batch_id.text():
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un ID de batch existant.")
            return
        
        if not self.output_dir.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier de sortie.")
            return
        
        # Déterminer la méthode à utiliser
        if self.batch_method_radio.isChecked():
            # Méthode batch avec matrix_batch_generator.py
            self._execute_batch_method()
        else:
            # Méthode directe (matrix_generator_classic)
            self._execute_direct_method()
    
    def _execute_batch_method(self):
        """Exécute la génération de matrices en utilisant l'approche batch"""
        # Vérifier le mode sélectionné
        if self.file_mode_radio.isChecked():
            # Utiliser matrix_batch_generator.py avec un fichier unique
            cmd_generator = ['python', 'matrix_generation/matrix_batch_generator.py']
            
            # Ajouter les arguments selon la documentation du script
            cmd_generator.extend(['--file', self.file_path.text()])
            cmd_generator.extend(['--output', self.output_dir.text()])
            cmd_generator.extend(['--model', self.pred_model.currentText()])
            cmd_generator.extend(['--poll-interval', str(self.poll_interval.value())])
            
            # Options de maximum d'essais
            cmd_generator.extend(['--max-attempts', '1000'])
            
            # Option d'attente illimitée
            if not self.wait_unlimited.isChecked():
                cmd_generator.append('--no-wait-unlimited')
            
            # Options de gestion des erreurs réseau
            cmd_generator.extend(['--max-connection-retries', str(self.connection_retries.value())])
            if self.continue_on_error.isChecked():
                cmd_generator.append('--continue-on-error')
            
            self.console.clear()
            self.progress_bar.show()
            self.execute_button.setEnabled(False)
            
            # Afficher la commande qui sera exécutée
            command_str = ' '.join(cmd_generator)
            self.console.append(f"Génération de matrice avec matrix_batch_generator.py")
            self.console.append(f"Exécution de la commande: {command_str}\n")
            
            # Exécuter dans un thread
            self.thread = ProcessThread(command_str)
            self.thread.update_signal.connect(self.update_console)
            self.thread.finished_signal.connect(self.process_finished)
            self.thread.start()
        elif self.dir_mode_radio.isChecked():
            # Utiliser matrix_batch_generator.py avec un dossier
            cmd_generator = ['python', 'matrix_generation/matrix_batch_generator.py']
            
            # Ajouter les arguments pour le dossier
            cmd_generator.extend(['--directory', self.dir_path.text()])
            cmd_generator.extend(['--output', self.output_dir.text()])
            cmd_generator.extend(['--model', self.pred_model.currentText()])
            cmd_generator.extend(['--poll-interval', str(self.poll_interval.value())])
            
            # Options de maximum d'essais
            cmd_generator.extend(['--max-attempts', '1000'])
            
            # Option d'attente illimitée
            if not self.wait_unlimited.isChecked():
                cmd_generator.append('--no-wait-unlimited')
            
            # Option de récursivité
            if self.recursive_checkbox.isChecked():
                cmd_generator.append('--recursive')
            
            # Options de gestion des erreurs réseau
            cmd_generator.extend(['--max-connection-retries', str(self.connection_retries.value())])
            if self.continue_on_error.isChecked():
                cmd_generator.append('--continue-on-error')
            
            self.console.clear()
            self.progress_bar.show()
            self.execute_button.setEnabled(False)
            
            # Afficher la commande qui sera exécutée
            command_str = ' '.join(cmd_generator)
            self.console.append(f"Traitement du dossier avec matrix_batch_generator.py")
            self.console.append(f"Exécution de la commande: {command_str}\n")
            
            # Exécuter dans un thread
            self.thread = ProcessThread(command_str)
            self.thread.update_signal.connect(self.update_console)
            self.thread.finished_signal.connect(self.process_finished)
            self.thread.start()
        elif self.batch_id_mode_radio.isChecked():
            # Utiliser matrix_batch_generator.py avec un ID de batch existant
            cmd_generator = ['python', 'matrix_generation/matrix_batch_generator.py']
            
            # Ajouter les arguments pour le batch existant
            cmd_generator.extend(['--batch-id', self.batch_id.text()])
            cmd_generator.extend(['--output', self.output_dir.text()])
            cmd_generator.extend(['--poll-interval', str(self.poll_interval.value())])
            
            # Options de maximum d'essais
            cmd_generator.extend(['--max-attempts', '1000'])
            
            # Option d'attente illimitée
            if not self.wait_unlimited.isChecked():
                cmd_generator.append('--no-wait-unlimited')
            
            # Options de gestion des erreurs réseau
            cmd_generator.extend(['--max-connection-retries', str(self.connection_retries.value())])
            
            self.console.clear()
            self.progress_bar.show()
            self.execute_button.setEnabled(False)
            
            # Afficher la commande qui sera exécutée
            command_str = ' '.join(cmd_generator)
            self.console.append(f"Reprise d'un batch existant avec matrix_batch_generator.py")
            self.console.append(f"Exécution de la commande: {command_str}\n")
            
            # Exécuter dans un thread
            self.thread = ProcessThread(command_str)
            self.thread.update_signal.connect(self.update_console)
            self.thread.finished_signal.connect(self.process_finished)
            self.thread.start()
        else:
            QMessageBox.warning(self, "Erreur", "Mode de génération non reconnu.")
            return
    
    def _execute_direct_method(self):
        """Exécute la génération de matrices en utilisant l'approche directe"""
        cmd = ['python', 'matrix_generation/matrix_generator_classic.py']
        
        # Paramètres spécifiques au mode
        if self.file_mode_radio.isChecked():
            # Le script attend --file avec juste le nom du fichier, pas le chemin complet
            file_path = self.file_path.text()
            file_name = os.path.basename(file_path)
            file_dir = os.path.dirname(file_path)
            
            cmd.extend(['--file', file_name])
            cmd.extend(['--directory', file_dir])
        else:
            cmd.extend(['--directory', self.dir_path.text()])
            cmd.append('--all')  # Analyser tous les fichiers du dossier
            
            # Ajouter l'option récursive si la case est cochée
            if self.recursive_checkbox.isChecked():
                cmd.append('--recursive')
        
        # Répertoire de sortie
        cmd.extend(['--output', self.output_dir.text()])
        
        # Ajout du type d'API (chat ou completions)
        api_type = "chat" if self.chat_api_radio.isChecked() else "completions"
        cmd.extend(['--api', api_type])
        
        self.console.clear()
        self.progress_bar.show()
        self.execute_button.setEnabled(False)
        
        # Afficher la commande qui sera exécutée
        command_str = ' '.join(cmd)
        self.console.append(f"Exécution de la commande: {command_str}\n")
        
        # Exécuter dans un thread
        self.thread = ProcessThread(command_str)
        self.thread.update_signal.connect(self.update_console)
        self.thread.finished_signal.connect(self.process_finished)
        self.thread.start()
    
    def update_console(self, text):
        # Ajouter une coloration pour les erreurs de connexion
        if "Erreur de connexion" in text or "Connection error" in text:
            self.console.append("<span style='color: #FFA500; font-weight: bold;'>" + text + "</span>")
        elif "erreur" in text.lower() or "error" in text.lower():
            self.console.append("<span style='color: red;'>" + text + "</span>")
        elif "tentative" in text.lower() or "retry" in text.lower():
            self.console.append("<span style='color: #66CDAA;'>" + text + "</span>")
        else:
            self.console.append(text)
        
        # Faire défiler vers le bas
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def process_finished(self, success, message):
        self.progress_bar.hide()
        self.execute_button.setEnabled(True)
        status = "Succès" if success else "Échec"
        QMessageBox.information(self, status, message)


class MatrixTilingTab(QWidget):
    """Onglet pour la génération des tuiles"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Sélection des dossiers
        input_group = QGroupBox("Selection batch")
        input_layout = QHBoxLayout()
        
        self.input_dir = QLineEdit()
        self.input_dir.setPlaceholderText("Chemin vers le dossier batch")
        input_button = QPushButton("Parcourir...")
        input_button.clicked.connect(self.browse_input)
        
        input_layout.addWidget(self.input_dir)
        input_layout.addWidget(input_button)
        input_group.setLayout(input_layout)
        
        # Sélection du dossier de sortie
        output_group = QGroupBox("Dossier de sortie")
        output_layout = QHBoxLayout()
        
        self.output_dir = QLineEdit()
        self.output_dir.setPlaceholderText("Chemin vers le dossier de sortie pour les tuiles")
        output_button = QPushButton("Parcourir...")
        output_button.clicked.connect(self.browse_output)
        
        output_layout.addWidget(self.output_dir)
        output_layout.addWidget(output_button)
        output_group.setLayout(output_layout)
        
        # Configuration des tuiles
        tile_group = QGroupBox("Configuration des tuiles")
        tile_layout = QHBoxLayout()
        
        tile_layout.addWidget(QLabel("Lignes:"))
        self.rows_spinbox = QSpinBox()
        self.rows_spinbox.setRange(1, 1000)  # Augmentation de la limite maximale à 1000
        self.rows_spinbox.setValue(3)
        self.rows_spinbox.setSingleStep(1)  # Pas de 1
        tile_layout.addWidget(self.rows_spinbox)
        
        tile_layout.addWidget(QLabel("Colonnes:"))
        self.cols_spinbox = QSpinBox()
        self.cols_spinbox.setRange(1, 1000)  # Augmentation de la limite maximale à 1000
        self.cols_spinbox.setValue(3)
        self.cols_spinbox.setSingleStep(1)  # Pas de 1
        tile_layout.addWidget(self.cols_spinbox)
        
        # Note: Le padding est toujours activé avec valeur 100 par défaut dans le script
        info_label = QLabel("Note: Le padding est automatiquement ajouté si nécessaire (valeur: 100)")
        info_label.setStyleSheet("color: #666; font-style: italic;")
        tile_layout.addWidget(info_label)
        
        tile_group.setLayout(tile_layout)
        
        # Bouton d'exécution
        self.execute_button = QPushButton("Générer les tuiles")
        self.execute_button.clicked.connect(self.execute_tiling)
        
        # Métadonnées
        metadata_group = QGroupBox("Métadonnées des tuiles")
        metadata_layout = QVBoxLayout()
        self.metadata_text = QTextEdit()
        self.metadata_text.setReadOnly(True)
        metadata_layout.addWidget(self.metadata_text)
        metadata_group.setLayout(metadata_layout)
        
        # Console de sortie
        console_group = QGroupBox("Sortie")
        console_layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        console_layout.addWidget(self.console)
        console_group.setLayout(console_layout)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addWidget(input_group)
        layout.addWidget(output_group)
        layout.addWidget(tile_group)
        layout.addWidget(self.execute_button)
        layout.addWidget(metadata_group)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        # Suppression de la ligne qui cause l'erreur
    
    def browse_input(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le batch")
        if folder:
            self.input_dir.setText(folder)
            
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sortie")
        if folder:
            self.output_dir.setText(folder)
            
    def execute_tiling(self):
        if not self.input_dir.text() or not self.output_dir.text():
            QMessageBox.warning(self, "Erreur", "Les dossiers d'entrée et de sortie sont requis.")
            return
        
        cmd = ['python', 'matrix_generation/matrix_tiling.py']
        # Ajouter les arguments positionnels dans le bon ordre
        cmd.append(self.input_dir.text())
        cmd.append(self.output_dir.text())
        # Retirer l'argument archive qui n'existe pas dans le script
        
        # Utiliser le bon format pour les dimensions des tuiles
        cmd.extend(['--taille_tuile', str(self.rows_spinbox.value()), str(self.cols_spinbox.value())])
        
        # Les options de padding ne sont pas dans le script matrix_tiling.py
        # Le padding est toujours activé avec valeur 100 par défaut
        
        self.console.clear()
        self.metadata_text.clear()
        self.progress_bar.show()
        self.execute_button.setEnabled(False)
        
        # Exécuter dans un thread
        self.thread = ProcessThread(' '.join(cmd))
        self.thread.update_signal.connect(self.update_console)
        self.thread.finished_signal.connect(self.process_finished)
        self.thread.start()
    
    def update_console(self, text):
        self.console.append(text)
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
        # Extraire les métadonnées potentielles
        if "Métadonnées:" in text:
            self.metadata_text.append(text)
    
    def process_finished(self, success, message):
        self.progress_bar.hide()
        self.execute_button.setEnabled(True)
        status = "Succès" if success else "Échec"
        QMessageBox.information(self, status, message)


class UNetTrainingTab(QWidget):
    """Onglet pour l'entraînement du modèle U-Net"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Sélection des données
        data_group = QGroupBox("Données d'entraînement")
        data_layout = QVBoxLayout()
        
        batch_layout = QHBoxLayout()
        batch_layout.addWidget(QLabel("Dossier batch:"))
        self.batch_directory = QLineEdit()
        self.batch_directory.setPlaceholderText("Chemin vers le dossier batch contenant les tuiles")
        browse_button = QPushButton("Parcourir...")
        browse_button.clicked.connect(self.browse_batch_directory)
        batch_layout.addWidget(self.batch_directory)
        batch_layout.addWidget(browse_button)
        
        data_layout.addLayout(batch_layout)
        data_group.setLayout(data_layout)
        
        # Paramètres d'entraînement
        params_group = QGroupBox("Paramètres d'entraînement")
        params_layout = QVBoxLayout()
        
        # Paramètres principaux
        epochs_layout = QHBoxLayout()
        epochs_layout.addWidget(QLabel("Nombre d'époques:"))
        self.epochs_spinbox = QSpinBox()
        self.epochs_spinbox.setRange(1, 1000)
        self.epochs_spinbox.setValue(20)  # Valeur par défaut selon le guide
        epochs_layout.addWidget(self.epochs_spinbox)
        
        batch_size_layout = QHBoxLayout()
        batch_size_layout.addWidget(QLabel("Taille des batches:"))
        self.batch_size_spinbox = QSpinBox()
        self.batch_size_spinbox.setRange(1, 128)
        self.batch_size_spinbox.setValue(16)  # Valeur par défaut selon le guide
        batch_size_layout.addWidget(self.batch_size_spinbox)
        
        lr_layout = QHBoxLayout()
        lr_layout.addWidget(QLabel("Taux d'apprentissage:"))
        self.lr_spinbox = QLineEdit("0.001")  # Valeur par défaut selon le guide
        lr_layout.addWidget(self.lr_spinbox)
        
        # Sauvegarde du modèle
        save_layout = QHBoxLayout()
        save_layout.addWidget(QLabel("Dossier de sauvegarde:"))
        self.save_dir = QLineEdit("models")  # Valeur par défaut selon le guide
        save_button = QPushButton("Parcourir...")
        save_button.clicked.connect(self.browse_save_dir)
        save_layout.addWidget(self.save_dir)
        save_layout.addWidget(save_button)
        
        params_layout.addLayout(epochs_layout)
        params_layout.addLayout(batch_size_layout)
        params_layout.addLayout(lr_layout)
        params_layout.addLayout(save_layout)
        params_group.setLayout(params_layout)
        
        # Bouton d'action
        self.train_button = QPushButton("Entraîner le modèle")
        self.train_button.clicked.connect(self.train_model)
        
        # Visualisation de l'apprentissage
        plot_group = QGroupBox("Courbes d'apprentissage")
        plot_layout = QVBoxLayout()
        
        # Créer un widget Matplotlib pour les courbes d'apprentissage
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        plot_layout.addWidget(self.canvas)
        
        plot_group.setLayout(plot_layout)
        
        # Console de sortie
        console_group = QGroupBox("Sortie du processus")
        console_layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        console_layout.addWidget(self.console)
        console_group.setLayout(console_layout)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addWidget(data_group)
        layout.addWidget(params_group)
        layout.addWidget(self.train_button)
        layout.addWidget(plot_group)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        # Stocker les données d'apprentissage
        self.train_losses = []
        self.val_losses = []
        self.train_accuracies = []
        self.val_accuracies = []
        self.current_epoch = 0
        self.training_thread = None
    
    def browse_batch_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier batch")
        if folder:
            self.batch_directory.setText(folder)
    
    def browse_save_dir(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sauvegarde")
        if folder:
            self.save_dir.setText(folder)
    
    def train_model(self):
        if not self.batch_directory.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier batch.")
            return
        
        # Créer la commande d'entraînement
        cmd = ['python', './unet/train_unet.py']
        
        # Ajouter les paramètres
        cmd.extend(['--batch_directory', self.batch_directory.text()])
        cmd.extend(['--batch_size', str(self.batch_size_spinbox.value())])
        cmd.extend(['--num_epochs', str(self.epochs_spinbox.value())])
        cmd.extend(['--learning_rate', self.lr_spinbox.text()])
        cmd.extend(['--model_save_dir', self.save_dir.text()])
        
        # Préparation de l'interface
        self.console.clear()
        self.progress_bar.setValue(0)
        self.progress_bar.show()
        self.train_button.setEnabled(False)
        
        # Initialiser les courbes d'apprentissage
        self.train_losses = []
        self.val_losses = []
        self.train_accuracies = []
        self.val_accuracies = []
        self.current_epoch = 0
        self.figure.clear()
        
        # Configurer le graphique
        self.figure.subplots_adjust(hspace=0.3)
        self.ax1 = self.figure.add_subplot(211)
        self.ax2 = self.figure.add_subplot(212)
        self.ax1.set_title("Pertes")
        self.ax1.set_xlabel("Époque")
        self.ax1.set_ylabel("Perte")
        self.ax2.set_title("Précision")
        self.ax2.set_xlabel("Époque")
        self.ax2.set_ylabel("Précision")
        self.canvas.draw()
        
        # Afficher la commande qui sera exécutée
        command_str = ' '.join(cmd)
        self.console.append(f"Exécution de la commande: {command_str}\n")
        
        # Exécuter dans un thread
        self.thread = ProcessThread(command_str)
        self.thread.update_signal.connect(self.update_training_progress)
        self.thread.finished_signal.connect(self.training_finished)
        self.thread.start()
    
    def update_training_progress(self, text):
        self.console.append(text)
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
        # Analyser la sortie pour les métriques d'entraînement
        try:
            # Extraire époque en cours
            if "Époque" in text and "/" in text:
                parts = text.split("/")
                current_epoch = int(parts[0].split()[-1])
                total_epochs = int(parts[1].split()[0])
                progress = int((current_epoch / total_epochs) * 100)
                self.progress_bar.setValue(progress)
                self.current_epoch = current_epoch
            
            # Extraire pertes et précisions
            if "Perte d'entraînement:" in text:
                train_loss = float(text.split("Perte d'entraînement:")[1].split(",")[0].strip())
                if self.current_epoch >= len(self.train_losses):
                    self.train_losses.append(train_loss)
                else:
                    self.train_losses[self.current_epoch-1] = train_loss
            
            if "Perte de validation:" in text:
                val_loss = float(text.split("Perte de validation:")[1].split(",")[0].strip())
                if self.current_epoch >= len(self.val_losses):
                    self.val_losses.append(val_loss)
                else:
                    self.val_losses[self.current_epoch-1] = val_loss
            
            if "Précision d'entraînement:" in text:
                train_acc = float(text.split("Précision d'entraînement:")[1].split("%")[0].strip())
                if self.current_epoch >= len(self.train_accuracies):
                    self.train_accuracies.append(train_acc)
                else:
                    self.train_accuracies[self.current_epoch-1] = train_acc
            
            if "Précision de validation:" in text:
                val_acc = float(text.split("Précision de validation:")[1].split("%")[0].strip())
                if self.current_epoch >= len(self.val_accuracies):
                    self.val_accuracies.append(val_acc)
                else:
                    self.val_accuracies[self.current_epoch-1] = val_acc
                
                # Mettre à jour le graphique après avoir récupéré toutes les métriques pour cette époque
                self.update_plot()
                
        except Exception as e:
            # Ignorer les erreurs d'analyse
            pass
        
        # Mettre en évidence les avertissements et erreurs
        if "erreur" in text.lower() or "error" in text.lower():
            self.console.append("<span style='color:red;'>" + text + "</span>")
        elif "attention" in text.lower() or "warning" in text.lower():
            self.console.append("<span style='color:orange;'>" + text + "</span>")
    
    def update_plot(self):
        if not self.train_losses or not self.val_losses:
            return
        
        # Effacer les graphiques précédents
        self.ax1.clear()
        self.ax2.clear()
        
        # Reconfigurer les titres et labels
        self.ax1.set_title("Pertes")
        self.ax1.set_xlabel("Époque")
        self.ax1.set_ylabel("Perte")
        self.ax2.set_title("Précision")
        self.ax2.set_xlabel("Époque")
        self.ax2.set_ylabel("Précision (%)")
        
        # Tracer les courbes
        epochs = list(range(1, len(self.train_losses) + 1))
        self.ax1.plot(epochs, self.train_losses, 'b-', label='Entraînement')
        self.ax1.plot(epochs, self.val_losses, 'r-', label='Validation')
        self.ax1.legend()
        
        if self.train_accuracies and self.val_accuracies:
            self.ax2.plot(epochs, self.train_accuracies, 'g-', label='Entraînement')
            self.ax2.plot(epochs, self.val_accuracies, 'm-', label='Validation')
            self.ax2.legend()
        
        # Redessiner le canvas
        self.figure.tight_layout()
        self.canvas.draw()
    
    def training_finished(self, success, message):
        self.progress_bar.hide()
        self.train_button.setEnabled(True)
        
        if success:
            QMessageBox.information(self, "Terminé", "Entraînement terminé avec succès!")
            
            # Afficher le résumé final
            self.console.append("\n=== RÉSUMÉ DE L'ENTRAÎNEMENT ===")
            self.console.append(f"Dossier batch: {self.batch_directory.text()}")
            self.console.append(f"Époques: {self.current_epoch}/{self.epochs_spinbox.value()}")
            
            if self.train_losses and self.val_losses:
                self.console.append(f"Perte finale (entraînement): {self.train_losses[-1]:.6f}")
                self.console.append(f"Perte finale (validation): {self.val_losses[-1]:.6f}")
                
            if self.train_accuracies and self.val_accuracies:
                self.console.append(f"Précision finale (entraînement): {self.train_accuracies[-1]:.2f}%")
                self.console.append(f"Précision finale (validation): {self.val_accuracies[-1]:.2f}%")
                
            # Afficher le chemin du modèle sauvegardé
            model_path = os.path.join(self.save_dir.text())
            self.console.append(f"Modèles sauvegardés dans: {model_path}")
            self.console.append("Deux modèles ont été sauvegardés:")
            self.console.append("  - Le meilleur modèle (préfixe 'best_')")
            self.console.append("  - Le modèle final (préfixe 'final_')")
        else:
            QMessageBox.warning(self, "Erreur", f"Entraînement terminé avec erreur: {message}")


class UNetTestingTab(QWidget):
    """Onglet pour le test du modèle U-Net"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Partie supérieure (contrôles)
        upper_layout = QVBoxLayout()
        
        # Sélection du modèle
        model_group = QGroupBox("Sélection du modèle")
        model_layout = QHBoxLayout()
        
        self.model_path = QLineEdit()
        self.model_path.setPlaceholderText("Chemin vers le modèle entraîné")
        model_button = QPushButton("Parcourir...")
        model_button.clicked.connect(self.browse_model)
        
        model_layout.addWidget(self.model_path)
        model_layout.addWidget(model_button)
        model_group.setLayout(model_layout)
        
        # Zone de sélection des fichiers/dossiers
        input_group = QGroupBox("Sélection des fichiers Python")
        input_layout = QVBoxLayout()
        
        # Mode de sélection
        mode_layout = QHBoxLayout()
        self.file_mode_radio = QRadioButton("Analyser un fichier unique")
        self.dir_mode_radio = QRadioButton("Analyser un dossier")
        self.file_mode_radio.setChecked(True)
        self.file_mode_radio.toggled.connect(self.toggle_mode)
        self.dir_mode_radio.toggled.connect(self.toggle_mode)
        
        mode_layout.addWidget(self.file_mode_radio)
        mode_layout.addWidget(self.dir_mode_radio)
        
        # Sélection de fichier
        file_layout = QHBoxLayout()
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText("Chemin vers le fichier Python à analyser")
        self.file_button = QPushButton("Parcourir...")
        self.file_button.clicked.connect(self.browse_file)
        
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(self.file_button)
        
        # Sélection de dossier
        dir_layout = QHBoxLayout()
        self.dir_path = QLineEdit()
        self.dir_path.setPlaceholderText("Chemin vers le dossier contenant des fichiers Python")
        self.dir_path.setEnabled(False)
        self.dir_button = QPushButton("Parcourir...")
        self.dir_button.clicked.connect(self.browse_directory)
        self.dir_button.setEnabled(False)
        
        dir_layout.addWidget(self.dir_path)
        dir_layout.addWidget(self.dir_button)
        
        # Instructions pour le glisser-déposer
        drop_label = QLabel("Ou glissez-déposez des fichiers/dossiers ici")
        drop_label.setAlignment(Qt.AlignCenter)
        drop_label.setStyleSheet("background-color: #f0f0f0; padding: 15px; border: 1px dashed #aaa;")
        
        input_layout.addLayout(mode_layout)
        input_layout.addLayout(file_layout)
        input_layout.addLayout(dir_layout)
        input_layout.addWidget(drop_label)
        input_group.setLayout(input_layout)
        
        # Options de visualisation
        viz_group = QGroupBox("Options de visualisation")
        viz_layout = QVBoxLayout()
        
        # Option pour visualiser les tuiles
        self.visualize_tiles_checkbox = QCheckBox("Visualiser les tuiles")
        self.visualize_tiles_checkbox.setChecked(False)
        viz_layout.addWidget(self.visualize_tiles_checkbox)
        
        # Option pour visualiser les activations
        self.visualize_activations_checkbox = QCheckBox("Visualiser les activations")
        self.visualize_activations_checkbox.setChecked(False)
        viz_layout.addWidget(self.visualize_activations_checkbox)
        
        # Dossier de sortie pour les visualisations
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel("Dossier de sortie:"))
        self.viz_output_dir = QLineEdit()
        self.viz_output_dir.setPlaceholderText("Dossier pour sauvegarder les visualisations")
        output_button = QPushButton("...")
        output_button.clicked.connect(self.browse_viz_output)
        output_layout.addWidget(self.viz_output_dir)
        output_layout.addWidget(output_button)
        viz_layout.addLayout(output_layout)
        
        viz_group.setLayout(viz_layout)
        
        # Bouton d'analyse
        self.test_button = QPushButton("Analyser")
        self.test_button.clicked.connect(self.analyze_code)
        
        # Ajouter les contrôles à la partie supérieure
        upper_layout.addWidget(model_group)
        upper_layout.addWidget(input_group)
        upper_layout.addWidget(viz_group)
        upper_layout.addWidget(self.test_button)
        
        # Partie inférieure avec deux colonnes
        lower_layout = QHBoxLayout()
        
        # Colonne de gauche: résultats et détails
        left_column = QVBoxLayout()
        
        # Liste des résultats
        results_group = QGroupBox("Résultats d'analyse")
        results_layout = QVBoxLayout()
        self.results_list = QListWidget()
        self.results_list.setSelectionMode(QListWidget.SingleSelection)
        self.results_list.itemClicked.connect(self.show_result_details)
        
        results_layout.addWidget(self.results_list)
        results_group.setLayout(results_layout)
        
        # Détails du résultat
        details_group = QGroupBox("Détails")
        details_layout = QVBoxLayout()
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        
        details_layout.addWidget(self.details_text)
        details_group.setLayout(details_layout)
        
        left_column.addWidget(results_group, 1)
        left_column.addWidget(details_group, 1)
        
        # Colonne de droite: visualisation et console
        right_column = QVBoxLayout()
        
        # Visualisation
        viz_group = QGroupBox("Visualisation")
        viz_layout = QVBoxLayout()
        
        # Figure plus grande
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumHeight(300)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        viz_layout.addWidget(self.canvas)
        
        viz_group.setLayout(viz_layout)
        
        # Console de sortie
        console_group = QGroupBox("Sortie du processus")
        console_layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        
        console_layout.addWidget(self.console)
        console_group.setLayout(console_layout)
        
        right_column.addWidget(viz_group, 2)
        right_column.addWidget(console_group, 1)
        
        # Équilibrer les colonnes
        lower_layout.addLayout(left_column, 40)
        lower_layout.addLayout(right_column, 60)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addLayout(upper_layout)
        layout.addLayout(lower_layout, 1)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        # Stockage des résultats
        self.all_results = []
        
    def browse_viz_output(self):
        """Ouvre une boîte de dialogue pour sélectionner le dossier de sortie des visualisations"""
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sortie pour les visualisations")
        if folder:
            self.viz_output_dir.setText(folder)
            
    def toggle_mode(self):
        """Change l'interface en fonction du mode sélectionné"""
        is_file_mode = self.file_mode_radio.isChecked()
        is_dir_mode = self.dir_mode_radio.isChecked()
        is_batch_id_mode = self.batch_id_mode_radio.isChecked()
        is_batch_method = self.batch_method_radio.isChecked()
        
        # Montrer/cacher les groupes appropriés
        self.file_group.setVisible(is_file_mode)
        self.dir_group.setVisible(is_dir_mode)
        self.batch_id_group.setVisible(is_batch_id_mode)
        
        # Rendre certains éléments visibles ou invisibles en fonction du mode
        self.token_model.setEnabled(not is_batch_id_mode)
        self.pred_model.setEnabled(not is_batch_id_mode)
        
        # Dans le mode batch_id, seul le dossier de sortie est nécessaire
        if is_batch_id_mode:
            self.batch_group.setEnabled(False)
        else:
            self.batch_group.setEnabled(is_batch_method)
    
    def browse_model(self):
        """Ouvre une boîte de dialogue pour sélectionner le modèle"""
        file, _ = QFileDialog.getOpenFileName(self, "Sélectionner un modèle", "", "Modèles (*.pth *.pt)")
        if file:
            self.model_path.setText(file)
    
    def browse_file(self):
        """Ouvre une boîte de dialogue pour sélectionner un fichier Python"""
        file, _ = QFileDialog.getOpenFileName(self, "Sélectionner un fichier Python", "", "Fichiers Python (*.py)")
        if file:
            self.file_path.setText(file)
    
    def browse_directory(self):
        """Ouvre une boîte de dialogue pour sélectionner un dossier"""
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier contenant des fichiers Python")
        if folder:
            self.dir_path.setText(folder)
            self.dir_path.setEnabled(True)  # S'assurer que le champ reste activé après la sélection
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        """Gère l'entrée d'un élément glissé-déposé"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        """Gère le dépôt d'un élément glissé"""
        urls = event.mimeData().urls()
        if not urls:
            return
        
        # Prendre le premier élément déposé
        path = urls[0].toLocalFile()
        
        if os.path.isfile(path) and path.endswith('.py'):
            # C'est un fichier Python
            self.file_mode_radio.setChecked(True)
            self.file_path.setText(path)
            self.toggle_mode()
        elif os.path.isdir(path):
            # C'est un dossier
            self.dir_mode_radio.setChecked(True)
            self.dir_path.setText(path)
            self.toggle_mode()
    
    def analyze_code(self):
        """Analyse le code Python en appelant le script test_unet.py"""
        
        # Vérifier les entrées
        if not self.model_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un modèle.")
            return
        
        # Vérifier le chemin d'entrée selon le mode
        if self.file_mode_radio.isChecked():
            if not self.file_path.text() or not os.path.isfile(self.file_path.text()):
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un fichier valide.")
                return
            input_path = self.file_path.text()
        else:
            if not self.dir_path.text() or not os.path.isdir(self.dir_path.text()):
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier valide.")
                return
            input_path = self.dir_path.text()
        
        # Construire la commande pour appeler test_unet.py
        cmd = ['python', 'unet/test_unet.py', '--model', self.model_path.text(), '--input', input_path]
        
        # Ajouter les options de visualisation si demandées
        if self.visualize_tiles_checkbox.isChecked():
            cmd.append('--visualize-tiles')
            if self.viz_output_dir.text():
                cmd.extend(['--viz-output', self.viz_output_dir.text()])
                
        if self.visualize_activations_checkbox.isChecked():
            cmd.append('--visualize-activations')
            if self.viz_output_dir.text():
                cmd.extend(['--viz-output', self.viz_output_dir.text()])
        
        # Préparer l'interface pour l'exécution
        self.console.clear()
        self.results_list.clear()
        self.details_text.clear()
        self.all_results = []
        self.progress_bar.show()
        self.test_button.setEnabled(False)
        
        # Afficher la commande exécutée pour le débogage
        cmd_str = ' '.join(cmd)
        self.console.append(f"Exécution de la commande: {cmd_str}")
        self.console.append("-" * 60 + "\n")
        
        # Créer et démarrer le thread de traitement
        self.process_thread = ProcessThread(cmd_str)
        self.process_thread.update_signal.connect(self.update_console)
        self.process_thread.finished_signal.connect(self.analysis_finished)
        self.process_thread.start()
        
        # Configurer un timer pour vérifier régulièrement les résultats
        self.check_timer = QTimer()
        self.check_timer.timeout.connect(self.parse_result_from_output)
        self.check_timer.start(1000)  # Vérifier toutes les secondes
    
    def update_console(self, text):
        """Met à jour la console avec la sortie du script"""
        self.console.append(text)
        
        # Faire défiler vers le bas
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
        # Analyser la sortie pour extraire les résultats
        if "Résultat pour:" in text or "Résultat global pour:" in text:
            self.parse_result_from_output()
    
    def parse_result_from_output(self):
        """Extrait les informations de résultat de la sortie de la console"""
        text = self.console.toPlainText()
        
        # Rechercher les sections de résultat entre les délimiteurs "=" répétés
        sections = text.split("="*60)
        results_found = False
        
        for section in sections:
            if ("Résultat pour:" in section or "Résultat global pour:" in section) and ("Prédiction:" in section or "predicted_class" in section):
                # C'est une section de résultat
                results_found = True
                lines = section.strip().split("\n")
                result = {}
                
                for line in lines:
                    line = line.strip()
                    if "Résultat pour:" in line:
                        result['file'] = line.split("Résultat pour:")[1].strip()
                    elif "Résultat global pour:" in line:
                        result['file'] = line.split("Résultat global pour:")[1].strip()
                    elif "Classe réelle:" in line:
                        result['true_class'] = line.split("Classe réelle:")[1].strip()
                    elif "Prédiction:" in line:
                        result['predicted_class'] = line.split("Prédiction:")[1].strip()
                    elif "Score brut:" in line:
                        try:
                            result['score'] = float(line.split("Score brut:")[1].strip())
                        except ValueError:
                            result['score'] = 0.5
                    elif "Score moyen:" in line:
                        try:
                            result['score'] = float(line.split("Score moyen:")[1].strip())
                        except ValueError:
                            result['score'] = 0.5
                    elif "Confiance:" in line:
                        try:
                            confidence_str = line.split("Confiance:")[1].strip()
                            result['confidence'] = float(confidence_str.replace("%", "")) / 100
                        except ValueError:
                            result['confidence'] = 0.5
                
                # Vérifier si ce résultat existe déjà dans la liste
                if result and 'file' in result and 'predicted_class' in result:
                    # Vérifier si cette entrée existe déjà
                    exists = False
                    for existing in self.all_results:
                        if existing.get('file') == result['file']:
                            exists = True
                            break
                    
                    if not exists:
                        # Si le fichier n'a pas de score, lui attribuer une valeur par défaut
                        if 'score' not in result:
                            result['score'] = 0.5
                        if 'confidence' not in result:
                            result['confidence'] = 0.5
                            
                        self.all_results.append(result)
                        self.add_result_to_list(result)
                        
                        self.console.append(f"Ajout du résultat pour {result['file']} à la liste")
        
        return results_found
    
    def add_result_to_list(self, result):
        """Ajoute un résultat à la liste des résultats"""
        # Extraire le nom de fichier du chemin complet si nécessaire
        if 'file' in result:
            # Obtenir juste le nom de fichier sans le chemin
            filename = os.path.basename(result['file'])
        else:
            filename = "Inconnu"
            
        predicted_class = result.get('predicted_class', 'Inconnu')
        confidence = result.get('confidence', 0) * 100
        
        item_text = f"{filename} - {predicted_class} ({confidence:.1f}%)"
        item = QListWidgetItem(item_text)
        
        # Définir la couleur de l'élément en fonction de la classe prédite
        if predicted_class == "IA":
            item.setBackground(Qt.red)
        else:
            item.setBackground(Qt.green)
        
        self.results_list.addItem(item)
    
    def show_result_details(self, item):
        """Affiche les détails d'un résultat sélectionné"""
        index = self.results_list.row(item)
        if 0 <= index < len(self.all_results):
            result = self.all_results[index]
            
            # Afficher les détails dans la zone de texte
            self.details_text.clear()
            self.details_text.append(f"<h3>Résultat pour: {result['file']}</h3>")
            self.details_text.append(f"<p><b>Prédiction:</b> {result['predicted_class']}</p>")
            self.details_text.append(f"<p><b>Confiance:</b> {result.get('confidence', 0)*100:.2f}%</p>")
            self.details_text.append(f"<p><b>Score brut:</b> {result.get('score', 0):.4f}</p>")
            
            if 'true_class' in result and result['true_class'] != "Inconnu":
                correct = result['predicted_class'] == result['true_class']
                self.details_text.append(f"<p><b>Classe réelle:</b> {result['true_class']}</p>")
                self.details_text.append(f"<p><b>Résultat:</b> {'Correct ✓' if correct else 'Incorrect ✗'}</p>")
            
            # Mettre à jour le graphique
            self.update_visualization(result)
    
    def update_visualization(self, result):
        """Met à jour la visualisation pour un résultat"""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        # Extraire le score
        score = result.get('score', 0)
        
        # Créer un graphique à barres montrant la probabilité IA vs Humain
        labels = ['Humain', 'IA']
        values = [1 - score, score]
        colors = ['green', 'red']
        
        # Tracer le graphique
        bars = ax.bar(labels, values, color=colors)
        
        # Ajouter les valeurs sur les barres
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{height:.2f}', ha='center', va='bottom')
        
        ax.set_ylim([0, 1.1])  # Limiter l'axe Y de 0 à 1.1
        ax.set_title('Probabilité IA vs Humain')
        ax.set_ylabel('Probabilité')
        
        # Mettre en évidence la classe prédite
        predicted_index = 1 if result.get('predicted_class') == 'IA' else 0
        ax.get_xticklabels()[predicted_index].set_fontweight('bold')
        
        self.canvas.draw()
    
    def analysis_finished(self, success, message):
        """Appelé lorsque l'analyse est terminée"""
        self.progress_bar.hide()
        self.test_button.setEnabled(True)
        
        # Arrêter le timer de vérification
        if hasattr(self, 'check_timer'):
            self.check_timer.stop()
        
        # Faire une dernière tentative de parse des résultats
        self.parse_result_from_output()
        
        if success:
            total_files = len(self.all_results)
            ia_count = sum(1 for r in self.all_results if r.get('predicted_class') == 'IA')
            human_count = total_files - ia_count
            
            status_message = f"Analyse terminée: {total_files} fichiers traités, {ia_count} détectés comme IA, {human_count} détectés comme Humain."
            QMessageBox.information(self, "Analyse terminée", status_message)
            
            # Mettre à jour la console avec un résumé
            self.console.append("\n" + "="*60)
            self.console.append("RÉSUMÉ DE L'ANALYSE")
            self.console.append("-"*60)
            self.console.append(status_message)
            
            # Mettre à jour le graphique avec un résumé global si des résultats sont disponibles
            if total_files > 0:
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                
                labels = ['Humain', 'IA']
                values = [human_count, ia_count]
                colors = ['green', 'red']
                
                ax.bar(labels, values, color=colors)
                ax.set_title(f'Résumé des {total_files} fichiers analysés')
                ax.set_ylabel('Nombre de fichiers')
                
                for i, v in enumerate(values):
                    ax.text(i, v + 0.5, str(v), ha='center')
                
                self.canvas.draw()
        else:
            QMessageBox.warning(self, "Erreur", f"Erreur lors de l'analyse: {message}")
            
        # Afficher les résultats
        self.console.append(f"\nRésultats collectés: {len(self.all_results)}")
        for i, result in enumerate(self.all_results):
            self.console.append(f"{i+1}. {result.get('file', 'Inconnu')} - {result.get('predicted_class', 'N/A')} ({result.get('confidence', 0)*100:.1f}%)")

class VisualizationTab(QWidget):
    """Onglet pour la visualisation des résultats"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Sélection du type de visualisation
        viz_type_group = QGroupBox("Type de visualisation")
        viz_type_layout = QHBoxLayout()
        
        self.viz_type = QComboBox()
        self.viz_type.addItems(["Matrices", "Activations"])
        self.viz_type.currentIndexChanged.connect(self.update_viz_options)
        
        viz_type_layout.addWidget(QLabel("Type:"))
        viz_type_layout.addWidget(self.viz_type)
        viz_type_group.setLayout(viz_type_layout)
        
        # Options de visualisation (dynamiques selon le type)
        self.options_group = QGroupBox("Options")
        self.options_layout = QVBoxLayout()
        self.options_group.setLayout(self.options_layout)
        
        # Sélection de fichier/dossier
        select_group = QGroupBox("Sélection de fichier/dossier")
        select_layout = QVBoxLayout()
        
        self.file_layout = QHBoxLayout()
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText("Chemin du fichier ou dossier à visualiser")
        self.select_button = QPushButton("Parcourir...")
        self.select_button.clicked.connect(self.browse_file)
        
        self.file_layout.addWidget(self.file_path)
        self.file_layout.addWidget(self.select_button)
        select_layout.addLayout(self.file_layout)
        
        # Options supplémentaires pour les activations
        self.model_layout = QHBoxLayout()
        self.model_label = QLabel("Modèle:")
        self.model_path = QLineEdit()
        self.model_path.setPlaceholderText("Chemin du modèle UNet (.pth)")
        self.model_button = QPushButton("Parcourir...")
        self.model_button.clicked.connect(self.browse_model)
        
        self.model_layout.addWidget(self.model_label)
        self.model_layout.addWidget(self.model_path)
        self.model_layout.addWidget(self.model_button)
        select_layout.addLayout(self.model_layout)
        
        self.matrix_layout = QHBoxLayout()
        self.matrix_label = QLabel("ID Matrice:")
        self.matrix_id = QLineEdit()
        self.matrix_id.setPlaceholderText("ID de la matrice (optionnel)")
        
        self.matrix_layout.addWidget(self.matrix_label)
        self.matrix_layout.addWidget(self.matrix_id)
        select_layout.addLayout(self.matrix_layout)
        
        select_group.setLayout(select_layout)
        
        # Bouton de visualisation
        self.visualize_button = QPushButton("Visualiser")
        self.visualize_button.clicked.connect(self.visualize)
        
        # Zone de sortie
        output_group = QGroupBox("Sortie du processus")
        output_layout = QVBoxLayout()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)
        output_group.setLayout(output_layout)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indéterminé
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addWidget(viz_type_group)
        layout.addWidget(self.options_group)
        layout.addWidget(select_group)
        layout.addWidget(self.visualize_button)
        layout.addWidget(output_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        # Initialiser les options
        self.update_viz_options(0)
    
    def update_viz_options(self, index):
        # Effacer les options actuelles
        for i in reversed(range(self.options_layout.count())): 
            item = self.options_layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
        
        viz_type = self.viz_type.currentText()
        
        if viz_type == "Matrices":
            # Options pour visualize_matrix.py
            # Mode de visualisation
            mode_layout = QHBoxLayout()
            mode_layout.addWidget(QLabel("Mode:"))
            self.viz_mode = QComboBox()
            self.viz_mode.addItems(["heatmap", "categorical"])
            mode_layout.addWidget(self.viz_mode)
            self.options_layout.addLayout(mode_layout)
            
            # Options console
            self.console_checkbox = QCheckBox("Afficher dans la console")
            self.options_layout.addWidget(self.console_checkbox)
            
            self.values_checkbox = QCheckBox("Afficher les valeurs numériques")
            self.options_layout.addWidget(self.values_checkbox)
            
            # Option de sauvegarde
            self.save_checkbox = QCheckBox("Sauvegarder en PNG")
            self.options_layout.addWidget(self.save_checkbox)
            
            output_layout = QHBoxLayout()
            output_layout.addWidget(QLabel("Dossier de sortie:"))
            self.output_dir = QLineEdit()
            self.output_dir.setPlaceholderText("Laisser vide pour utiliser le dossier de la matrice")
            output_button = QPushButton("...")
            output_button.clicked.connect(self.browse_output)
            output_layout.addWidget(self.output_dir)
            output_layout.addWidget(output_button)
            self.options_layout.addLayout(output_layout)
            
            # Masquer les options spécifiques aux activations
            self.model_label.setVisible(False)
            self.model_path.setVisible(False)
            self.model_button.setVisible(False)
            self.matrix_label.setVisible(False)
            self.matrix_id.setVisible(False)
            
        elif viz_type == "Activations":
            # Options pour visualize_activation.py
            # Afficher les options spécifiques aux activations
            self.model_label.setVisible(True)
            self.model_path.setVisible(True)
            self.model_button.setVisible(True)
            self.matrix_label.setVisible(True)
            self.matrix_id.setVisible(True)
            
            # Option device
            device_layout = QHBoxLayout()
            device_layout.addWidget(QLabel("Device:"))
            self.device_combo = QComboBox()
            self.device_combo.addItems(["auto", "cuda", "cpu"])
            device_layout.addWidget(self.device_combo)
            self.options_layout.addLayout(device_layout)
            
            # Option padding
            padding_layout = QHBoxLayout()
            padding_layout.addWidget(QLabel("Valeur de padding:"))
            self.padding_value = QLineEdit("100")
            padding_layout.addWidget(self.padding_value)
            self.options_layout.addLayout(padding_layout)
            
            # Dossier de sortie
            output_layout = QHBoxLayout()
            output_layout.addWidget(QLabel("Dossier de sortie:"))
            self.activation_output_dir = QLineEdit("activation_maps")
            output_button = QPushButton("...")
            output_button.clicked.connect(self.browse_activation_output)
            output_layout.addWidget(self.activation_output_dir)
            output_layout.addWidget(output_button)
            self.options_layout.addLayout(output_layout)
    
    def browse_file(self):
        viz_type = self.viz_type.currentText()
        
        if viz_type == "Matrices":
            file, _ = QFileDialog.getOpenFileName(self, "Sélectionner une matrice", "", "Fichiers NumPy (*.npy)")
        else:  # Activations
            # Pour les activations, permettre de sélectionner un fichier ou un dossier
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setNameFilter("Tous les fichiers (*)")
            dialog.setWindowTitle("Sélectionner une tuile ou un dossier")
            dialog.setOption(QFileDialog.DontUseNativeDialog, True)
            
            # Ajouter un bouton pour sélectionner un dossier
            for btn in dialog.findChildren(QPushButton):
                if btn.text() == 'Open' or btn.text() == "Ouvrir":
                    btn.setText("Sélectionner")
            
            if dialog.exec_():
                selected_files = dialog.selectedFiles()
                file = selected_files[0] if selected_files else None
            else:
                file = None
        
        if file:
            self.file_path.setText(file)
    
    def browse_model(self):
        file, _ = QFileDialog.getOpenFileName(self, "Sélectionner un modèle UNet", "", "Modèles PyTorch (*.pth *.pt)")
        if file:
            self.model_path.setText(file)
    
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sortie")
        if folder:
            self.output_dir.setText(folder)
    
    def browse_activation_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sortie pour les activations")
        if folder:
            self.activation_output_dir.setText(folder)
    
    def visualize(self):
        """Appelle le script de visualisation approprié en fonction du type sélectionné"""
        viz_type = self.viz_type.currentText()
        
        if not self.file_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un fichier ou dossier.")
            return
        
        # Préparer l'interface
        self.output_text.clear()
        self.progress_bar.show()
        self.visualize_button.setEnabled(False)
        
        # Construire la commande en fonction du type de visualisation
        if viz_type == "Matrices":
            cmd = ['python', 'visualization/visualize_matrix.py']
            
            # Ajouter les options
            cmd.extend(['--file', self.file_path.text()])
            
            if hasattr(self, 'viz_mode') and self.viz_mode.currentText():
                cmd.extend(['--mode', self.viz_mode.currentText()])
                
            if hasattr(self, 'console_checkbox') and self.console_checkbox.isChecked():
                cmd.append('--console')
                
            if hasattr(self, 'values_checkbox') and self.values_checkbox.isChecked():
                cmd.append('--values')
                
            if hasattr(self, 'save_checkbox') and self.save_checkbox.isChecked():
                cmd.append('--save')
                
            if hasattr(self, 'output_dir') and self.output_dir.text():
                cmd.extend(['--output-dir', self.output_dir.text()])
                
        else:  # Activations
            if not self.model_path.text():
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un modèle UNet.")
                self.progress_bar.hide()
                self.visualize_button.setEnabled(True)
                return
                
            cmd = ['python', 'visualization/visualize_activation.py']
            
            # Ajouter les options
            cmd.extend(['--model', self.model_path.text()])
            cmd.extend(['--input', self.file_path.text()])
            
            if self.matrix_id.text():
                cmd.extend(['--matrix', self.matrix_id.text()])
                
            if hasattr(self, 'activation_output_dir') and self.activation_output_dir.text():
                cmd.extend(['--output', self.activation_output_dir.text()])
                
            if hasattr(self, 'device_combo') and self.device_combo.currentText() != "auto":
                cmd.extend(['--device', self.device_combo.currentText()])
                
            if hasattr(self, 'padding_value') and self.padding_value.text():
                try:
                    float(self.padding_value.text())  # Vérifier que c'est bien un nombre
                    cmd.extend(['--padding', self.padding_value.text()])
                except ValueError:
                    QMessageBox.warning(self, "Erreur", "La valeur de padding doit être un nombre.")
                    self.progress_bar.hide()
                    self.visualize_button.setEnabled(True)
                    return
        
        # Afficher la commande exécutée
        command_str = ' '.join(cmd)
        self.output_text.append(f"Exécution de la commande: {command_str}")
        self.output_text.append("-" * 60)
        
        # Exécuter dans un thread
        self.thread = ProcessThread(command_str)
        self.thread.update_signal.connect(self.update_output)
        self.thread.finished_signal.connect(self.process_finished)
        self.thread.start()
    
    def update_output(self, text):
        """Met à jour la zone de sortie avec la sortie du script"""
        self.output_text.append(text)
        # Faire défiler vers le bas
        scrollbar = self.output_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def process_finished(self, success, message):
        """Appelé lorsque le processus est terminé"""
        self.progress_bar.hide()
        self.visualize_button.setEnabled(True)
        
        if success:
            self.output_text.append("-" * 60)
            self.output_text.append("Visualisation terminée avec succès!")
            
            if self.viz_type.currentText() == "Matrices":
                # Pour les matrices, indiquer où l'image a été sauvegardée
                if hasattr(self, 'save_checkbox') and self.save_checkbox.isChecked():
                    output_dir = (hasattr(self, 'output_dir') and self.output_dir.text()) or os.path.dirname(self.file_path.text())
                    filename = os.path.basename(self.file_path.text()).replace(".npy", ".png")
                    img_path = os.path.join(output_dir, filename)
                    
                    if os.path.exists(img_path):
                        self.output_text.append(f"Image sauvegardée dans: {img_path}")
            else:
                # Pour les activations, indiquer où les images ont été sauvegardées
                output_dir = (hasattr(self, 'activation_output_dir') and self.activation_output_dir.text()) or "activation_maps"
                self.output_text.append(f"Images sauvegardées dans le dossier: {output_dir}")
        else:
            self.output_text.append("-" * 60)
            self.output_text.append(f"Erreur lors de la visualisation: {message}")

class BatchRetrievalTab(QWidget):
    """Onglet pour récupérer les résultats des batches OpenAI"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Type de batch
        type_group = QGroupBox("Type de batch")
        type_layout = QHBoxLayout()
        
        self.ia_scripts_radio = QRadioButton("Scripts IA (ia_scripts_generator)")
        self.matrices_radio = QRadioButton("Matrices (matrix_batch_sender)")
        self.ia_scripts_radio.setChecked(True)
        self.ia_scripts_radio.toggled.connect(self.update_interface)
        self.matrices_radio.toggled.connect(self.update_interface)
        
        type_layout.addWidget(self.ia_scripts_radio)
        type_layout.addWidget(self.matrices_radio)
        type_group.setLayout(type_layout)
        
        # Méthode de récupération
        method_group = QGroupBox("Méthode de récupération")
        method_layout = QVBoxLayout()
        
        self.single_batch_radio = QRadioButton("Récupérer un batch spécifique")
        self.list_batches_radio = QRadioButton("Lister et récupérer plusieurs batches")
        self.single_batch_radio.setChecked(True)
        self.single_batch_radio.toggled.connect(self.toggle_method)
        self.list_batches_radio.toggled.connect(self.toggle_method)
        
        method_layout.addWidget(self.single_batch_radio)
        method_layout.addWidget(self.list_batches_radio)
        method_group.setLayout(method_layout)
        
        # Saisie du batch ID
        self.batch_id_group = QGroupBox("Batch ID")
        batch_id_layout = QHBoxLayout()
        
        self.batch_id_input = QLineEdit()
        self.batch_id_input.setPlaceholderText("batch_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        batch_id_layout.addWidget(QLabel("Batch ID:"))
        batch_id_layout.addWidget(self.batch_id_input)
        self.batch_id_group.setLayout(batch_id_layout)
        
        # Liste des batches
        self.batches_list_group = QGroupBox("Batches disponibles")
        batches_list_layout = QVBoxLayout()
        
        refresh_button = QPushButton("Rafraîchir la liste des batches")
        refresh_button.clicked.connect(self.refresh_batches_list)
        
        self.batches_list = QListWidget()
        self.batches_list.setSelectionMode(QListWidget.MultiSelection)
        
        limit_layout = QHBoxLayout()
        limit_layout.addWidget(QLabel("Limite:"))
        self.batches_limit = QSpinBox()
        self.batches_limit.setRange(10, 1000)
        self.batches_limit.setValue(50)
        limit_layout.addWidget(self.batches_limit)
        
        batches_list_layout.addWidget(refresh_button)
        batches_list_layout.addLayout(limit_layout)
        batches_list_layout.addWidget(self.batches_list)
        self.batches_list_group.setLayout(batches_list_layout)
        self.batches_list_group.hide()
        
        # Dossier de sortie
        output_group = QGroupBox("Dossier de sortie")
        output_layout = QHBoxLayout()
        
        self.output_dir = QLineEdit()
        self.output_dir.setPlaceholderText("Dossier où sauvegarder les résultats")
        output_button = QPushButton("Parcourir...")
        output_button.clicked.connect(self.browse_output)
        
        output_layout.addWidget(self.output_dir)
        output_layout.addWidget(output_button)
        output_group.setLayout(output_layout)
        
        # Options de récupération
        options_group = QGroupBox("Options")
        options_layout = QVBoxLayout()
        
        self.force_checkbox = QCheckBox("Forcer la récupération (même si non terminé)")
        self.save_raw_checkbox = QCheckBox("Sauvegarder les résultats bruts (JSONL)")
        self.save_processed_checkbox = QCheckBox("Sauvegarder les résultats traités")
        self.save_processed_checkbox.setChecked(True)
        
        # Options spécifiques aux matrices
        self.save_tokens_json_checkbox = QCheckBox("Sauvegarder les tokens JSON (pour matrices)")
        self.auto_construct_matrices_checkbox = QCheckBox("Construire automatiquement les matrices après récupération")
        
        options_layout.addWidget(self.force_checkbox)
        options_layout.addWidget(self.save_raw_checkbox)
        options_layout.addWidget(self.save_processed_checkbox)
        options_layout.addWidget(self.save_tokens_json_checkbox)
        options_layout.addWidget(self.auto_construct_matrices_checkbox)
        options_group.setLayout(options_layout)
        
        # Boutons d'action
        actions_layout = QHBoxLayout()
        
        self.check_status_button = QPushButton("Vérifier le statut")
        self.check_status_button.clicked.connect(self.check_status)
        
        self.retrieve_button = QPushButton("Récupérer les résultats")
        self.retrieve_button.clicked.connect(self.retrieve_results)
        
        actions_layout.addWidget(self.check_status_button)
        actions_layout.addWidget(self.retrieve_button)
        
        # Console de sortie
        console_group = QGroupBox("Sortie")
        console_layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        console_layout.addWidget(self.console)
        console_group.setLayout(console_layout)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addWidget(type_group)
        layout.addWidget(method_group)
        layout.addWidget(self.batch_id_group)
        layout.addWidget(self.batches_list_group)
        layout.addWidget(output_group)
        layout.addWidget(options_group)
        layout.addLayout(actions_layout)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        # Initialiser l'interface
        self.update_interface()
    
    def update_interface(self):
        """Met à jour l'interface selon le type de batch sélectionné"""
        is_matrices = self.matrices_radio.isChecked()
        
        # Les options spécifiques aux matrices ne sont visibles que pour les matrices
        self.save_tokens_json_checkbox.setVisible(is_matrices)
        self.auto_construct_matrices_checkbox.setVisible(is_matrices)
        
        # Mettre à jour les placeholders
        if is_matrices:
            self.output_dir.setPlaceholderText("Dossier pour les résultats de matrices (tokens JSON)")
        else:
            self.output_dir.setPlaceholderText("Dossier pour les scripts IA générés")
    
    def toggle_method(self):
        """Change l'interface selon la méthode de récupération"""
        if self.single_batch_radio.isChecked():
            self.batch_id_group.show()
            self.batches_list_group.hide()
        else:
            self.batch_id_group.hide()
            self.batches_list_group.show()
    
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sortie")
        if folder:
            self.output_dir.setText(folder)
    
    def update_console(self, text):
        """Met à jour la console avec du texte"""
        self.console.append(text)
        # Faire défiler automatiquement vers le bas
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def refresh_batches_list(self):
        """Rafraîchit la liste des batches disponibles"""
        if not self.output_dir.text():
            QMessageBox.warning(self, "Erreur", "Veuillez d'abord spécifier un dossier de sortie.")
            return
        
        self.console.clear()
        self.console.append(f"Recherche des batches dans: {self.output_dir.text()}")
        self.batches_list.clear()
        
        # Chercher les fichiers de métadonnées dans le dossier
        metadata_dir = os.path.join(self.output_dir.text(), "metadata")
        if os.path.exists(metadata_dir):
            # Lister les fichiers batch_*.json
            import glob
            import json
            batch_files = glob.glob(os.path.join(metadata_dir, "batch_*.json"))
            
            for batch_file in batch_files:
                try:
                    with open(batch_file, 'r') as f:
                        batch_data = json.load(f)
                    
                    batch_id = batch_data.get('batch_id', 'Unknown')
                    status = batch_data.get('status', 'Unknown')
                    created_at = batch_data.get('created_at', 'Unknown')
                    
                    # Ajouter à la liste
                    item_text = f"{batch_id} - Status: {status} - Créé: {created_at}"
                    self.batches_list.addItem(item_text)
                    
                except Exception as e:
                    self.console.append(f"Erreur lors de la lecture de {batch_file}: {str(e)}")
            
            if len(batch_files) == 0:
                self.console.append("Aucun fichier de batch trouvé dans le dossier metadata.")
            else:
                self.console.append(f"{len(batch_files)} batch(es) trouvé(s).")
        else:
            # Si pas de dossier metadata, utiliser l'ancienne méthode avec batch_manager.py
            cmd = ['python', 'utils/batch_manager.py', 'list']
            cmd.extend(['--output', self.output_dir.text()])
            cmd.extend(['--limit', str(self.batches_limit.value())])
            
            self.console.append(f"Commande: {' '.join(cmd)}\n")
            
            # Exécuter dans un thread
            self.thread = ProcessThread(' '.join(cmd))
            self.thread.update_signal.connect(self.update_console)
            self.thread.finished_signal.connect(self.on_list_finished)
            self.thread.start()
    
    def on_list_finished(self, success, message):
        """Traite les résultats de la liste des batches"""
        if success:
            # Parser la sortie pour extraire les IDs de batch
            # (Cette partie pourrait être améliorée avec un parsing plus sophistiqué)
            self.console.append("Liste récupérée avec succès.")
        else:
            self.console.append(f"Erreur lors de la récupération: {message}")
    
    def check_status(self):
        """Vérifie le statut d'un ou plusieurs batches"""
        if not self.output_dir.text():
            QMessageBox.warning(self, "Erreur", "Veuillez spécifier un dossier de sortie.")
            return
        
        if self.single_batch_radio.isChecked():
            if not self.batch_id_input.text():
                QMessageBox.warning(self, "Erreur", "Veuillez saisir un batch ID.")
                return
            
            batch_ids = [self.batch_id_input.text()]
        else:
            selected_items = self.batches_list.selectedItems()
            if not selected_items:
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner au moins un batch.")
                return
            
            batch_ids = [item.text().split()[0] for item in selected_items]  # Extraire l'ID du texte
        
        self.console.clear()
        self.progress_bar.show()
        
        for batch_id in batch_ids:
            cmd = ['python', 'utils/batch_manager.py', 'status', batch_id]
            cmd.extend(['--output', self.output_dir.text()])
            
            self.console.append(f"Vérification du statut de {batch_id}...")
            self.console.append(f"Commande: {' '.join(cmd)}\n")
            
            # Exécuter dans un thread
            self.thread = ProcessThread(' '.join(cmd))
            self.thread.update_signal.connect(self.update_console)
            self.thread.finished_signal.connect(self.on_status_finished)
            self.thread.start()
            break  # Pour l'instant, traiter un seul batch à la fois
    
    def retrieve_results(self):
        """Récupère les résultats d'un ou plusieurs batches"""
        if not self.output_dir.text():
            QMessageBox.warning(self, "Erreur", "Veuillez spécifier un dossier de sortie.")
            return
        
        if self.single_batch_radio.isChecked():
            if not self.batch_id_input.text():
                QMessageBox.warning(self, "Erreur", "Veuillez saisir un batch ID.")
                return
            
            batch_ids = [self.batch_id_input.text()]
        else:
            selected_items = self.batches_list.selectedItems()
            if not selected_items:
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner au moins un batch.")
                return
            
            batch_ids = [item.text().split()[0] for item in selected_items]
        
        self.console.clear()
        self.progress_bar.show()
        self.retrieve_button.setEnabled(False)
        
        for batch_id in batch_ids:
            cmd = ['python', 'utils/batch_manager.py', 'fetch', batch_id]
            cmd.extend(['--output', self.output_dir.text()])
            
            if self.output_dir.text():
                cmd.extend(['--destination', self.output_dir.text()])
            
            if self.force_checkbox.isChecked():
                cmd.append('--force')
            
            if self.save_processed_checkbox.isChecked():
                cmd.append('--save')
            
            if self.save_raw_checkbox.isChecked():
                cmd.append('--save-raw')
            
            if self.matrices_radio.isChecked() and self.save_tokens_json_checkbox.isChecked():
                cmd.append('--save-tokens-json')
            
            self.console.append(f"Récupération des résultats de {batch_id}...")
            self.console.append(f"Commande: {' '.join(cmd)}\n")
            
            # Exécuter dans un thread
            self.thread = ProcessThread(' '.join(cmd))
            self.thread.update_signal.connect(self.update_console)
            self.thread.finished_signal.connect(self.on_retrieve_finished)
            self.thread.start()
            break  # Pour l'instant, traiter un seul batch à la fois
    
    def on_status_finished(self, success, message):
        """Appelé quand la vérification de statut est terminée"""
        self.progress_bar.hide()
        if success:
            self.console.append("Vérification terminée.")
        else:
            self.console.append(f"Erreur: {message}")
    
    def on_retrieve_finished(self, success, message):
        """Appelé quand la récupération est terminée"""
        self.progress_bar.hide()
        self.retrieve_button.setEnabled(True)
        
        if success:
            self.console.append("Récupération terminée avec succès!")
            
            # Si on récupère des matrices ET qu'on veut construire automatiquement
            if (self.matrices_radio.isChecked() and 
                self.auto_construct_matrices_checkbox.isChecked() and
                self.save_tokens_json_checkbox.isChecked()):
                
                self.console.append("\nConstruction automatique des matrices...")
                self._construct_matrices_automatically()
        else:
            self.console.append(f"Erreur lors de la récupération: {message}")
    
    def _construct_matrices_automatically(self):
        """Construit automatiquement les matrices après récupération des tokens JSON"""
        # Une approche plus simple: utiliser directement matrix_batch_generator.py avec le fichier source
        self.console.append("\nPour générer les matrices, veuillez:")
        self.console.append("1. Aller dans l'onglet 'Génération des Matrices'")
        self.console.append("2. Sélectionner le fichier source original (pas le fichier tokens)")
        self.console.append("3. Cliquer sur 'Générer les matrices'")
        self.console.append("\nLe traitement automatique des matrices n'est pas disponible après récupération du batch.")


# Placer la définition de MainWindow après toutes les autres classes
class MainWindow(QMainWindow):
    """Fenêtre principale de l'application"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Pipeline de Traitement de Code - Cassiopée")
        self.setGeometry(100, 100, 1400, 900)
        
        # Créer les onglets
        self.tabs = QTabWidget()
        
        # Onglet 1: Génération de scripts IA
        self.script_generation_tab = ScriptGenerationTab()
        self.tabs.addTab(self.script_generation_tab, "Génération de Code IA")
        
        # Onglet 2: Récupération des batches
        self.batch_retrieval_tab = BatchRetrievalTab()
        self.tabs.addTab(self.batch_retrieval_tab, "Récupération de Batches")
        
        # Onglet 3: Génération des matrices
        self.matrix_generation_tab = MatrixGenerationTab()
        self.tabs.addTab(self.matrix_generation_tab, "Génération des Matrices")
        
        # Onglet 4: Génération des tuiles
        self.matrix_tiling_tab = MatrixTilingTab()
        self.tabs.addTab(self.matrix_tiling_tab, "Génération des Tuiles")
        
        # Onglet 5: Entraînement U-Net
        self.unet_training_tab = UNetTrainingTab()
        self.tabs.addTab(self.unet_training_tab, "Entraînement U-Net")
        
        # Onglet 6: Test U-Net
        self.unet_testing_tab = UNetTestingTab()
        self.tabs.addTab(self.unet_testing_tab, "Test U-Net")
        
        # Onglet 7: Visualisation
        self.visualization_tab = VisualizationTab()
        self.tabs.addTab(self.visualization_tab, "Visualisation")
        
        # Définir le widget central
        self.setCentralWidget(self.tabs)
        
        # Afficher la fenêtre
        self.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()