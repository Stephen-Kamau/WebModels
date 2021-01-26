from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# for cleaning
from . import clean




def Home(request):
    return render(request , "spam/index.html")

def spam(request):
    return render(request , "spam/form.html")


@csrf_exempt
def getSpam(request):
    if request.method == "POST":
        text = request.POST['msg']


        # clean the textv received
        #special chars
        text = clean.special_char_removal(text)
        # remove stop words
        text = clean.removeStop(text)
        # vectorize
        vec = clean.loadVec()
        text = [text]
        text = vec.transform(text)

        # do the predictions
        clf = clean.loadModel()
        pred_probs = clf.predict_proba(text)
        #
        score = pred_probs[0]
        score = round(score.max() , 2)*100
        pre = clf.predict(text)
        # print(round(score  , 2))
        # print(f"score is  {pre}")
        if pre == 0:
            pred = 0
        else:
            pred = 1
        return JsonResponse({"pred":pred  , "score":round(score  , 2)})
    return JsonResponse({ "pred":" " , "score" : ""})
