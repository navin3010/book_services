import string
from book_app import models as book_app_models
from django.db import models as django_models, connection
from rest_framework import serializers


class BookDetailsByIdApi:

    def get_book_details_by_id(self, project_guternberg_id:int , limit:int, offset:int):
        # book_details = book_app_models.BooksBookAuthors.objects.filter(
        #     book_id = project_guternberg_id
        # ).select_related("book").select_related("author")
        # return book_details
        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where bb.id={project_guternberg_id}'''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

class BookDetailsByLanguageApi:

    def get_book_details_by_language(self, language:string , limit:int, offset:int):

        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where bl.code like '%{language}%' '''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

    def get_book_details_by_multiple_language(self, languages:list , limit:int, offset:int):
        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where bl.code=any(array[{languages}])'''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

class BookDetailsByMimeTypeApi:

    def get_book_details_by_mime_type(self, mime_type:string , limit:int, offset:int):

        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where bf.mime_type like '%{mime_type}%' '''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

class BookDetailsByTopicApi:

    def get_book_details_by_topic(self, topic:string , limit:int, offset:int):

        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where bsub.name ilike '%{topic}%' or bshelf.name ilike '%{topic}%' '''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

    def get_book_details_by_multiple_topic(self, topic:list , limit:int, offset:int):

        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where bsub.name=any(array[{topic}]) or bshelf.name=any(array[{topic}]) '''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

class BookDetailsByAuthorNameApi:

    def get_book_details_by_author_name(self, author_name:string , limit:int, offset:int):

        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where ba.name ilike '%{author_name}%' '''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

class BookDetailsByTitle:

    def get_book_details_by_title(self, title:string , limit:int, offset:int):

        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        try:
            previous_limit = limit
            limit = int(previous_limit)+1
        except IndexError as e:
            raise serializers.ValidationError(str(e))
        with connection.cursor() as cursor:
            query = f'''
                select bb.title as title, bb.id as book_id,
                bba.author_id as author_id,
                ba.name as author_name,ba.birth_year as birth_year, ba.death_year as death_year,
                bl.code as language,
                bsub.name as subject_name,
                bshelf.name as genre,bshelf.id as bookshelf_number,
                bf.mime_type as download_link
                From books_book bb join books_book_authors bba on bba.book_id=bb.id
                join books_author ba on bba.author_id=ba.id 
                join books_book_languages bbl on bbl.book_id=bb.id
                join books_language bl on bbl.book_id=bl.id
                join books_book_subjects bbsub on bbsub.book_id=bb.id
                join books_subject bsub on bbsub.subject_id=bsub.id
                join books_book_bookshelves bbshelf on bbshelf.book_id=bb.id
                join books_bookshelf bshelf on bbshelf.bookshelf_id=bshelf.id
                join books_format bf on bf.book_id=bb.id
                where bb.title ilike '%{title}%' '''
            cursor.execute(query)
            book_details = dictfetchall(cursor)
            if len(book_details) > int(previous_limit):
                next_link = True
                final_data = book_details[:-1]
            else:
                next_link = False
                final_data = book_details
            return final_data, next_link

