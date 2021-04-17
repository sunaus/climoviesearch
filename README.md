# cli-movie-search

CommandLine Movie Search

## cli-movie-search.py

### Retrieve information from https://omdbapi.com/ with the following features,

* Search functionality. For instance, search for all movies with the word Planet In the title.
  The result can be saved to a file, or showing on screen for selection to show more details.
* Show details of a specific movie. With an option to show Rotten Tomatoes ratings.

###  This script relys on /usr/bin/python3

```bash
usage: cli-movie-search.py [-h] [-a API_KEY] [-s SEARCH_WORD] [-f FILELOCATION] [-i SEARCH_IMDB] [-v]

optional arguments:
  -h, --help       show this help message and exit
  -a API_KEY       API Key for www.omdbapi.com. (optional)
  -s SEARCH_WORD   Word from movie title to search for. (optional)
  -f FILELOCATION  File name to save the result from movie title to search for. (optional)
  -i SEARCH_IMDB   IMDB ID of movie title to search for. (optional)
  -v               Whether showing Rotten Tomatoes ratings, false by default (optional)
```

### For Example, search for all movies with the word Planet In the title, and write the result to a file:
```bash
$> ./cli-movie-search.py -s Planet -f Planet.txt
$> more Planet.txt
   1  Title :  Rise of the Planet of the Apes
      Year  :  2011
      imdbID:  tt1318514
      Type  :  movie
      Poster:  https://m.media-amazon.com/images/M/MV5BYzE3ZmNlZTctMDdmNy00MjMzLWFmZmYtN2M5N2YyYTQ1ZDJjXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg
   2  Title :  Dawn of the Planet of the Apes
      Year  :  2014
      imdbID:  tt2103281
      Type  :  movie
      Poster:  https://m.media-amazon.com/images/M/MV5BMTgwODk3NDc1N15BMl5BanBnXkFtZTgwNTc1NjQwMjE@._V1_SX300.jpg
   3  Title :  War for the Planet of the Apes
      Year  :  2017
      imdbID:  tt3450958
      Type  :  movie
      Poster:  https://m.media-amazon.com/images/M/MV5BNDNmYTQzMDEtMmY0MS00OTNjLTk4MjItMDZhMzkzOGI3MzA0XkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_SX300.jpg
   4  Title :  Planet of the Apes
      Year  :  2001
      imdbID:  tt0133152
      Type  :  movie
      Poster:  https://m.media-amazon.com/images/M/MV5BY2RlMDhlY2MtMjQ1Zi00NzI5LTgxOTgtZjliNWMzYTY3NWZkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg
   5  Title :  Planet Terror
      Year  :  2007
      imdbID:  tt1077258
      Type  :  movie
      Poster:  https://m.media-amazon.com/images/M/MV5BODdmNmM2ZTgtODM1MS00ZGMxLTk3MTMtMGQ1ODZhMTQ1NWEwL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg
......
```

### For Example, search for all movies with the word Planet In the title:
```bash
./cli-movie-search.py -s Planet

     #  Year        IMDB-ID    Type    Title
------------------------------------------------------------------------------------------------------------------------------------------------
     1  2011       tt1318514   movie   Rise of the Planet of the Apes
     2  2014       tt2103281   movie   Dawn of the Planet of the Apes
     3  2017       tt3450958   movie   War for the Planet of the Apes
     4  2001       tt0133152   movie   Planet of the Apes
     5  2007       tt1077258   movie   Planet Terror
     6  2006       tt0795176   series  Planet Earth
     7  1968       tt0063442   movie   Planet of the Apes
     8  2002       tt0133240   movie   Treasure Planet
     9  2016       tt5491994   series  Planet Earth II
    10  2000       tt0199753   movie   Red Planet
    11  2009       tt0762125   movie   Planet 51
    12  1956       tt0049223   movie   Forbidden Planet
    13  1970       tt0065462   movie   Beneath the Planet of the Apes
    14  2001       tt0296310   series  The Blue Planet
    15  2017       tt6769208   series  Blue Planet II
......
  1080  2010       tt1787752   movie   Lonely Planet
  1081  2010       tt1796554   movie   Man from the Dying Planet
  1082  2010       tt1805376   movie   Playing God with Planet Earth
  1083  2010       tt1726058   movie   Planet Galata - Eine Brücke in Istanbul
  1084  2011       tt1730349   movie   Silent Planet
  1085  2010       tt1664778   movie   Planet Blue Balls 5
  1086  2010       tt1706379   movie   Green Lobster Men from Planet Z
  1087  2010       tt1718953   movie   What Kind of Planet Are We On?

*** Please input the movie number 1-1087, r to refresh or q to exit:  10

  Spec          Description
--------------------------------------------------------------------
  Title         Red Planet
  Year          2000
  Rated         PG-13
  Released      10 Nov 2000
  Runtime       106 min
  Genre         Action, Sci-Fi, Thriller
  Director      Antony Hoffman
  Writer        Chuck Pfarrer (story), Chuck Pfarrer (screenplay),
                Jonathan Lemkin (screenplay)
  Actors        Val Kilmer, Carrie-Anne Moss, Tom Sizemore,
                Benjamin Bratt
  Plot          Astronauts, and their robotic dog AMEE (Autonomous
                Mapping Evaluation and Evasion), search for
                solutions to save a dying Earth by searching on
                Mars, only to have the mission go terribly awry.
  Language      English
  Country       USA, Australia
  Awards        1 nomination.
  Poster        https://m.media-amazon.com/images/M/MV5BMTY2MzE0Mj
                AwOF5BMl5BanBnXkFtZTYwNDM4Mzg2._V1_SX300.jpg
  Ratings       Source: Internet Movie Database
                Value : 5.7/10
                Source: Metacritic
                Value : 34/100
  Metascore     34
  imdbRating    5.7
  imdbVotes     55,563
  imdbID        tt0199753
  Type          movie
  DVD           24 Oct 2008
  BoxOffice     $17,480,890
  Production    Village Roadshow Prod., Mars Production Pty. Ltd.,
                NPV Entertainment
  Website       N/A
  Response      True
```

