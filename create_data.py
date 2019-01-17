import json
from agenda.models import Cadastro, OrdemDeCompra

with open('data.json') as f:
    datas = json.load(f)

# for data in datas['ordem_de_compra']:
#     print(data)


aux = []
for data in datas['ordem_de_compra']:
    _cli_name = data['cli_name']
    cli_name = Cadastro.objects.filter(nome=_cli_name).first()
    if cli_name:
        oc = OrdemDeCompra(
            cli_code=data['cli_code'],
            cli_name=cli_name,
            address1=data['address1'],
            state=data['state']
        )
        aux.append(oc)


OrdemDeCompra.objects.bulk_create(aux)
