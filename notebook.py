import datetime

# Stores the last id used in a note.
last_id = 0


class Note:
    """
    A note within the notebook
    """

    def __init__(self, memo, tags=''):
        """Init with a memo and an optinal tag(s)"""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.'''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        """init the class with empty list"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def modify_note(self, note_id, memo):
        """change the memo of the note with returned id"""

        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def _find_note(self, note_id):
        """find a note by its id and return it."""

        for note in self.notes:
            if str(note_id) == str(note.id):
                return note
            return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        self._find_note(note_id).memo = memo

    def search(self, filter):
        """search for the filter umong all the notes"""

        return [note for note in self.notes if note.match(filter)]


if __name__ == '__main__':
    print(f'{__name__} is not a script.')