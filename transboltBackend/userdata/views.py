from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .helpers import send_otp_to_phone , verify_otp_func 
from .models import UserData , VehicleModel
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer , VehicleSerializer


# Create your views here.

@csrf_exempt
@api_view(['POST'])
def send_otp(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response({
            'status': 400,
            'message' : 'Key Phone Number is Required'
        })
    
    if data.get('password') is None:
        return Response({
            'status': 400,
            'message' : 'Key Password is Required'
        })
    
    veri = send_otp_to_phone(data.get('phone_number'))
    return Response({
        'status': 200,
        'message' : 'OTP Sent'
    })



@api_view(['POST'])
def verify_otp(request):
    data = request.data
    if data.get('phone_number') is None:
        return Response({
            'status': 400,
            'message' : 'Key Phone Number is Required'
        })
    
    if data.get('otp') is None:
        return Response({
            'status': 400,
            'message' : 'Key OTP is Required'
        })
    
    phone_number = data.get('phone_number')
    otp = data.get('otp')  
    return Response(verify_otp_func(otp , phone_number))


@api_view(['POST'])
def userSignUp(request, *args, **kwargs):
    data = request.data
    if data.get('phone_number') is None:
        return Response({
            'status': 400,
            'message' : 'Key Phone Number is Required'
        })
    
    if data.get('otp') is None:
        return Response({
            'status': 400,
            'message' : 'Key OTP is Required'
        })
    
    phone_number = data.get('phone_number')
    otp = data.get('otp')
    if request.method == "POST":
        try:
            if verify_otp_func(otp , phone_number) == ({'Status': 'Success', 'Details': 'OTP Matched'}):
                try:
                    checkData = UserData.objects.filter( phone_number= data.get('phone_number'))
                    checkSerializer = UserSerializer(checkData , many = True)
                    if (len(checkSerializer.data) == 0):
                        try:

                            password = make_password(data.get('password'))
                            user = UserData.objects.create(
                            phone_number = data.get('phone_number'),
                            password = make_password(data.get('password')),
                            firstName = 'undefined',
                            userType = 'undefined',
                            lastName = 'undefined',
                            
                          
                            imgurl = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSN6vrUZeKVCZoP4XP1CIbyuNPJ_pcuRoC-A&usqp=CAU',
                            email = 'undefined@retinamonk.com',
                            lat = 0.0000,
                            lng = 0.0000,
                            fcmToken = 'undefined'
                            
                            )
                            
                            user.set_password = password
                            user.save()
                            return Response({
                                'status':200,
                                'message' : 'User Created Successfully.'
                                })

                        except Exception as e:
                            print('Error:   ', e)
                            return Response({
                                'status':500,
                                'message' : 'Something Went Wrong.'
                                })
                    else:
                        return Response({
                    'status':500,
                    'message' : 'Phone Number already Registered.'
                    })
                except Exception as e:
                            print('Error:   ', e)
                            return Response({
                                'status':500,
                                'message' : 'Something Went Wrong.'+str(e)
                                })
                

        except Exception as e:
            
            return Response({
                'status':500,
                'message' : 'Something Went Wrong.'
                })



@api_view(['POST','PUT','DELETE'])
def userdataorm(request, *args, **kwargs):
    data = request.data
    if request.method == "POST":
        
       
        try:
            fields_and_values = data.get('query').items()
            query_condition = Q()
            for field, value in fields_and_values:
                if field and value:
                    query_condition &= Q(**{f'{field}__exact': value})
            querydata = UserData.objects.filter(query_condition).order_by(data.get('orderBy'))[:data.get('limit')]
            serializer = UserSerializer(querydata , many = True)
            return Response({
                'status': 200,
                'response' : serializer.data
            })
        except Exception as e:
            return Response({
                'status': 500,
                'response' : 'Something Went Wrong.  Error: ' +str(e)
            })
        
    if request.method == "PUT":
        if request.data.get('userId'):
            try:
                updateObj= get_object_or_404(UserData, userId = request.data.get('userId'))
                model_fields = UserData._meta.get_fields()
                field_names = [field.name for field in model_fields if not field.is_relation]
                
                for key, value in request.data.get('data').items():
                    if key in field_names:  
                        setattr(updateObj, key, value)
                    else:
                        return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: Field not found.'
                })

                updateObj.save()
                return Response({
                    'status': 200,
                    'response' : 'Request Successful'
                })
            except Exception as e:
                return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: '+str(e)
                })
        else:
            return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: Update by UserId is allowed.'
                })

    if request.method == "DELETE":
        if request.data.get('userId'):
            try:
                UserData.objects.filter(userId = request.data.get('userId')).delete()
                return Response({
                    'status': 200,
                    'response' : 'Request Successful'
                })
            except Exception as e:
                return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: '+str(e)
                })
        else:
            return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: Delete by UserId is allowed.'
                })




#####################
'''VEHICLE OPERATIONS.'''
#####################
@api_view(['POST'])
def vehicleSignUp(request, *args, **kwargs):
    data = request.data
    if request.method == "POST":
        try:
                    vehicle = VehicleModel.objects.create(
                    type = 'undefined',
                    regNo = 'undefined',
                    modelNo = 'undefined',
                    brandName = 'undefined',
                    lat = 0.0000,
                    lng = 0.0000,
                    fcmToken = 'undefined',
                    liveUrl = 'undefined'
                    
                    )
                    
                    vehicle.save()
                    return Response({
                        'status':200,
                        'message' : 'Vehicle Created Successfully.'
                        })

        except Exception as e:
            print('Error:   ', e)
            return Response({
                'status':500,
                'message' : 'Something Went Wrong.'
                })
                

        



@api_view(['POST','PUT','DELETE'])
def vehicledataorm(request, *args, **kwargs):
    data = request.data
    if request.method == "POST":
        try:
            fields_and_values = data.get('query').items()
            query_condition = Q()
            for field, value in fields_and_values:
                if field and value:
                    query_condition &= Q(**{f'{field}__exact': value})
            querydata = VehicleModel.objects.filter(query_condition).order_by(data.get('orderBy'))[:data.get('limit')]
            serializer = VehicleSerializer(querydata , many = True)
            return Response({
                'status': 200,
                'response' : serializer.data
            })
        except Exception as e:
            return Response({
                'status': 500,
                'response' : 'Something Went Wrong.  Error: ' +str(e)
            })
        
    if request.method == "PUT":
        if request.data.get('id'):
            try:
                updateObj= get_object_or_404(VehicleModel, id = request.data.get('id'))
                model_fields = VehicleModel._meta.get_fields()
                field_names = [field.name for field in model_fields if not field.is_relation]
                
                for key, value in request.data.get('data').items():
                    if key in field_names:  
                        setattr(updateObj, key, value)
                    else:
                        return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: Field not found.'
                })

                updateObj.save()
                return Response({
                    'status': 200,
                    'response' : 'Request Successful'
                })
            except Exception as e:
                return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: '+str(e)
                })
        else:
            return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: Update by id is allowed.'
                })

    if request.method == "DELETE":
        if request.data.get('id'):
            try:
                VehicleModel.objects.filter(id = request.data.get('id')).delete()
                return Response({
                    'status': 200,
                    'response' : 'Request Successful'
                })
            except Exception as e:
                return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: '+str(e)
                })
        else:
            return Response({
                    'status': 500,
                    'response' : 'Something Went Wrong. Error: Delete by Id is allowed.'
                })
