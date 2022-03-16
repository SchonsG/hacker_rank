def checkArray(arr, threshold):
    count = 0
    for value in arr:  # [60, 30, 25, 33]
        for number in arr:  # [60, 30, 25, 33]
            if value == number:  # 60 == 30
                count +=1
        if count >= threshold:
            return True
        count = 0
        
    return False


print(checkArray([60, 30, 25, 33], 2))

