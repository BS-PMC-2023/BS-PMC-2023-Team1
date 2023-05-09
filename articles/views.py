from django.shortcuts import render
from OurArticlesModel import articlesModel
from registration.models import UserData
from .models import PredictionApproves


# Create your views here.
def catalog(request):
    if request.method == 'POST':
        if request.POST.get('likeBtn.x'):
            isApprove = True
        else:
            isApprove = False
        addApprove(request, isApprove)

    try:
        engine = articlesModel.initializeEngine("News")
        df = articlesModel.getPage(engine, 3)

        return render(request, 'articles/article.html', {'data': df.iterrows()})
    except:
        return render(request, 'articles/article.html')


def addApprove(request, isApprove: bool):
    data = request.POST

    link = data['link']
    expert = UserData.objects.filter(user_id=request.user.id).first()

    # Check if already exists, and delete if it is (To avoid duplicates)
    predictObj = PredictionApproves.objects.filter(link=link, expertId=request.user.id)
    if predictObj:
        predictObj.all().delete()

    # Add the new approval/denial
    PredictionApproves.objects.create(
        link = link,
        expertId = request.user.id,
        expertName = expert.firstname + ' ' + expert.lastname,
        approved = isApprove
    )
