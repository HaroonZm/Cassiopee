# Interface Utilisateur de Cassiopée

Cette interface graphique est une version simplifiée de l'application principale, conçue pour les utilisateurs finaux du projet Cassiopée.

## Fonctionnalités

L'interface utilisateur fournit deux fonctionnalités principales :

1.  **Analyse de code (U-Net)** : Cet onglet permet d'analyser des fichiers ou des dossiers de code Python à l'aide d'un modèle U-Net entraîné pour déterminer leur "part d'IA".
2.  **Visualisation** : Cet onglet permet de visualiser les matrices de caractéristiques (`.npy`) ou les cartes d'activation générées par le modèle.

## Comment lancer l'interface

Pour lancer l'interface utilisateur, exécutez la commande suivante depuis la **racine du projet** :

```bash
python "Model User/user_interface.py"
```

**Important** : Il est crucial de lancer le script depuis la racine du projet pour que les chemins vers les différents scripts et modèles soient correctement résolus.

## Configuration de l'API pour l'analyse

Pour analyser un fichier Python, le script doit d'abord le transformer en une "matrice de caractéristiques". Cette étape nécessite un Grand Modèle de Langage (LLM). Vous avez deux options :

1.  Utiliser l'API payante d'OpenAI.
2.  Utiliser un LLM qui tourne gratuitement sur votre propre ordinateur (recommandé).

### Option 1 : Utiliser l'API OpenAI

1.  **Obtenez une clé API** : Connectez-vous à votre compte OpenAI et créez une clé API.
2.  **Lancez l'interface** et allez dans l'onglet "Analyse de code (U-Net)".
3.  **Configurez l'API** :
    *   **Nom du Modèle LLM** : Laissez `gpt-4o-mini` ou choisissez un autre modèle OpenAI.
    *   Cochez l'option **"API OpenAI"**.
    *   Collez votre clé dans le champ **"Clé API OpenAI"**.

### Option 2 : Utiliser un LLM en Local avec Ollama (Recommandé)

Cette option est gratuite et plus privée.

**Étape 1 : Installer Ollama**

1.  Rendez-vous sur **[https://ollama.com](https://ollama.com)** et téléchargez l'application pour votre système d'exploitation.
2.  Installez-la. Un serveur sera lancé en arrière-plan sur votre machine.

**Étape 2 : Télécharger un modèle de code**

1.  Ouvrez un terminal (PowerShell, Terminal, etc.).
2.  Exécutez la commande suivante pour télécharger un modèle spécialisé pour le code. C'est le plus performant pour notre usage :
    ```bash
    ollama run codellama
    ```
3.  Attendez la fin du téléchargement. Vous pouvez vérifier les modèles installés avec `ollama list`.

**Étape 3 : Configurer l'interface**

1.  Lancez l'interface et allez dans l'onglet "Analyse de code (U-Net)".
2.  **Configurez l'API** :
    *   **Nom du Modèle LLM** : Entrez le nom exact du modèle téléchargé, par exemple `codellama`.
    *   Cochez l'option **"LLM Local"**.
    *   **URL du LLM Local** : Laissez la valeur par défaut `http://localhost:11434/v1`, qui est celle utilisée par Ollama.

Votre environnement est prêt ! Vous pouvez maintenant analyser des fichiers en utilisant la puissance de calcul de votre propre ordinateur. 