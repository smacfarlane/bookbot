def main():
    path = "books/frankenstein.txt"
    book = open_book(path)
    words = len(book.split());

    counts = count_letters(book)
    counts = sort_letter_counts(counts)

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()

    for c in counts:
        print(f"The '{c["letter"]}' character was found {c["count"]} times")

    print("--- End report ---")

def open_book(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def count_letters(contents):
    contents = contents.lower()
    counts = {}
    for c in contents:
        if c.isalpha():
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
    return counts

def sort_letter_counts(counts):
    sorted_counts = []
    for c in counts:
        sorted_counts.append({"letter": c, "count": counts[c]})

    sorted_counts.sort(reverse=True, key=sort_on);
    return sorted_counts

def sort_on(dict):
    return dict["count"]


main()
