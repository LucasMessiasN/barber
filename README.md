💈 **BarberFlow**
Sistema de Gerenciamento para Barbearias > Desenvolvido para ter controle de clientes e análise por dashboard e historicos.

O BarberFlow é uma aplicação web construída com Django, focada em oferecer uma experiência de usuário e um controle administrativo. 

🚀 **Funcionalidades Principais**

- **Gestão de Cadastros:** Controle completo de Clientes, Barbeiros e Usuários do sistema.
- **Fluxo de Atendimento:** Agendamento simplificado com status de serviço (Pendente/Concluído).
- **Dashboard Financeiro:** Visualização de métricas de faturamento real baseadas em atendimentos concluídos.
- **Histórico Inteligente:** Relatórios com filtros por período para auditoria e conferência de dados.
- **Interface Dinâmica:** Uso de Modais JavaScript para fechamento de atendimentos e feedbacks visuais sem recarregar a página.

🛠️ **Stack Tecnológica**

Para garantir performance e manutenibilidade, foram utilizadas as seguintes tecnologias:

Backend: Python & Django Framework (v6.0.2)
Frontend: Bootstrap 5 (Layout Responsivo) & Font Awesome (Iconografia)
Interatividade: JavaScript (Fetch API)
Banco de Dados: SQLite (padrão de desenvolvimento)
Estilização: Django-Crispy-Forms para formulários dinâmicos e profissionais.

🏁 **Como Rodar o Projeto**

Clone o repositório:

git clone [https://github.com/LucasMessiasN/barberflow.git](https://github.com/LucasMessiasN/barberflow.git)


Crie e ative o ambiente virtual (venv):

python -m venv venv
.\venv\Scripts\activate


Instale as dependências:

pip install -r requirements.txt


Execute as Migrations:

python manage.py migrate


Inicie o servidor:

python manage.py runserver


Acesse o endereço http://127.0.0.1:8000/ no seu navegador.

📂 Estrutura de Arquivos (Destaques)

base.html: Template mestre com Sidebar responsiva e hierarquia de menus.

views.py: Lógica de agregação financeira e tratamento de requisições.

models.py: Modelagem de dados.

requirements.txt: Lista de dependências isoladas do projeto.


👤 **Autor**

Lucas Messias Analista de Sistemas em Formação (ADS).

LinkedIn
[https://www.linkedin.com/in/lucas-messias-1aa2112b2/](https://www.linkedin.com/in/lucas-nunes-1aa2112b2/)
