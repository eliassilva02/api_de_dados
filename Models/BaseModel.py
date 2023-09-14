from pydantic import BaseModel


class JsonLinhas(BaseModel):
    lucro: list[str]
    dia: list[str]


class JsonBarras(BaseModel):
    lucro: list[str]
    empresa: list[str]


class FaturamentoPorDia(BaseModel):
    faturamento: list[str]
    dia: list[str]


class JsonDefault(BaseModel):
    Faturamento: str
    LinhasFaturamento: FaturamentoPorDia
    Lucro: str
    QtdeEmpresas: str
    Uf: str
    GraficoLinhas: JsonLinhas
    GraficoBarras: JsonBarras
