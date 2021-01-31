loan_amount = 200
#partication = [100, 90, 30, 200, 80, 100]
#percentage = [99, 100, 99, 98.9, 100, 99]
partication = [100, 90, 30, 200, 80, 100]
percentage = [100, 99, 99, 98.9, 100, 99]

def generate_buyer_map(partication, percentage):
    buyer_dict = {}
    if len(partication) != len(percentage):
        return None

    for i in range(len(partication)):
        if partication[i] not in buyer_dict:
            buyer_dict[partication[i]] = [i, percentage[i]]
        else:
            # Handle the case for duplicates
            buyer_dict[partication[i]].append([i, percentage[i]])
    return buyer_dict

def hasing_solution(loan_amount, partication, percentage):
    result = []
    max_amount = 0.0
    count = 0;
    space = 0;
    if len(partication) != len(percentage):
        return None

    for i in range(0, len(partication) - 1):
        if partication[i] == loan_amount:
            total = (percentage[i] * partication[i])/100
            if total > max_amount:
                result = [i]
            max_amount = max(max_amount, total)
        current_amount = loan_amount - partication[i]
        participation_dict = {}
        for j in range(i+1, len(partication)):
            if partication[i] + partication[j] == loan_amount:
                total = (percentage[i] * partication[i])/100 + (percentage[j] * partication[j])/100
                if total > max_amount:
                    result = [i,j]
                max_amount = max(max_amount,total)

            to_check = current_amount - partication[j]

            if participation_dict.get(to_check):
                index = participation_dict[to_check][0]
                total = (percentage[i] * partication[i])/100 + (percentage[j] * partication[j])/100 + (percentage[index] * partication[index])/100
                if total > max_amount:
                    result = [i,j,index]
                max_amount = max(max_amount,total)
                #result.append([i, j, index])
            else:
                participation_dict[partication[j]] = [j,percentage[j]]    
        print(participation_dict)        
        space += len(participation_dict)
        print(space)
    return result

print(hasing_solution(loan_amount,partication,percentage))
#print(generate_buyer_map(partication,percentage))
