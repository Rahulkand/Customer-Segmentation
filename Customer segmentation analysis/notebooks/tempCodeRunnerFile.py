i=0
    j=i+1
    add_arr = []
    while(i<len(temp_arr)-1 and j<len(temp_arr)):
          temp = temp_arr[i] + temp_arr[j]
          add_arr.append(temp)
          i = i + 1
          j = j + 1