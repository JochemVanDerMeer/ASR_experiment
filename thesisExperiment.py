import csv

filepath = "/Users/jochemvandermeer/Documents/Computing_Science_Year_4/ASR/thesisExperiment.py"

punctuation = ['.','?',',','-',"'"]
punctuationCounterCorrect = {'.': 0, '?':0 ,',': 0,'-': 0,"'": 0}
punctuationCounterIncorrect = {'.': 0, '?':0 ,',': 0,'-': 0,"'": 0}
punctuationCounterTotal = {'.': 0, '?':0 ,',': 0,'-': 0,"'": 0}

with open ('predictions_clean.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        cleanGeneratedText = row[1].lower().split(' ')
        actualText = row[3].lower().split(' ')
        for word in actualText:
            #case 1, the puncutation mark is seperate
            if word in punctuation:
                if word in cleanGeneratedText:
                    punctuationCounterCorrect[word] += 1
                else:
                        punctuationCounterIncorrect[word] += 1
            #case 2, the punctuation mark is connected to a word
            for character in word:     
                if character in punctuation:
                    if word in cleanGeneratedText:
                        punctuationCounterCorrect[character] += 1
                    else:
                        punctuationCounterIncorrect[character] += 1

    for i in punctuation:
        punctuationCounterTotal[i] = punctuationCounterCorrect[i] + punctuationCounterIncorrect[i]

    for j in punctuation:
        percentageCorrect = round((punctuationCounterCorrect[j] / punctuationCounterTotal[j]) * 100, 2)
        print("The punctuation mark ", j, " is ", percentageCorrect,"% correct.")