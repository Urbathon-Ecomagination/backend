from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Polls, Categories, Moderators, Service, AppealAnswer, AddressService, Appeal, Users, Posts, Comments
from .serializers import PollsSerializer, ModeratorsSerializer, CategoriesSerializer, ServiceSerializer, \
    AppealAnswerSerializer, AddressServiceSerializer, AppealSerializer, UsersSerializer, PostsSerializer, \
    CommentsSerializer


# Create your views here.


class PollsAPIView(APIView):
    def get(self, request):
        polls = Polls.objects.all()
        return Response({'posts': PollsSerializer(polls, many=True).data})

    def post(self, request):
        serializer = PollsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Polls.objects.create(
            title=request.data['title'],
            options=request.data['options']
        )

        return Response({'post': model_to_dict(post_new)})


class CategoriesAPIView(APIView):
    def get(self, request):
        polls = Categories.objects.all()
        return Response({'posts': CategoriesSerializer(polls, many=True).data})

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Categories.objects.create(
            name=request.data['name'],
        )

        return Response({'post': model_to_dict(post_new)})


class ModeratorsAPIView(APIView):
    def get(self, request):
        polls = Moderators.objects.all()
        return Response({'posts': ModeratorsSerializer(polls, many=True).data})

    def post(self, request):
        serializer = ModeratorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Moderators.objects.create(
            name=request.data['name'],
            email=request.data['email'],
            password=request.data['password']
        )

        return Response({'post': model_to_dict(post_new)})


class ServiceAPIView(APIView):
    def get(self, request):
        polls = Service.objects.all()
        return Response({'posts': ServiceSerializer(polls, many=True).data})

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Service.objects.create(
            name=request.data['name'],
            description=request['description'],
            email=request.data['email'],
            password=request.data['password'],
            approved_by=request.data['approved_by']
        )

        return Response({'post': model_to_dict(post_new)})


class AppealAnswerAPIView(APIView):
    def get(self, request):
        polls = AppealAnswer.objects.all()
        return Response({'posts': AppealAnswerSerializer(polls, many=True).data})

    def post(self, request):
        serializer = AppealAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = AppealAnswer.objects.create(
            appeal_id=request.data['appeal_id'],
            text=request.data['text'],
            score=request['score'],
            to_user_id=request.data['to_user_id'],
            from_service_id=request.data['from_service_id'],
        )

        return Response({'post': model_to_dict(post_new)})


class AddressServiceAPIView(APIView):
    def get(self, request):
        polls = AddressService.objects.all()
        return Response({'posts': AddressServiceSerializer(polls, many=True).data})

    def post(self, request):
        serializer = AddressServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = AddressService.objects.create(
            category_id=request.data['category_id'],
            service_id=request.data['service_id'],
        )

        return Response({'post': model_to_dict(post_new)})


class AppealAPIView(APIView):
    def get(self, request):
        polls = Appeal.objects.all()
        return Response({'posts': AppealSerializer(polls, many=True).data})

    def post(self, request):
        serializer = AppealSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Appeal.objects.create(
            text=request.data['text'],
            author_id=request.data['author_id'],
            category_id=request.data['category_id'],
            name=request.data['name'],
            phone_number=request.data['phone_number'],
            email=request.data['email'],
            approved_by=request.data['approved_by'],
            status=request.data['status'],
        )

        return Response({'post': model_to_dict(post_new)})


class UsersAPIView(APIView):
    def get(self, request):
        polls = Users.objects.all()
        return Response({'posts': UsersSerializer(polls, many=True).data})

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Users.objects.create(
            name=request.data['name'],
            email=request.data['email'],
            password=request.data['password'],
            rating=request.data['rating'],
        )

        return Response({'post': model_to_dict(post_new)})


class CommentsAPIView(APIView):
    def get(self, request):
        polls = Comments.objects.all()
        return Response({'posts': CommentsSerializer(polls, many=True).data})

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Comments.objects.create(
            user_id=request.data['user_id'],
            text=request.data['text'],
            post_id=request.data['post_id'],
        )

        return Response({'post': model_to_dict(post_new)})


class PostsAPIView(APIView):
    def get(self, request):
        polls = Posts.objects.all()
        return Response({'posts': PostsSerializer(polls, many=True).data})

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Posts.objects.create(
            title=request.data['title'],
            text=request.data['text'],
            author_id=request.data['author_id'],
            category_id=request.data['category_id'],
            picture=request.data['picture'],
            poll_id=request.data['poll_id'],
            approved_by=request.data['approved_by'],

        )

        return Response({'post': model_to_dict(post_new)})
