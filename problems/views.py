# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Problem
from .serializers import *

@api_view(['GET', 'POST'])
def problems_list(request):
    """
    List  problems, or create a new problem.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        problems = Problem.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(problems, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ProblemSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/problems/?page=' + str(nextPage), 'prevlink': '/api/problems/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)