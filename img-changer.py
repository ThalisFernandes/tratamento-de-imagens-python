from PIL import Image
from numpy import array

img = Image.open("img-changer\paisagem.jpeg")

img_array = array(img)

# Warning.filterwarnings('ignore')

def running():
    print("Qual tipo de mudança você quer \n fazer na image: \n Preto e Branco : pb \n canal vermelho : Red \n canal verde: Green \n Canal azul : Blue \n")
    resposta = input();
    print(resposta)

    if resposta == 'Red':
        red_chanel(img_array)
    elif resposta == 'Green':
        green_chanel(img_array)
    elif resposta == 'Blue':
        blue_chanel(img_array)
    elif resposta == 'pb':
        pb(img_array)
    




def red_chanel(imgArr):
    if imgArr.any():
        for pixelbloc in imgArr:
            for pixel in pixelbloc:
                pixel[1] = 0
                pixel[2] = 0
    
    new_img = Image.fromarray(imgArr).save('canal_vermelho.jpeg')
    return new_img

def blue_chanel(imgArr):
    if imgArr.any():
        for pixelbloc in imgArr:
            for pixel in pixelbloc:
                pixel[0] = 0
                pixel[1] = 0 
    
    new_img = Image.fromarray(imgArr).save('canal_azul.jpeg')
    return new_img

def green_chanel(imgArr):
    if imgArr.any():
        for pixelbloc in imgArr:
            for pixel in pixelbloc:
                pixel[0] = 0
                pixel[2] = 0 
    
    new_img = Image.fromarray(imgArr).save('canal_verde.jpeg')
    return new_img

def pb(imgArr):
    if imgArr.any():
        for pixelbloc in imgArr:
            for pixel in pixelbloc:
                media = (pixel[0]+pixel[1]+pixel[2]) / len(pixel)
                pixel[0] = media
                pixel[1] = media
                pixel[2] = media
    
    new_img = Image.fromarray(imgArr).save('pretoEbranco.jpeg')
    return new_img



red_chanel(img_array)
pb(img_array)
green_chanel(img_array)
blue_chanel(img_array)
print(img)