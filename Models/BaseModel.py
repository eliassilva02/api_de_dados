from pydantic import BaseModel


class JsonLinhas(BaseModel):
    lucro: list[str]
    dia: list[str]


class JsonBarras(BaseModel):
    lucro: list[str]
    empresa: list[str]


class JsonDefault(BaseModel):
    Faturamento: str
    Lucro: str
    QtdeEmpresas: str
    Uf: str
    GraficoLinhas: JsonLinhas
    GraficoBarras: JsonBarras
