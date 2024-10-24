import requests
from bs4 import BeautifulSoup
from langchain_openai.chat_models.azure import AzureChatOpenAI

def extrair_texto_url(url):
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(['script', 'style']):
      script_or_style.decompose()
    text = soup.get_text(separator= ' ')
    linhas = (line.strip() for line in text.splitlines())
    parts = (phrase.strip() for line in linhas for phrase in line.split(" "))
    text_clean = '\n'.join(part for part in parts if part)
    return text_clean
  else:
    print(f"Failed to fetch the URL. Status code: {response.status_code}")
    return None
  text = soup.get_text()
  return text

extrair_texto_url('https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo')

url = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'
text = extrair_texto_url(url)
article = translate_article(text, "pt-br")
print(article)



client = AzureChatOpenAI(
    azure_endpoint="",
    api_key="",
    api_version="2024-08-01-preview",
    azure_deployment="gpt-4o-mini",
    max_retries=0
)

def translate_article(text, lang):
  messages = [
      ("system" , "Você atua como tradutor de textos"),
      ("user" , f"Traduza o {text} para o idioma {lang} e responda em markdown")
  ]

  response = client.invoke(messages)
  print(response.content)
  return response.content

translate_article("GPT models are hosted in multiple service vendor at the moment, and Microsoft Azure is one of them.","português")