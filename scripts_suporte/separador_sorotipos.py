import pandas as pd
from Bio import SeqIO

df = pd.read_csv("sequences.csv", sep=',')

df = df[df["Organism_Name"] != "Dengue virus"]


nome_fasta = "sequences.fasta"


with open(nome_fasta) as align:
    dic_seq = {str(record.id):str(record.seq) for record in SeqIO.parse(align,'fasta')}
with open("DENV1.fasta","w") as denv1, open("DENV2.fasta","w") as denv2, open("DENV3.fasta","w") as denv3:
    for nome_virus_fasta in dic_seq:
        if nome_virus_fasta in df["Accession"].tolist():
            temp_df = df[df["Accession"] == nome_virus_fasta]
            sorotipo = str(temp_df["Organism_Name"].item())
            novo_nome_virus = sorotipo.replace(" ","_")+"_"+nome_virus_fasta
            if sorotipo == "dengue virus type 1":
                denv1.write(f">{novo_nome_virus}\n")
                denv1.write(f"{dic_seq[nome_virus_fasta]}\n")
            elif sorotipo == "dengue virus type 2":
                denv2.write(f">{novo_nome_virus}\n")
                denv2.write(f"{dic_seq[nome_virus_fasta]}\n")
            elif sorotipo == "dengue virus type 3":
                denv3.write(f">{novo_nome_virus}\n")
                denv3.write(f"{dic_seq[nome_virus_fasta]}\n")
            else:
                print("sorotipo não encontrado")