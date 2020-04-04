import numpy as np
import pdb
import copy #a = copy.deepcopy(b)

###  list(map(list, a))
###  np.array(sorted(list(map(list, a))))

def ordena_sistema(matriz):
    """
    matriz: Entrada: contém os coeficientes e os termos independentes do
            sistema linear;
            Saída: contem 'matriz' ordenada e normalizada pelo primeiro
            elemento da linha.
    """
    # normalizando as linhas pelo primeiro elemento da linha
    m = copy.deepcopy(matriz)
    linha = 0
    #pdb.set_trace()
    for i in m[:, 0]:
        if i != 0:
            m[linha, :] = m[linha, :] /abs(i)
        linha = linha + 1
    # ordenando a matriz m
    m = np.array(sorted(list(map(list, m))))
    #pdb.set_trace()
    conta_zero = 0
    negativo = 0
    positivo = 0
    primeiro_zero = -1
    k = -1
    for i in m[:,0]:
        k = k + 1
        if i == 0:
            if primeiro_zero == -1:
                primeiro_zero = k
            conta_zero = conta_zero + 1
        elif i == -1:
            negativo = negativo + 1
        elif i == 1:
            positivo = positivo + 1
    aux = m[primeiro_zero : primeiro_zero + conta_zero,:]
    nl, nc = np.shape(m)
    aux3 = m[primeiro_zero + conta_zero : nl,:]
    #pdb.set_trace()
    matriz[0 : primeiro_zero, :] = m[0 : primeiro_zero, :]
    matriz[primeiro_zero:primeiro_zero+(nl- (primeiro_zero+conta_zero))] [:]= m[primeiro_zero + conta_zero : nl,:]
    matriz[primeiro_zero+(nl- (primeiro_zero+conta_zero)):nl][:] = aux
    return(matriz, positivo, negativo, conta_zero)
#  return(m)

def monta_c(positivo, negativo, conta_zero):

    auxiliar_contador = np.array(range(positivo))
    c = np.zeros((negativo*positivo + conta_zero, positivo + negativo + conta_zero))
    k = 0
    contador = 0
    while k < negativo:
        for i in list(range(contador, contador + positivo)):
            c[i][k] = 1
        c[contador: contador + positivo, negativo:negativo + positivo] = np.eye(positivo)
        contador  = contador + i + 1
        k = k + 1
    if conta_zero > 0:
        c[negativo*positivo : negativo*positivo + conta_zero, positivo + negativo: positivo + negativo + conta_zero] = np.eye(conta_zero)
    return(c)

def dados():

    matriz = np.array([[ 0.7071,  0.4082,  0.2887,  0.500,  3.4654],
                       [-0.7071, -0.4082, -0.2887, -0.500, -1.4654],
                       [-0.7071,  0.4082,  0.2887,  0.500, -0.7772],
                       [ 0.7071, -0.4082, -0.2887, -0.500,  2.7772],
                       [ 0,      -0.8164,  0.2887,  0.500, -3.5543],
                       [ 0,       0.8164, -0.2887, -0.500,  5.5547],
                       [ 0,       0,      -0.8660,  0.500,  0.8660],
                       [ 0,       0,       0.8660, -0.500,  1.1340]])
    return(matriz)

