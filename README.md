# Guardião do SIGA

Este é um projeto de um bot do Telegram desenvolvido em Python para ajudar os alunos a acompanhar os prazos de inscrição no SIGA (Sistema Integrado de Gestão Acadêmica). O bot envia lembretes automáticos sobre os períodos de inscrição, garantindo que os usuários não percam nenhuma data importante.

### Recursos:
- Consulta automática das datas de inscrição com base em um calendário acadêmico.
- Envio diário de lembretes às 17:30 durante os períodos de inscrição.
- Configuração personalizada para diferentes períodos acadêmicos.
- Comandos interativos para ativar e desativar os lembretes.

### Tecnologias utilizadas:
- Python
- Biblioteca python-telegram-bot
- Web scraping com BeautifulSoup

Contribuições e melhorias são bem-vindas. Fique à vontade para abrir issues, enviar pull requests e compartilhar ideias para aprimorar este projeto.

Procure pelo bot no Telegram e inicie a conversa para receber os lembretes!

### Instruções para criar o seu próprio bot a partir desse
1. Clone o repositório.
2. Instale as dependências listadas no arquivo `requirements.txt`: `pip install -r requirements.txt`
3. Configure o token do seu bot do Telegram no `botSIGA.py`
4. Abra o arquivo `executa_bot_siga.bat` em um editor de texto.

Adicione o seguinte conteúdo ao arquivo para iniciar o bot:
```
@echo off
python C:\caminho\para\o\repositorio\botSIGA.py
```
Lembre-se de substituir `caminho\para\o\repositorio` pelo caminho real para o diretório do repositório clonado.
Salve e feche o arquivo `executa_bot_siga.bat`.

5. Pressione `Win + R` para abrir a janela `Executar`. Digite `shell:startup` e pressione Enter. Isso abrirá a pasta de inicialização do Windows.

6. Mova o arquivo `executa_bot_siga.bat` para a pasta de inicialização. Agora, o bot será iniciado automaticamente sempre que você ligar o computador.

7. Abra o aplicativo do Telegram e pesquise pelo nome bot. Inicie uma conversa com o bot e siga as instruções fornecidas para configurar e receber os lembretes de inscrição no SIGA.
   

## Uso

Para usar o Guardião do SIGA, siga estas etapas:

1. Inicie o bot executando o arquivo `executa_bot_siga.bat`.

2. Abra o aplicativo do Telegram e pesquise pelo nome do bot.

3. Inicie uma conversa com o bot e siga as instruções fornecidas para configurar e receber os lembretes de inscrição no SIGA.

Aproveite a conveniência de receber lembretes automáticos sobre as inscrições no SIGA com o Guardião do SIGA!
