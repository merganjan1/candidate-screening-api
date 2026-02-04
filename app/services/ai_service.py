from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def score_resume(resume_text: str, job_text: str) -> float:
    embeddings = model.encode([resume_text, job_text], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(similarity[0][0]) * 100, 2)
