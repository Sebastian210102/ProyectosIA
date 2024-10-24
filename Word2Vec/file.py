from gensim.models import Word2Vec

# Ejemplo de datos de entrenamiento
sentences = [["este", "es", "un","buen", "ejemplo"], ["esto", "es", "otro", "ejemplo"]]

# Entrena el modelo
model = Word2Vec(sentences, vector_size=1, window=5, min_count=1, sg=0)

# Obtén el vector para una palabra
vector = model.wv['ejemplo']
print(vector)
