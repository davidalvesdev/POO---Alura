from def_banco import cria_conta, saca, deposita, extrato

conta = cria_conta(123, "nico", 55.0, 1000.0)

deposita(conta, 15.0)
extrato(conta)
saca(conta, 20.0)
extrato(conta)
