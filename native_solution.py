# Brute Force Solution O(n-cube)

loan_amount = 200
#partication = [100, 90, 30, 200, 80, 100]
#percentage = [99, 100, 99, 98.9, 100, 99]
partication = [100, 90, 30, 200, 80, 100]
percentage = [99, 99, 98, 99.8, 100, 99]

def native_solution(loan_amount, partication, percentage):
    result = []
    if len(partication) != len(percentage):
        return None
    max_amount = 0;
    count = 0;
    for i in range(0, len(partication)):
        if partication[i] == loan_amount:
            total = (percentage[i] * partication[i])/100
            if total > max_amount:
                result = [i]
            max_amount = max(max_amount, total)
        for j in range(i+1, len(partication)):
            if partication[i] + partication[j] == loan_amount:
                total = (percentage[i] * partication[i])/100 + (percentage[j] * partication[j])/100
                if total > max_amount:
                    result = [i,j]
                max_amount = max(max_amount,total)
            for k in range(i+2, len(partication)):
                count += 1
                if partication[i] + partication[j] + partication[k] == loan_amount:
                    total = (percentage[i] * partication[i])/100 + (percentage[j] * partication[j])/100 + (percentage[k] * partication[k])/100
                    if total > max_amount:
                        result = [i,j,k]
                    max_amount = max(max_amount,total)
    print("max amount for the seller is: {}".format(max_amount))
    print("conter is {} --> to check the complexity:".format(count))
    return result

print(native_solution(loan_amount, partication, percentage))


