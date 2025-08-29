SELECT
    LPAD(Cli.IdCliente, 3 ,'0')IdCliente,
    Bol.sacado_nome,
    Bol.Emissao,
    Count(Cli.IdCliente) Titulos,
    Sum(Bol.Valor) as Valor
FROM TCOBBOLETO Bol
    -- LEFT JOIN TRECCLIENTE Cli ON(Bol.IdCliente = Cli.IdCliente) ---
where
    Bol.Emissao >= {?Data Inicial} AND
    Bol.Emissao <= {?pData Final}
group by
    Cli.IdCliente,
    Bol.emissao,
    Cli.Nome