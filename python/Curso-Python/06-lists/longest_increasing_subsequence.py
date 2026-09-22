numbers = [1, 2, 1, 2, 3, 1, 2, 3, 4, 2]

numbers = [3, 2, 1, 4, 5]


current_sequence = [numbers[0]]
longest_sequence = []


for i in range(len(numbers) - 1):
    
    if numbers[i+1] > numbers[i]:
        #print("Aumenta")
        current_sequence.append(numbers[i + 1])
    else:
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
            
        current_sequence = [numbers[i + 1]]
        

# Comprobar la última secuencia
if len(current_sequence) > len(longest_sequence):
    longest_sequence = current_sequence

print(longest_sequence)