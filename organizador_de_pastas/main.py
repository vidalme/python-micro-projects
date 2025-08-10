import os
import magic

# receber diretorio a ser organizado
# organizar folder
    # checar se os folder necessarios existem e crialos se necessarios
    # classificar e colocar em seu devido folder todos os arquivos
# enviar mensagem para o usuario que a operacao foi concluida com sucesso com a quantidade de items que foram movidos para cada folder
# /mnt/c/Users/AlAn192/Downloads/

pastas_organizadoras = ["Outros","Videos","Imagens","Documentos","Audios","Programas"]
videos_fmt = ["video/mp4","video/x-matroska","video/x-msvideo","video/quicktime",
              "video/x-ms-wmv","video/webm","video/x-flv","video/ogg",
              "video/x-matroska-3d","video/x-matroska-360"]
imagens_fmt = ["image/png","image/jpeg","image/heic","image/gif","image/bmp","image/webp",
               "image/tiff","image/x-icon","image/svg+xml","image/vnd.microsoft.icon",
               "image/x-xbitmap","image/x-xpixmap","image/x-xwindowdump"]
documentos_fmt = ["text/plain","application/pdf","text/csv","application/msword",
                  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                  "application/vnd.ms-excel","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                  "application/vnd.ms-powerpoint","application/vnd.openxmlformats-officedocument.presentationml.presentation",
                  "application/rtf","application/x-tex","application/x-latex","text/html"]
saudios_fmt = ["audio/mp3","audio/mpeg","audio/x-wav","audio/x-flac",
              "audio/ogg","audio/aac","audio/x-aiff","audio/x-ms-wma",
              "audio/x-matroska","audio/webm","audio/x-mpegurl"]
programas_fmt = ["application/x-dosexec","application/gzip","application/x-msi","application/x-iso9660-image",
                 "application/vnd.microsoft.portable-executable",
                 "application/zip", "application/x-rar-compressed",
                 "application/x-7z-compressed", "application/x-tar",
                 "application/x-bzip2", "application/x-xz"]

def generaliza_pasta_alvo(pasta_alvo:str)->str:
    pasta_alvo_generica = os.path.join(pasta_alvo)

def recebe_input_usuario()->str:
    # pasta_alvo = input()
    pasta_alvo = "/mnt/c/Users/andre/Downloads/"
    return os.path.join(pasta_alvo)

def checa_pastas_organizadoras(pasta_alvo:str):
    for i, pasta in enumerate(pastas_organizadoras):
        if not os.path.isdir(os.path.join(pasta_alvo,pastas_organizadoras[i])):
            os.mkdir(os.path.join(pasta_alvo,pastas_organizadoras[i]))

def organiza_pasta(pasta_alvo:str):
    checa_pastas_organizadoras(pasta_alvo)
    os.chdir(pasta_alvo)
    
    arquivos = os.listdir(pasta_alvo)
    
    quantidade_videos=0
    quantidade_imagens=0
    quantidade_documentos=0
    quantidade_audios=0
    quantidade_programas=0
    quantidade_outros=0

    for arquivo in arquivos:
        if not os.path.isdir(arquivo):

            assinatura_arquivo = magic.from_file(arquivo, mime=True)

            for fmt in videos_fmt:
                if fmt in assinatura_arquivo:
                    os.rename(arquivo , os.path.join(pasta_alvo,pastas_organizadoras[1],arquivo))
                    quantidade_videos+=1
            for fmt in imagens_fmt:
                if fmt in assinatura_arquivo:
                    os.rename(arquivo , os.path.join(pasta_alvo,pastas_organizadoras[2],arquivo))
                    quantidade_imagens+=1
            for fmt in documentos_fmt:
                print("-----------------------")
                print(fmt)
                if fmt in assinatura_arquivo:
                    print(arquivo)
                    print('----------------')
                    os.rename(arquivo , os.path.join(pasta_alvo,pastas_organizadoras[3],arquivo))
                    quantidade_documentos+=1
            for fmt in audios_fmt:
                if fmt in assinatura_arquivo:
                    os.rename(arquivo , os.path.join(pasta_alvo,pastas_organizadoras[4],arquivo))
                    quantidade_audios+=1
            for fmt in programas_fmt:
                if fmt in assinatura_arquivo:
                    os.rename(arquivo , os.path.join(pasta_alvo,pastas_organizadoras[5],arquivo))
                    quantidade_programas+=1
            
            if os.path.isfile(os.path.join(pasta_alvo,arquivo)):
                print(f"O arquivo {arquivo} do tipo {assinatura_arquivo} e vai ser movido para o folder Outros")
                os.rename(arquivo , os.path.join(pasta_alvo,pastas_organizadoras[0],arquivo))
                quantidade_outros+=1

    print("+++++++++++++++++++++++++++++++++++++")
    print(f"Um total de {quantidade_videos} videos foram movidas para o folder {os.path.join(pasta_alvo,pastas_organizadoras[1])}")
    print(f"Um total de {quantidade_imagens} iamgens foram movidas para o folder {os.path.join(pasta_alvo,pastas_organizadoras[2])}")
    print(f"Um total de {quantidade_documentos} documentos foram movidas para o folder {os.path.join(pasta_alvo,pastas_organizadoras[3])}")
    print(f"Um total de {quantidade_audios} audios foram movidas para o folder {os.path.join(pasta_alvo,pastas_organizadoras[4])}")
    print(f"Um total de {quantidade_programas} programas foram movidas para o folder {os.path.join(pasta_alvo,pastas_organizadoras[5])}")
    print(f"Um total de {quantidade_outros} outros foram movidas para o folder {os.path.join(pasta_alvo,pastas_organizadoras[0])}")
    print("+++++++++++++++++++++++++++++++++++++")  

def main():
    pasta_alvo = recebe_input_usuario()
    organiza_pasta(pasta_alvo)

if __name__ == "__main__":
    main()
