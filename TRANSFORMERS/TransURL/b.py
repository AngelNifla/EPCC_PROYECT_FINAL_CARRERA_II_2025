input_file = "Data/Grambedding_dataset/Train.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

with open("benign_urls.txt", "w") as benign, open("malicious_urls.txt", "w") as malicious:
    for line in lines:
        line = line.strip()
        if line.endswith("0"):
            benign.write(line + "\n")
        elif line.endswith("1"):
            malicious.write(line + "\n")
