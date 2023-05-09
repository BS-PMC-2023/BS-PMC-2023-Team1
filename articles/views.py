from django.shortcuts import render
from OurArticlesModel import articlesModel
from registration.models import UserData
from .models import PredictionApproves


# Create your views here.
def catalog(request):
    def generatePage(engine, page):
        """ Recursively search for a valid page. """
        if page == 5: # Max tries - 5
            return render(request, 'articles/article.html')

        try:
            df = articlesModel.getPage(engine, page)

            return render(request, 'articles/article.html', {'data': df.iterrows()})
        except:
            return generatePage(engine, page + 1)

    page = 1

    if request.method == 'POST':
        if request.POST.get('likeBtn.x'):
            isApprove = True
        else:
            isApprove = False
        addApprove(request, isApprove)

    engine = articlesModel.initializeEngine("News")

    return generatePage(engine, page) # Recursively find the first valid page


def addApprove(request, isApprove: bool):
    data = request.POST
    title = data['title']
    link = data['link']
    expert = UserData.objects.filter(user_id=request.user.id).first()

    # Check if already exists, and delete if it is (To avoid duplicates)
    predictObj = PredictionApproves.objects.filter(link=link, expertId=request.user.id)
    if predictObj:
        predictObj.all().delete()

    # Add the new approval/denial
    PredictionApproves.objects.create(
        title = title,
        link = link,
        expertId = request.user.id,
        expertName = expert.firstname + ' ' + expert.lastname,
        approved = isApprove
    )
