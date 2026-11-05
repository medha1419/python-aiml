from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love machine learning",
    "I enjoy studying artificial intelligence",
    "I like playing badminton",
    "Deep learning is a branch of AI"
]

# Convert sentences into embeddings
embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)

# Calculate cosine similarity
similarity = cosine_similarity(embeddings)

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        print(
            f"\n{sentences[i]} vs {sentences[j]}"
        )
        print("Similarity:", round(similarity[i][j], 4))