# API de Dados de Combustíveis

Esta API fornece indicadores e dados para gráficos de uma planilha de Combustíveis com valores de Janeiro de 2007 disponibilizada pelo Governo Federal.

## Indicadores
- Faturamento
- Lucro Líquido
- Quantidade de Postos
- Estado que mais lucra com a venda de Combustíveis
- Lucro divido sob os dias de janeiro
- Faturamento divido sob os dias de janeiro
- 5 postos que mais lucram com a venda de Combustíveis

## Libs usadas
- Flask
- Pydantic
- Pandas
- SQLite3
- Locale
- Flask-Pydantic-Spec
- Flask-CORS

## Endpoints
| Endpoint         | Métodos | Regra                                |
|----------------- | ------- | ------------------------------------ |
| Busca todos os dados     | GET     | /GetData                    |
| Redoc   | GET     | /apidoc/redoc                        |
| Swagger | GET     | /apidoc/swagger                      |
| OpenApi          | GET     | /apidoc/openapi.json                 |


*v1.0.0*
