from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def score_resume(resume_text: str, job_text: str) -> float:
    embeddings = model.encode([resume_text, job_text], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(similarity[0][0]) * 100, 2)

BACKEND_PROFILE = """
REST APIs, databases, distributed systems, caching, microservices,
docker, kubernetes, authentication, message queues, backend architecture
"""

AI_PROFILE = """
machine learning, transformers, pytorch, model training, fine-tuning,
embeddings, NLP, deep learning, model inference
"""

def ai_department_eval(resume_text: str):
    embeddings = model.encode(
        [resume_text, BACKEND_PROFILE, AI_PROFILE],
        convert_to_tensor=True
    )

    backend_score = util.cos_sim(embeddings[0], embeddings[1])[0][0]
    ai_score = util.cos_sim(embeddings[0], embeddings[2])[0][0]

    if backend_score >= ai_score:
        return "backend", round(float(backend_score), 3)
    else:
        return "ai/ml", round(float(ai_score), 3)



