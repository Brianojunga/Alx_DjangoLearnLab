To create command in python shell you use the following commands then save them later 

*book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)*

    OR

*book = Book( title = "1984", author = "George Orwell", publication_year = 1949)*
*book.save()*

You can then inspect the raw SQL query to know how Django runs under the hood

*print(str(Booking.objects.filter(title = "1984").query))*