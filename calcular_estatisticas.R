# Ler os dados do arquivo CSV
dados <- read.csv("dados_culturas.csv")

# Calcular a área (base * altura)
dados$area <- dados$base * dados$altura

# Calcular a média e o desvio padrão da área
media_area <- mean(dados$area)
desvio_area <- sd(dados$area)

# Exibir os resultados
cat("Média da área plantada:", media_area, "\n")
cat("Desvio padrão da área plantada:", desvio_area, "\n")