# Serverless Pattern
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Sever-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)

Muchas veces no es complicado iniciar un proyecto de backend, aun cuando tenemos definido algún framework instalado. Por eso en este proyecto de git se muestra una sugerencia para iniciar un proyecto de serverless en la nube de azure, utilizando su producto para ellos, las azure functions.

Aunque este ejemplo se centra con su integracion en SQL Server, puede migrarse a cualquier otro gestor de base de datos agregando las dependencias correspondientes en el archivo [code/requirements.txt](code/requirements.txt)

## Para correr este proyecto

Para este ejemplo se utilizará el Azure Toolkits del IDE Visual Studio Code, por lo que se recomienda utilizar el mismo IDE. Para instalar el complemento de Azure Toolkits, se puede guiar del [siguiente enlace](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=csharp).

Si no tenemos instalador la herramienta func core tools, se puede instalar ejecutando el siguiente comando.

```
npm install -g azure-functions-core-tools@3 --unsafe-perm true
```

De igual forma se debe copiar y modificar las variables declaradas en el en archivo `local.settings.json.example` y renombrarlo a `local.settings.json`. Estas serán nuestras variables de entorno, donde queremos guardar la información sensible como base de datos, llaves de acceso, etc.

Creamos un ambiente virtual para mejor manejo del proyecto con los comandos:

```
python -m virutalenv venv
```

En caso de no tener el paquete de virutalenv podemos instalarlo en el sistema con el siguiente comando:
```
pip install virtualenv
```

Finalmente ejecutamos el ambiente virutal.

En windows
```
venv\Scripts\activate
```

En mac o linux
```
source venv/bin/activate
```

## Documentacion de API

De igual manera se deja un [template de la API en OpenAPI3](documentation/api/api_gateway.yaml), para integrarse facilmente con swagger o postman

