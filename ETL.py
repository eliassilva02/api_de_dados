import sqlite3
from ObjectAPI import JsonDefault, JsonLinhas, JsonBarras
from locale import setlocale, format_string, LC_ALL


class Number:
    def FormatNumber(number):

        setlocale(LC_ALL, '')
        number = format_string('%d', int(number), grouping=True)

        num_pontos = number.count('.')
        splitNumber = str(number).split('.')

        match num_pontos:
            case 1:
                number = splitNumber[0] + ' Mil'
                return number
            case 2:
                number = splitNumber[0] + ' Mi'
                return number
            case _:
                return number


class Application:
    def SqlQuery(query):
        conn = sqlite3.connect("petrobras.db")

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Executar a consulta
        cursor.execute(query)

        # Recuperar os resultados
        resultados = cursor.fetchall()

        return resultados

    def Faturamento():
        consulta = f"SELECT SUM(venda) FROM tabela_produtos"

        resultados = Application.SqlQuery(consulta)

        faturamento = resultados[0][0]

        return Number.FormatNumber(faturamento)

    def Lucro():
        consulta = f"SELECT SUM(venda - compra) FROM tabela_produtos"

        resultados = Application.SqlQuery(consulta)

        lucro = resultados[0][0]

        return Number.FormatNumber(lucro)

    def QuantidadePostos():
        consulta = f"SELECT COUNT(cnpj) FROM pj"

        resultados = Application.SqlQuery(consulta)

        qtdePostos = resultados[0][0]

        return Number.FormatNumber(qtdePostos)

    def UFMaisCara():
        consulta = f"""SELECT SUM(t1.venda - t1.compra),
                        t2.uf
                    FROM tabela_produtos t1
                    INNER JOIN pj t2 ON t1.cnpj = t2.Cnpj
                    GROUP BY 2
                    ORDER BY 1 DESC
                    LIMIT 1"""

        resultados = Application.SqlQuery(consulta)

        uf = resultados[0][1]

        return uf

    def LucroPorDia():
        lucro = []
        dia = []

        consulta = f"""SELECT SUM(venda - compra),
                    strftime('%d', data, 'unixepoch')
                FROM tabela_produtos
                GROUP BY 2
                ORDER BY 2;"""

        resultados = Application.SqlQuery(consulta)

        for resultado in resultados:
            valor = Number.FormatNumber(resultado[0])
            lucro.append(valor)

            dia.append(resultado[1])

        return lucro, dia

    def LucroPorRazaoSocial():
        lucro = []
        empresa = []

        consulta = f"""SELECT SUM(t1.venda - t1.compra) as lucro,
                    t2.nome
                FROM tabela_produtos t1
                INNER JOIN pj t2 ON t1.cnpj = t2.Cnpj
                GROUP BY 2
                ORDER BY 1 DESC
                LIMIT 10;"""

        resultados = Application.SqlQuery(consulta)

        for resultado in resultados:
            # Formatando valores
            valor = Number.FormatNumber(resultado[0])
            lucro.append(valor)
            # Formatando strings
            empresaSplit = resultado[1].split()
            razaoSocial = ' '.join(empresaSplit[:2])
            empresa.append(razaoSocial)

        return lucro, empresa

    def ConstruindoJson():
        lucroDiario = Application.LucroPorDia()
        lucroRazaoSocial = Application.LucroPorRazaoSocial()

        json = JsonDefault(
            Faturamento=Application.Faturamento(),
            Lucro=Application.Lucro(),
            QtdeEmpresas=Application.QuantidadePostos(),
            Uf=Application.UFMaisCara(),
            GraficoLinhas=JsonLinhas(
                lucro=lucroDiario[0],
                dia=lucroDiario[1]
            ),
            GraficoBarras=JsonBarras(
                lucro=lucroRazaoSocial[0],
                empresa=lucroRazaoSocial[1]
            )
        )

        return json.dict()
