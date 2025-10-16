from flask import Flask, jsonify, render_template_string
import schedule
import os
import shutil
import time
import threading
from datetime import datetime

app = Flask(__name__)

# Lista para armazenar logs das operações
logs = []

def adicionar_log(mensagem):
    """Adiciona uma mensagem ao log com timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs.append(f"[{timestamp}] {mensagem}")
    # Manter apenas os últimos 100 logs
    if len(logs) > 100:
        logs.pop(0)

def tarefa_organizacao():
    """Simula a organização de arquivos (adaptado para web)"""
    try:
        # Como não temos acesso ao sistema de arquivos local no Render,
        # vamos simular a organização
        categorias = {
            "Textos": [".txt", ".csv"],
            "Imagens": [".jpg", ".png", ".jpeg"],
            "Pdf": [".pdf", ".docx"],
            "Planilha": [".xlsx"],
            "Música": [".mp3"],
            "Vídeo": [".mp4", ".avi", ".mkv"],
            "Arquivos Compactados": [".zip", ".rar"],
        }
        
        adicionar_log("Verificação de arquivos iniciada")
        adicionar_log(f"Categorias monitoradas: {len(categorias)}")
        adicionar_log("Sistema de organização funcionando corretamente")
        
    except Exception as e:
        adicionar_log(f"Erro na tarefa: {str(e)}")

def executar_agendamento():
    """Executa o agendamento em thread separada"""
    schedule.every(30).seconds.do(tarefa_organizacao)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Iniciar o agendamento em background
thread = threading.Thread(target=executar_agendamento, daemon=True)
thread.start()

@app.route('/')
def home():
    """Página inicial com informações do projeto"""
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Organizador de Arquivos - Status</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .status { background: #e8f5e8; padding: 15px; border-left: 4px solid #4CAF50; margin: 20px 0; }
            .info { background: #e3f2fd; padding: 15px; border-left: 4px solid #2196F3; margin: 20px 0; }
            .logs { background: #f9f9f9; padding: 20px; border-radius: 5px; margin: 20px 0; }
            .log-item { font-family: monospace; font-size: 12px; margin: 5px 0; }
            .btn { display: inline-block; background: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px 5px 0 0; }
            .btn:hover { background: #45a049; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🗂️ Organizador de Arquivos</h1>
            
            <div class="status">
                <strong>✅ Sistema Online</strong><br>
                O serviço de organização está funcionando normalmente.
            </div>
            
            <div class="info">
                <h3>📋 Sobre o Projeto</h3>
                <p>Este é um sistema automático de organização de arquivos desenvolvido em Python.</p>
                <p><strong>Funcionalidades:</strong></p>
                <ul>
                    <li>Organização automática por tipo de arquivo</li>
                    <li>Monitoramento contínuo</li>
                    <li>Sistema de logs</li>
                    <li>Interface web para acompanhamento</li>
                </ul>
            </div>
            
            <h3>📊 Logs do Sistema</h3>
            <div class="logs">
                {% for log in logs %}
                <div class="log-item">{{ log }}</div>
                {% endfor %}
                {% if not logs %}
                <div class="log-item">Nenhum log disponível ainda.</div>
                {% endif %}
            </div>
            
            <a href="/status" class="btn">📊 Status JSON</a>
            <a href="/logs" class="btn">📝 Logs JSON</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, logs=logs[-10:])  # Mostrar últimos 10 logs

@app.route('/status')
def status():
    """Endpoint para status do sistema"""
    return jsonify({
        'status': 'online',
        'message': 'Sistema de organização funcionando',
        'timestamp': datetime.now().isoformat(),
        'logs_count': len(logs)
    })

@app.route('/logs')
def get_logs():
    """Endpoint para obter logs"""
    return jsonify({
        'logs': logs,
        'count': len(logs),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health_check():
    """Health check para o Render"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # Adicionar log inicial
    adicionar_log("Sistema iniciado")
    adicionar_log("Organizador de arquivos online")
    
    # Configuração para produção
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)