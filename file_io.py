
# Return tuples with descriptions and and the its corresponding sequence -> (description, sequence)
def read_sequences(filename):
    with open('data/' + filename, 'r') as f:
        text = f.read()
    
    # Split all the sequences
    sequences = text.split('>')[1:]

    # Split the sequences and descriptions and remove all the "\n"
    for i in range(0, len(sequences)):
        sequences[i] = sequences[i].split('\n', 1)  
        sequences[i][1] = sequences[i][1].replace('\n', '')
        sequences[i] = (sequences[i][0], sequences[i][1])

    return sequences


def write_matrix(matrix, seq1_index, seq2_index):
    with open('results/matrices/' + str(seq1_index+1) + '-' + str(seq2_index+1) + '_matrix' + '.txt', 'w') as f:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                f.write("{0}".format(str(matrix[i][j]).rjust(5)))
            f.write('\n')


def write_alignments(seq1, seq2, seq1_index, seq2_index, score):
    with open('results/alignments/' + str(seq1_index+1) + '-' + str(seq2_index+1) + '.txt', 'w') as f:
        f.write('Score: ' + str(score) + '\n\n')
        f.write('Alignment: \n')
        f.write('Sequence ' + str(seq1_index + 1) + ': ' + seq1 + '\n')
        f.write('Sequence ' + str(seq2_index + 1) + ': ' + seq2)
