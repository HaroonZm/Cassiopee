import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import os
import glob
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# Définition d'un Dataset personnalisé pour les matrices
class CodeMatrixDataset(Dataset):
    def __init__(self, matrices, labels):
        self.matrices = matrices
        self.labels = labels
        
    def __len__(self):
        return len(self.matrices)
    
    def __getitem__(self, idx):
        matrix = self.matrices[idx]
        label = self.labels[idx]
        
        # Conversion en tenseur PyTorch et ajout de la dimension de canal
        matrix_tensor = torch.tensor(matrix, dtype=torch.float32).unsqueeze(0)
        label_tensor = torch.tensor(label, dtype=torch.float32)
        
        return matrix_tensor, label_tensor

# Architecture UNet modifiée pour gérer les dimensions asymétriques
class UNetForCodeDetection(nn.Module):
    def __init__(self):
        super(UNetForCodeDetection, self).__init__()
        # Encoder
        self.enc1 = self.conv_block(1, 64)
        self.enc2 = self.conv_block(64, 128)
        self.enc3 = self.conv_block(128, 256)
        self.enc4 = self.conv_block(256, 512)
        
        # Decoder
        self.upconv3 = nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2)
        self.dec3 = self.conv_block(512, 256)
        
        self.upconv2 = nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2)
        self.dec2 = self.conv_block(256, 128)
        
        self.upconv1 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.dec1 = self.conv_block(128, 64)
        
        # Classification head
        self.final_conv = nn.Conv2d(64, 32, kernel_size=1)
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )
        
        # Max pooling
        self.pool = nn.MaxPool2d(2)
        
    def conv_block(self, in_ch, out_ch):
        return nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True)
        )
    
    def forward(self, x):
        # Encoder
        e1 = self.enc1(x)
        p1 = self.pool(e1)
        
        e2 = self.enc2(p1)
        p2 = self.pool(e2)
        
        e3 = self.enc3(p2)
        p3 = self.pool(e3)
        
        # Bottleneck
        e4 = self.enc4(p3)
        
        # Decoder avec gestion des dimensions
        d3 = self.upconv3(e4)
        # Vérifier et ajuster les dimensions si nécessaire
        if d3.size() != e3.size():
            d3 = F.interpolate(d3, size=e3.size()[2:], mode='bilinear', align_corners=True)
        d3 = torch.cat([d3, e3], dim=1)
        d3 = self.dec3(d3)
        
        d2 = self.upconv2(d3)
        # Vérifier et ajuster les dimensions si nécessaire
        if d2.size() != e2.size():
            d2 = F.interpolate(d2, size=e2.size()[2:], mode='bilinear', align_corners=True)
        d2 = torch.cat([d2, e2], dim=1)
        d2 = self.dec2(d2)
        
        d1 = self.upconv1(d2)
        # Vérifier et ajuster les dimensions si nécessaire
        if d1.size() != e1.size():
            d1 = F.interpolate(d1, size=e1.size()[2:], mode='bilinear', align_corners=True)
        d1 = torch.cat([d1, e1], dim=1)
        d1 = self.dec1(d1)
        
        # Classification
        x = self.final_conv(d1)
        output = self.classifier(x)
        return output

# Fonction pour charger les matrices et les étiquettes
def load_data_from_folder(folder_path):
    matrices = []
    labels = []
    
    # Charger les fichiers .npy du dossier
    matrix_files = glob.glob(os.path.join(folder_path, "*.npy"))
    
    print(f"Chargement de {len(matrix_files)} fichiers...")
    for file_path in tqdm(matrix_files):
        try:
            # Chargement de la matrice
            matrix = np.load(file_path)
            
            # Déterminer l'étiquette selon la convention de nommage spécifiée
            filename = os.path.basename(file_path).lower()
            if "var" in filename:
                label = 1.0  # Code généré par IA
            elif "gen" in filename:
                label = 1.0  # Code généré par IA
            elif "human" in filename:
                label = 0.0  # Code écrit par humain
            else:
                print(f"Convention de nommage non reconnue pour {file_path}, ignoré")
                continue
            
            # Remplacer les valeurs -inf ou NaN par une valeur numérique
            matrix = np.nan_to_num(matrix, neginf=-100.0)
            
            # Normalisation min-max pour ramener entre 0 et 1
            min_val = np.min(matrix)
            max_val = np.max(matrix)
            if max_val > min_val:  # Éviter la division par zéro
                matrix = (matrix - min_val) / (max_val - min_val)
            
            matrices.append(matrix)
            labels.append(label)
        except Exception as e:
            print(f"Erreur lors du chargement de {file_path}: {e}")
    
    return matrices, labels

