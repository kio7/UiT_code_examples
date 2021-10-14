genome = input("Enter a Genome string: ").upper()

length = len(genome)
count_1 = 0
count_2 = 0
failsafe = 0
end_of_genome = 0
beginning_of_genome = 0


while "ATG" in genome[end_of_genome:length]:
    failsafe += 1
    while True:
        if genome[count_1] == "A" and genome[count_1+1] == "T" and genome[count_1+2] == "G":
            beginning_of_genome = count_1 + 3
            count_2 = beginning_of_genome
            break
        else:
            count_1 += 1
        
    if "TAG" in genome[beginning_of_genome:length] or "TGA" in genome[beginning_of_genome:length] \
        or "TAA" in genome[beginning_of_genome:length]:

        while True:
            if genome[count_2] == "T" and genome[count_2+1] == "A" and genome[count_2+2] == "G" or \
            genome[count_2] == "T" and genome[count_2+1] == "G" and genome[count_2+2] == "A"  or \
            genome[count_2] == "T" and genome[count_2+1] == "A" and genome[count_2+2] == "A":
                end_of_genome = count_2

                if len(genome[beginning_of_genome:end_of_genome]) % 3 == 0 \
                and "ATG" not in genome[beginning_of_genome:end_of_genome]:
                    print(genome[beginning_of_genome:end_of_genome])

                beginning_of_genome = end_of_genome + 1
                count_1 += 3
                break

            else:
                count_2 += 1

    else:
        if "ATG" in genome[beginning_of_genome:end_of_genome]:
                    failsafe2 = 1
                    count_1 += 3
                    break
        if len(genome[beginning_of_genome:length]) % 3 == 0 \
        and "ATG" not in genome[beginning_of_genome:length]:
            print(genome[beginning_of_genome:length])
            break
        break

else:
    if failsafe < 1:
        print("no gene is found.")