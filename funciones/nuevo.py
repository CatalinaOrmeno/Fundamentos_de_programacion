import mis_modulos.lista_f
import mis_modulos.resp_f
menup = ['Ver clientes', 'Buscar cliente', 'Agregar cliente', 'Salir']

while True:
    mis_modulos.lista_f.iterar(menup)
    resp = mis_modulos.resp_f.solicitar_respuesta()