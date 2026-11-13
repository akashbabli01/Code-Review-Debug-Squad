import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

_client = chromadb.PersistentClient(path="./chroma_db")
_collection = _client.get_or_create_collection(
    name="coding_guidelines",
    embedding_function=DefaultEmbeddingFunction()
)

def add_guidance(text):
    count = _collection.count()
    _collection.add(
        ids=[f"guideline-{count}-{abs(hash(text))}"],
        documents=[text],
        metadatas=[{"source": "user_added_guideline"}]
    )

def retrieve_guidance(query, n_results=3):
    if _collection.count() == 0:
        return ""
    result = _collection.query(query_texts=[query], n_results=min(n_results, _collection.count()))
    docs = result.get("documents", [[]])[0]
    return "\n".join(docs)
