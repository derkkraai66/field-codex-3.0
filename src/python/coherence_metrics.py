import numpy as np

def cosine_similarity(a, b):
    """Compute cosine similarity between two vectors."""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def spatial_coherence(activations):
    """
    Compute spatial coherence C_space for a field of shape (N, d):
    N = number of nodes/tokens
    d = dimensionality
    """
    N = activations.shape[0]
    sims = []

    for i in range(N):
        for j in range(N):
            sims.append(cosine_similarity(activations[i], activations[j]))

    return np.mean(sims)


def temporal_coherence(field_t, field_t_next):
    """
    Compute temporal coherence C_time between two time slices
    field_t      = activations at time t    (N, d)
    field_t_next = activations at time t+1  (N, d)
    """
    N = field_t.shape[0]
    sims = [cosine_similarity(field_t[i], field_t_next[i]) for i in range(N)]
    return np.mean(sims)


def conceptual_interference(A, B):
    """
    Compute conceptual interference between concept vectors A and B.
    Positive → constructive interference
    Negative → destructive interference
    """
    return cosine_similarity(A, B)


# ------------------------------
# Demo usage with fake data
# ------------------------------

if __name__ == "__main__":
    # Fake token activations: 5 tokens, embedding dim 3
    field_t = np.array([
        [0.9, 0.1, 0.0],
        [0.8, 0.2, 0.0],
        [0.85, 0.15, 0.0],
        [0.1, 0.9, 0.1],
        [0.0, 0.8, 0.2]
    ])

    # Slightly updated field for temporal coherence
    field_t_next = field_t + np.random.normal(0, 0.01, field_t.shape)

    print("C_space:", spatial_coherence(field_t))
    print("C_time :", temporal_coherence(field_t, field_t_next))

    # Example conceptual vectors
    A = np.array([1, 0, 0])
    B = np.array([0.8, 0.1, 0])

    print("Interference(A,B):", conceptual_interference(A, B))
