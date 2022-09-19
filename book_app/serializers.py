from rest_framework import serializers
from book_app import models as book_app_models


class BooksAuthorSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = book_app_models.BooksAuthor
        fields = [
            "birth_year",
            "death_year",
            "name"
        ]

class BooksBookSerializer(serializers.ModelSerializer):
    book_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = book_app_models.BooksBook
        fields = [
            "download_count",
            "gutenberg_id",
            "media_type",
            "title",
            "book_id"
        ]


class BooksBookShelfSerializer(serializers.ModelSerializer):
    books_book_shelf_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = book_app_models.BooksBookshelf
        fields = [
            "name",
        ]

class BooksFormatSerializer(serializers.ModelSerializer):
    books_format_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = book_app_models.BooksFormat
        fields = [
            "mime_type",
            "url",
        ]

class BooksLanguageSerializer(serializers.ModelSerializer):
    books_language_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = book_app_models.BooksLanguage
        fields = [
            "code",
        ]
    
class ReadBooksLanguageSerializer(serializers.ModelSerializer):
    # book_language_id = serializers.ReadOnlyField(source="language_id")
    language = serializers.ReadOnlyField(source="language.code")
    title = serializers.ReadOnlyField(source="book.title")
    gutenberg_id = serializers.ReadOnlyField(source="book.gutenberg_id")
    download_count = serializers.ReadOnlyField(source="book.download_count")
    author_name = serializers.ReadOnlyField(source="author.name")
    birth = serializers.ReadOnlyField(source="author.birth_year")
    death = serializers.ReadOnlyField(source="author.death_year")
    subject = serializers.ReadOnlyField(source="subject.name")
    

    class Meta:
        model = book_app_models.BooksBookLanguages
        fields = [
            # "book_language_id",
            "title",
            "language",
            "gutenberg_id",
            "download_count",
            "author_name",
            "birth",
            "death",
            "subject"
            
        ]

class BooksSubjectSerializer(serializers.ModelSerializer):
    books_subject_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = book_app_models.BooksSubject
        fields = [
            "name",
        ]