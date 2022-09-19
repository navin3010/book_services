from django.shortcuts import render
from rest_framework.views import APIView
from common import custom_pagination
from . import models as book_app_models
from book_app import models_api as models_api
from rest_framework import response, status
from book_app import serializers


# from rest_framework import (
#     response,
#     status,
#     serializers as rest_serializers,
#     parsers,
# )
# Create your views here.

class BooksSearchAPI(APIView):

    def get(self, request):
        params = request.query_params
        limit = params.get("limit", 25)
        offset = params.get("offset", 0)
        project_guternberg_id = params.get("project_guternberg_id", "")
        language = params.get("language", "")
        print(language)
        mime_type = params.get("mime_type", "")
        topic = params.get("topic", "")
        author_name = params.get("author_name", "")
        title = params.get("title", "")

        if not language and not mime_type and not author_name and not title and not topic:
            # project_guternberg_id
            book_details_object = models_api.BookDetailsByIdApi()
            book_details, next_link = book_details_object.get_book_details_by_id(
                project_guternberg_id = project_guternberg_id,
                limit=limit,
                offset=offset
                )
        if not project_guternberg_id and not mime_type and not author_name and not title and not topic:
            # language
            no_of_language = len(language.split(","))
            if no_of_language == 1:
                book_details_object = models_api.BookDetailsByLanguageApi()
                book_details, next_link = book_details_object.get_book_details_by_language(
                    language = language,
                    limit=limit,
                    offset=offset
                    )
            else:
                # multiple language request=['fr','la']
                book_details_object = models_api.BookDetailsByLanguageApi()
                book_details, next_link = book_details_object.get_book_details_by_multiple_language(
                    languages = language,
                    limit=limit,
                    offset=offset
                    )
        if not language and not project_guternberg_id and not author_name and not title and not topic:
            # mime_type
            book_details_object = models_api.BookDetailsByMimeTypeApi()
            book_details, next_link = book_details_object.get_book_details_by_mime_type(
                mime_type = mime_type,
                limit=limit,
                offset=offset
                )  
        if not language and not project_guternberg_id and not author_name and not title:
            # topic
            no_of_topic = len(topic.split(","))
            if no_of_topic == 1:
                book_details_object = models_api.BookDetailsByTopicApi()
                book_details, next_link = book_details_object.get_book_details_by_topic(
                    topic = topic,
                    limit=limit,
                    offset=offset
                    )
            else:
                # multiple topic
                book_details_object = models_api.BookDetailsByTopicApi()
                book_details, next_link = book_details_object.get_book_details_by_multiple_topic(
                    topic = topic,
                    limit=limit,
                    offset=offset
                    )

        if not language and not project_guternberg_id and not topic and not title:
            # author_name
            book_details_object = models_api.BookDetailsByAuthorNameApi()
            book_details, next_link = book_details_object.get_book_details_by_author_name(
                author_name = author_name,
                limit=limit,
                offset=offset
                ) 
        if not language and not project_guternberg_id and not topic and not author_name:
            # book title
            book_details_object = models_api.BookDetailsByTitle()
            book_details, next_link = book_details_object.get_book_details_by_title(
                title = title,
                limit=limit,
                offset=offset
                )            
        # limit is set to 25 records.If next_link is true we are going for another data fetch
        return response.Response(
            {
                "result": True,
                "msg": "success",
                "next_link": next_link,
                "data": book_details
            },
            status=status.HTTP_200_OK,
        )

        



        
