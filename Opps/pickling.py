import pickle
# cars=["audi","bmw","ferrari","suzuki","toyota"]
# file = "mycarsss.pkl"
# fileobj=open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

# read the values from pkl file




file="mycarsss.pkl"
fileObj=open(file,'rb')
mycars=pickle.load(fileObj)
print(mycars)