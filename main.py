
import sys
import os
import subprocess
import tempfile

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFileDialog, QProgressBar, QSpinBox, QCheckBox,
    QComboBox, QListWidget, QMessageBox, QLineEdit,
    QGroupBox, QRadioButton, QTextEdit, QScrollArea,
    QListWidgetItem
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QMimeData
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



class MatrixGenerationTab(QWidget):
    """Onglet pour la génération des matrices"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Mode de sélection (fichier unique ou dossier batch)
        mode_group = QGroupBox("Mode de génération")
        mode_layout = QVBoxLayout()
        
        self.file_mode_radio = QRadioButton("Analyser un fichier unique")
        self.dir_mode_radio = QRadioButton("Analyser un dossier batch complet")
        self.file_mode_radio.setChecked(True)
        self.file_mode_radio.toggled.connect(self.toggle_mode)
        self.dir_mode_radio.toggled.connect(self.toggle_mode)
        
        mode_layout.addWidget(self.file_mode_radio)
        mode_layout.addWidget(self.dir_mode_radio)
        mode_group.setLayout(mode_layout)
        
class ProcessThread(QThread):
    """Thread pour exécuter les scripts sans bloquer l'interface"""
    update_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)
    
    def __init__(self, command):
        super().__init__()
        self.command = command
        
    def run(self):
        try:
            process = subprocess.Popen(self.command, 
                                      stdout=subprocess.PIPE, 
                                      stderr=subprocess.STDOUT,
                                      shell=True,
                                      text=True,
                                      bufsize=1)
            
            for line in iter(process.stdout.readline, ''):
                self.update_signal.emit(line.strip())
            
            exit_code = process.wait()
            success = exit_code == 0
            self.finished_signal.emit(success, "Terminé avec succès" if success else f"Échec (code {exit_code})")
        except Exception as e:
            self.update_signal.emit(f"Erreur: {str(e)}")
            self.finished_signal.emit(False, str(e))


