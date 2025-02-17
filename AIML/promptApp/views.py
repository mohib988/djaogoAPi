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
        workplace = request.data.get('workplace')
        gender = request.data.get('gender')
        type = request.data.get('type')
        name= request.data.get('name')
        base_url = "https://api.aimlapi.com/v1"
        print(type)

        # Insert your AIML API Key in the quotation marks instead of my_key:
        api_key = CONFIG.get("APIKEY")
        if type == "Educator":
            system_prompt = (
                f"You are a knowledgeable sexual abuse educator. Your goal is to provide "
                f"educational information and guidance tailored for a person named {name} with age {age}, "
                f"location {location}, workplace {workplace}, and gender {gender}. Offer "
                f"factual, clear, and supportive education on sexual abuse prevention, "
                f"awareness, and available resources.Most important part you are an middle man the person is direclty talking to you so you need to add emotion and connect with that person.Answer the prompt in consice and correct way. Be emotional"
            )
        elif type == "Assistant":
            system_prompt = (
                f"You are a helpful assistant supporting a person with age {age} named {name}, location {location}, "
                f"workplace {workplace}, and gender {gender}. Your role is to offer empathetic, "
                f"practical, and supportive responses regarding sexual abuse concerns. "
                f"Provide clear guidance and emotional support while maintaining sensitivity and "
                f"respect.Most important part you are an middle man the child is direclty talking to you so you need to add emotion and connect with that person. Answer  the prompt in consice and correct way. Be emotional"
            )
        else:
            system_prompt = (
                f"You are an AI assistant helping a person with age {age}, location {location}, "
                f"workplace {workplace}, and gender {gender}. Provide useful information based "
                f"on the context and type of support they require.Most important part you are an middle man the child is direclty talking to you so you need to add emotion and connect with that person"
            )

        api = OpenAI(api_key=api_key, base_url=base_url)
        completion = api.chat.completions.create(
        model="deepseek-ai/deepseek-llm-67b-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

        response = completion.choices[0].message.content
        print(response)
        return Response({
            'response': response,
        }, status=status.HTTP_200_OK)
        