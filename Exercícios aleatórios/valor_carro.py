custo_fab = 10000
percent_dist = 28/100
percent_imp = 45/100

custo_final = custo_fab + (custo_fab * percent_dist) + (custo_fab * percent_imp)

print("Custo final de fabricação é de: ", custo_final)

assert custo_final == 17300.0