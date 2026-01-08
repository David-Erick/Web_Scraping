import requests;
from bs4 import BeautifulSoup;

link = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/259/recife-pe"

requisicao = requests.get(link);
print(requisicao);  

site = BeautifulSoup(requisicao.text, "html.parser"); 

temperatura = site.find("span", class_="_margin-r-15");
print("------------------------------------------")
print("|                                        |")
print(f"|      A temperatura em Recife é: {temperatura.get_text()}C   |")
print("|            by: ClimaTempo              |")
print("|                                        |")
print("------------------------------------------")
