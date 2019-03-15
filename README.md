# AuthorProfiling
NLP project: classification of time period and author age in fiction

## Preprocessing
Get text files in English Language (ISO code EN)
```
wget -w 2 -m -H "http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=en"
```

Get Catalog Data
The complete Project Gutenberg catalog is available in [RDF/XML Format](https://www.w3.org/RDF/).
This file is a tar archive that contains one RDF file for each book. The RDF is based on the [DCMI](http://dublincore.org/documents/dc-rdf/) recommendation
Since the file size is too large for git/github, here's the link to download the [catalog](https://www.gutenberg.org/wiki/Gutenberg:Feeds).

For instance, here's an extraction from the catalogue,
note in the first row, the text ID is 14600
```
<pgterms:etext rdf:ID="etext14600">
  <dc:publisher>&pg;</dc:publisher>
  <dc:title rdf:parseType="Literal">Theory of Silk Weaving
A Treatise on the Construction and Application of Weaves, and the Decomposition and Calculation of Broad and Narrow, Plain, Novelty and Jacquard Silk Fabrics</dc:title>
  <dc:creator rdf:parseType="Literal">Wolfensberger, Arnold</dc:creator>
  <pgterms:friendlytitle rdf:parseType="Literal">Theory of Silk Weaving by Arnold Wolfensberger</pgterms:friendlytitle>
  <dc:language><dcterms:ISO639-2><rdf:value>en</rdf:value></dcterms:ISO639-2></dc:language>
  <dc:subject>
    <rdf:Bag>
      <rdf:li><dcterms:LCSH><rdf:value>Weaving</rdf:value></dcterms:LCSH></rdf:li>
      <rdf:li><dcterms:LCSH><rdf:value>Silk industry</rdf:value></dcterms:LCSH></rdf:li>
    </rdf:Bag>
  </dc:subject>
  <dc:subject><dcterms:LCC><rdf:value>TS</rdf:value></dcterms:LCC></dc:subject>
  <dc:created><dcterms:W3CDTF><rdf:value>2005-01-05</rdf:value></dcterms:W3CDTF></dc:created>
  <pgterms:downloads><xsd:nonNegativeInteger><rdf:value>146</rdf:value></xsd:nonNegativeInteger></pgterms:downloads>
  <dc:rights rdf:resource="&lic;" />
</pgterms:etext>
```
To get the above line of code, use:
```
wget http://www.gutenberg.org/cache/epub/14600/pg14600.txt
```
