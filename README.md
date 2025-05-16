# Vitrine AI Chat Model 🤖

Um chatbot local desenvolvido para fins de apresentação de produtos, utilizando modelos de IA do Google para processamento de linguagem natural.

## 📋 Sobre o Projeto

Este projeto implementa um chatbot interativo usando Streamlit como interface gráfica e a API do Google AI para processamento de linguagem natural. O chatbot é projetado para ser uma vitrine de demonstração de produtos, oferecendo respostas inteligentes e contextuais às perguntas dos usuários.

## 🔧 Requisitos do Sistema

- Python >= 3.13
- UV (Gerenciador de pacotes Python)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd vitrine_ai_chat_model
```

2. Instale as dependências usando UV:
```bash
uv venv
uv pip install -r requirements.txt
```

## ⚙️ Configuração

1. Copie o arquivo de exemplo de variáveis de ambiente:
```bash
cp env_files/.env.example env_files/.env
```

2. Configure as seguintes variáveis de ambiente no arquivo `env_files/.env`:
```env
GOOGLE_API_KEY="Sua chave de API do Google"
GOOGLE_AI_MODEL="Nome do modelo do Google AI"
GOOGLE_AI_TEMPERATURE="Temperatura do modelo (ex: 0.7)"
```

## 💻 Uso

Para iniciar a aplicação:

```bash
uv pip run task run
```

A aplicação estará disponível em `http://localhost:8501`

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
.
├── env_files/          # Arquivos de configuração de ambiente
├── src/                # Código fonte
│   ├── config/         # Configurações da aplicação
│   └── app.py          # Aplicação principal
├── .gitignore          # Arquivos ignorados pelo git
├── pyproject.toml      # Configuração do projeto
└── README.md          # Este arquivo
```

### Ferramentas de Desenvolvimento

- **Ruff**: Linter e formatador de código
- **Taskipy**: Gerenciador de tarefas

### Comandos Úteis

```bash
# Formatar código
uv pip run task format

# Executar verificações de código
uv pip run task pre_format
```

## 📦 Dependências Principais

- `langchain`: Framework para aplicações de IA
- `langchain-google-genai`: Integração com Google AI
- `pydantic`: Validação de dados
- `streamlit`: Interface web

## 🤝 Contribuindo

1. Faça o fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.