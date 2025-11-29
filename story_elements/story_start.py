from story_elements.story_node import StoryNode
from story_elements.story_text import get_prolog


class StoryStart(StoryNode):
    def __init__(self):
        super().__init__()

    def play(self):
        print(get_prolog())