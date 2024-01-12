# A* Skripta 

--- 

## Obsah
1. 
2. 
3. 
4. 
5. 
6. 


## Co to je algoritmus?
Algoritmus je přesný postup, díky kterému se dá vyřešit daný typ úlohy. Algoritmy se používají všude v programování.


## Co to vlastně A* je? 
A* je algoritmus, který se pokusí najít nejkratší cestu, pokud mu zadáme start a cíl. Existují ale vyjímky, kdy nalezená cesta nebude nejkratší. <br>
Ke správnému fungování algoritmu, ale potřebujeme znát nějaké údaje. Potřebujeme být schopni kdykoli v průběhu hledání cesty být schopni zjistit vzdálenost od místa kde se právě nacházíme ke startu a cíli. Musíme také ukládat pro každé políčko které prozkoumáme uložit ze které políčka jsme na něj přišly. Tím pak můžeme jednoduše nakonci jen jít po zpátku a zjistit cestu.

## Kde se A* používá? 
Algoritmus má široké využití v mnoha oborech. 

- Používá se v herním průmyslu pro hledání cesty v reálném čase pro různé postavy. 
- V robotice se také používá pro navigování robotů například v různých bludištích. 
- Plánování tra a logistika je další z oborů kde se A* užívá pro plánování tras. 
- A mnoho dalších.

## Jak A* funguje? 
Představme si že máme čtvercovou síť ve které se můžeme hýbat jen do čtyř směrů (Pro jednodušší vizualizaci a pochopení). Máme také určený start a cíl a nějaké  ty zdi (překážky). 

### 1. Naše první prozkoumané políčko je tedy start.

![A*-step1](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-001.png)

### 2. Podíváme se na každé ze 4 políček okolo a spočítáme jak daleko jsou od startu a od cíle a tyto dvě hodnoty sečteme.
- Vidíme, že nahoře je zeď, takže to ani nepočítáme, protože se tam stejně nedá dostat
- Nalevo je 1 od startu a 5 od cíle. To je 6 dohromady.
- Napravo je také 1 od startu ale 7 od cíle, takže to je 8 dohromady
- Dole je stále 1 od startu ale od cíle je také 7 a to je také 8 dohromady.

- Alogritmus tedy vybere nejmenší součet což je v tomto případě 6, neboli nalevo.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-002.png)

### 3. Teď se zase podíváme, jaké hodnoty mají políčka okolo našeho nově vybraného. 
- Doprava je start, takže tamtudy zase jít nemůžeme a tedy nepočítáme.
- Doleva je 2 od startu a 4 od cíle, takže dohromady 6.
- Dolu je to také 2 od startu, ale 6 od cíle, neboli 8 dohromady.
- Nahoru také 2 od startu a 4 od cíle, takže také 6 dohromady.

- Vidíme, že je zde dvakrát nejmenší 6, algoritmus se podívá, které z nich je blíž k cíli, ale oba jsou stejně, tak kontroluje, které má menší souřadnice x. Vybere tedy políčko v levo.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-003.png)

### 4. Zase se podíváme.
- Nahoru je 3 ke startu a 3 k cíli. Celkem 6.
- Dolu je to také 3 ke startu, ale 5 k cíli. Celkem 8.
- Nalevo je to také 3 ke startu a 5 k cíli. Celkem také 8.
- Doprava je políčko již prozkoumané, takže se nebude počítat znovu.

- Algortimus ale také kontroluje všechna neprozkoumaná políčka z dřívějších počítání a vidí tak, že i políčko nahoře z 3. kroku má hodnotu 6. Ale zase políčko nahoru z tohoto prozkoumávání je blíže k cíli, je tím pádem na řadě jako první.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-004.png)

### 5. A znovu
- Nahoru a dolu je zeď a dříve prozkoumané políčko, takže je nebudeme počítat.
- Doprava je políčko sice, již prozkoumané, ale algoritmus to udělá znovu, kdyby tam cesta byla kratší. Je tedy 2 od startu a 4 od cíle. Celkem 6.
- Doleva je 4 od startu a 4 od cíle. Celkem 8.

- Teď je tedy nejmenší políčko doprava i když se podíváme na všechny předchozí kroky.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-005.png)

### 6. A znovu
- Na všechny strany je teď ale již prozkoumané políčko, nebo zeď.

- Algoritmus se zase jako vždy podívá i na minulá políčka a vidí 6 políček s hodnotou 8. Podívá se které má nejmenší hodnotu na souřadnici x a vidí stále 2 možná políčka. A vyzkouší tedy ještě hodnotu na souřadnici y a vyjde mu tak jen jedno políčko a to doleva z kroku 5.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-006.png)

### 7. A znovu
- Algoritmus pokračuje jako dosud a objevuje nová políčka.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-007.png)

### 8. A znovu
- Algoritmus pokračuje jako dosud a objevuje nová políčka.

![A*- step2](/Vizualizace/Vizualizace-008.png)

### 9. A znovu
- Algoritmus pokračuje jako dosud a objevuje nová políčka.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-009.png)

### 10. A naposledy
- Když se algoritmus dostane k políčku napravo zjistí, že jeho hodnota k cíli je 0, tím pádem je to cíl. Algoritmus tedy toto políčko vybere a posune se k poslední části algoritmu.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-010.png)

### 11. Algoritmus našel políčka vedoucí až k cíli.
- Teď už se jenom podívá zpátky a zjistí ze kterého políčka přišel a opakuje tak, než se vrátí na začátek. Nakonec nám tedy vykreslí cestu, kterou našel.

![A*- step2](/home/jachym/Plocha/Škola/Programování a vývoj aplikací/A*/Vizualizace/Vizualizace-011.png)
## Porovnání s jinými pathfinding algoritmy 

### DFS
- Podívá se vždy okolo posledního prohledaného políčka. Když tedy půjdeme v pořadí nahoru, doprava, dolu, doleva, půjde tedy pokud možno vždy doleva a pokud nemůže tak dolu.

#### Výhody
- Jednoduché implementování.

#### Nevýhody
- I když cíl bude kousek rovně, ale nebude na správné straně, tak prohledá velkou část mapy a bude trvat dlouho, než se dostane do cíle.
- Ne vždy se kvůli tomu také vůbec nepovede najít cíl.

### BFS
- Prohledá okolí políčka, které bylo prohledáno před nejdelší dobou. Po nalezení cíle se vrátí kudy přišel a vykreslí cestu.

#### Výhody
- Vždy najde cestu, která je vždy nejkratší, pokud nejsou implementovány různé podmínky. 
- S některými podmínkami ale zvládne pracovat a omezit se podle nich.

#### Nevýhody
- Hledání trvá dlouho, protože prohledá kruhy v celém rádiusu, než se dostane k cíli.

### Djikstra

#### Výhody

#### Nevýhody

### A*

#### Výhody

#### Nevýhody

## Historie 
