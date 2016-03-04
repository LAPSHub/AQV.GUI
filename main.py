import numpy as np
import PsnrMsim as p
import avaliacao

def aqv(orig,teste, arquivo,  psnr, mse, msim, lin, log, pearson, spearman, out):
    f = open('Avaliacao de Desempenho de Metricas de Qualidade Visual.txt', 'a')
    a = p.metricas(orig, teste, arquivo)
    if psnr:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, logistica, linear = avaliacao.avaliacao(1, arquivo)
        f.write('PSNR' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if mse:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, logistica, linear = avaliacao.avaliacao(2, arquivo)
        f.write('MSE' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    if msim:
        razao_outliers, coeficiente_spearman, coeficiente_pearson, logistica, linear = avaliacao.avaliacao(3, arquivo)
        f.write('MSIM' + '\n')
        if out:
            f.write('Razao de outliers: ' + str(razao_outliers)+ '\n')
        if spearman:
            f.write('Coeficiente de Spearman: ' + str(coeficiente_spearman) + '\n')
        if pearson:
            f.write('Coeficiente de Pearson: ' + str(coeficiente_pearson) + '\n')
        if log:
            f.write('Funcao Losgistica:' + logistica + '\n')
        if linear:
            f.write('Regressao Linear:' + linear + '\n')
    f.close()
