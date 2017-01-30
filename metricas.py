import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import metrica

def metricas (orig, test, arquivo):

    arquiv = arquivo
    subjectscores = open(arquiv, 'r')
    conteudo_texto1 = subjectscores.read()
    aa = conteudo_texto1.split('\n')                
    cc = aa[:-1]                                       
    subjectscores.close()


    for i in xrange(0, len(cc)):
        a = aa[i].split('\t')
        dirOrig = orig
        imag = a[0]
        e =  dirOrig+'/'+imag
        ref = plt.imread(e)
        dirTest = test
        imag = a[1]
        ee = dirTest + '/'+imag
        teste = plt.imread(ee)
        
        psrn = metrica.psnr(ref, teste)
        mse  = metrica.mse(ref, teste)
        
        j = 0
        a = ref[:,:,j]
        b = teste[:,:,j]
        ssim0 = metrica.msim(a, b)

        j = j+1
        a = ref[:,:,j]
        b = teste[:,:,j]
        ssim1 = metrica.msim(a, b)

        j = j+1
        a = ref[:,:,j]
        b = teste[:,:,j]
        ssim2 = metrica.msim(a, b)
        ssim = (ssim0 + ssim1 + ssim2)/3
        
        psrn2 = str(psrn)
        ssim2 = str(ssim)
        mse2 = str(mse)
        print 'img' + str(i) + ';' + psrn2 + ';' + ssim2 + ';' + mse2 
        f = open('arquivo.txt','a')
        f.write('img' + str(i) + ';' + psrn2 + ';' + ssim2 + ';' + mse2 + '\n' )
        f.close()