# Fonction d'entraînement
def train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs=10, device='cuda'):
    model.to(device)
    best_val_acc = 0.0
    
    for epoch in range(num_epochs):
        # Mode entraînement
        model.train()
        train_loss = 0.0
        train_correct = 0
        train_total = 0
        
        for inputs, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Training"):
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Forward pass
            optimizer.zero_grad()
            outputs = model(inputs).squeeze()
            loss = criterion(outputs, labels)
            
            # Backward pass
            loss.backward()
            optimizer.step()
            
            # Statistiques
            train_loss += loss.item() * inputs.size(0)
            predictions = (outputs > 0.5).float()
            train_correct += (predictions == labels).sum().item()
            train_total += labels.size(0)
        
        train_loss = train_loss / len(train_loader.dataset)
        train_acc = train_correct / train_total
        
        # Mode évaluation
        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0
        
        with torch.no_grad():
            for inputs, labels in tqdm(val_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Validation"):
                inputs, labels = inputs.to(device), labels.to(device)
                
                # Forward pass
                outputs = model(inputs).squeeze()
                loss = criterion(outputs, labels)
                
                # Statistiques
                val_loss += loss.item() * inputs.size(0)
                predictions = (outputs > 0.5).float()
                val_correct += (predictions == labels).sum().item()
                val_total += labels.size(0)
        
        val_loss = val_loss / len(val_loader.dataset)
        val_acc = val_correct / val_total
        
        print(f"Epoch {epoch+1}/{num_epochs} - "
              f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}, "
              f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
        
        # Sauvegarde du meilleur modèle
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_unet_code_detector.pth')
            print(f"Model saved with validation accuracy: {val_acc:.4f}")
    
    return model

# Fonction principale
def main():
    # Paramètres
    data_folder = "matrixes_test"  # Votre dossier spécifique
    batch_size = 4  # Réduit pour éviter les problèmes de mémoire avec de petits datasets
    num_epochs = 20
    learning_rate = 0.001
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    print(f"Utilisation de: {device}")
    
    # Chargement des données
    print("Chargement des données...")
    matrices, labels = load_data_from_folder(data_folder)
    
    # Vérification du nombre d'exemples par classe
    num_ia = sum([1 for label in labels if label == 1.0])
    num_human = sum([1 for label in labels if label == 0.0])
    print(f"Données chargées: {len(matrices)} matrices au total")
    print(f"  - Code IA: {num_ia} exemples")
    print(f"  - Code humain: {num_human} exemples")
    
    # Division train/test
    print("Division des données en ensembles d'entraînement et de validation...")
    X_train, X_val, y_train, y_val = train_test_split(matrices, labels, test_size=0.2, random_state=42, stratify=labels)
    
    # Création des datasets et dataloaders
    train_dataset = CodeMatrixDataset(X_train, y_train)
    val_dataset = CodeMatrixDataset(X_val, y_val)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)
    
    print(f"Ensemble d'entraînement: {len(X_train)} exemples")
    print(f"Ensemble de validation: {len(X_val)} exemples")
    
    # Initialisation du modèle, de la fonction de perte et de l'optimiseur
    model = UNetForCodeDetection()
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # Entraînement du modèle
    print(f"Début de l'entraînement...")
    model = train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs, device)
    
    print("Entraînement terminé!")

if __name__ == "__main__":
    main()