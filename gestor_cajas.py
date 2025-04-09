def cliente_a_caja(cliente, cajas):
    cajas_ordenadas = sorted(cajas, key=lambda c: len(c.cola))
    for caja in cajas_ordenadas:
        if caja.agregar_cliente(cliente):
            return True
    return False
