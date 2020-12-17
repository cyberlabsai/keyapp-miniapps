# MiniApp: Python+Bottle

Esta é a implementação usando `bottle`, mas deve ser bem familiar para
quem já trabalha com `flask` (ambos são meio aparentados, afinal).

## Rodando

Versão do Python requerida: **pelo menos 3.6**.

### Variáveis de ambiente

Primeiro, exporte as seguintes variáveis de ambiente:

* `PORT`
* `KEYAPP_KEY`
* `KEYAPP_SECRET`
* `KEYAPP_URL` (geralmente `https://api.keyapp.ai/v1`)

Para gerar credenciais de acesso para sua aplicação, consulte:

https://api.keyapp.ai/docs/autenticacao/


Já as seguintes variáveis são opcionais:

* `DOMAIN` : o domínio em que sua miniapp se encontra. Default=`localhost`
* `BASE_PATH` : o caminho base, caso sua miniapp esteja dentro de um
  diretório (e esse diretório precise constar nas URLs)

### Instalando os requirements

Com o devido virtualenv ativado, instale os requirements do projeto:

```bash
$ python3 -m pip install -r requirements.txt
```

### Executando

(Você sempre pode consultar o `Procfile`.)

```bash
$ python3 -m miniapp
```
