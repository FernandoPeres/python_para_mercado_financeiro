import statistics as st

preco=[10,11,11,10,10,10,8,8,9,7,11,12,13,8,9]
print(preco)
#MÉDIA
media=st.mean(preco)
print("media: ",media)
#MODA
moda=st.mode(preco)
print("moda: ", moda)
#MEDIANA
mediana=st.median(preco)
print("mediana: ", mediana)
#DESVIO PADRÃO
desvio_padrao = st.stdev(preco)
print("desvio padrão: ", desvio_padrao)
#VARIÂNCIA
variancia=st.variance(preco)
print("variância: ", variancia)