class ScriptsGeneratorTab(QWidget):
    """Onglet pour la génération de scripts Python"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Sélection du dataset
        dataset_group = QGroupBox("Dataset d'entrée")
        dataset_layout = QVBoxLayout()
        
        self.codenet_radio = QRadioButton("CodeNet")
        self.thestack_radio = QRadioButton("The Stack")
        self.codenet_radio.setChecked(True)
        
        dataset_layout.addWidget(self.codenet_radio)
        dataset_layout.addWidget(self.thestack_radio)
        
        # Sélection du chemin d'entrée
        input_layout = QHBoxLayout()
        self.input_path = QLineEdit()
        self.input_path.setPlaceholderText("Chemin vers le dataset d'entrée")
        input_button = QPushButton("Parcourir...")
        input_button.clicked.connect(self.browse_input)
        input_layout.addWidget(self.input_path)
        input_layout.addWidget(input_button)
        
        # Sélection du chemin de sortie
        output_layout = QHBoxLayout()
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Chemin de sortie pour les fichiers générés")
        output_button = QPushButton("Parcourir...")
        output_button.clicked.connect(self.browse_output)
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(output_button)
        
        dataset_layout.addLayout(input_layout)
        dataset_group.setLayout(dataset_layout)
        
        # Configuration des paramètres
        params_group = QGroupBox("Paramètres de génération")
        params_layout = QVBoxLayout()
        
        folders_layout = QHBoxLayout()
        folders_layout.addWidget(QLabel("Nombre de sous-dossiers:"))
        self.folders_spinbox = QSpinBox()
        self.folders_spinbox.setRange(1, 1000)
        self.folders_spinbox.setValue(5)
        folders_layout.addWidget(self.folders_spinbox)
        
        variations_layout = QHBoxLayout()
        variations_layout.addWidget(QLabel("Variations par script:"))
        self.variations_spinbox = QSpinBox()
        self.variations_spinbox.setRange(1, 10)
        self.variations_spinbox.setValue(3)
        variations_layout.addWidget(self.variations_spinbox)
        
        generations_layout = QHBoxLayout()
        generations_layout.addWidget(QLabel("Générations par problème:"))
        self.generations_spinbox = QSpinBox()
        self.generations_spinbox.setRange(1, 10)
        self.generations_spinbox.setValue(2)
        generations_layout.addWidget(self.generations_spinbox)
        
        batch_layout = QHBoxLayout()
        batch_layout.addWidget(QLabel("Taille des batches:"))
        self.batch_spinbox = QSpinBox()
        self.batch_spinbox.setRange(100, 50000)
        self.batch_spinbox.setValue(1000)
        self.batch_spinbox.setSingleStep(100)
        batch_layout.addWidget(self.batch_spinbox)
        
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("Intervalle de vérification (s):"))
        self.interval_spinbox = QSpinBox()
        self.interval_spinbox.setRange(10, 300)
        self.interval_spinbox.setValue(60)
        interval_layout.addWidget(self.interval_spinbox)
        
        # Options
        self.test_checkbox = QCheckBox("Mode test (petit échantillon)")
        self.no_batch_checkbox = QCheckBox("Désactiver l'API Batch (appels synchrones)")
        self.wait_completion_checkbox = QCheckBox("Attendre la complétion des batchs")
        
        # API Key
        apikey_layout = QHBoxLayout()
        apikey_layout.addWidget(QLabel("Clé API OpenAI:"))
        self.apikey_input = QLineEdit()
        self.apikey_input.setPlaceholderText("Laissez vide pour utiliser la variable d'environnement")
        apikey_layout.addWidget(self.apikey_input)
        
        params_layout.addLayout(folders_layout)
        params_layout.addLayout(variations_layout)
        params_layout.addLayout(generations_layout)
        params_layout.addLayout(batch_layout)
        params_layout.addLayout(interval_layout)
        params_layout.addWidget(self.test_checkbox)
        params_layout.addWidget(self.no_batch_checkbox)
        params_layout.addWidget(self.wait_completion_checkbox)
        params_layout.addLayout(apikey_layout)
        
        params_group.setLayout(params_layout)
        
        # Output console
        console_group = QGroupBox("Sortie du programme")
        console_layout = QVBoxLayout()
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        console_layout.addWidget(self.console_output)
        console_group.setLayout(console_layout)
        
        # Execute button
        self.execute_button = QPushButton("Exécuter la génération de scripts")
        self.execute_button.clicked.connect(self.execute_script)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate
        self.progress_bar.hide()
        
        # Construct main layout
        layout.addWidget(dataset_group)
        layout.addLayout(output_layout)
        layout.addWidget(params_group)
        layout.addWidget(console_group)
        layout.addWidget(self.execute_button)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
    
    def browse_input(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier d'entrée")
        if folder:
            self.input_path.setText(folder)
    
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de sortie")
        if folder:
            self.output_path.setText(folder)
    
    def execute_script(self):
        # Valider les entrées
        if not self.input_path.text() or not self.output_path.text():
            QMessageBox.warning(self, "Erreur", "Les chemins d'entrée et de sortie sont requis.")
            return
        
        # Construire la commande
        cmd = ['python', 'scripts_generation/ia_scripts_generator.py']
        cmd.append('--input')
        cmd.append(self.input_path.text())
        cmd.append('--output')
        cmd.append(self.output_path.text())
        
        if self.folders_spinbox.value() > 0:
            cmd.extend(['--folders', str(self.folders_spinbox.value())])
        
        cmd.extend(['--variations', str(self.variations_spinbox.value())])
        cmd.extend(['--generations', str(self.generations_spinbox.value())])
        cmd.extend(['--batch-size', str(self.batch_spinbox.value())])
        cmd.extend(['--poll-interval', str(self.interval_spinbox.value())])
        
        if self.test_checkbox.isChecked():
            cmd.append('--test')
        
        if self.no_batch_checkbox.isChecked():
            cmd.append('--no-batch')
        
        if self.wait_completion_checkbox.isChecked():
            cmd.append('--wait-completion')
        
        if self.apikey_input.text():
            cmd.extend(['--api-key', self.apikey_input.text()])
        
        # Préparer l'interface
        self.console_output.clear()
        self.progress_bar.show()
        self.execute_button.setEnabled(False)
        
        # Exécuter dans un thread
        self.thread = ProcessThread(' '.join(cmd))
        self.thread.update_signal.connect(self.update_console)
        self.thread.finished_signal.connect(self.process_finished)
        self.thread.start()
    
    def update_console(self, text):
        self.console_output.append(text)
        # Scroll to bottom
        scrollbar = self.console_output.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def process_finished(self, success, message):
        self.progress_bar.hide()
        self.execute_button.setEnabled(True)
        status = "Succès" if success else "Échec"
        QMessageBox.information(self, status, message)


class BatchManagerTab(QWidget):
    """Onglet pour la gestion des batches OpenAI"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Configuration générale
        config_group = QGroupBox("Configuration")
        config_layout = QVBoxLayout()
        
        api_layout = QHBoxLayout()
        api_layout.addWidget(QLabel("Clé API OpenAI:"))
        self.api_key = QLineEdit()
        self.api_key.setPlaceholderText("Laissez vide pour utiliser la variable d'environnement")
        api_layout.addWidget(self.api_key)
        
        self.output_dir = QLineEdit()
        self.output_dir.setPlaceholderText("../data/batches")
        self.output_browse_button = QPushButton("...")
        self.output_browse_button.clicked.connect(self.browse_output)

        
        dest_layout = QHBoxLayout()
        dest_layout.addWidget(QLabel("Destination des résultats:"))
        self.destination_path = QLineEdit()
        self.destination_path.setPlaceholderText("Par defaut data/batches")
        self.browse_dest_button = QPushButton("...")
        self.browse_dest_button.clicked.connect(self.browse_destination)
        dest_layout.addWidget(self.destination_path)
        dest_layout.addWidget(self.browse_dest_button) 
        config_layout.addLayout(api_layout)
        config_layout.addLayout(dest_layout)
        config_group.setLayout(config_layout)
        
        # Commande "list"
        list_group = QGroupBox("Lister les batches")
        list_layout = QHBoxLayout()
        
        self.refresh_button = QPushButton("Rafraîchir la liste")
        self.refresh_button.clicked.connect(self.refresh_batches)
        
        list_layout.addWidget(self.refresh_button)
        list_layout.addWidget(QLabel("Limite:"))
        self.batch_limit = QSpinBox()
        self.batch_limit.setRange(1, 1000)
        self.batch_limit.setValue(100)  # défaut selon le guide
        list_layout.addWidget(self.batch_limit)
        
        list_group.setLayout(list_layout)
        
        # Liste des batches
        batch_group = QGroupBox("Batches disponibles")
        batch_layout = QVBoxLayout()
        self.batch_list = QListWidget()
        self.batch_list.setSelectionMode(QListWidget.ExtendedSelection)
        batch_layout.addWidget(self.batch_list)
        batch_group.setLayout(batch_layout)
        
        # Commandes et actions
        actions_group = QGroupBox("Actions sur les batches")
        actions_layout = QVBoxLayout()
        
        # Commande "status"
        status_layout = QHBoxLayout()
        self.get_status_button = QPushButton("Vérifier l'état du batch")
        self.get_status_button.clicked.connect(self.get_batch_status)
        status_layout.addWidget(self.get_status_button)
        
        # Commande "fetch"
        fetch_layout = QHBoxLayout()
        self.fetch_button = QPushButton("Récupérer les résultats")
        self.fetch_button.clicked.connect(self.fetch_batch)
        
        fetch_layout.addWidget(self.fetch_button)
        
        # Commande "fetch-range"
        range_layout = QHBoxLayout()
        self.fetch_range_button = QPushButton("Récupérer N batches récents")
        self.fetch_range_button.clicked.connect(self.fetch_range)
        range_layout.addWidget(self.fetch_range_button)
        range_layout.addWidget(QLabel("Nombre de batches:"))
        self.range_spinbox = QSpinBox()
        self.range_spinbox.setRange(1, 100000)
        self.range_spinbox.setValue(5)
        range_layout.addWidget(self.range_spinbox)
        
        actions_layout.addLayout(status_layout)
        actions_layout.addLayout(fetch_layout)
        actions_layout.addLayout(range_layout)
        actions_group.setLayout(actions_layout)
        
        # Zone d'affichage des détails
        details_group = QGroupBox("Détails du batch")
        details_layout = QVBoxLayout()
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        details_layout.addWidget(self.details_text)
        details_group.setLayout(details_layout)
        
        # Console de sortie
        console_group = QGroupBox("Sortie du programme")
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
        layout.addWidget(config_group)
        layout.addWidget(list_group)
        layout.addWidget(batch_group)
        layout.addWidget(actions_group)
        layout.addWidget(details_group)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
    
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le répertoire de base")
        if folder:
            self.output_dir.setText(folder)
    
    def browse_destination(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier de destination")
        if folder:
            self.destination_path.setText(folder)
    
    def refresh_batches(self):
        """Liste les batchs disponibles via l'API OpenAI"""
        cmd = ['python', 'utils/batch_manager.py', 'list']
        
        # Ajouter les options selon le guide
        if self.batch_limit.value() > 0:
            cmd.extend(['--limit', str(self.batch_limit.value())])
        
        if self.output_dir.text():
            cmd.extend(['--output', self.output_dir.text()])
        
        if self.api_key.text():
            cmd.extend(['--api-key', self.api_key.text()])
        
        self.batch_list.clear()
        self.console.clear()
        self.details_text.clear()
        self.progress_bar.show()
        
        # Exécuter dans un thread
        self.thread = ProcessThread(' '.join(cmd))
        self.thread.update_signal.connect(self.update_console)
        self.thread.finished_signal.connect(self.update_batch_list)
        self.thread.start()
    
    def update_console(self, text):
        self.console.append(text)
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def update_batch_list(self, success, message):
        self.progress_bar.hide()
        if success:
            # Analyser la sortie pour extraire les IDs de batch
            console_text = self.console.toPlainText()
            lines = console_text.split('\n')
            
            batch_count = 0
            # Utiliser une expression plus souple pour détecter les IDs de batch
            for line in lines:
                # Chercher les lignes contenant un ID de batch au format batch_xxx
                if 'batch_' in line:
                    # Extraire le batch ID (peut apparaître sous différentes formes)
                    parts = line.split()
                    for part in parts:
                        if part.startswith('batch_'):
                            # Nettoyer l'ID des caractères potentiellement indésirables
                            batch_id = part.strip(',.:;()[]{}')
                            self.batch_list.addItem(batch_id)
                            batch_count += 1
                            break
                # Autre format possible: ligne contenant "ID:" suivi d'un ID de batch
                elif 'ID:' in line or 'Id:' in line or 'id:' in line:
                    parts = line.split('ID:' if 'ID:' in line else 'Id:' if 'Id:' in line else 'id:')
                    if len(parts) > 1:
                        batch_id = parts[1].strip().split()[0]
                        if batch_id.startswith('batch_'):
                            self.batch_list.addItem(batch_id)
                            batch_count += 1
            
            self.console.append("----------------------------------")
            self.console.append(f"Nombre de batches trouvés: {batch_count}")
        
            if batch_count == 0:
                self.console.append("Aucun batch trouvé dans la sortie du programme.")
                self.console.append("Vérifiez que le script 'simple_batch_manager.py' fonctionne correctement.")
                self.console.append("Voici la sortie complète pour analyse:")
                self.console.append("----------------------------------")
                self.console.append(console_text)
            else:
                self.console.append("Sélectionnez un batch dans la liste pour voir ses détails.")
        else:
            self.console.append(f"Erreur lors de la récupération des batches: {message}")
    
    def get_batch_status(self):
        """Vérifie l'état d'un batch spécifique"""
        selected = self.batch_list.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Attention", "Veuillez sélectionner un batch.")
            return
        
        batch_id = selected[0].text()
        cmd = ['python', 'utils/batch_manager.py', 'status', batch_id]
        
        if self.api_key.text():
            cmd.extend(['--api-key', self.api_key.text()])
        
        self.details_text.clear()
        self.progress_bar.show()
        
        # Exécuter dans un thread
        self.thread = ProcessThread(' '.join(cmd))
        self.thread.update_signal.connect(self.update_details)
        self.thread.finished_signal.connect(lambda success, message: self.progress_bar.hide())
        self.thread.start()
    
    def update_details(self, text):
        self.details_text.append(text)
        scrollbar = self.details_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def fetch_batch(self):
        """Récupère les résultats d'un ou plusieurs batches"""
        selected = self.batch_list.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Attention", "Veuillez sélectionner un ou plusieurs batches.")
            return
        
        for item in selected:
            batch_id = item.text()
            cmd = ['python', 'utils/batch_manager.py', 'fetch', batch_id]
            
            # Toujours ajouter l'option --save
            cmd.append('--save')
            
            if self.destination_path.text():
                cmd.extend(['--destination', self.destination_path.text()])
            
            if self.api_key.text():
                cmd.extend(['--api-key', self.api_key.text()])
            
            self.console.append(f"Récupération du batch {batch_id}...")
            self.progress_bar.show()
            
            # Exécuter dans un thread
            self.thread = ProcessThread(' '.join(cmd))
            self.thread.update_signal.connect(self.update_console)
            self.thread.finished_signal.connect(lambda success, message, bid=batch_id: 
                                              self.console.append(f"Batch {bid} : {'Succès' if success else 'Échec'} - {message}"))
            self.thread.start()
    
    def fetch_range(self):
        """Récupère les résultats des N batches les plus récents"""
        n = self.range_spinbox.value()
        cmd = ['python', 'utils/batch_manager.py', 'fetch-range', str(n)]
        
        # Ajouter les options selon le guide
        if self.batch_limit.value() > 0:
            cmd.extend(['--limit', str(self.batch_limit.value())])
        
        # Toujours ajouter l'option --save
        cmd.append('--save')
        
        if self.destination_path.text():
            cmd.extend(['--destination', self.destination_path.text()])
        
        if self.api_key.text():
            cmd.extend(['--api-key', self.api_key.text()])
        
        self.console.clear()
        self.console.append(f"Récupération des {n} batches les plus récents...")
        self.progress_bar.show()
        
        # Exécuter dans un thread
        self.thread = ProcessThread(' '.join(cmd))
        self.thread.update_signal.connect(self.update_console)
        self.thread.finished_signal.connect(self.on_fetch_range_finished)
        self.thread.start()
    
    def on_fetch_range_finished(self, success, message):
        """Appelé lorsque la récupération des batches par rang est terminée"""
        self.progress_bar.hide()
        if success:
            self.console.append("----------------------------------")
            self.console.append("Récupération des batches terminée avec succès.")
            if self.destination_path.text():
                self.console.append(f"Résultats sauvegardés dans: {self.destination_path.text()}")
        else:
            self.console.append(f"Erreur lors de la récupération des batches: {message}")
class BatchCompletionTab(QWidget):
    """Onglet pour la complétion des batches"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Sélection du batch
        batch_group = QGroupBox("Sélection du batch")
        batch_layout = QHBoxLayout()
        
        self.batch_path = QLineEdit()
        self.batch_path.setPlaceholderText("Chemin du dossier batch")
        batch_button = QPushButton("Parcourir...")
        batch_button.clicked.connect(self.browse_batch)
        
        batch_layout.addWidget(self.batch_path)
        batch_layout.addWidget(batch_button)
        batch_group.setLayout(batch_layout)
        
        # Source des données
        source_group = QGroupBox("Source des données")
        source_layout = QVBoxLayout()
        
        self.codenet_radio = QRadioButton("Dataset CodeNet")
        self.thestack_radio = QRadioButton("Dataset The Stack")
        self.codenet_radio.setChecked(True)
        
        source_layout.addWidget(self.codenet_radio)
        source_layout.addWidget(self.thestack_radio)
        source_group.setLayout(source_layout)
        
        # Prévisualisation
        preview_group = QGroupBox("Prévisualisation des fichiers")
        preview_layout = QVBoxLayout()
        self.preview_list = QListWidget()
        preview_button = QPushButton("Charger l'aperçu")
        preview_button.clicked.connect(self.load_preview)
        
        preview_layout.addWidget(self.preview_list)
        preview_layout.addWidget(preview_button)
        preview_group.setLayout(preview_layout)
        
        # Bouton d'exécution
        self.execute_button = QPushButton("Compléter le batch")
        self.execute_button.clicked.connect(self.execute_completion)
        
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
        layout.addWidget(batch_group)
        layout.addWidget(source_group)
        layout.addWidget(preview_group)
        layout.addWidget(self.execute_button)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
    
    def browse_batch(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier batch")
        if folder:
            self.batch_path.setText(folder)
    
    def load_preview(self):
        if not self.batch_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier batch.")
            return
        
        # Ici, vous pourriez analyser les fichiers disponibles et les afficher dans la liste
        # Pour simplifier, on va juste simuler quelques fichiers
        self.preview_list.clear()
        
        # Dans une implémentation réelle, vous pourriez:
        # 1. Vérifier les scripts existants dans le batch
        # 2. Comparer avec la source (CodeNet ou The Stack)
        # 3. Lister les fichiers qui seraient ajoutés
        
        self.preview_list.addItem("Fichier original 1.py")
        self.preview_list.addItem("Fichier original 2.py")
        self.preview_list.addItem("Fichier original 3.py")
    
    def execute_completion(self):
        if not self.batch_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier batch.")
            return
        
        cmd = ['python', 'utils/complete_batch.py', self.batch_path.text()]
        
        if self.codenet_radio.isChecked():
            cmd.append('--codenet')
        elif self.thestack_radio.isChecked():
            cmd.append('--thestack')
        
        self.console.clear()
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
    
    def process_finished(self, success, message):
        self.progress_bar.hide()
        self.execute_button.setEnabled(True)
        status = "Succès" if success else "Échec"
        QMessageBox.information(self, status, message)


class MatrixGenerationTab(QWidget):
    """Onglet pour la génération des matrices"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Mode de sélection (fichier unique ou dossier batch)
        mode_group = QGroupBox("Mode de génération")
        mode_layout = QVBoxLayout()
        
        self.file_mode_radio = QRadioButton("Analyser un fichier unique")
        self.dir_mode_radio = QRadioButton("Analyser un dossier batch complet")
        self.file_mode_radio.setChecked(True)
        self.file_mode_radio.toggled.connect(self.toggle_mode)
        self.dir_mode_radio.toggled.connect(self.toggle_mode)
        
        mode_layout.addWidget(self.file_mode_radio)
        mode_layout.addWidget(self.dir_mode_radio)
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
        
        # Sélection du dossier batch
        self.dir_group = QGroupBox("Sélection du dossier batch")
        dir_layout = QVBoxLayout()
        
        dir_select_layout = QHBoxLayout()
        self.dir_path = QLineEdit()
        self.dir_path.setPlaceholderText("Chemin du dossier batch (doit contenir un sous-dossier 'scripts')")
        dir_button = QPushButton("Parcourir...")
        dir_button.clicked.connect(self.browse_directory)
        dir_select_layout.addWidget(self.dir_path)
        dir_select_layout.addWidget(dir_button)
        
        info_label = QLabel("Le script analysera les fichiers Python dans le sous-dossier 'scripts' du dossier sélectionné")
        info_label.setStyleSheet("color: gray;")
        
        dir_layout.addLayout(dir_select_layout)
        dir_layout.addWidget(info_label)
        self.dir_group.setLayout(dir_layout)
        self.dir_group.hide()  # Caché par défaut
        
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
        
        # Options de batch
        batch_group = QGroupBox("Options de batch")
        batch_layout = QVBoxLayout()
        
        self.no_batch_checkbox = QCheckBox("Mode sans batch (une requête par token)")
        
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
        
        batch_layout.addWidget(self.no_batch_checkbox)
        batch_layout.addLayout(batch_size_layout)
        batch_layout.addLayout(poll_layout)
        batch_group.setLayout(batch_layout)
        
        # Répertoire de sortie
        output_group = QGroupBox("Répertoire de sortie")
        output_layout = QHBoxLayout()
        self.output_dir = QLineEdit()
        self.output_dir.setPlaceholderText("Laissez vide pour utiliser le dossier du batch avec sous-dossier 'matrixes'")
        output_button = QPushButton("Parcourir...")
        output_button.clicked.connect(self.browse_output)
        output_layout.addWidget(self.output_dir)
        output_layout.addWidget(output_button)
        output_group.setLayout(output_layout)
        
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
        layout.addWidget(mode_group)
        layout.addWidget(self.file_group)
        layout.addWidget(self.dir_group)
        layout.addWidget(models_group)
        layout.addWidget(batch_group)
        layout.addWidget(output_group)
        layout.addWidget(self.execute_button)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
    
    def toggle_mode(self):
        """Change l'interface en fonction du mode sélectionné"""
        if self.file_mode_radio.isChecked():
            self.file_group.show()
            self.dir_group.hide()
        else:
            self.file_group.hide()
            self.dir_group.show()
    
    def browse_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Sélectionner un script Python", "", "Fichiers Python (*.py)")
        if file:
            self.file_path.setText(file)
    
    def browse_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier batch")
        if folder:
            # Vérifier si le sous-dossier 'scripts' existe
            scripts_dir = os.path.join(folder, "scripts")
            if not os.path.exists(scripts_dir):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"Attention: Le sous-dossier 'scripts' n'existe pas dans {folder}")
                msg.setInformativeText("Le script matrix_generator_classic.py cherchera les fichiers Python dans ce sous-dossier.\nVoulez-vous créer ce sous-dossier maintenant?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                result = msg.exec_()
                
                if result == QMessageBox.Yes:
                    try:
                        os.makedirs(scripts_dir)
                        self.console.append(f"Sous-dossier 'scripts' créé dans {folder}")
                    except Exception as e:
                        self.console.append(f"Erreur lors de la création du sous-dossier: {str(e)}")
            
            self.dir_path.setText(folder)
    
    def browse_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le répertoire de sortie")
        if folder:
            self.output_dir.setText(folder)
    
    def execute_generation(self):
        # Vérifier que les chemins requis sont fournis
        if self.file_mode_radio.isChecked() and not self.file_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un script Python.")
            return
        elif self.dir_mode_radio.isChecked() and not self.dir_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier batch.")
            return
        
        cmd = ['python', 'matrix_generation/matrix_generator.py']
        
        # Paramètres spécifiques au mode
        if self.file_mode_radio.isChecked():
            cmd.extend(['--file', self.file_path.text()])
        else:
            cmd.extend(['--directory', self.dir_path.text()])
        
        # Modèles
        cmd.extend(['--token-model', self.token_model.currentText()])
        cmd.extend(['--pred-model', self.pred_model.currentText()])
        
        # Options de batch
        if self.no_batch_checkbox.isChecked():
            cmd.append('--no-batch')
        
        cmd.extend(['--batch-size', str(self.batch_size.value())])
        cmd.extend(['--poll-interval', str(self.poll_interval.value())])
        
        # Répertoire de sortie (optionnel)
        if self.output_dir.text():
            cmd.extend(['--output-dir', self.output_dir.text()])
        
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
        self.console.append(text)
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
        
        
        # Configuration des tuiles
        tile_group = QGroupBox("Configuration des tuiles")
        tile_layout = QHBoxLayout()
        
        tile_layout.addWidget(QLabel("Lignes:"))
        self.rows_spinbox = QSpinBox()
        self.rows_spinbox.setRange(1, 10)
        self.rows_spinbox.setValue(3)
        tile_layout.addWidget(self.rows_spinbox)
        
        tile_layout.addWidget(QLabel("Colonnes:"))
        self.cols_spinbox = QSpinBox()
        self.cols_spinbox.setRange(1, 10)
        self.cols_spinbox.setValue(3)
        tile_layout.addWidget(self.cols_spinbox)
        
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
        layout.addWidget(tile_group)
        layout.addWidget(self.execute_button)
        layout.addWidget(metadata_group)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
    
    def browse_input(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le batch")
        if folder:
            self.input_dir.setText(folder)

    def execute_tiling(self):
        if not self.input_dir.text():
            QMessageBox.warning(self, "Erreur", "Les dossiers d'entrée et de sortie sont requis.")
            return
        
        cmd = ['python', 'matrix_generation/matrix_tiling.py']
        cmd.append(self.input_dir.text()+"/matrixes")
        cmd.append(self.input_dir.text()+"/tiles")
        cmd.extend(['--taille_tuile', str(self.rows_spinbox.value()), str(self.cols_spinbox.value())])
        
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



class ProcessThread(QThread):
    """Thread pour exécuter le script test_unet.py sans bloquer l'interface"""
    update_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)
    
    def __init__(self, command):
        super().__init__()
        self.command = command
        
    def run(self):
        try:
            process = subprocess.Popen(self.command, 
                                      stdout=subprocess.PIPE, 
                                      stderr=subprocess.STDOUT,
                                      shell=True,
                                      text=True,
                                      bufsize=1)
            
            for line in iter(process.stdout.readline, ''):
                self.update_signal.emit(line.strip())
            
            exit_code = process.wait()
            success = exit_code == 0
            self.finished_signal.emit(success, "Terminé avec succès" if success else f"Échec (code {exit_code})")
        except Exception as e:
            self.update_signal.emit(f"Erreur: {str(e)}")
            self.finished_signal.emit(False, str(e))

class UNetTestingTab(QWidget):
    """Onglet pour le test du modèle U-Net"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
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
        
        mode_layout.addWidget(self.file_mode_radio)
        mode_layout.addWidget(self.dir_mode_radio)
        
        # Sélection de fichier
        file_layout = QHBoxLayout()
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText("Chemin vers le fichier Python à analyser")
        file_button = QPushButton("Parcourir...")
        file_button.clicked.connect(self.browse_file)
        
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(file_button)
        
        # Sélection de dossier
        dir_layout = QHBoxLayout()
        self.dir_path = QLineEdit()
        self.dir_path.setPlaceholderText("Chemin vers le dossier contenant des fichiers Python")
        self.dir_path.setEnabled(False)
        dir_button = QPushButton("Parcourir...")
        dir_button.clicked.connect(self.browse_directory)
        dir_button.setEnabled(False)
        
        self.recursive_checkbox = QCheckBox("Rechercher également dans les sous-dossiers")
        self.recursive_checkbox.setEnabled(False)
        
        dir_layout.addWidget(self.dir_path)
        dir_layout.addWidget(dir_button)
        
        # Instructions pour le glisser-déposer
        drop_label = QLabel("Ou glissez-déposez des fichiers/dossiers ici")
        drop_label.setAlignment(Qt.AlignCenter)
        drop_label.setStyleSheet("background-color: #f0f0f0; padding: 20px; border: 1px dashed #aaa;")
        
        input_layout.addLayout(mode_layout)
        input_layout.addLayout(file_layout)
        input_layout.addLayout(dir_layout)
        input_layout.addWidget(self.recursive_checkbox)
        input_layout.addWidget(drop_label)
        input_group.setLayout(input_layout)
        
        # Activer la fonctionnalité de glisser-déposer
        self.setAcceptDrops(True)
        
        # Bouton d'analyse
        self.test_button = QPushButton("Analyser")
        self.test_button.clicked.connect(self.analyze_code)
        
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
        
        # Visualisation
        viz_group = QGroupBox("Visualisation")
        viz_layout = QVBoxLayout()
        
        # Graphique pour montrer les scores de confiance
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        viz_layout.addWidget(self.canvas)
        
        viz_group.setLayout(viz_layout)
        
        # Console de sortie
        console_group = QGroupBox("Sortie du processus")
        console_layout = QVBoxLayout()
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        
        console_layout.addWidget(self.console)
        console_group.setLayout(console_layout)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indéterminé
        self.progress_bar.hide()
        
        # Construction du layout principal
        layout.addWidget(model_group)
        layout.addWidget(input_group)
        layout.addWidget(self.test_button)
        layout.addWidget(results_group)
        layout.addWidget(details_group)
        layout.addWidget(viz_group)
        layout.addWidget(console_group)
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        # Stockage des résultats
        self.all_results = []
    
    def toggle_mode(self):
        """Change l'interface en fonction du mode sélectionné"""
        if self.file_mode_radio.isChecked():
            self.file_path.setEnabled(True)
            self.dir_path.setEnabled(False)
            self.recursive_checkbox.setEnabled(False)
        else:
            self.file_path.setEnabled(False)
            self.dir_path.setEnabled(True)
            self.recursive_checkbox.setEnabled(True)
    
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
            
            # Vérifier l'extension du fichier
            file_ext = os.path.splitext(self.file_path.text())[1].lower()
            if file_ext not in ['.py', '.npy']:
                QMessageBox.warning(self, "Erreur", "Le fichier doit être au format .py ou .npy")
                return
                
            input_path = self.file_path.text()
        else:
            if not self.dir_path.text() or not os.path.isdir(self.dir_path.text()):
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier valide.")
                return
            input_path = self.dir_path.text()
        
        # Construire la commande pour appeler test_unet.py
        cmd = ['python', 'unet/test_unet.py', '--model', self.model_path.text(), '--input', input_path]
        
        # Ajouter l'option récursive si nécessaire
        if self.dir_mode_radio.isChecked() and self.recursive_checkbox.isChecked():
            cmd.append('--recursive')
        
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
    
    def update_console(self, text):
        """Met à jour la console avec la sortie du script"""
        self.console.append(text)
        
        # Faire défiler vers le bas
        scrollbar = self.console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        
        # Analyser la sortie pour extraire les résultats
        if "Résultat pour:" in text:
            self.parse_result_from_output()
    
    def parse_result_from_output(self):
        """Extrait les informations de résultat de la sortie de la console"""
        text = self.console.toPlainText()
        sections = text.split("=" * 60)
        
        for section in sections:
            if "Résultat pour:" in section and "Prédiction:" in section:
                # C'est une section de résultat
                lines = section.strip().split("\n")
                result = {}
                
                for line in lines:
                    line = line.strip()
                    if line.startswith("Résultat pour:"):
                        result['file'] = line.split("Résultat pour:")[1].strip()
                    elif line.startswith("Classe réelle:"):
                        result['true_class'] = line.split("Classe réelle:")[1].strip()
                    elif line.startswith("Prédiction:"):
                        result['predicted_class'] = line.split("Prédiction:")[1].strip()
                    elif line.startswith("Score brut:"):
                        try:
                            result['score'] = float(line.split("Score brut:")[1].strip())
                        except ValueError:
                            # En cas d'erreur de conversion, utiliser une valeur par défaut
                            result['score'] = 0.5
                    elif line.startswith("Confiance:"):
                        try:
                            confidence_str = line.split("Confiance:")[1].strip()
                            result['confidence'] = float(confidence_str.replace("%", "")) / 100
                        except ValueError:
                            # En cas d'erreur de conversion, utiliser une valeur par défaut
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
                        
                        # Afficher dans la console pour le débogage
                        print(f"Ajout du résultat pour {result['file']} à la liste")
    
    def add_result_to_list(self, result):
        """Ajoute un résultat à la liste des résultats"""
        filename = result['file']
        predicted_class = result['predicted_class']
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
        self.viz_type.addItems(["Matrices", "Tuiles", "Heatmaps", "Activations"])
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
        select_layout = QHBoxLayout()
        
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText("Chemin du fichier ou dossier à visualiser")
        select_button = QPushButton("Parcourir...")
        select_button.clicked.connect(self.browse_file)
        
        select_layout.addWidget(self.file_path)
        select_layout.addWidget(select_button)
        select_group.setLayout(select_layout)
        
        # Bouton de visualisation
        self.visualize_button = QPushButton("Visualiser")
        self.visualize_button.clicked.connect(self.visualize)
        
        # Zone de visualisation
        viz_area_group = QGroupBox("Visualisation")
        viz_area_layout = QVBoxLayout()
        
        # Créer un widget Matplotlib pour l'affichage
        self.figure = Figure(figsize=(6, 5), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        viz_area_layout.addWidget(self.canvas)
        
        viz_area_group.setLayout(viz_area_layout)
        
        # Informations sur la visualisation
        info_group = QGroupBox("Informations")
        info_layout = QVBoxLayout()
        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        info_layout.addWidget(self.info_text)
        info_group.setLayout(info_layout)
        
        # Construction du layout principal
        layout.addWidget(viz_type_group)
        layout.addWidget(self.options_group)
        layout.addWidget(select_group)
        layout.addWidget(self.visualize_button)
        layout.addWidget(viz_area_group)
        layout.addWidget(info_group)
        
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
            # Options pour les matrices
            color_layout = QHBoxLayout()
            color_layout.addWidget(QLabel("Palette de couleurs:"))
            self.colormap = QComboBox()
            self.colormap.addItems(["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool"])
            color_layout.addWidget(self.colormap)
            self.options_layout.addLayout(color_layout)
            
            norm_layout = QHBoxLayout()
            self.normalize_checkbox = QCheckBox("Normaliser les valeurs")
            self.normalize_checkbox.setChecked(True)
            norm_layout.addWidget(self.normalize_checkbox)
            self.options_layout.addLayout(norm_layout)
        
        elif viz_type == "Tuiles":
            # Options pour les tuiles
            grid_layout = QHBoxLayout()
            grid_layout.addWidget(QLabel("Disposition de la grille:"))
            self.grid_rows = QSpinBox()
            self.grid_rows.setRange(1, 10)
            self.grid_rows.setValue(3)
            grid_layout.addWidget(self.grid_rows)
            grid_layout.addWidget(QLabel("x"))
            self.grid_cols = QSpinBox()
            self.grid_cols.setRange(1, 10)
            self.grid_cols.setValue(3)
            grid_layout.addWidget(self.grid_cols)
            self.options_layout.addLayout(grid_layout)
            
            self.show_borders_checkbox = QCheckBox("Afficher les bordures des tuiles")
            self.show_borders_checkbox.setChecked(True)
            self.options_layout.addWidget(self.show_borders_checkbox)
        
        elif viz_type == "Heatmaps":
            # Options pour les heatmaps
            color_layout = QHBoxLayout()
            color_layout.addWidget(QLabel("Palette de couleurs:"))
            self.heatmap_colormap = QComboBox()
            self.heatmap_colormap.addItems(["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool"])
            color_layout.addWidget(self.heatmap_colormap)
            self.options_layout.addLayout(color_layout)
            
            self.show_values_checkbox = QCheckBox("Afficher les valeurs")
            self.show_values_checkbox.setChecked(False)
            self.options_layout.addWidget(self.show_values_checkbox)
        
        elif viz_type == "Activations":
            # Options pour les activations
            layer_layout = QHBoxLayout()
            layer_layout.addWidget(QLabel("Couche:"))
            self.layer_spinbox = QSpinBox()
            self.layer_spinbox.setRange(1, 10)
            self.layer_spinbox.setValue(1)
            layer_layout.addWidget(self.layer_spinbox)
            self.options_layout.addLayout(layer_layout)
            
            filter_layout = QHBoxLayout()
            filter_layout.addWidget(QLabel("Filtre:"))
            self.filter_spinbox = QSpinBox()
            self.filter_spinbox.setRange(1, 64)
            self.filter_spinbox.setValue(1)
            filter_layout.addWidget(self.filter_spinbox)
            self.options_layout.addLayout(filter_layout)
    
    def browse_file(self):
        viz_type = self.viz_type.currentText()
        
        if viz_type in ["Tuiles", "Heatmaps"]:
            # Sélectionner un dossier
            folder = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier")
            if folder:
                self.file_path.setText(folder)
        else:
            # Sélectionner un fichier
            file, _ = QFileDialog.getOpenFileName(self, "Sélectionner un fichier", "", "Tous les fichiers (*)")
            if file:
                self.file_path.setText(file)
    
    def visualize(self):
        if not self.file_path.text():
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un fichier ou dossier.")
            return
        
        viz_type = self.viz_type.currentText()
        
        # Effacer la figure actuelle
        self.figure.clear()
        
        # Simuler différentes visualisations
        if viz_type == "Matrices":
            self.visualize_matrix()
        elif viz_type == "Tuiles":
            self.visualize_tiles()
        elif viz_type == "Heatmaps":
            self.visualize_heatmap()
        elif viz_type == "Activations":
            self.visualize_activations()
        
        # Mettre à jour le canvas
        self.canvas.draw()
    
    def visualize_matrix(self):
        # Simuler l'affichage d'une matrice
        import numpy as np
        
        # Dans une implémentation réelle, vous chargeriez la matrice depuis le fichier
        # Pour la simulation, on génère une matrice aléatoire
        matrix = np.random.rand(20, 20)
        
        ax = self.figure.add_subplot(111)
        cmap = self.colormap.currentText()
        normalize = self.normalize_checkbox.isChecked()
        
        if normalize:
            im = ax.imshow(matrix, cmap=cmap)
        else:
            im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=1)
        
        ax.set_title("Matrice de similarité")
        self.figure.colorbar(im)
        
        self.info_text.clear()
        self.info_text.append(f"Fichier: {self.file_path.text()}")
        self.info_text.append(f"Dimensions: {matrix.shape[0]}x{matrix.shape[1]}")
        self.info_text.append(f"Min: {matrix.min():.4f}, Max: {matrix.max():.4f}")
        self.info_text.append(f"Moyenne: {matrix.mean():.4f}, Écart-type: {matrix.std():.4f}")
    
    def visualize_tiles(self):
        # Simuler l'affichage d'une grille de tuiles
        import numpy as np
        
        rows = self.grid_rows.value()
        cols = self.grid_cols.value()
        show_borders = self.show_borders_checkbox.isChecked()
        
        # Créer un ensemble de tuiles simulées
        tiles = [np.random.rand(3, 3) for _ in range(rows * cols)]
        
        # Afficher les tuiles dans une grille
        for i in range(min(rows * cols, len(tiles))):
            ax = self.figure.add_subplot(rows, cols, i+1)
            im = ax.imshow(tiles[i], cmap="viridis")
            ax.set_title(f"Tuile {i+1}")
            ax.set_xticks([])
            ax.set_yticks([])
            
            if show_borders:
                ax.set_frame_on(True)
            else:
                ax.set_frame_on(False)
        
        self.figure.tight_layout()
        
        self.info_text.clear()
        self.info_text.append(f"Dossier: {self.file_path.text()}")
        self.info_text.append(f"Nombre de tuiles affichées: {min(rows * cols, len(tiles))}")
        self.info_text.append(f"Dimensions des tuiles: 3x3")
    
    def visualize_heatmap(self):
        # Simuler l'affichage d'une heatmap
        import numpy as np
        
        # Générer des données simulées
        data = np.random.rand(10, 10)
        
        ax = self.figure.add_subplot(111)
        cmap = self.heatmap_colormap.currentText()
        show_values = self.show_values_checkbox.isChecked()
        
        im = ax.imshow(data, cmap=cmap)
        ax.set_title("Heatmap")
        
        # Ajouter les étiquettes des axes
        ax.set_xticks(range(10))
        ax.set_yticks(range(10))
        ax.set_xticklabels([f"X{i+1}" for i in range(10)])
        ax.set_yticklabels([f"Y{i+1}" for i in range(10)])
        
        # Afficher les valeurs dans les cellules si demandé
        if show_values:
            for i in range(10):
                for j in range(10):
                    text = ax.text(j, i, f"{data[i, j]:.2f}",
                                  ha="center", va="center", 
                                  color="white" if data[i, j] > 0.5 else "black",
                                  fontsize=8)
        
        self.figure.colorbar(im)
        
        self.info_text.clear()
        self.info_text.append(f"Dossier: {self.file_path.text()}")
        self.info_text.append(f"Dimensions: 10x10")
        self.info_text.append(f"Min: {data.min():.4f}, Max: {data.max():.4f}")
        self.info_text.append(f"Moyenne: {data.mean():.4f}")
    
    def visualize_activations(self):
        # Simuler l'affichage des activations d'un modèle
        import numpy as np
        
        layer = self.layer_spinbox.value()
        filter_num = self.filter_spinbox.value()
        
        # Générer des activations simulées (16x16)
        activation = np.random.rand(16, 16)
        
        ax = self.figure.add_subplot(111)
        im = ax.imshow(activation, cmap="viridis")
        ax.set_title(f"Activation de la couche {layer}, filtre {filter_num}")
        self.figure.colorbar(im)
        
        self.info_text.clear()
        self.info_text.append(f"Modèle: {self.file_path.text()}")
        self.info_text.append(f"Couche: {layer}")
        self.info_text.append(f"Filtre: {filter_num}")
        self.info_text.append(f"Dimensions: {activation.shape[0]}x{activation.shape[1]}")
        self.info_text.append(f"Activation minimale: {activation.min():.4f}")
        self.info_text.append(f"Activation maximale: {activation.max():.4f}")
        self.info_text.append(f"Activation moyenne: {activation.mean():.4f}")


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Pipeline de Traitement de Code")
        self.setGeometry(100, 100, 1200, 800)
        
        # Créer les onglets
        self.tabs = QTabWidget()
        
        # Ajouter chaque onglet
        self.scripts_generator_tab = ScriptsGeneratorTab()
        self.tabs.addTab(self.scripts_generator_tab, "Génération de Scripts")
        
        self.batch_manager_tab = BatchManagerTab()
        self.tabs.addTab(self.batch_manager_tab, "Gestion des Batches")
        
        self.batch_completion_tab = BatchCompletionTab()
        self.tabs.addTab(self.batch_completion_tab, "Complétion des Batches")
        
        self.matrix_generation_tab = MatrixGenerationTab()
        self.tabs.addTab(self.matrix_generation_tab, "Génération des Matrices")
        
        self.matrix_tiling_tab = MatrixTilingTab()
        self.tabs.addTab(self.matrix_tiling_tab, "Génération des Tuiles")
        
        self.unet_training_tab = UNetTrainingTab()
        self.tabs.addTab(self.unet_training_tab, "Entraînement U-Net")
        
        self.unet_testing_tab = UNetTestingTab()
        self.tabs.addTab(self.unet_testing_tab, "Test U-Net")
        
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