### For Example, search for all movies with the word Planet In the title with Rotten Tomatoes ratings:
```bash
$> ./cli-movie-search.py -s Planet -v

     #  Year        IMDB-ID    Type    Title
------------------------------------------------------------------------------------------------------------------------------------------------
     1  2011       tt1318514   movie   Rise of the Planet of the Apes
     2  2014       tt2103281   movie   Dawn of the Planet of the Apes
     3  2017       tt3450958   movie   War for the Planet of the Apes
     4  2001       tt0133152   movie   Planet of the Apes
     5  2007       tt1077258   movie   Planet Terror
     6  2006       tt0795176   series  Planet Earth
     7  1968       tt0063442   movie   Planet of the Apes
     8  2002       tt0133240   movie   Treasure Planet
     9  2016       tt5491994   series  Planet Earth II
    10  2000       tt0199753   movie   Red Planet
    11  2009       tt0762125   movie   Planet 51
    12  1956       tt0049223   movie   Forbidden Planet
    13  1970       tt0065462   movie   Beneath the Planet of the Apes
    14  2001       tt0296310   series  The Blue Planet
    15  2017       tt6769208   series  Blue Planet II
......
  1080  2010       tt1787752   movie   Lonely Planet
  1081  2010       tt1796554   movie   Man from the Dying Planet
  1082  2010       tt1805376   movie   Playing God with Planet Earth
  1083  2010       tt1726058   movie   Planet Galata - Eine Brücke in Istanbul
  1084  2011       tt1730349   movie   Silent Planet
  1085  2010       tt1664778   movie   Planet Blue Balls 5
  1086  2010       tt1706379   movie   Green Lobster Men from Planet Z
  1087  2010       tt1718953   movie   What Kind of Planet Are We On?

*** Please input the movie number 1-1087, r to refresh or q to exit:  10

  Spec          Description
--------------------------------------------------------------------
  Title         Red Planet
  Year          2000
  Rated         PG-13
  Released      10 Nov 2000
  Runtime       106 min
  Genre         Action, Sci-Fi, Thriller
  Director      Antony Hoffman
  Writer        Chuck Pfarrer (story), Chuck Pfarrer (screenplay),
                Jonathan Lemkin (screenplay)
  Actors        Val Kilmer, Carrie-Anne Moss, Tom Sizemore,
                Benjamin Bratt
  Plot          Astronauts, and their robotic dog AMEE (Autonomous
                Mapping Evaluation and Evasion), search for
                solutions to save a dying Earth by searching on
                Mars, only to have the mission go terribly awry.
  Language      English
  Country       USA, Australia
  Awards        1 nomination.
  Poster        https://m.media-amazon.com/images/M/MV5BMTY2MzE0Mj
                AwOF5BMl5BanBnXkFtZTYwNDM4Mzg2._V1_SX300.jpg
  Ratings       Source: Internet Movie Database
                Value : 5.7/10
                Source: Rotten Tomatoes
                Value : 14%
                Source: Metacritic
                Value : 34/100
  Metascore     34
  imdbRating    5.7
  imdbVotes     55,563
  imdbID        tt0199753
  Type          movie
  DVD           24 Oct 2008
  BoxOffice     $17,480,890
  Production    Village Roadshow Prod., Mars Production Pty. Ltd.,
                NPV Entertainment
  Website       N/A
  Response      True
```

### For Example, search for movie with cmdb ID, and showing result with Rotten Tomatoes ratings:
```bash
$> ./cli-movie-search.py -i tt0133152 -v

  Spec          Description
--------------------------------------------------------------------
  Title         Planet of the Apes
  Year          2001
  Rated         PG-13
  Released      27 Jul 2001
  Runtime       119 min
  Genre         Action, Adventure, Sci-Fi, Thriller
  Director      Tim Burton
  Writer        Pierre Boulle (novel), William Broyles Jr.
                (screenplay), Lawrence Konner (screenplay), Mark
                Rosenthal (screenplay)
  Actors        Mark Wahlberg, Tim Roth, Helena Bonham Carter,
                Michael Clarke Duncan
  Plot          In 2029, an Air Force astronaut crash-lands on a
                mysterious planet where evolved, talking apes
                dominate a race of primitive humans.
  Language      English
  Country       USA
  Awards        Nominated for 2 BAFTA Film Awards. Another 11 wins
                & 30 nominations.
  Poster        https://m.media-amazon.com/images/M/MV5BY2RlMDhlY2
                MtMjQ1Zi00NzI5LTgxOTgtZjliNWMzYTY3NWZkL2ltYWdlL2lt
                YWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg
  Ratings       Source: Internet Movie Database
                Value : 5.7/10
                Source: Rotten Tomatoes
                Value : 44%
                Source: Metacritic
                Value : 50/100
  Metascore     50
  imdbRating    5.7
  imdbVotes     211,013
  imdbID        tt0133152
  Type          movie
  DVD           25 Nov 2015
  BoxOffice     $180,011,740
  Production    Zanuck Company, Twentieth Century Fox
  Website       N/A
  Response      True
```
