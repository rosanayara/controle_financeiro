# Controle Real - Controle Financeiro Pessoal

Um aplicativo web completo para controle financeiro pessoal, desenvolvido com Flask.

## 🚀 Funcionalidades

- **Cálculo de Salário Líquido**: Calcule automaticamente INSS e IRRF
- **Gerenciamento de Despesas**: Adicione, visualize e categorize suas despesas
- **Sistema de Metas**: Crie e acompanhe objetivos financeiros
- **Dashboard Interativo**: Gráficos e métricas em tempo real
- **Interface Moderna**: Design responsivo com tema claro/escuro

## 📋 Como Usar

### 1. Primeiro Acesso
- Acesse `http://127.0.0.1:5000`
- Faça login com: `test@example.com` / `senhateste`

### 2. Configurar Salário
- Vá para "Salário" no menu lateral
- Digite seu salário bruto
- O sistema calculará automaticamente o salário líquido

### 3. Adicionar Despesas
- Clique em "Despesas" > "Adicionar"
- Preencha valor, categoria e descrição
- Categorias disponíveis: Alimentação, Transporte, Moradia, Lazer, Saúde, Educação, Vestuário, Outros

### 4. Criar Metas
- Vá para "Metas" > "Criar Nova Meta"
- Defina nome, valor objetivo e valor atual
- Acompanhe o progresso no dashboard

### 5. Visualizar Dashboard
- Veja gráficos de gastos por categoria
- Acompanhe evolução mensal
- Monitore score financeiro e metas

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask, SQLAlchemy
- **Frontend**: Bootstrap 5, Chart.js, Bootstrap Icons
- **Banco de Dados**: SQLite
- **Autenticação**: Flask-Login

## 📊 Cálculos Realizados

### Salário Líquido
- **INSS**: Calculado por faixas progressivas
- **IRRF**: Baseado na tabela progressiva do IR

### Score Financeiro
- Avalia percentual de gastos sobre salário
- Penalidades por gastos excessivos ou saldos negativos

### Metas
- Progresso percentual automático
- Alertas visuais de conclusão

## 🎨 Interface

- **Sidebar responsiva** com navegação intuitiva
- **Tema escuro/claro** alternável
- **Gráficos interativos** com Chart.js
- **Cards informativos** com métricas importantes
- **Formulários validados** para entrada de dados

## 🔧 Instalação e Execução

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python run.py
```

Acesse em: `http://127.0.0.1:5000`

## 📝 Notas

- Dados são salvos localmente em SQLite
- Interface totalmente responsiva
- Funciona offline após carregamento inicial
- Dados de exemplo podem ser removidos editando o banco</content>
<parameter name="filePath">/home/nayara/Documentos/controle_financeiro/README.md