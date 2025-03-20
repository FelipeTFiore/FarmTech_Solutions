# calcular_estatisticas.R
Sys.setlocale("LC_ALL", "Portuguese_Brazil.UTF-8")  # Configura o locale para UTF-8
cat(enc2utf8("Iniciando o script R...\n"))

tryCatch({
  # Define o caminho do arquivo CSV
  caminho_csv <- "C:/Users/Felipe/Desktop/FarmTech_Solutions/dados_culturas.csv"
  cat(enc2utf8("Lendo o arquivo CSV: "), caminho_csv, "\n")

  # Lê o arquivo CSV com encoding UTF-8
  dados <- read.csv(caminho_csv, fileEncoding = "UTF-8")
  cat(enc2utf8("Arquivo CSV lido com sucesso!\n"))
  cat(enc2utf8("Conteúdo do CSV:\n"))
  print(dados)  # Exibe o conteúdo do CSV

  # Verifica se há dados
  if (nrow(dados) == 0) {
    stop(enc2utf8("O arquivo CSV está vazio ou não contém dados válidos."))
  }

  # Verifica se as colunas existem
  if (!"base" %in% colnames(dados) || !"altura" %in% colnames(dados)) {
    stop(enc2utf8("O arquivo CSV deve conter as colunas 'base' e 'altura'."))
  }

  # Converte as colunas para numérico (se necessário)
  dados$base <- as.numeric(as.character(dados$base))
  dados$altura <- as.numeric(as.character(dados$altura))

  # Verifica se as colunas são numéricas
  if (any(is.na(dados$base)) || any(is.na(dados$altura))) {
    stop(enc2utf8("As colunas 'base' e 'altura' devem conter apenas números."))
  }

  # Calcula estatísticas
  media_base <- mean(dados$base)
  desvio_base <- sd(dados$base)

  media_altura <- mean(dados$altura)
  desvio_altura <- sd(dados$altura)

  # Exibe os resultados
  cat(enc2utf8("Estatísticas das Culturas:\n"))
  cat(enc2utf8("Base:\n"))
  cat(enc2utf8("  Média: "), media_base, "\n")
  cat(enc2utf8("  Desvio Padrão: "), desvio_base, "\n\n")

  cat(enc2utf8("Altura:\n"))
  cat(enc2utf8("  Média: "), media_altura, "\n")
  cat(enc2utf8("  Desvio Padrão: "), desvio_altura, "\n")
}, error = function(e) {
  cat(enc2utf8("Erro no script R:\n"))
  cat(enc2utf8(e$message), "\n")
})