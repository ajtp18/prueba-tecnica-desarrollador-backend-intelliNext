import pandas as pd
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Import books from CSV file'

    def handle(self, *args, **options):
        df = pd.read_csv('books_data/books.csv', sep=";",on_bad_lines="skip", encoding="latin-1")
        for _, row in df.iterrows():
            book = Book.objects.create(
                isbn=row['ISBN'],
                title=row['Book-Title'],
                author=row['Book-Author'],
                yearOfPublication=row['Year-Of-Publication'],
                publisher=row['Publisher'],
            )
            self.stdout.write(self.style.SUCCESS(f'Book "{book.title}" imported successfully.'))