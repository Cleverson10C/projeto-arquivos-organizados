import schedule
import os
import shutil
import time


def tarefa():
    # Definir as categorias de arquivos e suas pastas correspondentes
    categorias = {
        "Textos": [".txt", ".csv"],
        "Imagens": [".jpg", ".png", ".jpeg"],
        "Pdf": [".pdf", ".docx"],
        "Planilha": [".xlsx"],
        "Música": [".mp3"],
        "Vídeo": [".mp4", ".avi", ".mkv"],
        "Arquivos Compactados": [".zip", ".rar"],
    }

    # Definir a pasta onde estão os arquivos desorganizados
    caminho_origem = r"C:\Users\cleve\Downloads"

    # Criar as subpastas para organização
    for pasta in categorias.keys():
        caminho_pasta = os.path.join(caminho_origem, pasta)
        if not os.path.exists(caminho_pasta):
            os.mkdir(caminho_pasta)

    # Organizar os arquivos
    for arquivo in os.listdir(caminho_origem):
        caminho_arquivo = os.path.join(caminho_origem, arquivo)
        # Verificar se é um arquivo (e não um diretório)
        if os.path.isfile(caminho_arquivo):
            extensao = os.path.splitext(arquivo)[1]
            # Mover para a pasta correspondente com base na extensão
            for pasta, extensoes in categorias.items():
                if extensao.lower() in extensoes:
                    destino = os.path.join(caminho_origem, pasta, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    print(f"Movido: {arquivo} → {pasta}")
                    break


schedule.every(10).seconds.do(tarefa)
while True:
    schedule.run_pending()
    time.sleep(1)
