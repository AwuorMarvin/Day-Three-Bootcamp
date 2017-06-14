def words(sentence):
    lib = {}
    count = 0
    sentence_list = sentence.split()
    length = len(sentence_list)
  
    for word in sentence_list:
        for i in range(length):
            if sentence_list[i].isdigit() == True:
                if sentence_list[i] == word:
                    count+=1
                    lib[int(sentence_list[i])] = count
            else:
                if sentence_list[i] == word:
                    count+=1
                    lib[sentence_list[i]] = count
        count = 0
        
    return lib
    
  
words('This is a test')