def calcular_PIS(val_produto):
    return val_produto * 0.0165

def calcular_COFINS(val_produto):
    return val_produto * 0.076

def calular_ISS(val_produto, estado):
    iss = 0.0 

    if estado == 'SP':
        iss = val_produto *0.03

    elif estado == 'BA':
        iss = val_produto * 0.04

    elif estado == 'RS':
        iss = val_produto * 0.05

    else:
        iss = val_produto * 0.02
    
    return iss

def calcular_ICMS(val_produto, estrangeira):
    if estrangeira == 'S':
        return val_produto * 0.04

    else:
        return val_produto * 0.1

def calcular_valor_total(val_produto, pis, cofins, iss, icms):
    return val_produto + pis + cofins + iss + icms