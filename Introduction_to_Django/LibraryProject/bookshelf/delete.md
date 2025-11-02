For delete you can use the following quries for delete

*book = Book.objects.get(id=1)*
*book.delete()*

    OR

*Book.objects.filter(publication_year=1949).delete()*