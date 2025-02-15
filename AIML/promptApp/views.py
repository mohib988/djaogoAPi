from openai import OpenAI
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.permissions import AllowAny
from AIML.settings import CONFIG
# Create your views here.



class CustomPromptView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt')
        age = request.data.get('age')
        location = request.data.get('location')
        

        base_url = "https://api.aimlapi.com/v1"

        # Insert your AIML API Key in the quotation marks instead of my_key:
        api_key = CONFIG.get("APIKEY")
        system_prompt = f"You are a sexual abuse educator for person with age {age} and location {location}"

        api = OpenAI(api_key=api_key, base_url=base_url)


        completion = api.chat.completions.create(
        model="deepseek/deepseek-r1",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

        response = completion.choices[0].message.content

        return Response({
            'response': response,
        }, status=status.HTTP_200_OK)
        