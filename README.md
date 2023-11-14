# Amazon Scraper

## Projeto feito com intuito de coletar automaticamente informações referentes aos preços de produtos da Amazon que tenho interesse.

### 1.Bibliotecas utilizadas:
![code](https://github.com/MonteiroMiguel/amazon-scraper/assets/148726548/918fb09f-79f9-4db5-bddc-ea08e0cedc14)


### 2.Conexão com o Google Sheets:
O programa selecionará os produtos a serem investigados com base numa planilha do Google Sheets que está no meu Google Drive
Para acessá-la foi necessário utilizar a API oficial dos respectivos serviços do Google, mais informações sobre a instalação das bibliotecas estão presentes na [documentação oficial](https://developers.google.com/sheets/api/quickstart/python?hl=pt-br), além do código que foi usado como base para esse programa. (por se tratar de um trecho de código consideravelmente grande e que se encontra na documentação oficial, não achei necessário anexar screenshots dessa parte)

### 3.Extração das informações:
Para acessar os links e coletar as informações decidi fazer uso da biblioteca [Selenium](https://selenium-python.readthedocs.io), ótima para web scrapings e testes automatizados.

#### Configurando a inicialização do navegador:
![code2](https://github.com/MonteiroMiguel/amazon-scraper/assets/148726548/11d94d78-46e5-4e96-95d6-74165a415dd0)

#### Coletando as informações:
![code3](https://github.com/MonteiroMiguel/amazon-scraper/assets/148726548/3be0480b-f24a-4dc2-9bf5-89c4b41d866a)

#### Exibindo as informações:
![code4](https://github.com/MonteiroMiguel/amazon-scraper/assets/148726548/5e0fa472-e49e-41bf-a02e-a5e9cae99c3d)

#### Resultado:
![image](https://github.com/MonteiroMiguel/amazon-scraper/assets/148726548/b904adc6-359b-4088-9c70-33af188a2ac0)




