# AuthorProfiling
NLP project: classification of time period and author age in fiction

## Preprocessing

### Get Corpus from Gutenberg
- Get text files in English Language (ISO code EN)
```shell
wget -w 2 -m -H "http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=en"
```

- Get Catalog Data
The complete Project Gutenberg catalog is available in [RDF/XML Format](https://www.w3.org/RDF/).
This file is a tar archive that contains one RDF file for each book. The RDF is based on the [DCMI](http://dublincore.org/documents/dc-rdf/) recommendation
Since the file size is too large for git/github, here's the link to download the [catalog](https://www.gutenberg.org/wiki/Gutenberg:Feeds).

  - For instance, here's an extraction from the catalogue, note that in the first row, the text ID is 1342
  ```xml
  <pgterms:etext rdf:ID="etext1342">
    <dc:publisher>&pg;</dc:publisher>
    <dc:title rdf:parseType="Literal">Pride and Prejudice</dc:title>
    <dc:creator rdf:parseType="Literal">Austen, Jane, 1775-1817</dc:creator>
    <pgterms:friendlytitle rdf:parseType="Literal">Pride and Prejudice by Jane Austen</pgterms:friendlytitle>
    <dc:language><dcterms:ISO639-2><rdf:value>en</rdf:value></dcterms:ISO639-2></dc:language>
    <dc:subject>
      <rdf:Bag>
        <rdf:li><dcterms:LCSH><rdf:value>Young women -- Fiction</rdf:value></dcterms:LCSH></rdf:li>
        <rdf:li><dcterms:LCSH><rdf:value>England -- Fiction</rdf:value></dcterms:LCSH></rdf:li>
        <rdf:li><dcterms:LCSH><rdf:value>Domestic fiction</rdf:value></dcterms:LCSH></rdf:li>
        <rdf:li><dcterms:LCSH><rdf:value>Love stories</rdf:value></dcterms:LCSH></rdf:li>
        <rdf:li><dcterms:LCSH><rdf:value>Sisters -- Fiction</rdf:value></dcterms:LCSH></rdf:li>
        <rdf:li><dcterms:LCSH><rdf:value>Social classes -- Fiction</rdf:value></dcterms:LCSH></rdf:li>
        <rdf:li><dcterms:LCSH><rdf:value>Courtship -- Fiction</rdf:value></dcterms:LCSH></rdf:li>
      </rdf:Bag>
    </dc:subject>
    <dc:subject><dcterms:LCC><rdf:value>PR</rdf:value></dcterms:LCC></dc:subject>
    <dc:created><dcterms:W3CDTF><rdf:value>1998-06-01</rdf:value></dcterms:W3CDTF></dc:created>
    <pgterms:downloads><xsd:nonNegativeInteger><rdf:value>38933</rdf:value></xsd:nonNegativeInteger></pgterms:downloads>
    <dc:rights rdf:resource="&lic;" />
  </pgterms:etext>
  ```

  - To get the book from the catalog above, use:
  ```shell
    wget "http://www.gutenberg.org/files/1342/1342-0.txt"
  ```

- Canonical URLs to txt format of the Books
  - http://www.gutenberg.org/files/1342/1342-0.txt
  - http://www.gutenberg.org/files/161/161.txt
  - http://www.gutenberg.org/cache/epub/946/pg946.txt
- Canonical URLs for Authors
  - http://www.gutenberg.org/authors/Jane_Austen
- Note that audio, and non-English documents should be excluded

### Get Age and Time Period from Wikipedia
- Begin by installing wikipedia:
```
$ pip install wikipedia
```

- Run wiki.py
  - When prompted to input query, type the query and hit Enter (for instance, try "jane austen")
  - Returns a summary from the Wikipedia page containing the birth and publication data of main authors

### Sample Data: Jane Austen
- Contains a txt with birth year, written year, and list of urls for (English, fictional, non-collection) books
- Contains the cleaned text for the books

### Cleaned Corpus and Metadata (.csv)
- [first 200 cleaned (57 books)](https://drive.google.com/open?id=1hDY0QSshBv_b2574L2pFXm7PvDpEGSr1)
- [first 600 cleaned (133 books)](https://drive.google.com/open?id=1FDJ1zvcHHAw5viKvEi3RAheISXYCRCX7)
- [first 1200 cleaned (238 books)](https://drive.google.com/open?id=1WcLkI-uBUKJ2V79wGyGE6oY6-24qfaWB)
