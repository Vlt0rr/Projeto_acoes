
# 📈 Painel de Preço de Ações

Este projeto é uma aplicação interativa desenvolvida com **Python** e **Streamlit**, que permite aos usuários visualizarem a evolução histórica do preço de ações da bolsa brasileira (**B3**) de forma simples, intuitiva e altamente visual.

---

## 🚀 Funcionalidades

✅ Visualização gráfica do histórico de preços de ações da B3  
✅ Filtro personalizado de ações com múltipla seleção  
✅ Seleção dinâmica de intervalo de datas com `slider`  
✅ Cálculo da performance individual e da carteira de investimentos  
✅ Destaque visual com cores indicando valorização ou desvalorização  
✅ Interface web interativa com tecnologia Streamlit

---

## 🧠 Tecnologias Utilizadas

- **Python 3.9+**
- **Streamlit** – criação da interface web
- **yFinance** – para obtenção dos dados de mercado em tempo real
- **Pandas** – manipulação e análise de dados
- **Datetime** – controle e manipulação de datas

---

## 📂 Estrutura do Projeto

```
📁 projeto/
│
├── Projeto_stream.py     # Script principal da aplicação
├── IBOV.csv              # Lista de ações da B3 utilizadas pelo app
└── README.md             # Documentação do projeto
```

---

## 📥 Como Rodar o Projeto

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**
```bash
streamlit run Projeto_stream.py
```

4. O navegador abrirá automaticamente a interface em:
```
http://localhost:8501
```

---

## 🗂️ Sobre o `IBOV.csv`

A aplicação carrega os ativos a partir do arquivo `IBOV.csv`, que deve conter a seguinte estrutura:

```csv
Código
PETR4
VALE3
ITUB4
...
```

> O código do ativo deve estar **sem o sufixo `.SA`**, pois ele é adicionado automaticamente pelo sistema.

---

## 📊 Exemplo de Uso

Com base nas ações selecionadas e no período definido, o sistema:

- Gera um **gráfico de linha** com os preços de fechamento históricos
- Calcula o desempenho percentual de cada ativo
- Simula uma **carteira de investimentos fictícia** com R$1000 investidos em cada ativo
- Apresenta a **performance total da carteira**

---

## 💡 Diferenciais

✨ Interface limpa, responsiva e fácil de usar  
✨ Códigos organizados e com comentários explicativos  
✨ Abordagem educativa e prática para quem está aprendendo análise de dados  
✨ Ideal para incluir em portfólios profissionais ou acadêmicos

---

## 👨‍💻 Autor

Desenvolvido por **Vitor Alves**  
📧 seuemail@gmail.com  
💼 [linkedin.com/in/seu-perfil](https://linkedin.com/in/seu-perfil)

---

## ⭐ Considerações Finais

Esse projeto mostra a integração entre Python, dados financeiros e visualização interativa em tempo real — uma vitrine ideal de habilidades técnicas em:

- **Análise de dados**
- **Desenvolvimento web com Streamlit**
- **Automatização com bibliotecas do ecossistema Python**

Se você está procurando um desenvolvedor com visão analítica, domínio técnico e foco em entregar soluções intuitivas — **vamos conversar!**
