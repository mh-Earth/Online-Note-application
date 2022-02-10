from urllib import response
from django.shortcuts import render,HttpResponse
from .serializer import UserSerializers,NoteSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User,Note
from api import serializer
# Create your views here.
def index(request):
    return HttpResponse("Hello world")


@api_view(["GET"])
def getData(request):
    all_user = User.objects.all()
    serializer = UserSerializers(all_user, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postData(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error_messages)

@api_view(["GET","DELETE"])
def getUserData(request,user_name):
    if request.method == "GET":
        user = User.objects.filter(user_name=user_name)
        serializer = UserSerializers(user,many=True)
        return Response(serializer.data)

    elif request.method == "DELETE":

        user = User.objects.filter(user_name=user_name)
        user.delete()
        return Response("deleted")



@api_view(["GET","POST"])
def getNotes(request):

    if request.method == "POST":

        # print(Note.objects.filter(request.data["title"]).count() == 0)
        if Note.objects.filter(title = request.data["title"]).count() == 0:

            note_to_add = NoteSerializers(data = request.data)
            if note_to_add.is_valid():
                note_to_add.save()
                return Response("succsee add note")
        
        else:
            request.data["title"] = request.data["title"] +"-"+ str(Note.objects.filter(title = request.data["title"]).count() + 1)
            note_to_add = NoteSerializers(data = request.data)
            if note_to_add.is_valid():
                note_to_add.save()
                return Response("succsee add note")

        return Response(note_to_add.error_messages)

    elif request.method == "GET":
        all_notes = Note.objects.all()
        serializers = NoteSerializers(all_notes,many=True)
        return Response(serializers.data)
    

@api_view(["DELETE"])
# @csrf_exempt
def modify_notes(request,title):
    
    # response.headers.add('Access-Control-Allow-Origin', '*')

    if request.method == "DELETE":
        try:
            title = title.replace("+", " ")
            note_to_delete = Note.objects.filter(title = title)
            note_to_delete.delete()
            return Response("succseefully delete note")
        except Exception as e:
            print(e)
            return HttpResponse(status=500)



