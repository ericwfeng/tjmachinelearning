
#change name of file to load in data from a different file.
#for testing data (no labels)
def getDataUnlabeled():
    x = []
    input = open("test.csv").read().split("\n")
    for index, i in enumerate(input):
        inputArray = i.split(",")
        if(index==0):
            inputArray[0] = '4'
        if(len(inputArray)==9): #number of features           
            x.append(inputArray)
        else:
            print(len(inputArray))
    return x

#change name of file to load in data from a different file.
#for training data (with labels)
def getDataLabeled():
    x = []
    y = []
    input = open("train.csv").read().split("\n")
    for i in input:
        inputArray = i.split(",")
        if(len(inputArray)==10): #number of features + number of labels        
            exp = inputArray.pop(len(inputArray)-1)
            x.append(inputArray)
            y.append(exp)
        else:
            print(len(inputArray))
    return x,y

#pass array of labels and method will generate output txt
def generateOutputFile(y_test):
	with open('out.txt', 'w') as f:
	    f.write("id,solution\n")
	    for i in range(len(y_test)):
	        f.write(str(i+1)+","+str(y_test[i]+"\n"))



X_train, y_train = getDataLabeled()
X_test = getDataUnlabeled()

# TODO: Write some ML
# TODO: use model to generate y_test from X_test
# generateOutputFile(y_test)