
pops = c("French", "Basque", "Spanish")
for(i in 1:length(pops)){

print(i)
pop_interest = pops[i]
yamnaya_europe_f4 <- f4(data = f2_blocks, pop1 = "Mbuti", pop2 = "Yamnaya", pop3 = "LBK", pop4 = pop_interest)

cat("Testing: Yamnaya and", pop_interest, "\n")
print(yamnaya_europe_f4)

}

