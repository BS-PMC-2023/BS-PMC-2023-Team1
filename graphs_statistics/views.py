from django.shortcuts import render
from registration.models import UserData
from articles.models import PredictionApproves, ArticleCache
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd


# Create your views here.
def modelsPredictionsGraph(request):
    # Generate Model's Predictions Graph
    plt.clf()

    legitCount = ArticleCache.objects.filter(isFake=False).count()
    fakeCount = ArticleCache.objects.filter(isFake=True).count()

    dfCount = pd.read_csv('OurArticlesModel/news data/validation set labels.csv')['label'].value_counts()

    legitCount += int(dfCount[1])
    fakeCount += int(dfCount[0])

    data = [legitCount, fakeCount]
    labels = ['Predicted as Legit', 'Predicted as Fake']
    colors = sns.color_palette('pastel')[0:2]

    plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
    plt.title("Classification Model's Predictions Comparison")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    modelGraph = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    return modelGraph


def usersTypeGraph(request):
    # Generate Type of Users Graph
    plt.clf()

    expertsCount = UserData.objects.filter(isexpert=True).count()
    adminCount = UserData.objects.filter(isAdmin=True).count()
    normalCount = UserData.objects.filter(isexpert=False, isAdmin=False).count()

    data = []
    labels = []

    if expertsCount > 0:
        data.append(expertsCount)
        labels.append('Experts')
    if adminCount > 0:
        data.append(adminCount)
        labels.append('Admins')
    if normalCount > 0:
        data.append(normalCount)
        labels.append('Users')

    colors = sns.color_palette('pastel')[0:3]

    plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
    plt.title("Total Registered Users Type")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    usersGraph = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    return usersGraph


def graphGeneral(request):
    """ Graph of general statistics about the model performance. """
    context = {
        'modelGraph': modelsPredictionsGraph(request),
        'usersGraph': usersTypeGraph(request)
    }

    return render(request, 'graphs_statistics/general_graphs.html', context)
