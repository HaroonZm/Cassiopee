import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.integrate import quad

def gaussian_pdf(x, mu=0, sigma=1):
    """Fonction de densité de probabilité pour une distribution gaussienne."""
    return stats.norm.pdf(x, mu, sigma)

def calculate_representation_levels(thresholds, pdf_func, x_min, x_max):
    """Calcule les niveaux de représentation optimaux selon les seuils de décision."""
    levels = []
    
    # Pour le premier niveau (de x_min au premier seuil)
    def integrand_num(x):
        return x * pdf_func(x)
    
    def integrand_denom(x):
        return pdf_func(x)
    
    # Ajouter x_min comme premier seuil pour simplifier la boucle
    all_thresholds = [x_min] + thresholds + [x_max]
    
    # Calculer chaque niveau comme le centroïde de sa région
    for i in range(len(all_thresholds) - 1):
        a, b = all_thresholds[i], all_thresholds[i + 1]
        
        # Intégration numérique pour le numérateur et le dénominateur
        numerator, _ = quad(integrand_num, a, b)
        denominator, _ = quad(integrand_denom, a, b)
        
        # Éviter la division par zéro
        if denominator < 1e-10:
            level = (a + b) / 2  # Utiliser le milieu si la probabilité est très faible
        else:
            level = numerator / denominator
            
        levels.append(level)
        
    return levels

def calculate_thresholds(levels):
    """Calcule les seuils de décision optimaux selon les niveaux de représentation."""
    return [(levels[i] + levels[i + 1]) / 2 for i in range(len(levels) - 1)]

def calculate_mse(levels, thresholds, pdf_func, x_min, x_max):
    """Calcule l'erreur quadratique moyenne (EQM) pour la quantification."""
    all_thresholds = [x_min] + thresholds + [x_max]
    mse = 0
    
    for i, level in enumerate(levels):
        a, b = all_thresholds[i], all_thresholds[i + 1]
        
        def squared_error(x):
            return (x - level)**2 * pdf_func(x)
        
        error, _ = quad(squared_error, a, b)
        mse += error
        
    return mse

def lloyd_max_algorithm(n_levels, pdf_func, x_min, x_max, max_iterations=100, tolerance=1e-6):
    """Implémentation de l'algorithme de Lloyd-Max."""
    # Initialisation des niveaux de représentation uniformément
    initial_levels = np.linspace(x_min, x_max, n_levels)
    levels = initial_levels
    
    history = [{'levels': levels.copy(), 'thresholds': None, 'mse': None}]
    
    for iteration in range(max_iterations):
        # Étape 1: Calculer les seuils de décision
        thresholds = calculate_thresholds(levels)
        
        # Étape 2: Mettre à jour les niveaux de représentation
        new_levels = calculate_representation_levels(thresholds, pdf_func, x_min, x_max)
        
        # Calculer l'erreur quadratique moyenne
        mse = calculate_mse(new_levels, thresholds, pdf_func, x_min, x_max)
        
        # Sauvegarder l'état actuel pour visualisation
        history.append({
            'levels': new_levels.copy(),
            'thresholds': thresholds.copy(),
            'mse': mse
        })
        
        # Vérifier la convergence
        if np.all(np.abs(np.array(new_levels) - np.array(levels)) < tolerance):
            print(f"Convergence atteinte après {iteration + 1} itérations")
            break
            
        levels = new_levels
        
        if iteration == max_iterations - 1:
            print("Nombre maximum d'itérations atteint sans convergence")
    
    return levels, thresholds, history

def uniform_quantizer(n_levels, x_min, x_max):
    """Crée un quantificateur uniforme pour comparaison."""
    levels = np.linspace(x_min, x_max, n_levels)
    thresholds = [(levels[i] + levels[i + 1]) / 2 for i in range(len(levels) - 1)]
    return levels, thresholds

