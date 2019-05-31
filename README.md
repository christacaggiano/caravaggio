# PyVaggio - a computational exploration into the paintings of Michelangelo Caravaggio

## *A work very much in progress*

*What begins in the work of Caravaggio is, quite simply, modern painting" - André Berne-Joffroy*

## Goal
- **Goal 1:** can a binary classifier to learn to distinguish the paintings of Caravaggio from those of his close followers?
    - motivated by the misattribution of  *The Taking of Christ*<sup id="a1">[1](#f1)</sup> and a 'new' Caravaggio painting found in 2016<sup id="a1">[2](#f1)</sup>)

## Data Gathering

### Positive Examples
All paintings from Caravaggio used as positive training examples (see [3]), totaling about 90 works


### Negative Examples

Three general categories (1) painters that influenced  Caravaggio,
(2) painters that Caravaggio influenced, and (3) paintings in similar medium to Caravaggio, such as Italian Renaissance oil painting,
but are not particularly related to his art

#### (1) Influence on Caravaggio

Painters that influenced Caravaggio generally were Italian manneris

Titian, Giorgione, Carracci, and Italian Mannerism

#### (2) Caravaggisti
Falls into five categories, by region *Italian*, *Dutch*, *Flemish*, *French* and *Spanish*.  
Hypothesis is that this will be the hardest case, since art historians have confused his followers paintings
with Caravaggio's, such as *The Taking of Christ* ([1])


Painters included in examples, and number of paintings downloaded:


- **Italian Caravaggisti:** A Gentileschi (10), O Gentileschi (3), Baglione (3), and Borgianni (3)
- **Dutch Caravaggisti:** Von Honthorst (10), van Baburen (3), and ter Brugghen (3)
- **Flemish Caravaggisti:** Janssens (3) and Coster (3)
- **French Caravaggisti:** de La Tour (5), Boulogne (3), and Vouet (3)
- **Spanish Caravaggisti:** Ribera (5), Zurbaran (5), and Ribalta (3)

#### (3) Italian Renaissance and Baroque Oil Painting




### Citations
<b id="f1">1</b> [Taking of Christ, National Gallery of Ireland](https://www.nationalgallery.ie/art-and-artists/highlights-collection/taking-christ-michelangelo-merisi-da-caravaggio)

<b id="f1">2</b>  [A Long-Lost Painting Experts Say Is by Caravaggio Was Discovered in an Attic. It Could Fetch $171 Million at Auction", Artsy, 2019](https://news.artnet.com/market/attic-carvaggio-171-million-auction-estimate-1477111)

[3] [List of paintings by Caravaggio](https://en.wikipedia.org/wiki/List_of_paintings_by_Caravaggio#/media)
