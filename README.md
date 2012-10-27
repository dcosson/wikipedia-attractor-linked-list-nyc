## Wikipedia Attractor Crawler that prints "linked list"

It crawls Wikipedia by following the first link on every page until it gets to "Greek language".  I've wanted to try implementing this myself to see if the rumors are true, turns out they pretty much are.  Doesn't always work and will occasionally even crash (gasp!)

It prints the characters at specific indices in the final page, which, at the moment, spell "LinkedList NYC".

An idea that actually makes sense would be to reverse-index a bunch of pages that link to the "Linked List" Wikipedia page and have this end there.  Next time.

[Context](http://us2.campaign-archive1.com/?u=193b767bbb3b0eb0d949d5924&id=49bf5dc644&e=e58374102f)

### To Run:

    $ git clone git://github.com/dcosson/wikipedia-attractor-linked-list-nyc.git
    $ cd wikipedia-attractor-linked-list-nyc
    $ mkvirtualenv dannyllnyc && workon dannyllnyc #(if you're into virtualenvwrapper)
    $ pip install -r requirements.txt 
    $ python main.py
    First word that comes to mind: new york  # whatever word you want
    checking page: /wiki/New_York
    checking page: /wiki/File:En-us-New_York.ogg
    checking page: /wiki/Outline_of_New_York
    checking page: /wiki/U.S.
    checking page: /wiki/Spanish_language_in_the_United_States
    checking page: /wiki/Spanish_language
    checking page: /wiki/List_of_countries_where_Spanish_is_an_official_language#International_organizations_where_Spanish_is_official
    checking page: /wiki/Sovereign_state
    checking page: /wiki/Centralized_government
    checking page: /wiki/American_and_British_English_spelling_differences
    checking page: /wiki/Comparison_of_American_and_British_English
    checking page: /wiki/British_English
    checking page: /wiki/English_language
    checking page: /wiki/West_Germanic_language
    checking page: /wiki/Germanic_languages
    checking page: /wiki/Indo-European_languages
    checking page: /wiki/Language_family
    checking page: /wiki/Language
    checking page: /wiki/Human
    checking page: /wiki/Homo_sapiens_idaltu
    checking page: /wiki/Subspecies
    checking page: /wiki/Biological_classification
    checking page: /wiki/Taxonomy
    checking page: /wiki/Ancient_Greek
    checking page: /wiki/Greek_language


    LinkedList NYC

