import sys
import os
# ATTENTION: Ce script doit être exécuté depuis la racine du projet
# pour que les chemins relatifs vers les autres scripts fonctionnent correctement.
# Exemple: python "Model User/user_interface.py"

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


class MainWindow(QMainWindow):
    """Fenêtre principale de l'application utilisateur"""
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Cassiopée - Interface Utilisateur")
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget central et layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Onglets
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Ajout des onglets (à implémenter)
        self.unet_testing_tab = UNetTestingTab()
        self.visualization_tab = VisualizationTab()
        
        self.tabs.addTab(self.unet_testing_tab, "Analyse de code (U-Net)")
        self.tabs.addTab(self.visualization_tab, "Visualisation")

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
        
        # API Configuration
        api_group = QGroupBox("Configuration de l'API pour la génération de matrice")
        api_layout = QVBoxLayout()

        # Model Name
        model_name_layout = QHBoxLayout()
        model_name_layout.addWidget(QLabel("Nom du Modèle LLM:"))
        self.model_name_input = QLineEdit("gpt-4o-mini")
        self.model_name_input.setPlaceholderText("ex: gpt-4o-mini, llama3, codellama")
        model_name_layout.addWidget(self.model_name_input)
        api_layout.addLayout(model_name_layout)

        # API Type Selection
        api_type_layout = QHBoxLayout()
        self.openai_radio = QRadioButton("API OpenAI")
        self.local_llm_radio = QRadioButton("LLM Local")
        self.openai_radio.setChecked(True)
        api_type_layout.addWidget(self.openai_radio)
        api_type_layout.addWidget(self.local_llm_radio)
        
        self.openai_radio.toggled.connect(self.toggle_api_options)

        # OpenAI API Key
        self.openai_key_widget = QWidget()
        openai_key_layout = QHBoxLayout(self.openai_key_widget)
        openai_key_layout.setContentsMargins(0, 0, 0, 0)
        openai_key_layout.addWidget(QLabel("Clé API OpenAI:"))
        self.openai_api_key = QLineEdit()
        self.openai_api_key.setPlaceholderText("Entrez votre clé API OpenAI (ou laissez vide si la variable d'environnement est définie)")
        self.openai_api_key.setEchoMode(QLineEdit.Password)
        openai_key_layout.addWidget(self.openai_api_key)

        # Local LLM URL
        self.local_llm_widget = QWidget()
        local_llm_layout = QHBoxLayout(self.local_llm_widget)
        local_llm_layout.setContentsMargins(0, 0, 0, 0)
        local_llm_layout.addWidget(QLabel("URL du LLM Local:"))
        self.local_llm_url = QLineEdit()
        self.local_llm_url.setPlaceholderText("ex: http://localhost:11434/v1")
        local_llm_layout.addWidget(self.local_llm_url)
        self.local_llm_widget.setVisible(False) # Initially hidden

        api_layout.addLayout(api_type_layout)
        api_layout.addWidget(self.openai_key_widget)
        api_layout.addWidget(self.local_llm_widget)
        api_group.setLayout(api_layout)
        
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
        upper_layout.addWidget(api_group)
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
        
        # Activer/désactiver les widgets appropriés
        self.file_path.setEnabled(is_file_mode)
        self.file_button.setEnabled(is_file_mode)
        self.dir_path.setEnabled(not is_file_mode)
        self.dir_button.setEnabled(not is_file_mode)
    
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
            self.toggle_mode()
        elif os.path.isdir(path):
            # C'est un dossier
            self.dir_mode_radio.setChecked(True)
            self.dir_path.setText(path)
            self.toggle_mode()

    def toggle_api_options(self):
        """Affiche/masque les options en fonction du type d'API sélectionné."""
        use_openai = self.openai_radio.isChecked()
        self.openai_key_widget.setVisible(use_openai)
        self.local_llm_widget.setVisible(not use_openai)

    def analyze_code(self):
        """Lance l'analyse du code source"""
        model_path = self.model_path.text()
        model_name = self.model_name_input.text()
        
        if not model_path:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un modèle.")
            return
            
        if self.file_mode_radio.isChecked():
            target_path = self.file_path.text()
            if not target_path:
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un fichier.")
                return
            command_arg = f'--file "{target_path}"'
        else:
            target_path = self.dir_path.text()
            if not target_path:
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier.")
                return
            command_arg = f'--directory "{target_path}"'
            
        # API arguments
        api_args = ""
        if self.openai_radio.isChecked():
            api_key = self.openai_api_key.text()
            if api_key:
                api_args = f'--api_key "{api_key}"'
        else: # Local LLM
            local_url = self.local_llm_url.text()
            if not local_url:
                QMessageBox.warning(self, "Erreur", "Veuillez entrer l'URL de l'API du LLM local.")
                return
            api_args = f'--local_api_url "{local_url}"'
            
        # Construire la commande
        # Note: le script test_unet.py doit être dans le path ou spécifié
        command = f'python unet/test_unet.py --model "{model_path}" --pred_model "{model_name}" --token_model "{model_name}" {command_arg} {api_args}'
        
        viz_output_dir = self.viz_output_dir.text()
        if self.visualize_tiles_checkbox.isChecked():
            command += f' --visualize_tiles'
            if viz_output_dir:
                command += f' --output_dir_tiles "{viz_output_dir}"'

        if self.visualize_activations_checkbox.isChecked():
            command += f' --visualize_activations'
            if viz_output_dir:
                command += f' --output_dir_activations "{viz_output_dir}"'

        # Exécution dans un thread
        self.console.clear()
        self.details_text.clear()
        self.results_list.clear()
        self.figure.clear()
        self.canvas.draw()
        
        self.progress_bar.show()
        
        self.thread = ProcessThread(command)
        self.thread.update_signal.connect(self.update_console)
        self.thread.finished_signal.connect(self.analysis_finished)
        self.thread.start()

    def update_console(self, text):
        """Met à jour la console de sortie"""
        self.console.append(text)
        self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())
        QApplication.processEvents() # Pour garder l'UI réactive

    def parse_result_from_output(self):
        """Extrait les résultats JSON de la sortie console"""
        console_text = self.console.toPlainText()
        results = []
        
        # Chercher les lignes qui contiennent le JSON
        for line in console_text.splitlines():
            if line.startswith("ANALYSIS_RESULT:"):
                try:
                    json_str = line.replace("ANALYSIS_RESULT:", "").strip()
                    results.append(json.loads(json_str))
                except json.JSONDecodeError:
                    print(f"Erreur de décodage JSON pour: {line}")
                    
        return results

    def add_result_to_list(self, result):
        """Ajoute un résultat à la liste des résultats"""
        file_path = result.get('file_path', 'Fichier inconnu')
        rebuilt_percentage = result.get('rebuilt_percentage', 0)
        
        item_text = f"{os.path.basename(file_path)} - {rebuilt_percentage:.2f}% reconstruit"
        list_item = QListWidgetItem(item_text)
        list_item.setData(Qt.UserRole, result) # Stocker le dict complet
        
        # Coloration en fonction du pourcentage
        if rebuilt_percentage > 80:
            list_item.setForeground(Qt.darkGreen)
        elif rebuilt_percentage > 50:
            list_item.setForeground(Qt.darkYellow)
        else:
            list_item.setForeground(Qt.red)
            
        self.results_list.addItem(list_item)

    def show_result_details(self, item):
        """Affiche les détails d'un résultat sélectionné"""
        result = item.data(Qt.UserRole)
        
        details = f"Chemin: {result.get('file_path')}\n"
        details += f"Pourcentage reconstruit: {result.get('rebuilt_percentage', 0):.2f}%\n"
        details += f"Perte: {result.get('loss', 'N/A')}\n"
        
        # Afficher les métriques
        if 'metrics' in result:
            details += "\n--- Métriques ---\n"
            for key, value in result['metrics'].items():
                details += f"{key}: {value}\n"
        
        # Afficher les erreurs
        if 'error' in result:
            details += f"\nErreur: {result['error']}\n"
            
        self.details_text.setText(details)
        
        # Mettre à jour la visualisation
        self.update_visualization(result)

    def update_visualization(self, result):
        """Met à jour le canvas de visualisation"""
        self.figure.clear()
        
        # Chercher les chemins des images de visualisation dans les résultats
        tile_img_path = result.get('visualization_paths', {}).get('tiles')
        activation_img_path = result.get('visualization_paths', {}).get('activations')

        # Décider quelle image afficher
        img_path_to_show = tile_img_path or activation_img_path
        
        if img_path_to_show and os.path.exists(img_path_to_show):
            try:
                img = plt.imread(img_path_to_show)
                ax = self.figure.add_subplot(111)
                ax.imshow(img)
                ax.axis('off')
                ax.set_title(os.path.basename(img_path_to_show))
            except Exception as e:
                ax = self.figure.add_subplot(111)
                ax.text(0.5, 0.5, f"Erreur de chargement de l'image:\n{e}", ha='center', va='center')
                ax.axis('off')
        else:
            # Si aucune image n'est disponible, afficher un message
            ax = self.figure.add_subplot(111)
            ax.text(0.5, 0.5, "Aucune visualisation disponible", ha='center', va='center')
            ax.axis('off')
            
        self.canvas.draw()

    def analysis_finished(self, success, message):
        """Gère la fin du processus d'analyse"""
        self.progress_bar.hide()
        QMessageBox.information(self, "Terminé", message)
        
        if success:
            # Extraire les résultats de la console
            self.all_results = self.parse_result_from_output()
            
            # Mettre à jour la liste des résultats
            self.results_list.clear()
            for res in self.all_results:
                self.add_result_to_list(res)
                
            # Sélectionner le premier élément par défaut
            if self.results_list.count() > 0:
                self.results_list.setCurrentRow(0)
                self.show_result_details(self.results_list.item(0))

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
                    btn.setText("Sélectionacter")
            
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
                cmd.extend(['--output_dir', self.output_dir.text()])
                
            # Exécuter la commande dans un thread
            self.thread = ProcessThread(" ".join(cmd))
            self.thread.update_signal.connect(self.update_output)
            self.thread.finished_signal.connect(self.process_finished)
            self.thread.start()
            
        elif viz_type == "Activations":
            if not self.model_path.text():
                QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un modèle UNet.")
                self.progress_bar.hide()
                self.visualize_button.setEnabled(True)
                return

            cmd = [
                'python', 'visualization/visualize_activation.py',
                '--model_path', self.model_path.text(),
                '--input_path', self.file_path.text(),
                '--output_dir', self.activation_output_dir.text(),
                '--device', self.device_combo.currentText(),
                '--padding_value', self.padding_value.text()
            ]

            if self.matrix_id.text():
                cmd.extend(['--matrix_id', self.matrix_id.text()])
            
            self.thread = ProcessThread(" ".join(cmd))
            self.thread.update_signal.connect(self.update_output)
            self.thread.finished_signal.connect(self.process_finished)
            self.thread.start()

    def update_output(self, text):
        """Met à jour le champ de texte de sortie"""
        self.output_text.append(text)
        self.output_text.verticalScrollBar().setValue(self.output_text.verticalScrollBar().maximum())
        QApplication.processEvents()

    def process_finished(self, success, message):
        """Gère la fin du processus de visualisation"""
        self.progress_bar.hide()
        self.visualize_button.setEnabled(True)
        
        if success:
            QMessageBox.information(self, "Succès", "Visualisation terminée.")
        else:
            QMessageBox.critical(self, "Erreur", f"Le processus a échoué: {message}")

def main():
    # Créer le dossier s'il n'existe pas
    if not os.path.exists("Model User"):
        os.makedirs("Model User")
        
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 