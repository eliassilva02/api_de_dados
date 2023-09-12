import sqlite3
import pandas as pd


class DataBase():
    def CreateDataBase():
        # Criar uma conexão com o banco de dados SQLite
        conn = sqlite3.connect("petrobras.db")

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Criar uma tabela no banco de dados
        cursor.execute("""
            CREATE TABLE pj (
                Cnpj INTEGER PRIMARY KEY NOT NULL,
                Nome TEXT NOT NULL,
                Cidade TEXT NOT NULL,
                Regiao TEXT NOT NULL,
                Uf TEXT NOT NULL,
                Cep INTEGER NOT NULL
                );"""
                       )

        # Criar uma tabela no banco de dados
        cursor.execute("""
            CREATE TABLE tabela_produtos (
                ID INTEGER PRIMARY KEY NOT NULL,
                Empresa_CNPJ INTEGER,
                Produto TEXT NOT NULL,
                Data_Coleta DATE NOT NULL,
                Valor_Venda REAL NOT NULL,
                Valor_Compra REAL NOT NULL,
                Unidade_Medida TEXT NOT NULL,
                Bandeira TEXT NOT NULL,
                FOREIGN KEY (Empresa_CNPJ) REFERENCES pj(cnpj)
                );"""
                       )

        DataBase.InsertFilesToDataBase(conn)

        cursor.close()

        conn.close()

    def InsertFilesToDataBase(conn):
        files = [
            'C:\\Users\\IMendes_41\\OneDrive\\Preto-Bras\\BaseDados\\Relatório_Combustiveis.xlsx',
            'C:\\Users\\IMendes_41\\OneDrive\\Preto-Bras\\BaseDados\\Vendas.xlsx'
        ]

        for i, file in enumerate(files):
            table = 'pj' if i == 0 else 'tabela_produtos'

            dt = Files.ReadFile(file)
            dt.to_sql(table, conn, if_exists="replace", index=False)


class Files():
    def ReadFile(path):
        dt = pd.read_excel(path,  dtype={'cnpj': str})

        return dt


DataBase.CreateDataBase()
