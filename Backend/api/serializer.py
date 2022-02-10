from rest_framework import serializers
from .models import User,Note

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields  = ["id","user_name","first_name","last_name","password","date_of_creat"]
        fields  = "__all__"


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields  = "__all__"
