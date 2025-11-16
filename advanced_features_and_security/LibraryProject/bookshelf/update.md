For updating the database one can use the following queries;

*book = Book.objects.get(publication_year=1949)*   
*book.title = "Nineteen Eighty-Four"*
*book.save()*

OR 

*Book.objects.filter(publication_year=2000).update(publication_year=1949)*