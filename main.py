import os
from src.data_loader import load_all_documents
from src.embedding import EmbeddingManager
from src.vectorstore import VectorStore
from src.rag_retriever import RAGRetriever
from src.llm import GroqLLM
from src.rag_search import RAGSearch


embedding_manager = EmbeddingManager()
vectorstore=VectorStore()

if False:
   docs = load_all_documents("data")
   ## Generate the Embeddings
   chunks = embedding_manager.chunk_documents(docs)
   texts=[doc.page_content for doc in chunks]
   embeddings = embedding_manager.generate_embeddings(texts)

   vectorstore.add_documents(chunks, embeddings)


rag_retriever=RAGRetriever(vectorstore, embedding_manager)
response = rag_retriever.retrieve("What is attention mechanism?")
#print(response)

groq_llm = GroqLLM(api_key=os.getenv("GROQ_API_KEY"))
response = groq_llm.generate_response(query="What is attention mechanism?", context="") 
print(response)


rag_search = RAGSearch(rag_retriever, groq_llm)
response = rag_search.generate_answer(query="What is attention mechanism?", top_k=3)
print(response)