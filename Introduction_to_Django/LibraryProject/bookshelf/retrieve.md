For retrieval or get command there are various commands one can write they are here;

**Get all bookings**
*book = Book.objects.all()*

**Get one booking id**
*book = Book.objects.get(id=1)*

**filter book**
*book = Book.objects.filter(publication_year=1949)*

**filter and get only one and error if none**
*Booking.objects.get(publication_year=1949)*

**Getting the first object**
*Booking.object.first()*

**count records**
*Booking.objects.count()*