import requests

# URL da API de classificação de imagem
api_url = "https://classifyimages0404.cognitiveservices.azure.com/customvision/v3.0/Prediction/64477bf1-aed7-4036-850a-b02903d2b8b6/classify/iterations/shoes/url"

# Chave de previsão
prediction_key = "3e790cdbc3604a2da8ea7ccfccd3a7a3"

# Cabeçalhos da solicitação
headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/json"
}

# URL do blob de imagem
blob_url = "https://storagecleber.blob.core.windows.net/imagetoclassify/image.jpg"

# Corpo da solicitação
data = {"Url": blob_url}

# Fazendo a solicitação POST para a API
response = requests.post(api_url, headers=headers, json=data)

# Verificando a resposta
if response.status_code == 200:
    result = response.json()
    # Extraindo a classe predita
    predicted_class = result["predictions"][0]["tagName"]
    print("A imagem foi classificada como:", predicted_class)
else:
    print("Falha ao chamar a API. Código de status:", response.status_code)



