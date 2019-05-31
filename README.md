# PyVaggio - a computational exploration into the paintings of Michelangelo Caravaggio

## *A work very much in progress*

*What begins in the work of Caravaggio is, quite simply, modern painting" - André Berne-Joffroy*

## Goal
- **Goal 1:** can a binary classifier to learn to distinguish the paintings of Caravaggio from those of his close followers?
    - motivated by the misattribution of  *The Taking of Christ*<sup id="a1">[1](#f1)</sup> and a 'new' Caravaggio painting found in 2016<sup id="a3">[2](#f1)</sup>

## Data Gathering

Jpegs were mostly downloaded from Wikimedia Commons. Files were downloaded manually, and there was some curation to pick higher quality images that were unobstructed and faithful reproductions of the original work (i.e. no [frames in the image](https://s3-us-west-2.amazonaws.com/prod-newel/images/inventory/MEN033/picture_portrait_Italian_Renaissance_MEN033-02.jpg), [extremely small files](https://www.oilpaintingfactory.com/pic-html/Oil%20Painting%20Masterpieces%20on%20Canvas/Lippi%20Fra%20Filippo_Italy_1406-1469/thumbnails/8_Adoration_Of_The_Child_religious_Renaissance_Filippo_Lippi.jpg), or images with obvious processing/[cropping](https://webartacademy.com/wp-content/uploads/2015/05/Venetian-Painting-Techniques-during-the-Italian-Renaissance-Sleeping-Venus-by-Titian.jpg))

### Positive Examples
All paintings from Caravaggio used as positive training examples<sup id="a3">[3](#f1)</sup>, totaling about 90 works.


### Negative Examples

Three general categories (1) painters that influenced  Caravaggio,
(2) painters that Caravaggio influenced, and (3) paintings in similar medium or topic to Caravaggio, such as Renaissance oil painting, but are not directly related in style to Caravaggio.

#### (1) Influence on Caravaggio

Caravaggio started his art career when mannerism was popular<sup id="a4">[4](#f1)</sup>. In particular, I downloaded (10) pieces from three painters whose work Caravaggio would have definitely known<sup id="a5">[5](#f1)</sup>: **Titian**<sup id="a6">[6](#f1)</sup>, **Carracci**<sup id="a7">[7](#f1)</sup> and **Giorgione**<sup id="a8">[8](#f1)</sup>. (10) random works were chosen from the **Mannerism**<sup id="a9">[9](#f1)</sup> and Northern Mannerism<sup id="a10">[10](#f1)</sup> wikipedia pages.


#### (2) Caravaggisti
Falls into five categories, by region *Italian*, *Dutch*, *Flemish*, *French* and *Spanish*.  


My hypothesis is that this will be the hardest case, since art historians have confused his followers paintings
with Caravaggio's, such as *The Taking of Christ* ([1])


Painters included in examples, and number of paintings downloaded:


- **Italian Caravaggisti:** A Gentileschi (10), O Gentileschi (3), Baglione (3), and Borgianni (3)
- **Dutch Caravaggisti:** Von Honthorst (10), van Baburen (3), and ter Brugghen (3)
- **Flemish Caravaggisti:** Janssens (3) and Coster (3)
- **French Caravaggisti:** de La Tour (5), Boulogne (3), and Vouet (3)
- **Spanish Caravaggisti:** Ribera (5), Zurbaran (5), and Ribalta (3)

#### (3) Oil Paintings

Paintings with similar medium and often with similar religious themes, but should only be distantly related to Caravaggio(15) **Italian Renaissance** oil paintings were accessed and downloaded, regardless of painter. These are generally related to Caravaggio's paintings- most directly influencing Mannerism- but aren't that visually similar to Caravaggio's work. (5) **French Renaissance** were also  downloaded, as they share some characteristics, but are generally very different from Caravaggio's paintings. Finally (5) **random "famous" paintings** were downloaded. These include work by van Gogh and Whistler. Why it can be argued that this work would not be possible without Caravaggio, they are very far in composition and theme from a Caravaggio piece. 




## Citations
<b id="f1">1</b> [Taking of Christ, National Gallery of Ireland](https://www.nationalgallery.ie/art-and-artists/highlights-collection/taking-christ-michelangelo-merisi-da-caravaggio) [↩](#a1)

<b id="f1">2</b>  [A Long-Lost Painting Experts Say Is by Caravaggio Was Discovered in an Attic. It Could Fetch $171 Million at Auction", Artsy, 2019](https://news.artnet.com/market/attic-carvaggio-171-million-auction-estimate-1477111) [↩](#a2)

<b id="f1">3</b>  [List of paintings by Caravaggio](https://en.wikipedia.org/wiki/List_of_paintings_by_Caravaggio#/media), Wikipedia [↩](#a3)

<b id="f1">4</b> [Italian Mannerism](https://psyc.ucalgary.ca/PACE/VA-Lab/AVDE-Website/mannerism.html) [↩](#a4)

<b id="f1">5</b> [*Caravaggio*](https://books.google.com/books?id=q_U8FzJThfcC&printsec=frontcover#v=onepage&q&f=false), by Helen Landon [↩](#a5)

<b id="f1">6</b> [Titian](https://en.wikipedia.org/wiki/Titian), Wikipedia [↩](#a6)

<b id="f1">7</b> [Annibale Carracci](https://en.wikipedia.org/wiki/Annibale_Carracci), Wikipedia [↩](#a7)

<b id="f1">8</b> [Giorgione](https://en.wikipedia.org/wiki/Giorgione), Wikipedia [↩](#a8)

<b id="f1">9</b> [Mannerism](https://en.wikipedia.org/wiki/Mannerism), Wikipedia [↩](#a9)

<b id="f1">10</b> [Northern Mannerism](https://en.wikipedia.org/wiki/Northern_Mannerism), Wikipedia [↩](#a10)
