#Recursively partition the list based on the characters sum of percentages
def partition(chars_list):
    if(len(chars_list) == 1):
        chars_list[0][0][1][1] = True #Partitioned
        return

    bestsum = 1
    differential = 0 #value used to find the best partitioning
    temp = -1 #counter used to determine where the list will be split for further partitioning?
    for i in range(len(chars_list)):
        newsum = 0
        for k in range(i):
            differential += chars_list[k][0][1][0]
        for j in range(i, len(chars_list)):
            newsum += chars_list[j][0][1][0] #sum the probabilities to find the least diff
        if(abs(differential/2 - newsum) < abs(differential/2 - bestsum)):
            bestsum = newsum
            temp = i
    for sublist in chars_list[:temp]:
        sublist[0][1][2].append(0)
    for sublist in chars_list[temp:]:
        sublist[0][1][2].append(1)

    partition(chars_list[:temp])
    partition(chars_list[temp:])

#Replace each character in raw_data with counterpart compressed set
def compress(raw_data, chars_dict):
    compressed_data = []
    for item in raw_data: 
            raw_data[raw_data.index(item)] = chars_dict[item][2]
    
    #Alternative way: Save list of lists instead of each binary digit
    for item in raw_data:
        for binary in item:
            compressed_data.append(binary)

    return(compressed_data)