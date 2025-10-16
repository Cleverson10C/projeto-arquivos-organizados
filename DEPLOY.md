# Organizador de Arquivos - Deploy Render

Este projeto demonstra um sistema de organização automática de arquivos, adaptado para rodar como web service no Render.

## 🚀 Deploy no Render

### Arquivos necessários criados:
- `requirements.txt` - Dependências Python
- `Procfile` - Comando de inicialização
- `runtime.txt` - Versão do Python
- `web_app.py` - Aplicação web Flask

### Como fazer o deploy:

1. **Push para GitHub**:
   ```bash
   git add .
   git commit -m "Preparar para deploy no Render"
   git push origin main
   ```

2. **Configurar no Render**:
   - Acesse [render.com](https://render.com)
   - Conecte seu repositório GitHub
   - Escolha "Web Service"
   - Configure:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn web_app:app`
     - **Environment**: Python 3

3. **Variáveis de ambiente** (opcional):
   - `PORT` - Porta do servidor (automática no Render)

### Funcionalidades da versão web:
- ✅ Interface web para monitoramento
- ✅ Sistema de logs em tempo real
- ✅ API endpoints para status
- ✅ Health check para monitoramento
- ✅ Simulação do sistema de organização

### Endpoints disponíveis:
- `/` - Interface principal
- `/status` - Status do sistema (JSON)
- `/logs` - Logs do sistema (JSON)
- `/health` - Health check

### Nota importante:
Como o Render não tem acesso ao sistema de arquivos local, esta versão simula o funcionamento do organizador e serve como demonstração do projeto.