from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import numpy as np
from .imgtotext import convert
from .yolo import objdetect
# Create your views here.
# with open('models\ectorizer.pickle', 'rb') as efile:
#     vectorizer = pickle.load(efile) #tera vectorizer daal de yaha
# index_word = dict([(index,word) for word, index in tokenizer.word_index.items()])
# def predict_caption(image):
#     '''
#     image.shape = (1,4462)
#     '''

#     in_text = 'startseq'

#     for iword in range(maxlen):
#         sequence = tokenizer.texts_to_sequences([in_text])[0]
#         sequence = pad_sequences([sequence],maxlen)
#         yhat = model.predict([image,sequence],verbose=0)
#         yhat = np.argmax(yhat)
#         newword = index_word[yhat]
#         in_text += " " + newword
#         if newword == "endseq":
#             break
#     return(in_text)


def index(request):
    context={'a':1}
    return render(request,'index.html',context)

img_height, img_width=224,224

def predictImage(request):
    print (request)
    print (request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName
    text=convert(testimage)
    print(text)
    
    return render(request,'index.html',{"text":text}) 

 

def detect(request):
    print (request)
    print (request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName
    objdetect(testimage)
    
    return render(request,'index.html') 


# def caption(request):
#     print (request)
#     print (request.POST.dict())
#     fileObj=request.FILES['filePath']
#     fs=FileSystemStorage()
#     filePathName=fs.save(fileObj.name,fileObj)
#     filePathName=fs.url(filePathName)
#     testimage='.'+filePathName
#     text=predict_caption(testimage)
#     print(text)
    
#     return render(request,'crop_index.html',{"text":text})