from book_app.models import *
from django.db import models as django_models


BooksBookAuthors.objects.filter(
    book_id=4, l_detail=django_models.Subquery(
        BooksBookLanguages.objects.filter(
            book_id=4))).values()

BooksBookAuthors.objects.filter(
    book_id=4).annotate(BooksBookLanguages.objects.filter(book_id=4).values())



1.
BooksBookLanguages.objects.filter(
    language__in = django_models.Subquery(
        BooksLanguage.objects.filter(code__in=['la','fr']).values("id")
    )).select_related("book").select_related("language").values("book_id")

BooksBookAuthors.objects.filter(
    book__in=django_models.Subquery(
        BooksBookLanguages.objects.filter(
            language__in = django_models.Subquery(
                BooksLanguage.objects.filter(code__in=['la','fr']).values("id")
            )).values("book_id")

    )
).select_related("author")












2.
BooksBookAuthors.objects.filter(
    book__in = django_models.Subquery(
        BooksBookLanguages.objects.filter(
    language__in = django_models.Subquery(
        BooksLanguage.objects.filter(code__in=['la','fr']).values("id")
        )).select_related("book").select_related("language")).values("book_id")).select_related("author")

3.
BooksBookAuthors.objects.filter(
    book__in = django_models.Subquery(
        BooksBookLanguages.objects.filter(
    language__in = django_models.Subquery(
        BooksLanguage.objects.filter(code__in=['la','fr']).values("id")
        )).select_related("book").select_related("language").values("book_id")
)).select_related("author")


4.
BooksBookSubjects.objects.filter(
    book__in = BooksBookAuthors.objects.filter(
    book__in = django_models.Subquery(
        BooksBookLanguages.objects.filter(
    language__in = django_models.Subquery(
        BooksLanguage.objects.filter(
            code__in=['la','fr']).values("id")
        )).select_related("book").select_related("language").values("book_id")
)).select_related("author").values("book_id")).select_related("subject")