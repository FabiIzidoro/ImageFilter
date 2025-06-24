from PIL import Image, ImageFilter, ImageOps

def aplicar_filtro(path, filtro):
    imagem = Image.open(path)
    if filtro == 'negativo':
        return ImageOps.invert(imagem.convert('RGB'))
    elif filtro == 'mediana':
        return imagem.filter(ImageFilter.MedianFilter(size=3))
    elif filtro == 'gaussiano':
        return imagem.filter(ImageFilter.GaussianBlur(radius=2))
    else:
        return imagem