def plot_quantization_results(pdf_func, x_min, x_max, lloyd_levels, lloyd_thresholds, 
                              uniform_levels, uniform_thresholds, history):
    """Visualise les résultats de la quantification."""
    x = np.linspace(x_min, x_max, 1000)
    y = [pdf_func(xi) for xi in x]
    
    # Créer une figure avec 2 sous-graphiques
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Graphique 1: Distribution et niveaux de quantification
    ax1.plot(x, y, 'b-', label='Distribution gaussienne')
    
    # Tracer les niveaux de Lloyd-Max
    for level in lloyd_levels:
        ax1.axvline(x=level, color='r', linestyle='-', alpha=0.5)
    
    # Tracer les seuils de Lloyd-Max
    for threshold in lloyd_thresholds:
        ax1.axvline(x=threshold, color='r', linestyle='--', alpha=0.3)
    
    # Tracer les niveaux uniformes pour comparaison
    for level in uniform_levels:
        ax1.axvline(x=level, color='g', linestyle='-', alpha=0.5)
    
    # Tracer les seuils uniformes pour comparaison
    for threshold in uniform_thresholds:
        ax1.axvline(x=threshold, color='g', linestyle='--', alpha=0.3)
    
    ax1.set_title('Distribution gaussienne avec niveaux de quantification')
    ax1.set_xlabel('Valeur')
    ax1.set_ylabel('Densité de probabilité')
    ax1.legend(['Distribution gaussienne', 
                'Niveaux Lloyd-Max', 'Seuils Lloyd-Max',
                'Niveaux uniformes', 'Seuils uniformes'])
    
    # Graphique 2: Évolution de l'erreur MSE
    iterations = range(len(history) - 1)
    mse_values = [entry['mse'] for entry in history[1:]]  # Ignorer la première entrée sans MSE
    
    ax2.plot(iterations, mse_values, 'ro-')
    ax2.set_title('Évolution de l\'erreur quadratique moyenne (EQM)')
    ax2.set_xlabel('Itération')
    ax2.set_ylabel('EQM')
    ax2.grid(True)
    
    plt.tight_layout()
    return fig

def main():
    # Paramètres de la distribution gaussienne
    mu = 0
    sigma = 1
    
    # Limites pour la quantification (±4 sigma couvre 99.99% de la distribution)
    x_min = mu - 4 * sigma
    x_max = mu + 4 * sigma
    
    # Nombre de niveaux de quantification
    n_levels = 8
    
    # Fonction de densité de probabilité gaussienne
    pdf_func = lambda x: gaussian_pdf(x, mu, sigma)
    
    # Appliquer l'algorithme de Lloyd-Max
    lloyd_levels, lloyd_thresholds, history = lloyd_max_algorithm(
        n_levels, pdf_func, x_min, x_max, max_iterations=50, tolerance=1e-6
    )
    
    # Créer un quantificateur uniforme pour comparaison
    uniform_levels, uniform_thresholds = uniform_quantizer(n_levels, x_min, x_max)
    
    # Calculer l'EQM pour le quantificateur uniforme
    uniform_mse = calculate_mse(uniform_levels, uniform_thresholds, pdf_func, x_min, x_max)
    
    # Calculer l'EQM pour le quantificateur Lloyd-Max
    lloyd_mse = calculate_mse(lloyd_levels, lloyd_thresholds, pdf_func, x_min, x_max)
    
    # Afficher les résultats
    print("\nRésultats finaux")
    print("-" * 50)
    print(f"Niveaux Lloyd-Max: {lloyd_levels}")
    print(f"Seuils Lloyd-Max: {lloyd_thresholds}")
    print(f"EQM Lloyd-Max: {lloyd_mse:.6f}")
    print("-" * 50)
    print(f"Niveaux quantification uniforme: {uniform_levels}")
    print(f"Seuils quantification uniforme: {uniform_thresholds}")
    print(f"EQM quantification uniforme: {uniform_mse:.6f}")
    print(f"Amélioration: {(uniform_mse - lloyd_mse) / uniform_mse * 100:.2f}%")
    
    # Visualiser les résultats
    fig = plot_quantization_results(pdf_func, x_min, x_max, lloyd_levels, lloyd_thresholds, 
                             uniform_levels, uniform_thresholds, history)
    plt.show()

if __name__ == "__main__":
    main()