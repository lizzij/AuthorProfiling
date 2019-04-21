# AuthorProfiling
NLP project: classification of time period and author age in fiction

## Reports
- [Proposal](https://github.com/lizzij/AuthorProfiling/blob/master/reports/NLP%20Proposal.pdf)
- [Progress Report](https://github.com/lizzij/AuthorProfiling/blob/master/reports/NLP%20Progress%20Report.pdf)
- [Final Report]()

## Data Preprocessing

### Navigating Gutenberg
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

### Generate Standard Corpus and Metadata
- generate the corpus locally [here](https://github.com/pgcorpus/gutenberg)
```bash
git clone https://github.com/pgcorpus/gutenberg.git
```
- enter the newly created `gutenberg` directory
```bash
cd gutenberg
```

- To install any missing dependencies, just run
```bash
pip install -r requirements.txt
```

- To get a local copy of the PG data, just run
```
python get_data.py
```
This will download a copy of all UTF-8 books in PG and will create a csv file with metadata (e.g. author, title, year, ...).
 `get_data.py`.

- To process all the data in the `raw/` directory, run
```bash
python process_data.py
```
This will fill in the `text/`, `tokens/` and `counts/` folders.

### Get Age and Time Period from Wikipedia
- Begin by installing wikipedia:
```bash
$ pip install wikipedia
```

- Run wiki.py
  - When prompted to input query, type the query and hit Enter (for instance, try "jane austen")
  - Returns a summary from the Wikipedia page containing the birth and publication data of main authors

### Clean Data, Tag Categories
- Move `text/` to the same directory rename `metadata.csv` to `clean_all.csv`
- Run `clean.ipynb`

### Data
- [first 200 cleaned (57 books)](https://drive.google.com/open?id=1hDY0QSshBv_b2574L2pFXm7PvDpEGSr1)
- [first 600 cleaned (133 books)](https://drive.google.com/open?id=1FDJ1zvcHHAw5viKvEi3RAheISXYCRCX7)
- [first 1200 cleaned (238 books)](https://drive.google.com/open?id=1WcLkI-uBUKJ2V79wGyGE6oY6-24qfaWB)
- [first 1200, 5000-6500 (328 books)](https://drive.google.com/open?id=1eJ7CR9lX544_IXwbBXgUgY9pEpIpg9vK)
- [first 1200, 5000-7500 (380 books)](https://drive.google.com/open?id=1CiAIq8zgWzrQRSkiacvkmIAaHaocmslT)
- [first 1200, 5000-8500 (412 books)](https://drive.google.com/open?id=1pEZ7zU4-HrkvWt2q-t83p-RPUvMPmb-1)
- [first 3000, 5000-6500 (582 books)](https://drive.google.com/open?id=1veTg-NOKbNrp-TIadYNLBlt7BZhdaL5Z)
- [first 3500, 5000-8500 (621 books)](https://drive.google.com/open?id=13OAsKLyJGmLsiOcZcc--F7fYBtCTndZg)
- [first 8500 (711 books)](https://drive.google.com/open?id=1u0iFeKaIEC7u7FBWkHS6fMWueHn3C30h)
