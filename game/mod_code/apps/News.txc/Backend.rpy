init python in _wm_news:
    import random
    THUMBNAILS_PATH = "mod_assets/news_thumbnails/"

    P_NS = "New Statesman"
    P_YT = "YouTube"
    P_BBC = "Big Black Cock News" if random.randint(0, 1000000) == 0 else "BBC News"
    P_I = "i News"
    P_TG = "The Guardian"
    P_DS = "Daily Star"
    P_TS = "The Sun"
    P_TT = "The Times"
    P_FT = "Financial Times"
    P_PCG = "PCGamer"

    from store import NoRollback

    def prefix_if_needed(t):
        if isinstance(t, renpy.Displayable):
            return t

        if not isinstance(t, unicode):
            raise Exception("Given argument is not a Displayable or a string.")

        if renpy.loadable(t):
            return t
        elif renpy.loadable(THUMBNAILS_PATH + t):
            return THUMBNAILS_PATH + t

        return t # Let renpy.easy.displayable deal with this.

    class News(NoRollback):
        """
        Representation of a News headline.

        `title`
            The headline.

        `thumbnail`
            Thumbnail associated with the headline.

        `publisher`
            Publisher of the headline's news.

        `author`
            Author of the news article.
        """
        def __init__(self, title, thumbnail, publisher, author):
            self.title = title.strip()
            self.thumbnail = prefix_if_needed(thumbnail)
            self.publisher = publisher
            self.author = author
