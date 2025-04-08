# Prédiction des Arrêts de Protection d’un Cobot

### Étudiants : EL-GHARSI Imane, Nouhaila Grgouz

## 1. Méthodologie adoptée

Ce projet a consisté en l'application de modèles de machine learning pour résoudre un problème de classification binaire. Les modèles choisis pour cette tâche incluent les réseaux de neurones LSTM (Long Short-Term Memory), RNN (Recurrent Neural Network) et CNN (Convolutional Neural Network), chacun ayant des caractéristiques et des performances uniques dans le traitement des séquences temporelles.

Le processus a débuté par le prétraitement des données, où les données brutes ont été nettoyées et transformées afin d'être adaptées à l'entraînement des modèles. Cela a impliqué la normalisation et le redimensionnement des entrées pour correspondre aux exigences des réseaux de neurones. Ensuite, les données ont été organisées en séquences temporelles, particulièrement pour les modèles LSTM et RNN, qui sont particulièrement efficaces pour traiter ce type de données.

Une fois les données préparées, l'entraînement des trois modèles a été lancé. Nous avons utilisé les métriques classiques de performance des modèles de classification, telles que l'accuracy, la précision, le rappel, le F1-score et l'AUC ROC, pour évaluer la qualité de chaque modèle. Ces modèles ont été soigneusement suivis tout au long de leur apprentissage et les résultats ont été enregistrés et visualisés via Weights & Biases (W&B).

Enfin, une attention particulière a été accordée à l'ajustement des hyperparamètres des modèles, notamment le taux d'apprentissage, la taille des couches cachées, le nombre de couches et le taux de dropout, afin d'optimiser les performances des modèles.

## 2. Comparaison des modèles et des hyperparamètres testés

Les trois modèles, LSTM, RNN et CNN, ont été comparés pour évaluer leur efficacité respective. Chacun a montré une performance remarquable sur les données d'entraînement et de test.

- **LSTM (Long Short-Term Memory)** : Le modèle LSTM a montré une performance exceptionnelle, particulièrement en termes de précision et d'AUC ROC. Il a atteint une précision de 98.97% et une AUC ROC de 0.9994. Ce modèle a également montré une excellente capacité à gérer les séquences temporelles, ce qui est l'une de ses principales forces.

- **RNN (Recurrent Neural Network)** : Le modèle RNN a fourni des résultats similaires à ceux du LSTM. Il a obtenu une précision de 98.93% et une AUC ROC de 0.9985. Bien qu'il soit également très performant, le RNN a légèrement moins bien performé que le LSTM en termes de métriques de rappel et de précision.

- **CNN (Convolutional Neural Network)** : Le modèle CNN a également montré des performances excellentes. Il a obtenu une précision de 98.98% et une AUC ROC de 1.00, ce qui est légèrement supérieur aux autres modèles. Bien que les CNN soient plus couramment utilisés pour les données d'image, ils ont montré une efficacité surprenante sur les données séquentielles dans ce projet.

Les hyperparamètres testés comprenaient le taux d'apprentissage (0.001), la taille des lots (64), le nombre d'époques (80), et le taux de dropout (0.3). Ces hyperparamètres ont été choisis après plusieurs tests et ajustements, et ont contribué à optimiser les performances des modèles.

### 3. Instructions pour exécuter l’API et utiliser le modèle

Pour exécuter l'API Flask et utiliser le modèle de prédiction, il est nécessaire de suivre quelques étapes simples. Tout d'abord, vous devez installer *Docker, un outil qui facilite la création et l'exécution de conteneurs d'application. Une fois Docker installé, vous pouvez construire une image Docker à partir du projet en utilisant un fichier **Dockerfile* fourni. Après avoir construit l'image, vous pouvez exécuter l'application Flask dans un conteneur en exposant le port 5000. Cela rendra l'API accessible localement sur *http://localhost:5000*.

Lorsque l'API est en cours d'exécution, vous pouvez tester la prédiction en envoyant une requête POST avec des données JSON via *Postman* ou *cURL*. Les données d'entrée doivent être envoyées sous forme de tableau (par exemple : [1.5, 2.3, 0.7, 4.0]), et l'API renverra la prédiction sous forme de réponse JSON. Cette méthode permet de facilement interagir avec le modèle pour obtenir des prédictions en temps réel.

De plus, pour faciliter la compréhension et l'exécution du modèle, une *vidéo démonstrative* est également disponible. Elle montre l'ensemble du processus d'exécution du modèle, de l'installation à la mise en place de l'API et à la réalisation de prédictions.

