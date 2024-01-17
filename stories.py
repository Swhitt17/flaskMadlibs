"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code,title, words, text):
        """Create story with words and template text."""
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1= Story(
    "history",
    "A Historical Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "birthday",
    "Birthday Wishes",
    ["number","past_tense_verb","adjective","noun","verb_s", "color","adjective2","noun2","adjective3","color2","plural_noun"],
    """This year I am turning {number} years old. I have already {past_tense_verb} my list.
      First, I want a {adjective} {noun} that {verb_s}. Also, I'd like a {color} {adjective2} {noun2}.
      For my cake, my favorite kind is {adjective3} with {color2} {plural_noun} on it."""
)

story3 = Story(
    "cafeteria",
    "School Cafeteria Food",
    ["adjective","body_part","verb","adjective2","noun", "plural_noun","verb","food","adjective3","noun2"],
    """ My school cafeteria has really {adjective} food. Just thinking about it makes my{body_part} {verb}.
        The spaghetti is {adjective2} and tastes like {noun}.
        One day, one of my {plural_noun} started to {verb}! 
        The{food} are totally {adjective3}and look like old {noun2}."""
)

stories = {s.code: s for s in [story1, story2, story3]}
