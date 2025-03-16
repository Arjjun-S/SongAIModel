import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r"AiMinor/spotify dataset.csv")

# Data preprocessing
df.dropna(inplace=True)  # Remove missing values
features = df.select_dtypes(include=['number'])  # Select numerical features

# Encode categorical labels if any
label_encoder = LabelEncoder()
df['encoded_labels'] = label_encoder.fit_transform(df['playlist_name'])  # Example encoding if needed

# Pair plot visualization
sns.pairplot(pd.DataFrame(features, columns=features.columns))
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(pd.DataFrame(features, columns=features.columns).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()

# Clustering using K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(features)

# Visualizing clusters
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['danceability'], y=df['energy'], hue=df['Cluster'], palette='viridis')
plt.title("Clusters based on Danceability and Energy")
plt.show()

#splitting data for training and test
X_train, X_test, y_train, y_test = train_test_split(features, df['Cluster'], test_size=0.2, random_state=42)



