from django.shortcuts import render
from myblog.models import Profile , Category, UserToken
from myblog.serializers import ProfileSerializer , CategorySerializer , RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator as tg
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class Register(APIView):
    """Register View"""

    model = User
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    
    def get_serializer_class(self):
        return self.serializer_class

    def post(self,request):
        import pdb;pdb.set_trace()
        

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            user = User.objects.create(username=request.data['email'],email=request.data['email'],first_name=request.data['first_name'],last_name=request.data['last_name'],is_active=False)
            user.set_password(request.data['email'])
            user.save()
            profile = Profile.objects.create(user=user,contact=request.data['contact_no'])

            # try:
            #     user = authenticate(email=user.email,
            #                         password=request.data['password'])
            # except User.MultipleObjectsReturned:
            #     users = User.objects.filter(email=user.email)
            #     for u in users[1:]:
            #         u.is_active = False
            #         u.save()
            #     user = users[0]
            # user = User.objects.get(email=request.data['email'])
            print user

            token, created = Token.objects.get_or_create(user=user)
            
            email_token, created = UserToken.objects.get_or_create(owner=user,token=tg.make_token(user))
            return Response({'token':token.key,
                                'id':user.id,
                                'first_name':user.first_name
                            },status = status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class CategoryView(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



