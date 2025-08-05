from PIL import Image

def redimensionar_imagem(caminho_imagem: str, nova_largura: int):
    # Abre a imagem
    img = Image.open(caminho_imagem)
    
    # Calcula a altura proporcional
    largura_original, altura_original = img.size

    # Se a imagem já for menor, não faz nada
    if nova_largura > largura_original:
        return img  
    
    nova_altura = int((nova_largura / largura_original) * altura_original) 
    
    # Redimensiona mantendo a proporção
    img_redimensionada = img.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)
    
    # Substitui a imagem original
    img_redimensionada.save(caminho_imagem)

    return img_redimensionada

