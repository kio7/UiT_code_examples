def gene_finder(genome):
    genome = genome.upper()
    start = "ATG"
    end1 = "TAA"
    end2 = "TGA"
    end3 = "TAG"

    index, index_end, failsafe, gene_num = 0, 0, 0, 1


    while start in genome[index:]: 
        failsafe += 1

        while True:
            if start == genome[index:index+3]:
                index += 3
                index_end = index
                break
            else:
                index += 1

#      find any ending after the first ATG, it can be endings: 1-4
        if end1 in genome[index:] or end2 in genome[index:] or end3 in genome[index:]:
            while True:
                if end1 == genome[index_end:index_end+3] or end2 == genome[index_end:index_end+3] \
                or end3 == genome[index_end:index_end+3]:
                    
                    if len(genome[index:index_end]) % 3 == 0:
                        if len(genome[index:index_end]) != 0 and start not in genome[index:index_end]:
                            print(f"Gene nr.{gene_num}: {genome[index:index_end]}")
                            gene_num += 1
                            
                    index = index_end + 1
                    break

                else:
                    index_end += 1
        else:
            if genome[index:] % 3 == 0 and start not in genome[index:]:
                print(f"Gene nr.{gene_num}: {genome[index:]}")
                gene_num += 1
                break

#   The failsafe makes sure that if it has found ATG once and does not find it again it will not continue.
    else:
        if failsafe < 1:
            return False


def main():
    genome = input("Enter a genome: ").upper()

#   For testing "the" string:
#    genome = "atgaaaaaagcaaaattattcggttttagtttgattgcattaggtttatcagtttcacttgcagcatgtggtggtggcaaaggcaaaaccgctgaaagcggcggtggcaaaggggatgcagcgcatagtgctgtaatcattacagatacaggcggcgtggatgacaagtcgttcaaccaatcttcttgggaaggattgcaagcttggggtaaagaacatgatttaccagaaggttcaaaagggtatgcatatattcaatcgaatgatgcagctgactatacaaccaatattgaccaagcggtatcaagtaaattcaacacaatctttggtattggctacttgctaaaagatgcaatttcttctgcagcagatgccaaccctgatacaaactttgttttaatcgatgatcaaatcgatggcaaaaagaatgtcgtttctgcaacatttagagataatgaagcagcttacttagccggtgttgctgctgcaaatgaaacaaaaacgaacaaagtcggttttgttggtggtgaagaaggggtcgtaattgaccgtttccaagctggttttgaaaaaggtgtggctgatgctgcgaaagaattaggtaaagaaattactgttgatacgaaatatgcggcttcatttgctgatcctgccaaagggaaagctttagctgctgcaatgtaccaaaacggcgttgatatcatcttccatgcttctggtgcgactggacaaggggtcttccaagaagcaaaagacttgaatgaatcaggttctggcgacaaagtttgggtaatcggcgttgaccgcgatcaagatgctgatggcaagtacaaaacaaaagacggcaaagaagacaacttcacgttaacttcaacgcttaaaggtgtcggcacagcggttcaagatattgccaaccgtgcgttagaagacaaattccctggtggcgaacatttagtttatggattaaaagatggtggcgttgacttaacagacggctatttaaacgacaaaacaaaagaagctgttaaaacagcaaaagataaagtaatctcaggtgacgtaaaagtcccagaaaaaccagaataa"
    
    print("=" * 20)

    if gene_finder(genome) == False:
        print("No gene was found.")

    print("=" * 20)

if __name__ == "__main__":
    main()
    