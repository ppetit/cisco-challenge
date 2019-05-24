============
movie-rating
============

This program can be used to get the rating of a movie.
Underneath, it uses the `OMDB API <http://www.omdbapi.com/>`_
to get information about movies from the OMDB database.

============
Installation
============
To resolve any potential dependency problems,
this application is better used as a containerized
application. Please follow the simplle installation
steps below to build your application as a Docker container.
The installation of Docker on your computer is not covered in this guide.

Clone the repository in a directory on your computer
-------------------------------------------------

# git clone `https://github.com/ppetit/cisco-challenge.git
<https://github.com/ppetit/cisco-challenge.git>`_

Build your container
--------------------

# cd movie-rating
# docker build -t movie-rating .

If no error where thrown at this point, you should be all
set !

=====
Usage
=====

# docker run movie-rating -t "star wars"
Star Wars: Episode IV - A New Hope:
        Released: 25 May 1977
        Rated: PG
        Rotten Tomatoes rating: 93%

What else could it be ;) !!!