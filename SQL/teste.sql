SELECT Cob.Empresa,
       Cob.Tipo AS TipoOcorrencia,
       LPad(Cob.IdOcorrencia, 3, '0') as IdOcorrencia,
       Cob.Data DataOcorrencia,
       Par.IdParcela,
       Par.IdDocumento,
       Bol.IdTipoDocumento,
       Cli.Nome,
       Tdc.Descricao,
       Par.Parcela,
       LPad(Par.Parcela,3,'0')||'/'||LPad(Doc.QtdeParcela,3,'0') AS NumeroParcela,
       Par.Vencimento,
       Par.ValorPendente,
       Par.Valor,
       Par.Valido,
       Bol.NossoNumero
FROM   TCobRemessaOcorrencia Cob
            JOIN TCobBoleto        Bol ON (Bol.Empresa     = Cob.Empresa
                                       AND Bol.IdBoleto    = Cob.IdBoleto)
       LEFT JOIN TRecParcela       Par ON (Par.Empresa     = Bol.Empresa
                                       AND Par.IdParcela   = Bol.IdParcela)
       LEFT JOIN TRecDocumento     Doc ON (Doc.Empresa     = Par.Empresa
                                       AND Doc.IdDocumento = Par.IdDocumento)
       LEFT JOIN TRecDocumentoTipo Tdc ON (Tdc.Empresa     = Bol.Empresa
                                       AND Tdc.IdTipo      = Bol.IdTipoDocumento)
       LEFT JOIN TRecCliente       Cli ON (Cli.IdCliente   = Bol.SACADO_IDPESSOA)
WHERE Cob.Empresa      = {?Empresa}       
      AND Cob.IdRemessa  = {?IdRemessa}
