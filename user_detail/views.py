from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ActivityModel,UserDetail
# Create your views here.

class UsersView(APIView):
    """ Test Api"""
    
    def get(self,request,format=None):
        users=UserDetail.objects.all()
        lst=[]
        if users:
            for i in users:
                av=ActivityModel.objects.filter(user=i)
                print(av)
                Dic={
                    "id":f"adsf{i.user.id}dsf".upper(),
                    "real_name":i.real_name,
                    "tz":i.tz,
                }
                ac=[]
                for x in av:
                    ac.append({
                        "start":x.start_time.strftime("%d %b %Y %I:%M%p"),
                        "end":x.end_time.strftime("%d %b %Y %I:%M%p"),
                    })
                    print(x.start_time)
                Dic["activity"]=ac
                lst.append(Dic)
            return Response({"ok":True,"members":lst})
        return Response({"ok":False})