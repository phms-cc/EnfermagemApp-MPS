class AdaptadorImagem():
    def mostra_imagem(self,mostrador,imagem,*args):
        if(len(*args)==1):
            #suponhamos que a imagem so recebeu o argumento de posicao
            #nesse caso, iremos enviar para MostrarImagem parametros de altura e largura do 
            #proprio tamanho da imagem
            posicao = args[1]
            imagem_altura = imagem.getHeight()
            imagem_largura = imagem.getWidth()
            mostrador.mostra_imagem(imagem,posicao,imagem_altura,imagem_largura)
        elif (len(*args)==3):
            posicao = args[1]
            imagem_altura = args[2]
            imagem_largura = args[3]
            mostrador.mostra_imagem(imagem,posicao,imagem_altura,imagem_largura)  
        else:
            pass
            #ou levantar um erro
            
