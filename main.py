
def ReadBook(BookPath):
    try:
        with open(BookPath) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"File not found: {BookPath}")
        return ""

def BookWordCount(BookContent):
    Wordcount =BookContent.split()
    return len(Wordcount)

def CharakterCount(BookContent):
    CharakterCount={}
    for char in BookContent.lower():
        if char in CharakterCount:
            CharakterCount[char] +=1
        else:
            CharakterCount[char] =1
    return CharakterCount

def CharakterCountReport(CharDict):
    SortedReport ={}
    for c in CharDict:
        if c.isalpha() == True :
            SortedReport[c] = CharDict[c]
    SortedReport = sorted(SortedReport.items(), key=lambda item: item[1], reverse=True)
    return SortedReport

def PrintReport(SortedReport, Book, BookWordCount):
    print(f"--- Begin report of {Book} ---")
    print(f"{BookWordCount} words found in the document")
    print("")
    for Charakter in SortedReport:
        print(f"The '{Charakter[0]}' character was found {Charakter[1]} times")
    print("--- End report ---")

def main():
    Book ="books/frankenstein.txt"
    BookContent = ReadBook(Book)
    BookWCount = BookWordCount(BookContent)
    CharCount = CharakterCount(BookContent)
    PrintReport(CharakterCountReport(CharCount),Book,BookWCount)

main()