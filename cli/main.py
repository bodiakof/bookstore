import argparse
import httpx
import json

from app.enums.book_format import BookFormat


API_URL = 'http://127.0.0.1:8000/books/'

def add_book(args):
    payload = {
        'title': args.title,
        'author': args.author,
        'price': args.price,
        'stock': args.stock,
        'format': args.format
    }

    response = httpx.post(API_URL, json=payload)
    if response.status_code == 200:
        print('Book added! ✅')
        print(json.dumps(response.json(), indent=2))
    else:
        print('Error:', response.status_code)
        print(response.text)

def list_books(args):
    response = httpx.get(API_URL)
    if response.status_code == 200:
        books = response.json()
        for book in books:
            print(f"{book['id']:>2} | {book['title']:<30} | {book['author']:<20} | ${book['price']:<5}")
    else:
        print('Error:', response.status_code)
        print(response.text)

def main():
    parser = argparse.ArgumentParser(description='📚 Bookstore CLI')

    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new book')
    add_parser.add_argument('--title', required=True)
    add_parser.add_argument('--author', required=True)
    add_parser.add_argument('--price', type=float, required=True)
    add_parser.add_argument('--stock', type=int, default=0)
    add_parser.add_argument(
        '--format',
        type=str,
        choices=[f.value for f in BookFormat],
        required=True,
        help='Book format (paperback, hardcover, ebook)' 
        )
    add_parser.set_defaults(func=add_book)

    # List command
    list_parser = subparsers.add_parser('list', help='List all books')
    list_parser.set_defaults(func=list_books)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
