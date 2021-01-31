# Solution Author : Srikanth

# data structure to combine the buyers particpation and percentage
class Bid:
    def __init__(self,participation, percentage, index ):
        super().__init__()
        self.participation = participation
        self.percentage = percentage
        self.index = index

# return the sorted Bid objects. key = participation
def sortedBids(bids):
    bids.sort(key=lambda x: x.participation, reverse=True)
    return bids

# process the raw_input and construct the sorted bids list
def construct_bids(raw_participations, raw_percentages):
    bid_array = []
    # exit for empty values
    if (not raw_participations ) or (not raw_percentages):
        return None

    participations =  raw_participations.split(' ')
    percentages = raw_percentages.split(' ')

    # if lengths do not match exit
    if len(participations) != len(percentages):
        return None

    # valid bids ? yes
    for value in range(len(participations)):
        bid = Bid(participation=float(participations[value]), 
                        percentage=float(percentages[value]), index=value)  
        bid_array.append(bid)

    # sort the bids
    sorted_bids = sortedBids(bid_array)
    return sorted_bids

# total participation amount for the given bids
def get_total_participation(*bids):
    total = 0.0
    for bid in bids:
        total += (bid.percentage * bid.participation)/100
    return total

# logic to give the indices to give max profit to the seller
def max_seller_profit(sorted_bids, loan_amount):
    result = []
    max_amount = 0.0
    # OUTER loop
    for bid_index in range(0, len(sorted_bids)):
        # check if the single bid participation value matches the loan amount
        if sorted_bids[bid_index].participation == loan_amount:
            total = get_total_participation(sorted_bids[bid_index])
            if total > max_amount:
                result = [sorted_bids[bid_index].index]
            max_amount = max(max_amount, total)

        # left points to the START & right to the END
        left, right = bid_index + 1, len(sorted_bids) - 1
        target_amount = loan_amount - sorted_bids[bid_index].participation

        # INNER loop
        while(left < right):
            # check if outer index & left bid participations matches loan amount
            if (sorted_bids[bid_index].participation + sorted_bids[left].participation) == target_amount:
                total = get_total_participation(sorted_bids[bid_index], sorted_bids[left])
                if total > max_amount:
                    result = [sorted_bids[bid_index].index, sorted_bids[left].index]
                max_amount = max(max_amount, total)

            # check if outer index & left bid participations matches loan amount    
            if (sorted_bids[bid_index].participation + sorted_bids[right].participation) == target_amount:
                total = get_total_participation(sorted_bids[bid_index], sorted_bids[right])
                if total > max_amount:
                    result = [sorted_bids[bid_index].index, sorted_bids[right].index]
                max_amount = max(max_amount, total)

            current_amount = sorted_bids[left].participation + sorted_bids[right].participation

            # check left & right bid participations matches loan amount
            if current_amount == loan_amount:
                total = get_total_participation(sorted_bids[left], sorted_bids[right])
                if total > max_amount:
                    result = [sorted_bids[left].index, sorted_bids[right].index]
                max_amount = max(max_amount, total)

            # start comparing from left and from right
            if current_amount == target_amount:
                total = get_total_participation(sorted_bids[bid_index], sorted_bids[left], sorted_bids[right])
                if total > max_amount:
                    result = [sorted_bids[bid_index].index, sorted_bids[left].index, sorted_bids[right].index]
                max_amount = max(max_amount, total)
            
            # shift left by one or reduce right by one 
            if target_amount > current_amount:
                left += 1
            else:
                right -= 1
    if max_amount > 0.0:
        print("max amount for the seller is: {}".format(max_amount))
    return result


if __name__ == "__main__":
    # take input form the user
    raw_loan_amount = input("Enter your value:\n")
    raw_participations = input("Enter your partiiation:\n")
    raw_percentages = input("Enter your percentages:\n")

    if not raw_loan_amount:
        print("Enter valid loan amount")
        exit(1)    
    loan_amount = float(raw_loan_amount)

    # get the sorted array of bid objects
    sorted_bids = construct_bids(raw_participations, raw_percentages)
    # check if particiaption exceeds loan amount
    for bid in sorted_bids:
        if bid.participation > loan_amount:
            print("Particiaption amount should NOT exceed loan amount")
            exit(1)

    if sorted_bids is not None:
        indices = max_seller_profit(sorted_bids, loan_amount)
        if not indices:
            print("There is no particiaption sum that equals given loan amount")
            exit(1)
        print("indeces for seller max profit: {}".format(indices))
    else:
        print("Enter valid particiaptions and percentages")
        exit(1)

