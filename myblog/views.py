from django.shortcuts import render
from myblog.models import Profile , Category, UserToken
from myblog.serializers import ProfileSerializer , CategorySerializer , RegisterSerializer,EmailVerifySerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator as tg
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from .tasks import send_email
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator as tg
from rest_framework import generics, permissions

# Create your views here.
class Register(APIView):
    """Register View"""

    model = User
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    
    def get_serializer_class(self):
        return self.serializer_class

    def post(self,request):
        #import pdb;pdb.set_trace()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            user = User.objects.create(username=request.data['email'],email=request.data['email'],first_name=request.data['first_name'],last_name=request.data['last_name'],is_active=False)
            user.set_password(request.data['email'])
            user.save()
            profile = Profile.objects.create(user=user,contact=request.data['contact_no'])
            print user

            token, created = Token.objects.get_or_create(user=user)            
            email_token, created = UserToken.objects.get_or_create(owner=user,token=tg.make_token(user))

            #additional information about user in email
            current_site = get_current_site(request)
            domain = current_site.domain
            site_name=current_site.name
            s=list(site_name.split(':'))   

            #now spliting site_name = localhost and domain=8000/2000 etc   
            site_name=s[0]
            domain=s[1]


            #email data
            email_data = {'user': user,'email': user.email,'domain': domain,'site_name': site_name,'protocol': settings.PROTOCOL,'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                         'token': tg.make_token(user)}
            email_data["sub"] ="You're receiving this email because you requested a email verification for your user account at"
            email_data["body"] ="Please go to the following page and verify your email:"
            email_data["html"] ='preregister_body_html.txt'
            send_email.delay(data=email_data)


            return Response({'token':token.key,
                                'id':user.id,
                                'first_name':user.first_name
                            },status = status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


# class CategoryView(ListCreateAPIView):
#     model = Category
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()

class EmailVerify(generics.GenericAPIView):
    serializer_class = EmailVerifySerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def post(self,request):
        #import pdb; pdb.set_trace()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.data['email'] == request.data['email']:
                email = request.data['email']
                user = User.objects.get(email=email)

                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
                s = list(site_name.split(':'))
                site_name = s[0]
                domain = s[1]

                email_data={'user':user,'email':email,'protocol':settings.PROTOCOL, 'domain':domain, 'site_name':site_name,'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                            'token':tg.make_token(user)}

                email_data["sub"] ="You're receiving this email because you requested a email verification for your user account at"
                email_data["body"] ="Please go to the following page and verify your email:"
                email_data["html"] ='preregister_body_html.txt'
                send_email.delay(data=email_data)

                return Response({'success':'Email verification mail has been sent.'},status=status.HTTP_200_OK)
            else:
                return Response({'error':['Entered email is not correct']},status = status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailVerifyConfirm(APIView):
    """
    Email Verify Confirm
    """
    
    def get(self, request, uidb64=None, token=None):
        return Response({'success': 'Email verified successfully'}, status=status.HTTP_200_OK)





