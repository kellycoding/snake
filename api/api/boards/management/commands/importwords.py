import re
from pypinyin import pinyin, Style
from django.core.management.base import BaseCommand
from api.boards.similar import similar
from api.boards.models import Word, Level, Proficiency, Homograph

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str)


    def handle(self, *args, **options):
        filename = options['filename'][0]
        content = open(filename, 'rb').read().decode('utf-8')
        lines = [l.strip() for l in content]
        lines = [l for l in lines if l]
        content = ''.join(lines)

        level = Level.objects.get(id=1)
        proficiency = Proficiency.objects.get(id=1)

        for w in content:
            try:
                Word.objects.get(name=w)
                print('Warning: %s already exists.' % w)
            except Word.DoesNotExist:

                spell = pinyin(w, Style.NORMAL)
                homographs = similar(w)

                word = Word(
                    name=w,
                    spell=spell[0][0],
                    level=level,
                    proficiency=proficiency,
                )

                word.save()

                for h in homographs:
                    Homograph.objects.create(word=word, name=h)

                print('%s imported.' % w)




