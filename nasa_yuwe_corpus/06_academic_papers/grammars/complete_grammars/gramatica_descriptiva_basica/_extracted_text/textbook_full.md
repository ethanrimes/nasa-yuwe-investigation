---
title: Gramática Descriptiva Básica del Nasa Yuwe — full extracted text
author: Rocío del Pilar Nieves Oviedo
publisher: Programa Editorial Universidad del Valle
year: 2019
isbn: 978-958-765-950-4
source: 143 page-screenshots OCR'd via Tesseract (spa+por+cat, PSM 6) on 2× upscaled crops; high-value paradigm tables vision-verified.
license: Quoted under fair use for linguistic / MT research; not for redistribution.
extraction_pipeline: |
  1. Pillow crop (870,155,2075,1857) → 2× LANCZOS upscale → grayscale
  2. tesseract --psm 6 -l spa+por+cat
  3. Per-chapter concatenation + viewer-chrome stripping
  4. Critical NY tables re-transcribed by Claude vision and substituted inline
markers: |
  <!-- vision-verified --> tables transcribed by Claude vision against the page image
  <!-- ocr -->             raw OCR prose (Spanish ~98% accurate, NY italics ~75%)
---

# Gramática Descriptiva Básica del Nasa Yuwe — full text

This is the **complete reusable extracted text** of Nieves Oviedo (2019). It supersedes
the partial digital-PDF chapter extractions in `clean/` (which only contain the first
few pages of each chapter and are entirely missing Cap 2 Fonología and Cap 5 Sintaxis).

The OCR of Spanish prose is excellent. Nasa-Yuwe orthographic forms — which use italics
in the original, with cedilla `ç`, tilde vowels `ã ẽ ĩ õ ũ` and apostrophe `ʼ / '`
glottalisation — survive with ~75-85% fidelity. **Where a paradigm table is critical
for the MT model (phoneme inventory, IPA↔orthography map, pronouns, mode-personal
markers, possessives) the OCR has been replaced with a vision-verified transcription**
marked `<!-- vision-verified -->`.

## How to use this file

- For Spanish-language exposition of the grammar → read the OCR sections directly.
- For Nasa-Yuwe forms to feed into the MT lexicon / morph analyser → use the
  vision-verified tables here, plus the derived CSVs in `../../../*.csv`.
- For per-rule lookup → see `UNIFIED_GRAMMAR_RULES.md` one directory up.

## Vision-verified tables (canonical)

These take precedence over any OCR rendering of the same table that appears later
in the chapter bodies.

### Tabla 1 — Fonemas consonánticos (sistema de 37, pp. 28-29)
<!-- vision-verified -->

|                    | Básicos | Palatalizados |
|---                 |---      |---            |
| Oclusivos básicos  | p, t, ts, k                | pʲ, tʲ, tsʲ, kʲ |
| Oclusivos aspirados | pʰ, tʰ, tsʰ, kʰ           | pʲʰ, tʲʰ, tsʲʰ, kʲʰ |
| Oclusivos prenasalizados | ᵐb, ⁿd, ⁿdz, ⁿg     | ᵐbʲ, ⁿdʲ, ⁿdzʲ, ⁿgʲ |
| Fricativos sordos  | s, h                       | ɸʲ, sʲ, hʲ |
| Fricativos sonoros | —                          | βʲ |
| Nasales            | m, n                       | nʲ |
| Laterales          | l                          | lʲ |
| Aproximantes       | w (labiovelar), j (palatoalveolar) | — |

Total: 37 consonantes (24 oclusivas + 6 fricativas + 3 nasales + 2 laterales + 2 aproximantes).
The reduced inventories reported for Munchique-Tigres / Toribío drop several
palatalised members (34-35 consonantes).

### Tabla 4-6 — Correspondencia AFI ↔ ortografía unificada (Cap 2, p. 56)
<!-- vision-verified --> **The single most important table for MT preprocessing.**

#### Consonantes — Básicos

| AFI | Orto. | AFI | Orto. |
|---|---|---|---|
| p   | p   | ᵐb   | b |
| t   | t   | ⁿd   | d |
| ts  | ç   | ⁿdz  | z |
| k   | k   | ⁿg   | g |
| pʰ  | ph  | s    | s |
| tʰ  | th  | h    | j |
| tsʰ | çh  | m    | m |
| kʰ  | kh  | n    | n |
|     |     | l    | l |

#### Consonantes — Palatalizados

| AFI | Orto. | AFI | Orto. |
|---|---|---|---|
| pʲ   | px   | ᵐbʲ   | bx |
| tʲ   | tx   | ⁿdʲ   | dx |
| tsʲ  | çx   | ⁿdzʲ  | zx |
| kʲ   | kx   | ⁿgʲ   | gx |
| pʲʰ  | pxh  | ɸʲ    | fx |
| tʲʰ  | txh  | sʲ    | sx |
| tsʲʰ | çxh  | hʲ    | jx |
| kʲʰ  | kxh  | βʲ    | vx |
|      |      | nʲ    | nx |
|      |      | lʲ    | lx |

#### Aproximantes

| AFI | Orto. |
|---|---|
| w | w |
| j | y |

#### Vocales (oral, nasal, glotalizada/interrupta, aspirada)

| Cualidad | Oral breve | Oral larga | Glotalizada (interrupta) | Aspirada | Nasal breve | Nasal larga | Nasal glotalizada | Nasal aspirada |
|---|---|---|---|---|---|---|---|---|
| /i/ | i | ii | iʼ | ih | ĩ | ĩĩ | ĩʼ | ĩh |
| /e/ | e | ee | eʼ | eh | ẽ | ẽẽ | ẽʼ | ẽh |
| /a/ | a | aa | aʼ | ah | ã | ãã | ãʼ | ãh |
| /u/ | u | uu | uʼ | uh | ũ | ũũ | ũʼ | ũh |

Nasa Yuwe is the **four-vowel** inheritor in its inventory (i, e, a, u — no /o/ in the
core inventory of Tierradentro/Caldono/Pueblo-Nuevo/Paniquitá; Munchique/Tigres has a
24-vowel reduced system without long vowels). Counting the 8 oppositions per quality
× 4 qualities = **32 vocal phonemes**.

### Tabla 8 — Pronombres personales (Cap 4 / Cap 6 p. 128)
<!-- vision-verified -->

| Persona | Género | Singular | Plural |
|---|---|---|---|
| 1ª | M | `adx` / `agx` | `kweʼsx` |
| 1ª | F | `uʼkwe`       | `kweʼsx` |
| 2ª | M | `idx` / `igx` | `iʼkweʼsx` |
| 2ª | F | `iʼkwe`       | `iʼkweʼsx` |
| 3ª | neutro | `txã` / `kxã` | `txãweʼsx` / `kxãweʼsx` |

Slash forms = dialectal / register variants (the `dx/gx` and `txã/kxã` alternations
are documented in Cap 6). Gender contrast is restricted to 1sg and 2sg.

### Tabla 9 — Morfemas modopersonales (paradigma completo, Cap 4 p. 64)
<!-- vision-verified -->

| Persona | Asertivo | Suspensivo | Interrogativo |
|---|---|---|---|
| 1sg | `-thu`            | `-tka`             | `-nja`              |
| 2sg | `-gu`             | `-ga`              | `-gaʼ`              |
| 3sg | `-ku` / `-aʼ`     | `-ka` / `-na`      | `-kaʼ` / `-naʼ`     |
| 1pl | `-thaʼw`          | `-tkhaʼw`          | `-njaʼw`            |
| 2pl | `-iʼkwe`          | `-kwe`             | `-kweʼ`             |
| 3pl | `-txi` / `-ta`    | `-txna` (≈ `-txina`, see Tabla 13) | `-txnaʼ` |

3sg slash forms = predicación dinámica (PD) / predicación estativa (PE) cell.
Discrepancy `-txna` (Tabla 9) vs `-txina` (Tabla 13) for 3pl suspensive likely
reflects an allomorph by stem-final phonology — both surface forms are attested
in the OCR'd examples.

### Tabla 13 — Marcadores modopersonales 3ª persona desambiguados (Cap 4 p. 107)
<!-- vision-verified -->

| Tipo predicación | 3sg ASER | 3sg SUS | 3sg INTE | 3pl ASER | 3pl SUS | 3pl INTE |
|---|---|---|---|---|---|---|
| Estativa (PE) | `-aʼ` | `-na` | `-naʼ` | `-ta` | `-txina` | `-txinaʼ` |
| Dinámica (PD) | `-ku` | `-ka` | `-kaʼ` | `-tx` | `-txna` | `-txnaʼ` |

This is the table to use when implementing the MT system. Tabla 9 collapses these
into single rows; Tabla 13 is the disambiguated reference.

### Tabla 14 — Determinantes posesivos (Cap 6 p. 128)
<!-- vision-verified -->

Identical to personal pronouns *except* for 3rd person, which adds the benefactive
`{-ji}` to disambiguate from the homophonous demonstrative.

| Persona | Singular | Plural |
|---|---|---|
| 1 M | `adx` / `agx`       | `kweʼsx` |
| 1 F | `uʼkwe`             | `kweʼsx` |
| 2 M | `idx` / `igx`       | `iʼkweʼsx` |
| 2 F | `iʼkwe`             | `iʼkweʼsx` |
| 3   | `txãji` / `kxãji`   | `txãweʼsx` / `kxãweʼsx` |

---

## Chapter contents (OCR'd, raw)

The remainder of this file is the cleaned per-chapter OCR. The headers `<!-- page N -->` indicate the source screenshot number for back-referencing.



# Front Matter (presentación, índice, símbolos, abreviaturas)
<!-- ocr -->

<!-- page 1 (screenshot 0001) -->
Gramática descriptiva básica del
NT VV,

ACA TW,
*INASA IUWE*
lengua indígena
colombiana
Colección Artes y Humanidades
Linguística

<!-- page 2 (screenshot 0002) -->
CONTENIDO
PRESENTACIÓN 11
SÍMBOLOS Y CONVENCIONES 14
ABREVIATURAS 15
Capítulo 1
GENERALIDADES
El pueblo nasa 17
La lengua 20
Sobre esta gramática 24
Capítulo 2
FONOLOGÍA 27
Fonemas consonánticos 28
Fonemas vocálicos 40
La sílaba 48
Morfofonologia 52
Ortografia normalizada 54
Capítulo 3
MORFOLOGÍA
El morfema 57
Procedimientos morfológicos 67
La palabra 76

<!-- page 3 (screenshot 0003) -->
Capitulo 4
MORFOSINTAXIS
La predicación 81
Clases de palabras 88
Capitulo 5
SINTAXIS 113
Funciones 114
La oración 126
Capitulo 6
EXPRESIÓN DE LA DEÍXIS 147
La persona 148
El espacio 149
El tiempo 156
BIBLIOGRAFÍA 163
GLOSARIO
Términos correspondientes a conceptos
de fonología y de fonética articulatoria 169

<!-- page 4 (screenshot 0004) -->
SÍMBOLOS Y CONVENCIONES

* agramatical o inexistente

= igual o equivalente a

— se realiza

- alternancia fonológica o condicionamiento fonoló-
gico entre alomorfos

- situado a la izquierda, indica que el morfema se su-
fija a una base
situado a la derecha, indica que el morfema se pre-
fija a una base
a ambos lados del morfema, indica que el morfema
puede estar rodeado de otros morfemas

. división silábica

fo] cero

+ agrega morfemas o categorías

La morfema

mm transcripción fonética

Ped transcripción fonológica

/...] :/.../ oposición fonológica

A significado en español de morfemas, palabras u ora-
ciones

En la notación yuxtalineal de los ejemplos:

La nivel morfológico

4.1 enunciado

/ separa palabras

- separa morfemas

e glosa en español

. amalgama de categorías

<!-- page 5 (screenshot 0005) -->
ABREVIATURAS
ADI - aditivo IMPpl imperativo plural
ALA —alativo (locativo) IMPF imperfectivo
ANT.DS anterioridad diferente sujeto INCER incertidumbre
ANT.IS anterioridad igual sujeto INCI — incitativo
AOR aspecto aoristo INCO aspecto incoativo
ASER modoasertivo INE — inesivo (locativo: genérico o eje
BEN — benefactivo corporal vertical)
C conector INEh  inesivo (eje corporal horizontal)
CAUS causativo INEi —inesivo (eje corporal ligeramente
CM caso morfológico inclinado)
COL colectivo INEp  inesivo (eje corporal con fuerte
CONC.DS concesivo diferente sujeto pendiente)
CONC.IS concesivo igual sujeto INM aspecto inminente
CONF confirmado INS — instrumental
CORR corroborativo INT aspecto interno
D deíctico INTE modo interrogativo
DEMI demostrativo cercano IS igual sujeto
DEM2 demostrativo lejano ITE — aspecto iterativo
DES —desiderativo LV lexema verbal
DIM diminutivo MPN modo.persona.número
DIN dinamizador N nominal
DUR aspecto durativo NEG negación
DS distinto sujeto NOM nominalizador
ELA —elativo (locativo) OBJ — objeto (acusativo/dativo)
ENF enfático OBJpl objeto plural
EXH  exhortativo PD predicación dinámica
EXT — aspecto externo PE predicación estativa
FACT factitivo PROH prohibitivo
FIN.G finalidad general PROS aspecto prospectivo
FIN.E finalidad específica Q cualificativo
FUT futuro TOP  topicalizador
HIP hipotético RECI recíproco
IMP imperativo REF — reflexivo

<!-- page 6 (screenshot 0006) -->
RES — aspecto resultativo VOL — volitivo

REST restrictivo 1ps primera persona del singular
SIMI — similativo Ipp primera persona del plural
SOC sociativo 2ps segunda persona del singular
SUS — modo suspensivo 2pp segunda persona del plural
TOP — topicalizador 3ps tercera persona del singular
V verbo 3pp tercera persona del plural
VN verbonominal

# Capítulo 2 — Fonología
<!-- ocr -->

<!-- page 7 (screenshot 0007) -->
CAPÍTULO 2
FONOLOGÍA

En este capítulo se presenta el sistema de fonemas de la lengua. Se entien-
de fonema como la unidad mínima de la lengua con carácter distintivo.
Este carácter distintivo se debe a que los fonemas establecen contraste u
oposición entre ellos, de tal manera que al sustituir uno por otro en un mis-
mo contexto puede resultar una palabra diferente. El fonema es la unidad
correspondiente al nivel fonológico, nivel en el que se organiza el material
fónico de la lengua.

Se considera un universal lingiístico relacionado con el nivel fonológico
de las lenguas el hecho de que en todas existen fonemas consonánticos y
fonemas vocálicos. En la mayoría de ellas, los fonemas vocálicos funcionan
como núcleo de la sílaba en tanto los fonemas consonánticos constituyen sus
márgenes; el nasa yuwe no es la excepción. Se presentan en esta fonología,
primero, los fonemas consonánticos y, después, los fonemas vocálicos. Pos-
teriormente se presenta la sílaba, que es el ámbito en el que se combinan y
funcionan estas dos grandes clases de unidades fonológicas.

En relación con el nivel fonológico de la lengua, se han adelantado en los
últimos decenios estudios académicos serios en diversas regiones. Se cuenta
en la actualidad con datos de Munchique-Tigres (Rojas, 1991a, 1998; Díaz,
2014), Toribío (Yule, 1991b), Caldono (Nieves, 1991b), Pueblo Nuevo (Nie-
ves, 1991a), Paniquitá (Nieves, 1991c), Novirao (Rojas, Perdomo y Corrales,
2011) y Tierradentro (Jung, 2000, 2008; Nieves, 1991a). Esto permite presen-
tar el sistema teniendo en cuenta lo que ocurre en la mayoría de las regiones.

Las variaciones dialectales o regionales de la lengua en lo fonológico tie-
nen que ver fundamentalmente con la presencia o ausencia de determinados

<!-- page 8 (screenshot 0008) -->
fonemas en el sistema, la manera en que los fonemas se disponen fonética-
mente, así como la estructura silábica.

En cuanto a los fonemas consonánticos, se ha reportado para Tierraden-
tro, Paniquitá y la zona de Caldono-Pueblo Nuevo el sistema más completo,
con 37 unidades (Nieves, 1991a, 1991c). En las otras regiones se han repor-
tado menos unidades, según los datos de Rojas (1991a, 1998), 34 fonemas;
Yule (1991b), 34 fonemas; Rojas, Perdomo y Corrales (2011), 35 fonemas. Si
bien el trabajo de Jung (2000, 2008) se hizo en Tierradentro, según sus datos
aparecen solamente 35 fonemas consonánticos. Para la presentación, se par-
te del sistema de 37 fonemas y posteriormente se enuncian las diferencias
encontradas en los otros sistemas.

En cuanto a los fonemas vocálicos, en Tierradentro, Caldono, Pueblo
Nuevo, Paniquitá, Novirao se reportan sistemas de 32 unidades. En la zona
norte (Toribio y Munchique- Tigres) se reportan ocho unidades menos que
en las demás regiones, es decir, un sistema de 24 fonemas. Sin embargo, un
trabajo reciente reporta para la región de Munchique la presencia de vocales
largas como fonemas de la lengua (Díaz, 2014). Para la presentación de los
fonemas vocálicos se procede de la misma manera.

En relación con la realización fonética de los fonemas, algunos procesos
se dan de manera similar en todas las regiones, pero se encuentran también
algunas particularidades regionales. Y en cuanto a la estructura silábica, en
Toribio se construye de manera diferente.

Después de que se hayan presentado los fonemas, la ilustración de las
oposiciones, las reglas de realización y la estructura silábica, dentro de este
capítulo se tratarán también los procesos morfofonológicos. Se presentará
igualmente la ortografía unificada de la lengua en correspondencia con el
sistema fonológico. En los siguientes capítulos, los ejemplos se escribirán
con dicha ortografía normalizada.

FONEMAS CONSONÁNTICOS

El nasa yuwe, en su sistema fonológico más completo, tiene treinta y sie-
te fonemas consonánticos, organizados en cuatro órdenes y ocho series.
Los órdenes articulatorios son: labial, apical, palatoalveolar” y posterior”.
Las series son: oclusivos básicos, oclusivos aspirados, oclusivos prenasali-
LU Hay que aclarar que los fonemas agrupados en este orden son fonéticamente africados, pero se

agrupan con los oclusivos por organización del sistema y porque en varios aspectos se comportan

de manera similar a los oclusivos.
BR. Se recurre a esta denominación para cubrir los puntos articulatorios velar y glotal.

<!-- page 9 (screenshot 0009) -->
FONOLOGÍA
zados, fricativos sordos, fricativos sonoros, nasales, laterales y aproximan-
tes. Existe, además, una correlación de palatalización con todas las series,
excepto la de los aproximantes. Se entiende por correlación una relación
sistemática entre dos series cuyos fonemas presentan cierto paralelismo.

Hay veinticuatro fonemas oclusivos: cuatro básicos, cuatro palatalizados,
cuatro aspirados, cuatro aspirados palatalizados —todos estos son sordos—,
cuatro prenasalizados y cuatro prenasalizados palatalizados —estos últimos
ocho son básicamente sonoros—. Los cuatro fonemas de cada uno de estos
grupos se sitúan en los cuatro órdenes articulatorios antes mencionados.

Hay seis fonemas fricativos: dos básicos y dos palatalizados, sordos, co-
rrespondientes a los órdenes apical y velar; en el orden labial hay dos pala-
talizados, sordo y sonoro. Los fonemas nasales son tres: labial, apical y su
correlato palatalizado. Hay dos laterales: apical y su correlato palatalizado. Y
dos fonemas aproximantes: labiovelar y palatoalveolar.

Tabla 1. Fonemas consonánticos
Básicos Palatalizados
Labial Apical Palatoalveolar Posterior | Labial Apical Palatoalveolar Posterior
Oclusivos p t ts R p t ts) ki
Ocl. aspirados Pp e ts! le p' ra th Ko
Ocl. prenasalizados "b  "d "dz "g Y “Y "dz "gi
Fricativos sordos Ss h (0) si h
Fricativo sonoro g
Nasales m n n
Laterales l y
Aproximantes w j

En Munchique no se reportan los fonemas consonánticos /p”/, /k/ ni
l"gi/ (Rojas, 1991a). En Toribío faltan los fonemas /k/ y /”gi/ (Yule, 1991b):.
En Novirao no se reporta la existencia de los fonemas /"b// ni /ts*/ (Rojas,
Perdomo y Corrales, 2011). Según los datos de Tierradentro presentados
por Jung (2000, 2008) no aparecen los fonemas /p"/, /k/ ni /"g//; en cambio
interpreta como fonema /n"/, que para los demás investigadores es una se-
cuencia de los fonemas /n/ y /h/.

4. Las palabras que tienen /K/ o /"g// en las otras regiones, se pronuncian en Toribío con /t/ y /"d//,
respectivamente.

<!-- page 10 (screenshot 0010) -->
FONOLOGÍA
NÒ: /k/ R'asi “sopa, mazamorra”
Ras “tejido ralo”
187 : lts) tê) “difícil”
tsEj “verde, azul”
Oclusivos palatalizados
/p)/ : /p/ túpla" "està desnudo"
túpa' “es araña”
/8/ : ft tut “estómago, barriga”
tut “puño”
/ts)/ : /ts/ ets “animalito extraño”
ets “hoja”
/ki/ : /K/ wa?ki- “morder”
wa?k “musgo de árbol”
/p)/ : // ap “diente remontado”
at “ropa”
IPI: /k/ ap “diente remontado”
a?k- “colgar”
/8/: /ts/ vit “barro”
tsits “carne”
/8/ : /K/ waht'- “cansarse”
wa k- “morder”
Oclusivos palatalizados aspirados
/p*/:/p/  tupPik “se voltea”
tápiik “se desnuda”
/6/ : /6/ ip. “seleccionar, escoger”
vit “barro”
/ts?/: /ts/ — ts"agi “quemado”
tsaf “venado”
SEL k"a “col”
kia “ese, aquel”
/8/ : /5/ mit” “olla”
mis “gato”
tst/:/S/ — tstatb pueblo"
sab “ombligo”
Oclusivos prenasalizados
7 : 1p/ "buta “grano en la piel”
puta “olor”

<!-- page 11 (screenshot 0011) -->
Las palabras que tienen los fonemas velares palatalizados se pronuncian
en las regiones del norte del territorio con los alveolares correspondientes.
Se observa que en las regiones en las que se reporta la existencia de esos fo-
nemas hay alternancia en el uso. Por ejemplo, los pronombres de primera y
segunda persona del singular para el género masculino son respectivamente
la"di/ — /a?g/ y /"d/ — Pg.
Ilustración de oposiciones"
Todos los fonemas de una lengua se encuentran en oposición con todos
los demás fonemas en tanto se trata de unidades distintivas. A continua-
ción se ilustran algunas oposiciones de los fonemas consonánticos; no se
presentan de manera exhaustiva todas las oposiciones existentes, que son
muchas, sino que se escogen las que tengan interés en función del parecido
fónico de las unidades involucradas. Se ilustran con pares de palabras en
las que hagan contraste las unidades, que es lo que se conoce como pares
mínimos.
Oclusivos básicos
pl: /t/ ape” “auyama”
[e El . »
ate limpio
lp! : NJ pus “fermentado”
kus “noche”
/t/ : /K/ tas “planta, árbol”
kas “tejido ralo”
/t/ : /ts/ tut “puño”
tsut “choclo”
Oclusivos aspirados
/p*/ : /p/ pra"d- “abrir”
pa"d- “barrer”
/8/:/t/ tuw “erizo”
tuw “corto”
he: hal waa! “está jecho”
? CC »”»
watsa es (la) roza
5 En la escritura de los fonemas y las palabras se sigue el Alfabeto Fonético Internacional (AFI)
'* Las palabras están escritas en representación fonológica

<!-- page 12 (screenshot 0012) -->
Pa: /t/ tu"d “rápido”
tut “puño”
Pdz/:/ts/  erdz “dos”
e?ts “colibr?”
Pgl : /k/ Ru"g “cartílago”
RO "R “llegó”
Pb: di tu"b “paloma”
tu"d “rápido”
Pd: dd “dk “durmió”
"dzek “flo”
"d/:/g/ — pe""d- “nadar”
tpe""g- “doblar”
Oclusivos prenasalizados palatalizados
Fo: b/ had “arisco”
ha"b “era (de sembrado)”
M"d/:d/ tada “es redondo”
ta"da" “es cucarrón"
l'dz/: "dz/ tsi"d7 “llorón”
tsi"dz “espalda”
Pgl:Pgl  tug- “beber”
Ru"g “cartílago”
VD dr eb “chorreado”
ted “mezquino”
Md/:/"d7/ we"d- “querer”
we"dz)- “halar”
Fricativos
/s/ : /h/ swe""de- “traspasar, hacer hueco”
hwe"de “hilera de cosas colgadas”
/s/ : /ts/ pusutsa' “se está fermentando”
pu:tsutsa” — “está dando de comer”
/s)/ :s/ es “coca”
Es “piojo”
/s/ : 1ts/ sal “árbol sp”
ts'al “grueso (objetos cilíndricos flexibles)"
(st: 1 mis “gato”
mit” “olla”
/hi/: /h/ hiuka “todo”
huna “bravo”

<!-- page 13 (screenshot 0013) -->
FONOLOGÍA
MiV: /s/ huth “hierba”
ute “gracias”
/h/ : /d/ ehia" "es rama"
epa “es derrumbe”
/0/ : 1p/ ad “guama”
ap “diente remontado”
/b/ : /8/ Dits “curi”
Bits “cerro, punta”
/8/:1"b/ Bite “otro”
"bite “pintado, de colores”
Nasales
/m/ : /n/ mem “canto, canción”
men “hijo último”
(nf : /n/ na “este, esta, esto”
na “yuca”
(m/:m/ ma “cuál?”
na “Yuca”
/1i/ : /j/ n'aha- “chuzar”
ja'ha “mochila”
/m/:b/ mea “vayamos”
"be"ka “como que es rojo”
Laterales
/1/: /V/ ul “culebra”
ul “gusano”
/V/ : /j/ wel “loro”
wej- “comprar”
Aproximantes
/w/ : /j/ Piwa' “es semilla”
Pija' “es diferente”
/w/ : /"b/ tuw “corto, cerca”
tu”b “paloma”
/w/ :/6/ "baw- “echar un líquido”
"baf- “escupir”
/j/ : Mhi/ juk “nalga”
hu “largo”
hi: Md! vj “mujer”
u?"d “seco”

<!-- page 14 (screenshot 0014) -->
i Pdd/ Poa "es diferente"
Qi"dza" “es codo”

il: 18/ Pij “diferente”

git “abierto”

Reglas de realización
Los fonemas son unidades abstractas que se realizan en el decurso fónico

por medio de los fonos o sonidos. Esas maneras de materializarse fonética-

mente son las que se recogen en las llamadas reglas de realización. Las diferen-
tes realizaciones fonéticas de un fonema reciben el nombre de alófonos. A con-
tinuación se presentan las reglas de realización que son generales al sistema”.

* Los fonemas oclusivos /p/, /t/ y /k/ se realizan aspirados en final absoluto
y no aspirados en los demás contextos.

/p/ > [p"]/-* — Ejemplo: /lap/ — [lap"] “falda corta”
[p]/d.c. /puta/ — [puta] “olor”
/ape/ — [ape] “auyama”
it — te (tut/ —/— [tut] “puño”
[t]/d.c. /tape/ — [tape] “ancho”
/ate/ — [ate] “limpio”
/k/ — [K]/-* juk/ —[[ul] “nalga”
[k]/d.c. /kus/ — [kus] “noche
/ka'ka/ — [ka?ka] “papa”

e El fonema /ts/ tiene tres alófonos: uno africado alveolar sordo [ts], uno
africado laminal sordo [ts ] y uno fricativo alveolar sordo [s]. Los dos
primeros alternan en final de palabra; el primero y el tercero están en al-
ternancia cuando preceden a una consonante oclusiva o se encuentra en
grupo consonántico de inicio de sílaba; en los demás contextos aparece el
alófono africado alveolar.

/ts/— [ts] — [ts ]/-* Ejemplo: /kuts/ — [kuts] - uts, J “ceniza”
[ts] — [s]/-Cocl. — /pitstaki/ — [pitstak'] — (pista) “hombre joven"
[ts]/d.c. /ptsu-/ — [ptsu-] — [psu-] “acabar”
/tsut/  — [tsut"] “choclo”
/patsu/ — [patsu] “lado derecho”

7 Sobre las particularidades regionales, pueden consultarse los estudios mencionados sobre Mun-
chique (Rojas, 1991a), Toribío (Yule, 1991b), Tierradentro (Jung, 2000, 2008), Caldono (Nieves,
1991b), Paniquitá (Nieves, 1991c) y Novirao (Rojas, Perdomo y Corrales, 2011), así como el estu-
dio de fonología comparada de Nieves (19914).

<!-- page 15 (screenshot 0015) -->
FONOLOGÍA
e Los fonemas /p/, /t/, /ts/ y /k/ se realizan oclusivos palatalizados sordos
en todos los contextos.
/p)/ — (pl Ejemplo:/pan/ — [p'a"n] “mitad”
/psu-/ — [psu-] “maltratar”
/lepla'/ — [lepia?] “es grueso”
fipi/ — [ip] “fuego”
/t/ — [t] Ejemplo: /tit/ — [vit] “barro”
/uta/ — [uta] “cerca”
/ts/ — [tf] Ejemplo: /tsits/ — [tfitf] “carne”
/tsá*tsa/ — [tfá?tfa] “carbón”
/k/ — [k] — Ejemplo: /Rà/ — [Wa] “ese, aquel”
/e?ka”/ — [e?ka?] “es leña”
/me?ki/ — [me?k] “hígado”
e Los fonemas /p”/, /t?/, /ts"/ y /k"/ se realizan oclusivos aspirados en todos
los contextos.
/p"/ — [p"] Ejemplo: /p*ats/ — [p"atf] “luciérnaga”
/kusep"ap"/ — [kusep"ap"] “palma de la mano”
/up"/  — [up] “cerco”
/'/ > [t*] Ejemplo: /Cut?/ — (Putt) “grueso (objeto laminar)”
/pet'e/ — [pete] “calabaza”
/ts"/ — [ts] Ejemplo: /ts"its"/ — [ts'its"] “paja”
/wats"a?/ > [wats"a?] “está jecho”
NÈ/ — [K*] Ejemplo: /kK'as/ — [k"as] “lana”
/akus/ — [ak"us] “ajo”
fik"/ — IM) “laguna”
* Los fonemas /p”"/, /t"/, /ts"/ y /kP/ se realizan oclusivos palatalizados as-
pirados en todos los contextos.
/p/ > [p"] Ejemplo: /p"ip”/ — [p*ip*] “tieso”
/tupPik/ — [tp"ik"] “se volteó”
/túp*/ — [túp*] “desnudo”
(dt — [] Ejemplo: //*ik/  — [Mk] “cuello”
(dit — it) (é) escoge”
/tsat?-/ — [tfar*-] “empujar”
/ts/ — [tf] Ejemplo: /ts"aB/ — [taB] “quemado”
Itsats"a/ — [tatf*a] “fuerte”
NE — [K*] Ejemplo: /k"a/ — [ka] “col”
'* El nombre regional para la calabaza en castellano es «mejicano».

<!-- page 16 (screenshot 0016) -->
/elPa?/ — [ekPa?] “es leña”
/sku:uld"/ — [skuuk"] “trigo”
e Los fonemas oclusivos prenasalizados tienen los siguientes alófonos:
o con prenasalización débil y segmento oclusivo sonoro, en posición
inicial"
/b/ — [*b]/é- Ejemplo: /"beh/ — ["beh] “rojo”
Md/ — ["d]/*- f'duh/ — ["duh] “pesado”
"dz/ — ["dz]/t- dzek/ — ["dzek"] “filo”
o con prenasalización fuerte y segmento oclusivo sonoro, en posición
intervocálica
/”b/ — [mb]/V-V Ejemplo: /hi"ba/ — [himba] “caballo”
"dl — [nd]/V-V /ta“da/ — [ta?nda] “cucarrón”
l'dz/ — [ndz]/V-V /tsu"dza”/ — [tsundza?] “es rana”
Pg/ — [ng]/V-V /ne"ga/ — [nenga] “sal”
o con prenasalización fuerte y segmento oclusivo sordo (tres de ellos
aspirados, según la regla anterior), en posición final
/”b/ — [mph]/-* Ejemplo: /tu”b/ — [tump"] “paloma”
Pd/ — [nth]/-+ /tu"d/ — [tunt"] “rápido”
Mdz/ — [nts]/-4 /tsi"dz/ — [tsints] “espalda”
Pg/ — Iykh]/-4 /ku"g/ — [kunk*] “cartílago”
El fonema /"dz/ a veces pierde la parte oclusiva y se realiza ["z] en inicio,
[nz] en posición intervocàlica y [ns] en posición final.
Mdz/ > ["dz] — ["z]/*- Ejemplo: /*dzek/ — ["dzek"] - ["sek"] “filo”
Índzl - [nz]/V-V /u"dza/ — [undza] — [unza] “rata”
[nts] — [ns]/-f /pte"dz/ — [ptents] — [ptens] “angosto”
e Los fonemas /"b/, /"d//, /"dz/ y /"gi/ tienen alófonos semejantes a los fo-
nemas prenasalizados, pero se realizan palatalizados. En posición final,
alternan los fonos sonoros con los sordos de la parte oclusiva.
("be — [mb]]/V-V. Ejemplo: /a"bku/ — [amblku] "hirvió"
[mb] - [mp)]/-+ (ha"bi/ — [hambi] - (hampil “arisco”
"d/ — ["d] /*- Ejemplo: /"dii?/ — [ndi?] “camino”
P. El fonema /"g/ no se da en posición inicial.
* Hasta ahora no se ha encontrado este fonema en inicio de palabra.

<!-- page 17 (screenshot 0017) -->
FONOLOGÍA

[nd]/V-V /wedik/ — [wendik*] “quiere”

[nd] - [nt]/-+ lta"d)/ — [tand] — [tant] “redondo”
"d7/ — ["d3]/é- Ejemplo: /"dZits/  l'dzits) “huevo”

[nd3]/V-V (di "dza/ > [Pindza] “codo”

[ndz] — [ntf]/-+ /pe"dz)/ — [pendz] - [pentf] “vieja”
Pr — [ng)]/V-V Ejemplo: /tungik/ — [tunglik"] “bebe”

[ng] - [nk]/-+ la"gi/ — [ang] - [ank] “yo (masculino)

* Los fonemas /s/ y /h/ se realizan respectivamente fricativo alveolar sordo
y fricativo glotal sordo. El fricativo alveolar a veces en posición final se
realiza laminal [s ].

(sí — [s] - [s,]/-4 — Ejemplo: /us/ — [us] - [us ] “frijol”
[s]/d.c. /sek/ — [sek"] “sol”
/psu/ — [psu] “sombra (de una entidad)”
/kuse/ — [kuse] “mano”
/me'skwe/ — [me?skwe] “cilantro”
/h/ — [h] Ejemplo: /huna/ — [huna] “bravo”
/tsahu/ — [tfahu] “piña”
e Los fonemas /s/ y /hi/ se realizan respectivamente como fricativo postal-
veolar sordo (I y fricativo palatal sordo [c].
/s/ — (I Ejemplo: /sita/ — [fita] “armadillo”
/spi:pi/ — [fpiipi] “pavo, bimbo”
/nusa/ — [pufa] “caña dulce”
/Kas/ — [kaf] “sopa, mazamorra”
/hi/ — [c] Ejemplo: /huka/ — [cuka] “todo”
/webla/ — [weca] “viento”

e Los fonemas /Òi/ y /P)/ se realizan respectivamente fricativo bilabial sordo
palatalizado [d] y fricativo bilabial sonoro palatalizado [Bj] en todos los
contextos.

IQ — [$] Ejemplo: /dits/ — [fits] “cur?”
ladia'/ > [ada?] “es guama"
/tú/ — [Htú] “palo”
/fnes/ — [neg] “saliva”
jadi/ — [jad/ “ojo”

(B/ — [$] Ejemplo: /Blite/ — [Bite] “otro”

** No se ha encontrado este fonema en posición inicial.

<!-- page 18 (screenshot 0018) -->
(Bi U/ — [BA] “uña”
NcuBia"/ — (RuBia2) “es flauta”
/tsaBi/ — [tfaB)] “venado”
e Los fonemas /m/, /n/ y /1/ se realizan respectivamente nasal bilabial [m],
nasal alveolar [n] y nasal palatal [n] en todos los contextos.
/m/ — [m] Ejemplo: /mem/ — [mem] “canción”
/ime/ — [ime] “excremento”
/n/ — [n] Ejemplo: /nus/ — [nus] “luvia”
/knene/ — [knene] “frente”
/me:n/ — [meen] “por favor"
nl — [n] Ejemplo: /n'a/ — [na] “yuca”
(niania/ — [nana] “desdentado”
/vwin/ — [nin] “pepa”
e Los fonemas /1/ y /l/ se realizan respectivamente lateral alveolar sonoro
[1] y lateral palatal sonoro [A] en todos los contextos.
/1/ — [1] Ejemplo: /lem/ — [lem] “amarillo”
/kla/ — [kla] “vaca”
/alku/ — [alku] “perro”
Ne'le/ — [le?le] “podrido”
/tul/ — [tul] “huerta, sembrado”
/V/ — [A] Ejemplo: /Vima/ — (A4imal “naranja”
(Bi U/ — [BA] “uña”
/spula/ — [spuña] “cebolla”
/atal/ — [ata] “gallina”
* El fonema aproximante labiovelar sonoro /w/ tiene varias realizaciones
alofónicas:

o fricativo bilabial sonoro (BJ delante de las vocales /i/, /u/

o aproximante labiovelar sonoro [w] en alternancia con fricativo bila-
bial sonoro (BJ en final de palabra, después de vocal /u/, y delante de
vocal /a/

o aproximante labiovelar sonoro [w] en los demás contextos

/w/ — [PB]/-i, -u, Ejemplo: /wuwuk/ — [BuBuk"] “(él) corre”
/witku/ — [Bitko] “(él) hizo”
[w] — [B]/u-* Ejemplo: /tuw/ — [tuw] — [tuB] “corto”
[w]/d.c. Ejemplo: /wa"wa/ — [wa"wa] “suave”
/we?/ — [we?] “puente, escalera”
/kwet/ — [kwet"] “piedra”

<!-- page 19 (screenshot 0019) -->
FONOLOGÍA
/kiwe/ — [kiwe] “tierra”
/taw/ — [taw] “chumbe”
/ew/ — [ew] “bueno, bien"
e El fonema aproximante palatal sonoro /j/ tiene los siguientes alófonos:

o aproximante palatal sonoro [j] en variación libre con oclusivo palatal

sonoro [17] o con fricativo palatal sonoro []], en posición inicial.

o aproximante palatal sonoro (jl en variación libre con fricativo palatal

sonoro []], en posición intervocàlica.

o aproximante palatal sonoro en los demás contextos.

ir > [] - IN - []/*- — Ejemplo: /jat/ — Bat") - [Fat"] — at) “casa”
G] - []]/V-V /pijak/ — [pijak*] — [pijak"] “(él) aprende”
[j]/d.c. /tsjun/ — [tsjun] “mora”
/njak"/ — [njak"] “hermano (de otro)”
fjadju'/ > [jadju?] “lágrima”
/ajte/ — [ajte] “aqu?”
/kuskaj/ — [kuskaj] “mañana”

A veces, cuando el aproximante palatal sonoro /j/ se encuentra junto a
vocal nasal, se realiza nasal palatal sonoro [n]; en estos casos, la vocal puede
perder su carácter nasal y realizarse oral.

/i/ > Dl - [n]/V Ejemplo: /pewját”/ — [pewját*] - [pewnat"] “ya me bañe”

Se da un caso de neutralización. Se entiende por neutralización la situa-
ción que se presenta cuando una oposición fonológica pierde pertinencia en
un determinado contexto. Al realizarse aspirados los fonemas oclusivos en
posición final, se neutraliza en dicho contexto la oposición que existe entre
los oclusivos básicos y los oclusivos aspirados.

Ejemplo:

/tut/ > [tut”] “puño”

/Rutt/ > [ut] grueso (objetos laminares flexibles)”
/juk/ — [juk"] “nalga”

/jak"/ — [jak"] “hermano del mismo sexo”

No se han encontrado casos de palabras que resulten homófonas como
producto de esta neutralización. Es claro que la aspiración, cuando no es fo-
nológica, se da solamente al final de la secuencia; no se presenta si la palabra
está dentro de la cadena. Ejemplo: /tuta'/ — [tuta?] “es puño”.

* Especie de cinturón tejido en telar

<!-- page 20 (screenshot 0020) -->
Las razones para interpretar como unidades fonológicas y no como gru-
pos consonánticos los complejos articulatorios oclusivo aspirado, oclusivo
palatalizado, oclusivo prenasalizado, oclusivo palatalizado-aspirado y oclu-
sivo prenasalizado-palatalizado son las siguientes:

1) No se reparten en dos sílabas al ser pronunciados.

2) Aparecen en una posición en la cual la lengua no acepta grupos con-
sonánticos: la margen posnuclear de la sílaba; es decir, conmutan con
fonemas consonánticos sencillos.

3) Presentan una distribución similar a la de sus correlatos básicos.

4) El sistema así constituido presenta una simetría indiscutible.

Las dos primeras razones valen también para la consideración como uni-

dad fonológica de /ts/ y todos sus correlatos en el sistema.

Por las siguientes razones se ha considerado que los aproximantes /w/ y

/j/ son fonemas consonánticos:

1) Se sitúan en las márgenes prenuclear o posnuclear de la sílaba, es decir
que no son núcleos de sílaba.

2) Conmutan con fonemas consonánticos.

3) Tienen alófonos fonéticamente consonánticos.

4) Cuando están al final de una base que recibe un morfema gramatical,
el alomorfo que aparece es el que va normalmente después de fonemas
consonánticos y no el que aparece después de fonemas vocálicos.

FONEMAS VOCÁLICOS
El sistema de fonemas vocálicos del nasa yuwe se estructura a partir de cua-
tro timbres básicos sobre los cuales juegan oposiciones de rasgos. Hay una
oposición de dos términos: oral / nasal, y una oposición de cuatro términos:
breve / larga / interrupta / aspirada. Los cuatro timbres básicos se organizan
en dos posiciones y dos grados de abertura:
Tabla 2. Timbres vocálicos
Anterior Posterior
Alta i u
No alta e a
Los rasgos de las dos oposiciones se dan en una misma vocal, los rasgos
de cada oposición se excluyen mutuamente. Así, hay vocales orales breves,
orales largas, orales interruptas, orales aspiradas, nasales breves, nasales lar-
gas, nasales interruptas y nasales aspiradas.

<!-- page 21 (screenshot 0021) -->
FONOLOGÍA
Tabla 3. Fonemas vocálicos
Oral Nasal
Breve ieau 1eaú
Larga i:e:a:Uu: 1: é: à: Ú:
Interrupta Peru rezo
Aspirada eat reso
; =
Hay que anotar que en las regiones del norte del territorio, como Mun
chique y Toribio, no se dan las vocales largas fonológicas, lo que hace que en
esas regiones existan 24 y no 32 fonemas vocálicos.
Ilustración de oposiciones
Se presentan a continuación pares de palabras que permiten establecer con-
traste entre las distintas unidades, para mostrar la oposición entre ellas. Se
ilustran las oposiciones que presentan mayor interés en relación con la ma-
nera como está estructurado el sistema.
Orales (diferentes timbres)
/i/ : /e/ pil “canilla”
pel “carrizo”
lil:/al id “tú (masculino)
a"d “yo (masculino)
/i/:/u/ tsi"dz “espalda”
tsu"dz “rana”
/e/ :/a/ ed “colmillo”
ap — “guama”
del : 1) tel “trapiche, telar”
tul “huerta, sembrado”
/a/:/u/ ap" — “tapa, cierre”
up" — “cerco”
Orales : nasales
/i/:/i/ kits “quebrada, zanjón”
kits- — “agacharse”
/e/ :/€/ eb “colmillo”
ed “derrumbe”
/a/:/á/ Kas “sopa, mazamorra”
kas “saltamontes”
fil: fal tf its “paja”
ts"ats" “espina”

<!-- page 22 (screenshot 0022) -->
Breve : larga
Ri ke  “maní
kit” “depara abajo”
fel : /e:/ penal “abunda”
pe:nak “repite”
far: tal ap” — “mosca”
ap" “salto”
(él: /0:/ és “piojo”
ú:s “corazón”
fu/:/u:/ huk" “nudo”
hu:k (El) trae”
/E/:/€:/ pets. — “cuello”
pe:ts- “tumbar”
/0/: /0:/ ot “batata”
ut” me muero”
Interrupta : breve (no interrupta)
117 :1i/ kt — “diente”
kit" “mané
/e'/:1e/ wet “tieso”
wel “loro”
faif: tal ate — una"
ate “limpio”
fu"/: /0/ u'kwe “yo (femenino)”
ukwe “plano”
i kh “Visión”
ikh “laguna”
Aspirada : breve (no aspirada)
//:/i/ BS. “cazar”
Bit “puerta”
le! :/0/ tk “limpio”
sek “sol”
lab: /à/ wa'wa “suave”
wáwá “abejón”
u/:/u/ ju"t* “vo vengo”
jut- — “atizar la candela”
Larga / interrupta
li:/ : /i7/ "di:te “dentro”
"dite “enel camino”

<!-- page 23 (screenshot 0023) -->
FONOLOGÍA
/e:/ :/e'/ we: — “enfermedad, peste”
ve — “puente, escalera”
fail :/a'/ ja:ha? “picante”
ja?ha “jigra, mochila”
/u:/: 47 u:k “se murió”
uk “sefuo
107: 1007: Ú:s “corazón”
-? « P
a's arracacha
Larga : aspirada
dl: 7 kis- “alzar”
ki" “qué?”
h 21 »
e) : 10 e sangre
el “roza”
/a:/ : /a"/ "daki “indígena del Sibundoy”
tal “animal”
hs i E
ful i 1 e “piña”
i CC .
su tenga, tome, reciba”
Interrupta : aspirada
RI: ko “otra vez”
ki" cc, ué?”
¿quer
le! :1e1 dz "dos"
e"dz “verano”
/E/ :1e"/ tsé'k “robo
tsek — “limpio”
a Nat “estrella”
a “humo”
14: fu un “se fue"
uk “sembró”
Reglas de realización
Se presentan a continuación las reglas de realización de los fonemas vocáli-
cos. Se recogen los procesos que son generales al sistema o que se presentan
en varias regiones. Para información sobre las particularidades regionales,
se pueden consultar los estudios específicos.
* En Caldono es frecuente que se usen las raíces verbales sin marca alguna para expresar el impe-
rativo.

<!-- page 24 (screenshot 0024) -->
Orales breves
e El fonema /i/ se realiza anterior cerrado no redondeado en todos los
contextos.
/i/ — fi) Ejemplo: /ime/ — [ime] “excremento”
/kiwe/ — [kiwe] “tierra”
/bite/ — ["bite] “pintado, de colores”
/kutsi/ — [kutfi] “cerdo”

e El fonema /e/ tiene dos alófonos: anterior semiabierto no redondeado
(el en alternancia con anterior medio no redondeado [e]* en sílaba
acentuada y anterior medio no redondeado [e] en los demás contextos.

/e/ > [e] - [e]/síl. acent. Ejemplo: /P'une/ — [une] - [une] lengua”
letse'/ — [etse?] - [etse?] “hace frío”
[e]/d.c. /ets/ — [ets] “hoja”
/mem/ — [mem] “canción, canto”
/kite/ — [Kite] “flor”
e El fonema /a/ se realiza abierto central en todos los contextos”.
(al — [a] Ejemplo: /ape/ — [ape] “auyama”
/wala/ — [wala] “grande, mucho”
/atsja/ — [atfa] “caliente”
e El fonema /u/ tiene dos alófonos en variación libre: uno cerrado pos-
terior redondeado [u] y uno semicerrado posterior redondeado [o].
/u/ — [u] — [o] Ejemplo: /us/ — [us] — [os] “fríjol”
/kus/ > [kus] — [kos] “noche”
/alku/ > [alku] — [alko] “perro”

e Los fonemas vocálicos nasales: /1/, /é/ y /à/ se realizan respectivamente
cerrado anterior no redondeado nasal [1], medio anterior no redon-
deado nasal [€] y abierto central nasal [á] en todos los contextos.

/1/ — (i) Ejemplo: /ik"/ > [ik*] laguna”
/Pis/ — [Hif] “Mosco”
/€/ — le] Ejemplo: /ésekwe/ — [Esekwe] “liviano”
/péts/ — [pétf] “cuello”
” Se toma el símbolo fonético correspondiente al sonido vocálico anterior semicerrado no
redondeado ante la inexistencia en el AFI de un símbolo para el sonido de abertura media.
> En la región de Caldono, este fonema tiene un alófono casi-abierto (82), que aparece delante de [/].
Ejemplo: /btútas/ — [$tútees] “árbol”.

<!-- page 25 (screenshot 0025) -->
FONOLOGÍA
/a*tewe/ — [a?tewe] “luz de luna”
/ a/ — fal Ejemplo: /àvvà/ — [áwa] “aj?”
/kK"as/ — (Mal) “saltamontes”

e El fonema vocálico nasal /ú/ se realiza cerrado posterior redondeado
nasal [ú]. A veces, alterna con realizaciones de la respectiva vocal oral
seguida de un segmento nasal débil [u"], cuando está delante de con-
sonante oclusiva.

/0/ — [ú] - [u"]/-Cocl.
Ejemplo: /é'tútas/ — [tata] — [Ptu"taf] “árbol”
[ú]/d.c. Ejemplo: /ttúwa/ — ["úwa] “oreja”
/sús/ — [fas] “estregado”

* Los fonemas vocálicos /i:/, /e:/, /a:/ y /u:/ se realizan respectivamente
cerrado anterior no redondeado alargado [ii], medio anterior no redon-
deado alargado [ee], abierto central alargado [aa] y cerrado posterior
redondeado alargado [uu]. A veces en el habla rápida se realizan breves,
pero en el habla cuidadosa siempre se da el alargamiento. Ese alarga-
miento puede ser de dos segmentos [V:]* o de segmento y medio [V-].

/i:/ — fiil Ejemplo: "di:te/ > ["diite] “dentro”
/vi:s/ — [niif] “gordo”
/e:/ > [ee] Ejemplo: /e:n/ — [een] “día”
/we:/ — [wee] “enfermedad”
/a:/ > [aa] Ejemplo: /tsa:m/ — [tsaam] “hierro”
/da:ki/ — ["daaki] “indígena del Sibundoy”
fu:/ > [uu] Ejemplo: /u:k/ > [uuk*] “se murió”
/pu:tsuk/ — [puutsuk*] “da de comer”

e Los fonemas vocálicos /i/, /a'/ y /u"/ se realizan respectivamente ce-
rrado anterior no redondeado interrupto [i?], abierto central inte-
rrupto [a?] y cerrado posterior redondeado interrupto, en todos los
contextos.

/i/ — [i?] Ejemplo: /i'kwe/ > [i?kwe] “tú (femenino)”
Mdzii's/ > ["d3i?f] “hermano de mujer”
Pdi'/ — Edi?] “camino”
/a'/ — [a?] Ejemplo: /a'te/ — [a?te] “luna”
/ja*ha/ — [ja?ha] “mochila”
/ewa'/ — [ewa?] “está bien, está bueno”
** V representa una vocal.

<!-- page 26 (screenshot 0026) -->
/u% — [u?] Ejemplo: /u'kwe/ — [u?kwe] “yo (femenino)”
/su's/ — [su?s] “orina”
/ju'/ — [ju?] “agua”

e El fonema /e'/ tiene dos alófonos: uno medio anterior no redondeado
interrupto [e?] en variación libre con uno semiabierto anterior no re-
dondeado interrupto (22).

/e'/ — [e?] - [£?] Ejemplo: /e'ts/ — [e?ts] — [£?ts] “colibr?”
Ne'le/ — [le?le] — [le?le] “podrido”
/we'/ — [we?] - [we?] “puente, escalera”

e Los fonemas /i"/, /a"/ y /u"/ se realizan respectivamente cerrado ante-
rior no redondeado aspirado [i"], abierto central aspirado [a"] y cerra-
do posterior redondeado aspirado (ut.

ft — [1] Ejemplo: /i"/ > [1] junto”
/tsi"me/ — [tf?me] “blanco”
/ki"/ — (it) “¿qué?”
Jal] — [a] Ejemplo: /a"/ — [a"] “humo”
/wa'wa/ — [wa"wa] “suave”
/ba"ts/ — ["ba"ts] fique”
fu > [Wu] Ejemplo: /u"/ > qu") “águila”
(tutme/ > [tu'me] gris"
/jug/ > [jug] “vienes”
Pdut/ > [du] “pesado”
e El fonema /e'/ tiene dos alófonos en variación libre: medio anterior no
redondeado aspirado [e"] y semiabierto anterior no redondeado [£"].
/e"/ — fet) - [e] Ejemplo: /e*/ > [e] - [£"] “huerta, cultivo”
/kwe"ne/— [kwe"ne] - [kwe"ne] “relámpago”
/nme"/ > [nme"] - [ame] “último”

* Los fonemas vocálicos /1:/, /€:/, /à:/ y /ú:/ se realizan respectivamente
cerrado anterior no redondeado nasal alargado [1:], medio anterior no
redondeado nasal alargado [é:] abierto central nasal alargado [4á:] y
cerrado posterior redondeado nasal alargado [ú:].

Y) — hal Ejemplo: /bji:k/ — IQ) “se marchitó"
/€:/ — [ee] Ejemplo: /é:kat"é?/ — [eékat"e?] “trueno”
/4:/ — [ãã] Ejemplo: /à:te/ — [ááte] “visible”
/ú:/ > [44] Ejemplo: /ú:s/ — [úús] “corazón”
(sú:/ — [faú] “orejuela (planta sp.”

<!-- page 27 (screenshot 0027) -->
3) Cuando las raíces léxicas o las bases que reciben sufijos terminan en
una vocal acompañada de aspiración o de cierre glotal, reciben los alo-
morfos que van normalmente después de vocal y no los que aparecen
después de consonante.

4) Un haz de correlaciones así planteado no es extraño al nasa yuwe. Se
ve que es un mecanismo normal en la lengua para construir su sistema
fonológico tanto en lo consonántico como en lo vocálico.

En fonología se habla de rendimiento funcional para referirse a la ca-
pacidad que tiene una oposición lingiística de producir pares de palabras
contrastantes. A veces se entiende como la frecuencia con la que los fonemas
intervienen en la formación de palabras. En nasa yuwe parece haber una
proporción inversa entre la complejidad articulatoria y el rendimiento fun-
cional: a mayor complejidad articulatoria, menor rendimiento funcional y
viceversa. Es decir, los fonemas de menor complejidad articulatoria son los
que más intervienen en la formación de palabras y, por consiguiente, tienen
más probabilidad de aparecer en pares mínimos.

LA SÍLABA
La sílaba, agrupación mínima de fonemas, estructura básica en la construc-
ción de la cadena hablada, es el marco en el cual se definen vocales y con-
sonantes como fonemas diferentes. La sílaba del nasa yuwe está constitui-
da por un núcleo —obligatorio— y unas márgenes —facultativas—. Así, lo
mínimo que debe haber para que exista la sílaba es el núcleo. El núcleo está
constituido por un fonema vocálico y las márgenes por fonemas consonán-
ticos, de tal manera que una vocal puede por sí sola formar una sílaba. Se
aceptan hasta dos consonantes en margen prenuclear y solo una consonante
en margen posnuclear.
Estructura silábica
La sílaba (S) consta de ataque (A), núcleo (N) y coda (C)”. Desde S se des-
prenden el ataque y la rima (R), y desde R se desprenden el núcleo y la coda.
El ataque está formado por consonantes que preceden el núcleo; a esta posi-
ción también se la llama margen prenuclear. La coda está formada por con-
sonantes que van después del núcleo; esta posición se llama también margen
posnuclear. Los tres elementos —ataque, núcleo y coda— se organizan de la
siguiente manera:
7 El nudo que une a núcleo y coda es la rima (R).

<!-- page 28 (screenshot 0028) -->
FONOLOGÍA

* Los fonemas /1?/, /á?/ y /ú?/ se realizan respectivamente cerrado an-
terior no redondeado nasal interrupto [1?], abierto central nasal inte-
rrupto [ã?] y cerrado posterior redondeado nasal interrupto [ú?].

/i*/ — [1?] Ejemplo: /P'k"/ — [1?kh] “visión”
/3/ — [á?] Ejemplo: /Sã'wa/ — [fá?wa] “lombriz”
/0”/ — (02) Ejemplo: /sú's/ — [[ú?/] “crespo”

e El fonema /è2/ tiene dos alófonos: uno medio anterior no redondeado
nasal interrupto [E?] en variación libre con uno semiabierto anterior
no redondeado nasal interrupto [E?].

(€2/ — (82) - [82] Ejemplo: /tsé'k/ — [tse?k"] — [ts£?k"] “robo”
/Ee?wala/ — [*e?wala] — [e?wala]
“médico tradicional”

e Los fonemas /1"/, /à"/, y /ú"/ se realizan respectivamente cerrado ante-
rior no redondeado nasal aspirado [1], abierto central nasal aspirado
(a y cerrado posterior redondeado nasal aspirado [0].

A) — [E] Ejemplo: /4"1/ — (tt) “caña brava"
fat — [a] Ejemplo: /á"/ — [à] “completo, suficiente”
107 — [à] Ejemplo: /sú*ut”/ — [sú*ut"] “pienso, creo”

e El fonema /é"/ tiene dos alófonos en variación libre: uno medio ante-
rior no redondeado nasal aspirado [é¿"] y uno semiabierto anterior no
redondeado nasal aspirado [E"].

/éh/ — [éh] - [Eh] — Ejemplo: /e*"d/ — [E"nd] - [End] “temblor”
/se'k/ — (see) - [s£*k] “bajó”
/we/ — [we] - [we*] “tabaco”

Se han considerado la oclusión glotal que produce la interrupción y la
aspiración como rasgos vocálicos y no como fonemas consonánticos inde-
pendientes de los vocálicos, por las siguientes razones:

1) Existe una correlación relacionada con la cantidad en el núcleo silábi-
co, la del alargamiento de la vocal, lo que da pie a formular que entren
en esa correlación de cantidad también la interrupción y la aspiración.

2) La sílaba acepta solamente un fonema consonántico en el margen
posnuclear. Si se consideraran consonantes estos dos rasgos, al apa-
recer antes de consonante en la misma sílaba habría que postular la
posibilidad de que haya dos consonantes en el margen posnuclear,
pero en este caso la consonante más cercana a la vocal podría ser
únicamente /?/ o /h/.

<!-- page 29 (screenshot 0029) -->
FONOLOGÍA
A N C
XX Xx Xx
Figura 1. Estructura silábica

En el ataque (A) pueden ir una o dos consonantes; en el núcleo (N) una
sola vocal y en la coda (C) una sola consonante.

La fórmula general de la sílaba es, entonces:

((C2) C1) V (C3)
de la cual se desprende la existencia de los siguientes tipos silàbicos:

V a" “humo”

a.te “limpio”
CV ju “agua”

ki.we “tierra”
VC us “frijol”

al.ku “perro”
CYC sus “sonido”

nal.tuk — “culebra coral”
CCY kla “vaca”

Ptú.tas — “árbol”
CCVC kwet “piedra”

Rpi's “trueno”

Merece una mención el hecho de que en Toribio la sílaba puede aceptar
dos consonantes en margen posnuclear, en palabras verbales flexionadas.
En las otras regiones, si el lexema verbal termina en consonante, aparece
como sufijo modopersonal un alomorfo formado por una sílaba del tipo
CV, y si el lexema termina en vocal, aparece un alomorfo formado por una
consonante. Ejemplo: /um-/ “tejer” um-t"u “yo tejí, um-ku “él o ella tejió", /
wete-/ “caer”, wete-t" “yo (me) caí”, wete-k “él o ella (se) cayó”. En Toribio, en
ambos casos la forma del morfema modopersonal es una consonante: um-t"
“vo tejí”, um-k “él o ella tejió", al igual que wete-t" “yo (me) caí”, wete-k “él o
ella (se) cayo”.

<!-- page 30 (screenshot 0030) -->
Distribución en la sílaba

Todos los fonemas vocálicos de la lengua pueden aparecer como núcleo,
tanto de sílaba abierta como de sílaba cerrada”. No hay vocales breves for-
mando núcleo de sílabas del tipo V —sin márgenes— en palabras monosilá-
bicas; las hay largas, interruptas y aspiradas. Ejemplo: e: “sangre”, ú' “comi-
da", u “águila”. No se presentan diptongos, es decir, no hay núcleos formados
por dos fonemas vocálicos. Los fonemas vocálicos interruptos y aspirados
tienden a tener el acento de la palabra.

En la posición de C1 pueden aparecer todos los fonemas consonánticos,
excepto /"g//. El fonema /"g/ no aparece en inicio de palabra ni en grupo
consonántico de inicio de sílaba —margen prenuclear—. En la posición de
C3 —margen posnuclear— pueden aparecer todos los fonemas consonán-
ticos.

Cuando hay grupo consonántico de margen prenuclear, como Cl —la
más cercana al núcleo— pueden aparecer los siguientes fonemas: /p/, /t/,
ts/, /K/, NÒ, /p'/, 1s/, MV, 1ts)/, SH, mt, af, MV, 18/, Iw/, /j/. Como C2 pueden
ir /p/, /t/, /ts/, /K/, /p)/, /s/, 1h/, /14)/, /s//, /m/, /1/. Esto se refiere al ámbito del
morfema léxico sin considerar la adición de prefijos formados por una sola
consonante, hecho que también se presenta en la lengua.

En estos grupos consonánticos nunca se encuentran dos fonemas de ar-
ticulación compleja; si aparece alguno, va acompañado de otro fonema de
articulación simple o básica. Si bien algunas consonantes palatalizadas pue-
den formar grupo consonántico, lo hacen con consonantes no palatalizadas.

Se ilustran a continuación los grupos consonánticos encontrados:

pt pte"dz “angosto”
pts ptsu- “acabar”
pk" pkak*- “reunir
pw pwe:sa"- — “jugar”
pts ptsa'ga + “escoba (planta sp.)
tp tpehb"g- “doblar”
tsm tsme'me “mariposa”
kp kpi's “trueno”
ks kse"ba “diez”
kl kla “vaca”
kl Elu"b “duende”
ks' ksiaw “espíritu”
** Se llama abierta cuando termina en vocal, es decir que no tiene margen posnuclear, y cerrada
cuando sí lo tiene, es decir que termina en consonante.

<!-- page 31 (screenshot 0031) -->
FONOLOGÍA

kw kwet “piedra”
pt pta “melancólico”
pk p'ki- “prestar”
ps p'su- “maltratar”
kt kite “all?”
kn kna'sa “jovencita”

ah cc »
sp spet - cortar
sk skuk “trigo”
sw swe"de- “traspasar”
sj sjun “mora”
hw hwe"dz “machete antiguo”
hj hja"- “terminar”
Pt pra “palo”
bn bnes “hollín”
sp spi:pi “pavo, bimbo”

. >
sh sha"d7- “tocar”
mt mte “¿dónde?”
h CC 1 . »”»

nm nme último
mh mhi- “trabajar”
nh nhi* “madre (de otra persona)”

Se ha encontrado una restricción en la distribución del rasgo de nasalidad
entre vocales y consonantes en el ámbito de la sílaba: nunca se encuentran
vocales fonológicamente nasales junto a consonantes prenasalizadas dentro
de la misma sílaba. Es decir que si la vocal nuclear es nasal, la consonante
que la acompañe como margen de la misma sílaba no será prenasalizada.
Sin embargo, se da a veces una asimilación del rasgo de la nasalidad, en tan-
to algunas consonantes, como las aproximantes, que fonológicamente son
orales, toman el rasgo de nasalidad de la vocal nasal que las siga. Ejemplo:
/we'/ — [we] - [we] “tabaco” y “/jús/ — [jús] — [nús] “triste”.

Se puede agregar información acerca de los grupos consonánticos que se
dan en préstamos del español. Cuando se trata de palabras trisilábicas, estas
se adaptan como bisilábicas y, al perderse una vocal, se forma un grupo con-
sonántico. Algunos ejemplos:

kp kpun “jabón”
km kmisa “camisa”
kn kneja “banano” (guineo)
sp spatu “zapato”
st stela “estera”

<!-- page 32 (screenshot 0032) -->
sn sn'ula “mujer blanca” (señora o española)

CC »

pl kapla cabra

tm Tmigu “Domingo” (nombre propio)

ks Kse “José” (nombre propio)

ml Mlia Maria" (nombre propio)

MORFOFONOLOGÍA

Se tratan en la morfofonología los procesos fonológicos que se producen
cuando se unen los morfemas para formar las palabras de la lengua.

e La mayoría de sufijos monosilábicos presentan dos alomorfos", cuya
aparición está condicionada por el entorno final de la base a la cual se
sufijan. Hay un alomorfo que aparece después de consonante y otro
que aparece después de vocal. Ejemplos:
> Morfemas modopersonales:

. . h CC 10
1 de primera persona del singular: um-t'u yo tejí
h CC 7
wete-t yo (me) caí
" de segunda persona del singular: um-gu “tú tejiste”
wete-"g "tú (te) caíste”
" de tercera persona del singular:  um-ku “el oellatejió”
wete-k “él o ella (se) cayó”
" de tercera persona del singular predicación estativa:
yat-a?  “escas”
kiwe-" — "es tierra"
> Morfema aspectual de durativo: um-na — “tejiendo”
wete-n cayendo”
> Morfema de caso locativo alativo: yat-na “ao hacia la casa”
ju'wala-n “a o hacia el río”

* Algunos prefijos monosilábicos formados por consonante y vocal, al
entrar en contacto con otros morfemas, pueden perder la vocal, siem-
pre y cuando se conserve la estructura silábica. Ejemplo:

(ka + pembe + ku) — /kape"bek/ “lo hizo llorar”
puede ser también: /k-pe"be-Kk/
” Como se verá en el capítulo de Morfología, alomorfos son las variaciones presentadas por los
morfemas —unidades abstractas— en su realización.

<!-- page 33 (screenshot 0033) -->
FONOLOGÍA
pero si se une a un verbo que empiece por grupo consonántico:
(ka + pwe:sa + ku) — /kapwe:sak/“lo hizo jugar”

y no * kpwe:sak

O se intercala la vocal dentro entre las consonantes del grupo. Ejemplo:
(ka + mhi + vé + ku + tu) — /kmahiwékut"/ “quise hacer trabajar”

* Según la estructura silábica, no se admite la presencia de dos fonemas
vocálicos juntos. Así, si al juntar dos morfemas en una palabra resul-
tan dos núcleos silábicos —vocálicos— juntos, puede suceder:

o Sila primera de las dos vocales es acentuada o interrupta —caso en
el que normalmente es acentuada—, entre las dos vocales aparece
la fricativa glotal sorda /h/ estableciendo el límite. Ejemplo:

(pwe:'sa + a + ku) — /pwe:sahak/ “el o ella juega”
(Qi ra lu) —/fihat/ — “escribo”

o Si se trata de dos vocales inacentuadas: a) Si son del mismo tim-
bre, se funden en una sola. b) Si no lo son, se elide una de las dos.
Ejemplo:

a) ('wete + e + tut > /wetet”/ “yo (me) caigo”
b) fkite + a”) — / kite”/ “la flor (tópico)

o En otros casos, aparece un refuerzo consonántico entre las dos vo-

cales, como sucede en los deícticos espaciales. Ejemplo:
(he + ay +te) — /khekhayte/” “allá abajo, cerca”

e Cuando un sufijo formado por una vocal va después de vocal inte-
rrupta, puede aparecer el fricativo glotal sordo entre las dos vocales.
Ejemplo:

fu +a — /juha”/ “es agua"
* Se repite la consonante inicial.

<!-- page 34 (screenshot 0034) -->
e Cuando un lexema verbal termina en consonante palatalizada, el mor-
fema de aspecto imperfectivo está formado por la vocal /i/. En este
caso, la consonante se despalataliza. Ejemplo:

(wa'k+i+ku) — /wakik/ “él o ella mordió”
flip +i+ts+a')  /ipitsa'/ “está haciendo fuego”

e Cuando el lexema verbal termina en fricativo glotal sordo /h/, si le
sigue un morfema que empiece con el aproximante palatal /j/, pueden
fusionarse, dando como resultado un fricativo glotal sordo palataliza-
do. Ejemplo:

(ku”h + já + tu) > /ku”biat*/ “ya baile”

e El rasgo de la nasalidad puede pasar de uno a otro morfema que se
encuentren en contacto. Ejemplo:

(0 +ja) — /úna'/ > “a comer?”

* Algunos lexemas verbales monosilábicos que empiezan por la vocal
/u/, la cambian por /e/ cuando tienen prefijado el morfema de impe-
rativo (m-). Ejemplo:

fm +u) — /me'/ “¡siembre!”

im +0) —/m-€/ “¡coma!”

ORTOGRAFÍA NORMALIZADA

A continuación se presentan los grafemas o letras con las que se escribe la
lengua, cuya determinación fue el resultado de un proceso de unificación de
diferentes propuestas de escritura que coexistieron durante un tiempo. En la
actualidad, las diversas comunidades del pueblo nasa aceptan esta manera
de escribir su lengua y la usan en todos sus documentos. Con este sistema
ortográfico se alfabetiza a los niños en las escuelas.

Se presenta con base en el sistema fonológico. A la izquierda se sitúan los
fonemas y a la derecha, en disposición similar, las letras que los representan
ortográficamente.

* Fonéticamente: [G?na?].

<!-- page 35 (screenshot 0035) -->
en unas regiones y (-waj en otras, el morfema de primera persona mascu-
lino es (adx) en unas regiones y (agx) en otras, etc. El auxiliar posicional
es (us-) en unas regiones y (ús-) en otras. En todos los casos se respetará el
origen de la palabra o la oración que se dé como ejemplo.

N. B.: Como anexo se agrega a esta gramática un glosario de términos
correspondientes a conceptos de fonología y de fonética articulatoria usados
en este capítulo; el lector podrá consultarlo cuando le resulte necesario.

<!-- page 36 (screenshot 0036) -->
FONOLOGÍA
Consonantes
Tabla 4. Fonemas consonánticos básicos y grafemas correspondientes
Palato- Graf
Básicos Labial Apical Posterior a
alveolar (letras)
Oclusivos p t ts k P t c k
Ocl. Aspirados po t ts” ke | ph th ch kh
Oclusivos prenasalizados | "b "d "dz "g b d z g
Fricativos sordos S h | S j
Nasales m n m n
Laterales l | 1
Aproximantes VV j vv y
Tabla 5. Fonemas consonánticos palatalizados y grafemas correspondientes
A Palato- ,
Palatalizados Labial  Apical Posterior Grafemas (letras)
alveolar
Oclusivos básicos p t ts k px tx Xx kx
Oclusivos aspirados Pp” o ts" Ko pxh txh çxh kxh
Ocl. Prenasalizados "bj "di "dz "gi bx dx ZX gx
Fricativos sordos (0) si hi fx sx jx
Fricativo sonoro g VX
Nasal n nx
Lateral V lx
Vocales
Tabla 6. Fonemas vocálicos y grafemas correspondientes
| Oral Grafemas (letras) | Nasal Grafemas (letras)
Breve i é a u i e a u i e a ú i e a ú
Larga | i e a uu (ii ee aa uu | i €: à UÚ: | e àa úu
Incrrupta  E a w e a vw PP es a er r a
Aspirada | ea yw liheh ah uh | Pa à bn ãh õh
En los siguientes capítulos de esta gramática, los ejemplos se escribirán
con este sistema. Como hay variaciones regionales en relación con el uso de
uno u otro fonema o con el rasgo de nasalidad en las vocales, se representará
como se haya recogido el dato, es decir, en la forma correspondiente a la re-
gión de donde provenga dicho dato. Por ejemplo: el sufijo “aditivo” es (-pa)

# Capítulo 3 — Morfología
<!-- ocr -->

<!-- page 37 (screenshot 0037) -->
CAPÍTULO 3
MORFOLOGÍA
En este capítulo se presenta la información correspondiente al nivel mor-
fológico de la lengua. Se describen los morfemas, que son las unidades bá-
sicas del nivel morfológico. Se presentan los morfemas léxicos y gramati-
cales, y con ellos los procedimientos morfológicos —flexión, derivación y
composición— presentes en la lengua. De las distintas clases de morfemas
léxicos o lexemas se hace una caracterización tanto en términos formales
como en términos semánticos. Posteriormente se hace una caracterización
de la palabra y se presentan en términos generales las clases de palabras de
la lengua. Esta clasificación general se detallará en el capítulo siguiente, el
de Mortosintaxis.
EL MORFEMA

Se adopta para esta gramática la noción de morfema como equivalente de
segmento morfológico, es decir, la mínima unidad identificable y aislable en
el análisis morfológico, consistente en un significante que se pueda asociar
a un significado propio. En otras palabras, la mínima unidad portadora de
significado. El morfema, como unidad abstracta que es, se realiza o se mate-
rializa en morfos concretos.

Entre las distintas formas que pueden tener los morfos en los que se
materializan los morfemas, en nasa yuwe los encontramos formados por
un fonema o una cadena de fonemas, articulados en secuencia lineal; no
existen morfemas discontinuos ni por marcación suprasegmental. Tampo-
co se expresan significados mediante alternancia de elementos. Se usa la

<!-- page 38 (screenshot 0038) -->
duplicación para la expresión del aspecto iterativo y para la atenuación, en

el caso de algunos lexemas cualificativos; el aspecto imperfectivo se expresa

por medio de un fonema vocálico determinado léxicamente; el aoristo se
expresa con la ausencia de marca específica, es decir, con morfema cero.

Aunque en la lengua existen estas otras formas de realizarse los morfemas,

la gran mayoría de ellos tiene por significante conjuntos de fonemas articu-

lados en secuencia lineal.

Los morfemas se pueden clasificar según distintos criterios. Se pueden
considerar libres o ligados, en tanto puedan o no formar una palabra por sí
solos; raíces, si funcionan como núcleo o base para la formación de las pala-
bras, y afijos, si se agregan a las raíces.

La clasificación acaso más importante para la gramática de la lengua es
la que los divide en morfemas léxicos o lexemas y morfemas gramaticales
o gramemas. Esta clasificación se establece según dos criterios generales:
según el criterio distribucional, los primeros pertenecen a paradigmas ex-
tensos y abiertos, y los segundos, a paradigmas limitados y cerrados; según
el criterio semántico, los primeros expresan nociones correspondientes a
referentes que pueden ser ubicados en la realidad, mientras los segundos se
refieren a nociones abstractas que son el resultado de la categorización que
se hace de esa realidad en la lengua.

Los morfemas léxicos en nasa yuwe se dividen en cuatro grupos: nomi-
nales, verbonominales, cualificativos y verbales; los tres primeros pueden
aparecer solos, formando palabras, es decir, funcionan como morfemas li-
bres; los verbales van normalmente como morfemas ligados, es decir, acom-
pañados de otros morfemas, aunque en condiciones particulares pueden
funcionar como morfemas libres”. Todos estos morfemas léxicos funcionan
como raíces cuando intervienen en la formación de palabras, es decir, pue-
den ir acompañados por afijos flexivos o derivativos.

El grupo de los morfemas gramaticales está constituido por todos los
afijos flexivos y derivativos, morfemas ligados que se unen a una raíz léxica
o gramatical, y por morfemas libres tales como los deícticos (personales,
temporales y los demostrativos dentro de los espaciales), los interrogativos,
los conectores, los numerales y los cuantificadores.

La mayoría de los morfemas son monosilábicos o bisilábicos. A conti-
nuación, unos ejemplos:

* Con el procedimiento de la focalización, los morfemas flexivos se trasladan y puede quedar sola la
raíz verbal; en algunas regiones, por ejemplo en Caldono, se usa a veces la raíz verbal sin ninguna
marca morfológica con valor semántico de imperativo.

<!-- page 39 (screenshot 0039) -->
MORFOLOGÍA

Morfemas léxicos libres
Monosilàbicos

V a "estrella"

CV yu "agua"

VC ul “culebra”, ús "corazón"

CVC Rus “noche” sus “sonido”

CCV Rla "vaca"

CCVC kwet “piedra”, fxnesx “saliva”

Entre los monosilábicos, el esquema CVC es el más frecuente.
Bisilábicos

V.CV a.pe “auyama”

V.CVC a.talx “gallina”

CV.CV ka.ka "papa", ku.se “mano”

VC.CV —alku“perro”

CV.CVC kuh.txil "torcaza', la.wecx “lagarto”

CCVCV kne.ne frente”

CVC.CVC nxal.tuk “culebra coral”

CCVCVC klxi.khun “callejón”

CCV.CCV kwe.kwe “cuerpo”

Entre los bisilábicos, el esquema CV.CV es el más frecuente
Morfemas léxicos ligados
Monosilábicos

V Ú- comer"

CV deh- “dormir”

VC um- “tejer”

CVC pud- “hilar”

CCV mji- “trabajar”

CCVC ksxaw- “soñar”

Entre los monosilábicos, el esquema CVC es el más frecuente.
Bisilábicos

V.CV Úú.se- “respirar”

V.CVC a.sxisx- “echar granos en un recipiente”

V.CCVC  a.jwed- “azotar”

CV.CV pa.ka- “recibir”

CVCVC  sxawed- regresar”

CVCCV  pa.kwe- “buscar”

<!-- page 40 (screenshot 0040) -->
CVC.CV  kpa.te- “cambiar de piel una serpiente”, “perder una persona
un vicio, una mala costumbre”
CCV.CV pwee.sa- “jugar”
CCV.CVC sbe.txitx- “aletear un pajarito”
Trisilábicos
V.CV.CV a.ka.yu “nacer”
V.CV.CVC u.ka.wahkx- “empujar”
CVC.CV.CV vac.ki.pu- “arrear”
Morfemas gramaticales libres
Monosilábicos
CV na “este, esta, esto (deíctico espacial cercano)”, ma “ninguno/
ninguna”
VC agx o adx “yo (masculino)”
CVC kim “¿quién?”
CCV mte “¿dónde?”
CCVC kwesx “nosotros”
Bisilábicos
V.CV u.na “ayer”
V.CCV u.kwe “yo (femenino)”
CV.CV — vxite “otro jxu.ka “todos” na.pa “pero”
CV.CCV ma.kwe “¿cuánto?”
CCV.CV — kse.ba “diez”
CVC.CVC kus.kay “mañana”
Morfemas gramaticales ligados
V -a morfema predicativo de tercera persona del singular
C m- morfema de imperativo
-ç- morfema de aspecto
-kx- morfema deíctico espacial (punto preciso)
CV -te morfema de caso (locativo)
-sa morfema nominalizador
ka- morfema derivativo del verbo (factitivo)
VC ay- deíctico espacial
CCV -kwe morfema derivativo del nombre (diminutivo)
CVC -wesx morfema derivativo del nombre (colectivo)
CV.CV -pa Ra morfema de subordinación de predicados, indica causa

<!-- page 41 (screenshot 0041) -->
MORFOLOGÍA
La mayoría de afijos son monosilábicos, aunque hay algunos constituidos
por un solo fonema, que entran a formar sílaba con algún fonema de la base

a la cual se afijan. Los sufijos que suelen ir al final de la palabra tienen dos

alomorfos condicionados fonológicamente, dependiendo de si el último fo-

nema de la base a la cual se sufijan es vocálico o consonàntico". Algo similar
ocurre con algunos prefijos, según el fonema inicial de la base a la cual se
prefijan. Ejemplos:

yatna “a la casa, hacia la casa”

(yat-na)

//casa-ALA//

yu walan “al río, hacia el río”

(yu -wala-na)

//agua-grande-ALA//

yawakxtha “me mordí"

(ya -wakx-0-thuj

//REF-morder- AOR-1psASER//

yuyith “me pegué

(ya -uyi-g-thu)

//REF-pegar- AOR-1psASER//

Morfemas léxicos
Los morfemas léxicos o lexemas funcionan todos como raíces en tanto ac-
túan como núcleo en los procesos de formación de palabras; a ellos se afijan
los morfemas gramaticales, tanto flexivos como derivativos. Los morfemas
léxicos del nasa yuwe se pueden clasificar en cuatro grupos: nominales, ver-
bales, verbonominales y cualificativos. Puede decirse que hay dos polos, los
nominales y los verbales, cuya distinción se basa en criterios morfosemán-
ticos, es decir, por la compatibilidad e incompatibilidad con determinados
morfemas, pues algunos morfemas que son compatibles con los nominales
no lo son con los verbales y viceversa. A partir de estos dos polos se estable-
ce la existencia de las otras dos clases. La relación entre las cuatro clases de
lexemas puede representarse de la siguiente manera:

* Al representar el nivel morfológico en la glosa yuxtalineal de los ejemplos, se tomará siempre la
forma larga para representar el morfema. Por ejemplo, en el caso de (-na --nj se tomará «-na», en
el caso de Í-thu —-th) se tomará «-thu», etcétera.

<!-- page 42 (screenshot 0042) -->
Nominal Verbonominal Cualificativo Verbal
+ + + +
Figura 2. Escala de clasificación de los morfemas léxicos

Las dos clases situadas en los extremos forman palabras nominales y ver-

bales, respectivamente. Las dos clases del centro forman indistintamente

palabras de una y otra clase. Las cuatro clases de lexemas pueden funcionar
como raíces para formar tanto palabras predicativas como palabras no pre-
dicativas. Con los nominales y los verbonominales se pueden formar pala-
bras no predicativas de carácter nominal sin que medie ningún morfema
derivativo; los cualificativos y verbales requieren de un morfema transposi-
tor** para ello. Los lexemas verbonominales, cualificativos y verbales pueden

formar palabras predicativas de carácter verbal (predicación dinámica) di-

rectamente, sin derivación, mientras que los lexemas nominales requieren

de un morfema transpositor para formar esta clase de palabras.

Lexemas nominales (N)

Los morfemas léxicos nominales se caracterizan porque:

e Son morfemas libres, es decir, pueden formar palabras por sí solos.

e Puedenir precedidos de los posesivos, demostrativos y cuantificadores.

* Reciben los morfemas derivativos diminutivo, colectivo, aditivo y si-
milativo.

* Reciben los morfemas flexivos de caso.

e No se combinan en forma directa con los morfemas flexivos de aspecto;
para hacerlo necesitan del morfema transpositor (-yuu) (dinamizador).

e Forman palabras predicativas y no predicativas.

Semánticamente, los lexemas nominales corresponden a:

e Los nombres de persona, en su mayoría préstamos del español: Kse
“José”, Tmigu "Domingo, Mlxia “María”, Malse “Mercedes”, Salvxiku
“Salvador” etcétera.

e Los nombres de lugares, tales como Domo “Mondomo”, Cxidaku
“Chindaco”, Payan “Popayán”, Vxlaçxi "Vilachí, etcétera.

e Los nombres de animales, como sxita “armadillo” alku “perro” çxavx
“venado” misx “gato”, sxuma “ardilla”, atalx “gallina” welx “loro” ul
“culebra”, jiba “caballo” tub “paloma”, etcétera”.

* Un morfema transpositor es el que habilita a una palabra perteneciente a una categoría para que
funcione como las de una categoría diferente.

* Se ha encontrado una excepción: en la región de Paniquitá fxu significa “pájaro”, además de
“volar”, (en otras regiones “pájaro” se dice vxiexakwe); en este caso el nombre del animal se estaría
construyendo con un lexema verbonominal.

<!-- page 43 (screenshot 0043) -->
MORFOLOGÍA

e Los nombres de plantas, tales como nxa “yuca” çxaju “piña” á's “arra-
cacha, meskwe “cilantro” kaka “papa”, úth “batata” jxuth “hierba” us
“frijol” etcétera.

e Los términos de parentesco. Ejemplo: ney “padre”, peçuç “tía paterna”
cum “cuñado de hombre”, kahka “tío materno”, zxisx “hermano de
mujer”, pesx “hermana de hombre”, etcétera.

e Los nombres de las partes del cuerpo, como yafx “ojo kwta “bra-
zo, hombro”, me kx “hígado” cida "pie, us “riñón” yuwe "boca, jibe
“pierna etcétera.*

e Los nombres dados a los seres humanos según el sexo y las distintas
etapas de la vida: luuçx “niño/niña” kna'sa “jovencita” pictakx “jo-
vencito”, pezx "Vieja, isx “viejo” y los genéricos, piç “hombre/macho”,
Wwy “mujer/hembra”, nasa “gente/ser vivo”, que funciona también como
etnónimo de denominación endógena. Con él, se pueden agrupar
aquí igualmente otros etnónimos: mu “guambiano” musxka “blanco”,
pipsxaw “pijao”, etcétera.

e Los nombres de accidentes geográficos y de la topografía, tales como
ikh “laguna”, vxiç “cerro” jega “acantilado”, kig “cañada, zanjón”, çx-
hab “pueblo”, we pe “páramo”, etcétera.

e Nombres para divisiones del tiempo: ki'su “semana”, kus “noche” een
“día” etcétera.

Lexemas verbales (V)

Los lexemas verbales se caracterizan porque:

* Salvo en condiciones especiales, no aparecen libremente, sino como
morfemas ligados.

e Forman palabras predicativas; para formar palabras no predicativas
deben recibir el morfema transpositor (-sa) (nominalizador).

* Se combinan con los morfemas de aspecto.

e Se combinan con los morfemas de la modalidad que expresa la rela-
ción del locutor con su interlocutor: imperativo, prohibitivo, exhorta-
tivo, incitativo.

* Reciben los morfemas derivativos que modifican la valencia verbal:
factitivo y reflexivo.

* Son incompatibles con los morfemas de caso.

e No pueden ir acompañados de posesivos, demostrativos ni cuantifi-
cadores.

* Se han encontrado dos excepciones: en Caldono, kuse significa “mano” y “quitar”, y en Toribío ús
significa “corazón” y “respirar”; se trata en estos casos de lexemas verbonominales.

<!-- page 44 (screenshot 0044) -->
MORFOLOGÍA
mochila” beka “chicha/hacer chicha”, yat “casa/construir casa”, mitx
“olla/hacer olla”, pud “hilar fique/atado de fique hilado” etcétera.

* Algunas acciones con su resultado. Ejemplos: mem “cantar/canción”
pekwe "golpear/golpe, wa kx “morder/mordedura”, kab “quemar/lo

» . Les A . » CC . » Z
quemado”, sxihka “reír/risa” sus “sonar/ruido” etcétera.
* Algunas acciones con una entidad con la que se relaciona estrecha-
. CC Lo 7. » CC » CC
mente. Ejemplos: ksxaw “soñar/espíritu” puta “oler/olor”, peswe “ro-
bar/ladrón", ah “cocinar/humo”, efx “derrumbe/derrumbarse” etcétera.
Lexemas cualificativos (Q)

Los lexemas cualificativos se caracterizan porque:

* Pueden aparecer como morfemas libres.

e Pueden formar palabras tanto predicativas como no predicativas; for-
man las predicativas sin necesidad de un proceso de derivación, com-
binándose con los morfemas que van tanto con los nominales como
con los verbales.

e Para recibir los morfemas de caso necesitan, al igual que los lexemas
verbales, del morfema transpositor Í-sa) (nominalizador con valor se-
mántico de agentivo: “el que hace x”).

* Pueden funcionar como modificadores semánticos del nombre en un
sintagma nominal.

Semánticamente los lexemas cualificativos se refieren a:

* Cualidades físicas tales como tamaño, forma, color, temperatura, tex-

. CC 238 3 CC -
tura, sabor, etc. Ejemplos: wala grande/crecer Y, leçx “pequeño/re-
ducirse””, nxiisx “gordo/engordarse”, talx “flaco/enflaquecerse” tadx
CC . » CC . . » CC . .

redondo/girar”, beh “rojo/enrojecerse, arder”, lem “amarillo/amari-
llear, fize "frio/enfriarse', agxa "caliente/calentarse, txi tx “roñoso/
Lo » Ed «7 LA » CC
volverse roñoso”, sxikh “áspero/volverse áspero” duh "pesado/pe-
» - CC » CC
sar, volverse pesado”, wet “sabroso/volverse sabroso”, nxusxa dulce/
endulzar”.

* Cualidades referidas a comportamientos. Ejemplos: chedx “mez-

: : » > CC » CC .
quino/mezquinar”, wa'l “perezoso/rehusar hacer algo”, habx “arisco/
volverse arisco” juna “bravo/ponerse bravo”, tud “rápido/volverse

7 . » CC V4Q Z
rápido, ev bueno/volverse bueno”, etcétera.
* El cualificativo wala funciona también como cuantificador para significar “mucho, muchos”.
” El cualificativo le'çx funciona también como cuantificador, con el significado de “poco, pocos”.
“ En realidad, el cualificativo ew se refiere tanto a comportamientos como a estados.

<!-- page 45 (screenshot 0045) -->
e Son incompatibles con los sufijos derivativos diminutivo, colectivo,
similativo y aditivo.

Semánticamente, los lexemas verbales se refieren a:

* Eventos monoactanciales" de movimiento o desplazamiento: u"- “ca-
minar, wuwu- “correr”, wete- “caer”, tehka- “subir”, çah- “bajar a tie-
rra, pehd- “nadar” etcétera.

e Actividades monoactanciales que no implican desplazamiento o mo-
vimiento, tales como deh- “dormir”, une- “llorar”, pebe- “chillar”,
kase- “descansar use- “respirar”, we W- “hablar”, uu “morir” etcétera.

e Actividades que, aunque pueden involucrar a más de un participante,
se consideran genéricas, por cuanto no están asociadas a un objeto en
particular: um- “tejer, mji- “trabajar” pad- “barrer”, uh- “sembrar”,
pweesa- “jugar”, ku - “bailar”, theg- “ver”, ú"- “comer” etcétera.

e Eventos considerados «estativos»: ús- “estar (eje corporal alargado)”,
wp- “estar (eje corporal no alargado)”, ji ph- “tener”, jiy- “saber, cono-
cer”, yuh- “venir”.

Lexemas verbonominales (VN)

Los lexemas verbonominales se caracterizan porque:

e Pueden aparecer como morfemas libres.

e Pueden formar palabras predicativas y no predicativas sin que sea ne-
cesario un proceso de derivación.

* Se combinan con todos los morfemas compatibles tanto con los lexe-
mas nominales como con los lexemas verbales.

Semánticamente los lexemas verbonominales se refieren a realidades sus-
ceptibles de ser concebidas tanto en su acontecer, como procesos (faz verbal
o dinámica), como en su resultado, en cuanto entidades (faz nominal). Son
los siguientes:

e Fenómenos y seres naturales tales como sek “sol/hacer sol”, kiwe “tie-
rra/volverse tierra”, kwet “piedra/volverse (como) piedra”, kite “flor/
florecer”, kpi'sx “trueno/tronar”, kwehne “relámpago/brillar”, nus “llu-
via/hacer invierno, etcétera.

* Sentimientos, como thame “vergienza/avergonzarse” yús “tristeza/
entristecerse, wecxa “beso/ponerse contento” kutx “aburrido/abu-
rrirse, etcétera.

* Objetos de la cultura material. Aquí se considera el objeto como en-
tidad y el proceso de su elaboración. Ejemplos: ya'ja "mochila/hacer

* Eventos en los que hay un solo participante.

<!-- page 46 (screenshot 0046) -->
e Cualidades referidas a estados. Ejemplos: aga “enfermo/enfermarse”,
zxicxkwe “bonito/ponerse bonito” cehk “limpio/limpiar”, they "difí-
cil/ponerse difícil”, etcétera.

Morfemas gramaticales

Entre los morfemas gramaticales o gramemas hay libres y ligados. Los li-
bres pueden formar palabra solos y pueden servir de base para agregar otros
morfemas gramaticales; los ligados son todos los afijos, entre los que se en-
cuentran morfemas flexivos, morfemas derivativos y otros.

Como morfemas gramaticales libres se encuentran:

e Pronombres personales: adx o agx “yo (masculino), ukwe “yo (fe-
menino)” idx o igx “tú (masculino) 'kwe “tú (femenino) kwe'sx
“nosotros”,  kwe'sx “ustedes”

e Demostrativos: na “este, esta, esto”, txà o kxa “ese, esa, eso”.

e  Deícticos temporales: àçxh "hoy/ahora, unah “ayer”, kuskay “maña-
na kusi “esta mañana”.

e Interrogativos: kih “¿qué?” kim “¿quién?”, maa “¿cuál?” maz “¿cuán-
to, makwe “¿cuánta cantidad?” ma'w “¿cómo?” mte “¿dónde?”
bakacx “¿cuándo?”. Estos pronombres se combinan con el morfema
-yuhpa para expresar valores semánticos negativos. Ejemplos: kimyu-
hpa “nadie”, bakacxyuhpa “nunca” mteyuhpa “en ninguna parte” ki-
hyuhpa “nada”.

e Cuantificadores. Indefinidos como jxuka “todo”, veh “poco”, kúh “va-
rios, muchos", ma “ningún, ninguno”, pxahn “mitad” sena “mucho,
demasiado, thaakwe “mucho”. Funcionan también como cuantifi-
cadores los numerales cardinales. Del sistema de numeración tradi-
cional solo se conservan pocos números: teeçx “uno” ez “dos”, tekh
“tres, pahz “cuatro” tahç “cinco” y kseba “diez”.

* Conectores, como kicxa “entonces”, txaju “entonces, así que, napa
“pero” meeçxa “tal vez”, txa wi "así, entonces”?

Entre los morfemas gramaticales ligados están los morfemas flexivos,
los morfemas derivativos, los morfemas de organización de la información
en la oración y los morfemas con los que se construyen los deícticos es-
paciales. Los morfemas flexivos y los morfemas derivativos se relacionan
“1 Como pronombre de tercera persona del singular se usa el demostrativo lejano txà o kxã; el plural

se construye agregándole el morfema derivativo de colectivo -vvesx: txiwe'sx o kxawe'sx.

1. De los morfemas gramaticales libres, los conectores no funcionan como base para formar una
palabra predicativa.

<!-- page 47 (screenshot 0047) -->
MORFOLOGÍA
directamente con los procedimientos morfológicos flexión y derivación,
respectivamente.

Para relacionar los morfemas ligados flexivos y derivativos, se presentan
a continuación los procedimientos morfológicos bàsicos encontrados en la
lengua: flexión, derivación y composición. Posteriormente, se relacionan los
otros morfemas gramaticales ligados.

PROCEDIMIENTOS MORFOLÓGICOS
A continuación se presentan los procedimientos morfológicos encontrados
en la lengua, a saber: flexión, derivación y composición. El procedimiento
de la flexión se presenta en términos generales, ya que se describirá deta-
lladamente en el capítulo de Morfosintaxis. Posteriormente se describe la
constitución de las palabras y sus clases básicas.
La flexión
Se entiende aquí la flexión como el procedimiento de formación de pala-
bras mediante el cual se agrega a una raíz (0 a una base formada por dos
raíces o por una raíz más un afijo derivativo) información proveniente
de categorías gramaticales; este procedimiento tiene implicaciones en las
relaciones sintácticas que se establecen entre las palabras. En nasa yuwe
se presenta el procedimiento de la flexión tanto en el ámbito nominal
como en el verbal. En el ámbito nominal, existen morfemas de caso mor-
fológico, para establecer la función que dicho nominal cumple en una es-
tructura oracional. En el ámbito verbal, los morfemas flexivos se encargan
de expresar la información correspondiente a las categorías de persona,
número, modalidad, aspecto y distancia nocional o temporal. La mayoría
de los morfemas flexivos son sufijos, aunque se encuentran también algu-
nos prefijos.

Ejemplos de flexión:

yatte dehk “durmió en la casa”
(yat-te deh-o-Ru)
//casa-INE/dormir- AOR-3psASER//

Como puede verse, hay un morfema de caso locativo (inesivo: “en”) que
acompaña al nombre y con el verbo, un morfema que expresa la categoría
del aspecto (aoristo, en este caso) y un morfema que expresa la tercera per-
sona del singular en la modalidad asertiva.

<!-- page 48 (screenshot 0048) -->
misxas theguth “veo al gato”
(misx-a's theng-u-thul
//gato-OBJ/ver-IMPE-1psASER//

En este ejemplo se encuentra en el nombre el morfema de caso acusati-
vo-dativo (glosado como “objeto”) y en el verbo, el morfema de aspecto im-
perfectivo más el morfema que amalgama las categorías de modo, persona
y número.

La derivación

El procedimiento de derivación se presenta cuando se añade un afijo a una
raíz léxica para formar con ella una nueva palabra. Se ha encontrado que en
nasa yuwe la derivación puede darse tanto con prefijos como con sufijos; la
derivación en el ámbito verbal se da mayoritariamente por prefijos y en el
ámbito nominal, por sufijos.

Ejemplos de derivación:

alkukwe “perrito”
falku-kwej

//perro-DIM//

luuexwesx “niños”
(luuçx-vesxt

//niño-COL//

En el primer ejemplo, el nombre ha recibido el morfema de diminutivo y
en el segundo, el colectivo, ambos sufijos derivativos.

kapiyak “(él o ella) enseñó”
(ka-piya-o-kuj
//FACT-aprender-AOR-3psASER//

Agregando a la raíz del verbo piya- (“aprender”) el prefijo factitivo, se
obtiene el verbo kapiya-, que significa “enseñar” es decir que “enseñar” es
“hacer aprender”.

puutxwedxitx “(ellos) se quieren (uno al otro)”
(puutx-wedx-i-tx)
//RECI-querer-IMPF-3ppASER//

<!-- page 49 (screenshot 0049) -->
MORFOLOGÍA

Del verbo wedx- “querer” se deriva el verbo puutxwedx- “quererse (mu-
tuamente)” mediante la prefijación del morfema que agrega el significado de
reciprocidad.

Morfemas derivativos del nombre
Son morfemas derivativos del ámbito nominal:
[-kwe) diminutivo (DIM)
[-we'sx) colectivo (COL)
[-wao -paj* aditivo (ADI)
(-na'vvi similativo (SIMD
[-cxa) restrictivo (REST)

El morfema diminutivo agrega la noción de tamaño pequeño o reduci-
do; el colectivo se usa para pluralizar los nombres, cuando se trata de un
conjunto mayor a la unidad; el aditivo agrega un nombre a otro nombre; el
similativo agrega a un nombre el significado de “parecido a”; el restrictivo,
como su nombre lo indica, restringe a una entidad, particularizándola, o a
un conjunto, cerrando la posibilidad de agregar nuevos elementos. Hay que
agregar que estos morfemas se pueden sufijar también a los pronombres
personales.

Ejemplos:

yatkwe “casita”

(yat-kwej

/casa-DIM/

luuexwesx “(los) niños”

(luucx-vesxt

/niño-COL/

uypa “la mujer también”

(uy-paj

/mujer-ADI/

piçna w “como varón”

(pic-naw)

/varón-SIMI/

** Según variantes regionales: (-pa) en Tierradentro y el norte, (-wa) en Caldono.

<!-- page 50 (screenshot 0050) -->
nxacxa “yuca no más”
ínxa-çxal
(yuca-REST/

En el léxico de parentesco, la lengua distingue si el nombre del parien-
te mencionado es el del hablante o el de otra persona. En unos casos esta
distinción se hace léxicamente, es decir, con palabras diferentes, como es el
caso de las palabras para “padre”: tata, si es el padre de quien habla, y ney,
si es el padre de otra persona, o las palabras para “madre”: mama, si es del
hablante, y nxji, si es de otra persona. Pero en otros casos la distinción se
hace agregando un prefijo al nombre del pariente cuando es el de una per-
sona distinta del hablante: (n-). Algunos ejemplos: kahka “tío materno” (del
hablante) y nkahka “tío materno” (de otra persona); cuwa “cuñado/a (de
distinto sexo)” del hablante, neuwa “cuñado/cuñada (de distinto sexo)” de
otra persona; çiza “cuñado/a” (de igual sexo)” del hablante, nçiza “cuñado/a
(de igual sexo)” de otra persona. Puede decirse que este prefijo funciona
como un morfema derivativo específico para los nombres de parentesco.
Morfemas derivativos del verbo

Son morfemas derivativos del ámbito verbal:

(Xa-) “factitivo” (FACT)
[ya -) “reflexivo” (REF)
(puutx-) o (puukx-) — “recíproco” (RECD*

Estos prefijos derivativos establecen operaciones en relación con los roles
actanciales del verbo y en esa medida modifican la valencia verbal“. El fac-
titivo aumenta un participante, que funciona como instigador para que otro
haga la acción. El reflexivo establece una correferencia entre el agente y el
paciente semánticos. El recíproco establece que la acción la realizan simul-
táneamente el agente y el paciente, es decir que cada participante es agente
de su accionar y paciente del accionar del otro. Ejemplos:

kapiya- “enseñar”

(ka-piya-)

/FACT-aprender-/

4. Este morfema puede aparecer también como forma libre.
5 La valencia verbal se refiere al número de participantes que tiene un verbo según el evento que

Expresa.

<!-- page 51 (screenshot 0051) -->
MORFOLOGÍA
ya wa kx- “morderse”

(ya -wa'kx-)

/REF-morder-/

puukxtheg- “verse mutuamente”

(puutx-theg-)

/RECI-ver-/

La derivación anteriormente presentada no produce un cambio en la cla-
se a la que pertenece el lexema que sirve de base. Pero también existen en la
lengua dos morfemas derivativos transpositores: el morfema nominalizador
(-sal, que sufijado a una raíz verbal o cualificativa forma con ella una pa-
labra apta para cumplir funciones no predicativas propias del nombre, y el
morfema dinamizador (-yuuj, que sufijado a una raíz nominal produce una
palabra verbal. Ejemplos:

mjisa “trabajador, el que trabaja”

(mji-sa)

/trabajar-NOM/

nasa-yuu- “volverse gente”

(nasa-yuu-)

/gente-DIN-/
La composición
Además de la flexión y la derivación, se encuentra el procedimiento de la
composición. Se entiende como la formación de palabras en las que se unen
dos morfemas léxicos; en este caso, uno de ellos conserva su acento y el
otro lo pierde. Pueden unirse dos lexemas nominales, lo más frecuente, pero
también un lexema nominal con uno cualificativo o un lexema verbal con
uno nominal. Ejemplos:

N+N

picthe “hombre” (pihç “varón” + the “adulto, mayor”)

ipxkwet “fogón”  (ipx “fuego” + kwet “piedra”)

fxthúsyafx “libélula” (fxthús “arco iris” + yafx “ojo”)

yu kwet “hielo” — (yu “agua” + kwet “piedra”)

yafxkhas “cejas, pestañas” (yafx “ojo” + khas “pelo, lana”)

yafxyu “lágrima” (yafx “ojo” + yu “agua”)

kwetuba “granizo” (kwet "piedra +tub “paloma” o tuba “es paloma”)

<!-- page 52 (screenshot 0052) -->
apkhas “zancudo” (áp “mosca” + khas “pelos”)
fxtáutasx “árbol” (fxtúu “palo” + tasx “mata”)
dxkhas “cabello” (dxip “cara” + khas “pelo”)
CC » «o » «os. »
yafxkwet frente" (yafx “ojo” + kwet piedra”)
N+Q
thewala “médico tradicional” (thé “adulto, mayor” + wala “grande”)
> «7 5 » CC » CC »
yu wala “río” (yu “agua” + wala grande")
taphçxihme “neblina” (taph “nube” + cxihme “blanco”)
. CC XV . CC » CC »
vxicwala montaña” (vxig cerro” + wala grande”)
Y +N
fxuRu'ta “ala” (fxu- “volar” + kuta “brazo, hombro, rama”)
Este procedimiento de la composición actualmente se emplea en la for-
mación de neologismos —palabras nuevas—. Algunos ejemplos:
cawelx “radio” — (caam “hierro” + welx “loro”)
catud “moto” (caam “hierro” + tud “rápido”)
capuyaksa “sistemas informáticos”
(caam “hierro” + puyak “ayudar” + sa NOM)
cakha'kh “chiva” (caam “hierro” + khi'kh “hormiga”)
. CC » . CC » CC »
piyayat “escuela” (piya aprender” + yat casa”)
fxi pil “boligrafo” (fxi “escribir” + pil “alargado”)
fxicxal "marcador " (fxi “escribir” + cxal “grueso”)
kajxad “balón” — (kahta “levantar” + jxad “esférico”)
Otros morfemas gramaticales
Además de los morfemas flexivos y derivativos presentados hasta el mo-
mento, existen en la lengua otros morfemas gramaticales ligados. Entre ellos
se encuentran los morfemas con los que se forman los deícticos espaciales,
morfemas que intervienen en la organización de la información en las ora-
ciones y morfemas que indican la subordinación de predicados en oraciones
complejas.
* Çaam se refiere a hierro, de manera específica, y se puede aplicar de modo genérico a todo lo metálico.
1 “Moto” es una forma abreviada de «motocicleta».
18. Chiva o bus escalera: vehículo de transporte público de pasajeros y carga.
5 “Marcador” como instrumento de escritura.

<!-- page 53 (screenshot 0053) -->
MORFOLOGÍA
Morfemas de organización de la información

Existen en nasa yuwe varios morfemas gramaticales ligados que ejercen
su función en la organización que se hace de la información en una estruc-
tura oracional. Ellos son:

a) topicalizador (TOP)

(yu) enfático (ENF)

(-i-) corroborativo (CORR)

faç-) conector consecutivo (“entonces”)
(-pçel o Í-çel confirmativo (CONF)

El topicalizador f-a't suele acompañar al nominal que explicita léxi-
camente al sujeto de la oración, que se sitúa normalmente al inicio, así
como a circunstantes de lugar o tiempo que encabezan la oración; estos
elementos así marcados morfológicamente se presentan como tópico o
tema de lo que se va a hablar. El topicalizador (-a') también acompaña al
conector (ac-). El enfático [-yuw ) va también sufijado a un nominal al que
se le quiere dar un cierto realce como constituyente de la oración. El co-
rroborativo (-i-) acompaña a un nominal cuando se quiere establecer que
sí es el elemento del cual se predica algo. El confirmativo (-pçel o [-ce) se
agrega a un predicado flexionado para confirmar lo que se está diciendo.
Ejemplos:

misxa pebek “el gato chilló”
ímisx-a' pebe-o-kuj
//gato-TOP/chillar- AOR-3psASER.PD//
kuskaya Cxidakun wjecthaw “mañana vamos para Chindaco”
(kuskay-a”/Cxidaku-na wj-e-c-thaw)
//mañana-TOP/Chindaco-ALA/ir-IMPF-INT-1ppASER//
aca e kxha pcune “entonces la leña se acabó”
faç-a' ekxh-a” pçu-o-ne-a')
//entonces- TOP/leña-TOP/acabar- AOR-D3-3psASER.PE//
klaik “sí es vaca”
(kla-i-kuj)
//vaca-CORR-3psASER.PD//

<!-- page 54 (screenshot 0054) -->
ayteyu txaju wakaswesxa nawe upta “entonces los blancos están así”
(ay-te-yu txaju' wakas-wesx-a' nawê u'p-tal
(/cerca-INE-ENF/entonces/blanco-COL-TOP/así/estar-3ppASER.PE//
Siskayu” dehmeneka petepce mutxi ahna
[Siska-yu” deh-me-ne-ka pete-pce mutxi ah-naj
//Siska-ENF/dormir-NEG-D3-3psSUS.PD/amanecer-CONF/mote/
cocinar-DUR//
“La siska solía no dormir y amanecía cocinando mote””

Los subordinadores son morfemas que se sufijan a las raíces en las formas
verbales no finitas” que corresponden a predicados subordinados, indican
que dicho predicado está subordinado a otro al tiempo que agregan la infor-
mación semántica correspondiente a la relación existente entre el predicado
subordinado y el principal (esto se presentará en el capítulo de Sintaxis). Son
ellos, además del inesivo (-tej y el restrictivo (-exaj, que también funcionan
en la subordinación de predicados, los siguientes:

[-pa'ka) subordinador causal (CAUS)

(-paçal subordinador hipotético (HIP)

(-val  subordinador de finalidad general (FIN.G)

(kan) subordinador de finalidad específica (FIN.E)

(-mey) subordinador temporal de anterioridad, igual sujeto (ANT.IS)

(-meynal subordinador temporal de anterioridad, diferente sujeto (ANT-DS)

[-exapa) subordinador concesivo igual sujeto (CONC.IS)

(-tepal subordinador concesivo distinto sujeto (CONC.DS)

Ejemplos:

nasacxapa “aunque es paez”
(nasa-çxapal
(paez-REST-CONC.IS/
zxicxkwepa ka “porque es bonita”
(zxiçxlave-pa Xa)
/bonita-CAUS/
Comida muy común entre los nasa, a base de maíz pelado.
>! Se trata de palabras verbales que no tienen el morfema flexivo modopersonal.

<!-- page 55 (screenshot 0055) -->
MORFOLOGÍA

pajpaça “si llegara”

(paj-paca)

/legar-HIP/

ujmey “antes de ir”

(uj-mey)

fir-ANT.IS/

padwa “para barrer”

(pad-vva)

(barrer-FIN/
Deícticos espaciales
Además de los demostrativos ya presentados, el espacio como categoría gra-
matical se expresa en deícticos que se forman a partir de la combinación de
tres paradigmas.

El primer paradigma, situado a la izquierda del deíctico, contiene cinco
morfemas que dan información acerca de la ubicación espacial de la entidad
con relación al punto de referencia o centro de la deíxis y en atención a ejes
de verticalidad u horizontalidad. Los morfemas son: (khe-) “abajo, vertical-
mente”, (súu-) “abajo, diagonalmente”, (úy-) “horizontalmente”, (kaa-) “arri-
ba, diagonalmente” y (kutee-) “arriba, verticalmente”.

Hay un segundo paradigma, que se sitúa en el centro y contiene la in-
formación acerca de la distancia de la entidad situada con relación al punto
de referencia. Los morfemas son: fay-) “cerca” (nu-) “lejos” y (kx-) “punto
preciso”.

El tercer paradigma, situado a la derecha del deíctico, aporta información
acerca del eje corporal de la entidad que se sitúa espacialmente y corres-
ponde a los cuatro morfemas presentados con el valor semántico de inesivo
entre los morfemas de caso. Son ellos (-te, (-kaj, (-suj y (-khej>.

Para la construcción del deíctico se pueden combinar los tres paradig-
mas, los paradigmas primero y tercero, o los paradigmas segundo y terce-
ro. La combinatoria de todos esos morfemas arroja la suma de 92 posibi-
lidades de expresión de la ubicación espacial de una entidad o un hecho
cualquiera”.

* En el capítulo 6 se describe con más detalle la expresión del espacio: allí se encuentran las figuras
ilustrativas.
* Este aspecto de la gramática de la lengua fue desarrollado detalladamente en Nieves y Ramos

(1992).

<!-- page 56 (screenshot 0056) -->
Tabla 7. Morfemas de los deícticos espaciales
khe ay te |
súu ha
úy nu
Raa su
Rutee Rx khe
Ejemplos:
Uy-ay-te “situado en zona horizontal, cerca, eje corporal vertical”
khe-nu-ka “abajo (descenso fuerte) lejos, eje corporal horizontal”
Rutee-su “arriba (ascenso fuerte), eje corporal ligeramente inclinado”
úy-te “en zona horizontal, eje corporal vertical o no marcado”
ay-khe + “cerca, eje corporal fuertemente inclinado”
LA PALABRA
Si bien la palabra es difícil de definir en linguística, a pesar de haber sido re-
conocida como una unidad de significación desde la Antiguedad, se trata de
una realidad presente en muchas lenguas y se ubica como un nivel interme-
dio entre el morfema y el sintagma, es decir, la transición entre la morfología
y la sintaxis. Las palabras pueden estar constituidas por unidades menores
dotadas de significado, los morfemas, que se articulan según los procedi-
mientos antes vistos. Desde el punto de vista de la sintaxis, las palabras se
combinan entre ellas para formar grupos —sintagmas— que, combinados
entre sí o con otras palabras, dan lugar a las oraciones.
En nasa yuwe las palabras se caracterizan por los siguientes criterios ge-
nerales:
e Pueden ser pronunciadas aisladas o entre dos pausas.
e Entre dos palabras se pueden intercalar otras palabras.
e Sus partes constitutivas no pueden ser reorganizadas en un orden di-
ferente.
e Son la sede del acento: hay por lo menos un acento primario en cada
palabra.
* Son la sede de los procesos morfofonológicos.
e Pueden constituir una unidad mínima de comunicación.
La palabra puede estar formada por:
Un morfema libre, sea léxico o gramatical. Ejemplo: kite “flor” adx “yo
(masculino)”.

<!-- page 57 (screenshot 0057) -->
MORFOLOGÍA

Un morfema léxico más un morfema gramatical. Ejemplo: wy-thu “soy
mujer” lem-a “es amarillo”.

Dos morfemas gramaticales. Ejemplo: Rim-na “¿quién es?”, na-a' “es este”.

Dos morfemas léxicos y un morfema gramatical. Ejemplo: ipx-kwet-a”
“es (un) fogón”, yu -wala-te “en el río”.

Un morfema léxico y varios morfemas gramaticales. Ejemplo: ka-sus-
yawa-ki-ku “no lo va a hacer sonar”, lem-u-ç-a “se está amarilleando”.
Clases de palabras
Desde el punto de vista morfológico, las palabras del nasa yuwe se dividen
en flexionadas y no flexionadas. Desde el punto de vista sintáctico, es decir,
teniendo en cuenta su funcionamiento en una estructura oracional, las pa-
labras pueden ser predicativas y no predicativas. Entre las no predicativas se
encuentran algunas flexionadas, los nombres que llevan el morfema de caso,
que cumplen en la oración funciones argumentales o circunstanciales y no
la función predicativa.

Una palabra flexionada puede estar constituida por una base más una fle-
xión; el orden de estos dos constituyentes puede variar. La base puede estar
constituida por un lexema, por dos lexemas o por un lexema más un mor-
fema derivativo. La flexión puede estar formada por uno o varios morfemas
flexivos. Las palabras no flexionadas carecen de morfemas flexivos.

A excepción de los conectores, todas las palabras del nasa yuwe pueden ser
predicativas. Por la estrecha relación que tiene la construcción de las diferentes
clases de palabras con la predicación, dichas clases se tratarán detalladamente
en el próximo capítulo. Entonces, se hace aquí una presentación general.

Las palabras que tienen flexión modopersonal son predicativas y cum-
plen por lo tanto la función sintáctica de núcleo predicativo de la oración.
Como raíz de estas palabras pueden encontrarse lexemas de las cuatro clases
—nominales, verbales, verbonominales y cualificativos— o algunos grame-
mas: deícticos personales, espaciales y temporales, cuantificadores, interro-
gativos y el morfema de la negación.

Ejemplos de palabra predicativa con lexema como núcleo:

dehg “dormiste”
1 deh-o-gu +
//dormir-AOR-2psASER//
uyth “soy mujer”
(uy-thuj
//mujer-1psASER//

<!-- page 58 (screenshot 0058) -->
MORFOLOGÍA
circunstanciales, los cualificativos en función de modificadores del nombre
y los conectores. Ejemplos:

wnaha alku wkwe's wa kxku “ayer me mordió el perro”

(unah-a alku u'kwe-as wa Rx-o-Rut

(/ayer- TOP/perro/-yo(fem)-OBJ/morder- AOR-3psASER.PD//

Kse yatte úsa “José está en la casa”

(Rse-a' yat-te Us-9-a')

//José-TOP/casa-INE/estar-AOR-3psASER.PE//

ayte aça ptasxkitha'w “aquí entonces avisamos”

(ay-te aç-a ptasx-ki-thawj

//cerca-INE/entonces- TOP/avisar- D1-1ppASER//

Las palabras del nasa yuvve también se pueden clasificar en léxicas y gra-
maticales, según los mismos criterios que se aplicaron a la clasificación de
los morfemas. Las palabras léxicas son las que tienen como núcleo o raíz
un morfema léxico y las palabras gramaticales son las que tienen como
núcleo un morfema gramatical o simplemente estàn formadas por un gra-
mema libre.

Son palabras léxicas:

e El verbo. Se forma con un lexema verbal o un lexema verbonominal

como núcleo. Siempre es palabra flexionada y predicativa.

e El nombre. Se forma con un lexema nominal o un lexema verbonomi-
nal como núcleo. Puede ser flexionada o no; puede ser predicativa o no.

e La palabra cualificativa. Se forma con un lexema cualificativo y actúa
como modificador semántico de palabras nominales o verbales.

Son palabras gramaticales:

e Los deícticos. Personales: pronombres personales. Espaciales: demos-
trativos y deícticos espaciales (de localización). Temporales: pueden ser
flexionadas o no flexionadas; pueden ser predicativas o no predicativas.

e Los interrogativos. Son predicativos, se combinan con los morfemas
del modo interrogativo.

e Los cuantificadores: indefinidos y numerales. Pueden ser flexionadas
o no; pueden ser predicativas o no.

e Los conectores. No son flexionadas; no son predicativas.

<!-- page 59 (screenshot 0059) -->
kitek “floreció”
(kite-0-ku)
//flor-AOR-3psASER.PE//
talxthu “soy flaco”
(talx-thut
(/flaco- IpsASER//

Ejemplos de palabra predicativa con gramema como núcleo:

agxthu “soy yo”
(agx-thuj
//yo(masc)-1psASER//
na “es este”
ina-a
//este-3psASER.PE//
jxuka “es todo”
(jxuka-a')
//todo-3psASER.PE//
teecxa “es uno”
[teecx-a')
//uno-3psASER.PE//
kimka “¿quién es?”
(kim-kaj
//quién-3psINTE.PD//
acxha “es hoy”
(açxh-a'l
//hoy-3psASER.PE//

Palabras no predicativas son las que no tienen el morfema modoper-
sonal. Se encuentran en este grupo los nombres en funciones actancia-
les o circunstanciales”, los deícticos espaciales y temporales en funciones
** Se refiere a las funciones de sujeto y complementos.

<!-- page 60 (screenshot 0060) -->
A manera de recapitulación

En el nasa yuwe la mayoría de los morfemas son monosilábicos o bisilábicos.
La forma más frecuente de materialización de los morfemas es la secuencia
de fonemas; no se presentan morfemas discontinuos.

Como en toda lengua, hay morfemas léxicos —lexemas— y gramaticales
—gramemas—.

Hay cuatro clases de morfemas léxicos.

Hay morfemas gramaticales libres y ligados. Entre los ligados están los
flexivos, los derivativos, los que forman deícticos espaciales y los de organi-
zación de la información.

Se dan en la lengua los procedimientos morfológicos flexión, derivación
y composición.

Hay palabras flexionadas y no flexionadas. Dentro de las flexionadas hay
predicativas y no predicativas.

Hay palabras léxicas y palabras gramaticales. Las palabras léxicas son:
nombre, verbo, palabra cualificativa. Las palabras gramaticales son: deícti-
cos —pronombres personales, demostrativos, deícticos espaciales, deícticos
temporales—, interrogativos, cuantificadores, conectores.

# Capítulo 4 — Morfosintaxis
<!-- ocr -->

<!-- page 61 (screenshot 0061) -->
CAPÍTULO 4
MORFOSINTAXIS

En el presente capítulo se presenta la información sobre las palabras de la
lengua y su funcionamiento. En tanto que la palabra constituye al mismo
tiempo el ámbito máximo de la morfologia y el constituyente mínimo de la
sintaxis, y que en nasa yuwe el criterio de la predicatividad cumple un papel
fundamental para una adecuada clasificación de las palabras, en esta parte
de la gramática de la lengua se relacionan estrechamente los niveles morfo-
lógico y sintáctico. Puede decirse que es la zona de intersección, en la que
interactúan de manera más estrecha estos dos niveles.

Asimismo, se retoma de modo más detallado la clasificación de las pa-
labras que se presentó de manera somera al final del capítulo anterior. Para
ello se hace necesario hablar primero de la predicación en la lengua y de los
tipos de predicación que hay en ella, para posteriormente presentar cada
una de las clases de palabras.

LA PREDICACIÓN
Se entiende la predicación como la operación que permite poner en relación
un predicado con una base de predicación; con esta operación se atribuyen a
dicha base —entidad o situación, estado de cosas— las propiedades o even-
tos —acciones o procesos— expresados por el predicado.

En nasa yuwe existen dos clases de predicación: la predicación dinámica
y la predicación estativa. La predicación estativa relaciona a la entidad base
de predicación con propiedades, características o estados. La predicación
dinámica relaciona a la entidad base de predicación con un evento —acción,

<!-- page 62 (screenshot 0062) -->
proceso o fenómeno natural— dotado de dinamismo. La diferencia entre las
dos predicaciones se manifiesta en la tercera persona, en el morfema mo-
dopersonal, que es obligatorio para la predicación por cuanto en él se expre-
sa la persona gramatical que remite a la base de predicación; es el elemento
que establece la relación predicativa.

La categoría gramatical de persona —primera, segunda y tercera— se
combina con la categoría gramatical de número —singular y plural—, lo
que da como resultado un paradigma de seis formas. Estas dos categorías
se combinan en amalgama con la modalidad de conocimiento —asertiva,
suspensiva e interrogativa— para la construcción del morfema predicativo.

Los morfemas de las dos clases de predicación se combinan según la clase
de lexema que funcione como núcleo del predicado y en atención también
a la combinatoria de dichos lexemas con los demás morfemas que interven-
gan en la palabra.

El morfema de la predicación
El morfema de la predicación expresa las categorías de persona, número y
modalidad. La persona gramatical expresada en dicho morfema remite a la
entidad base de predicación. La modalidad expresa la formulación del ha-
blante frente a lo presentado en la proposición contenida en la oración. Se
presentan a continuación las categorías que forman el morfema predicativo.
La persona y el número
Con tres personas gramaticales y dos números, singular y plural, se estruc-
tura un sistema de seis: primera, segunda y tercera persona del singular (1ps,
2ps, 3ps), y primera, segunda y tercera persona del plural (1pp, 2pp, 3pp).
En la Tabla 8 se ilustra el sistema personal de la lengua con los pronombres
personales.
Tabla 8. Pronombres personales
Número Persona Cu
Masculino Femenino
Primera adx / agx” u'kwe
Singular Segunda idx / igx i kwe
Tercera txã / kxã
Continúa
* En los casos en que aparecen dos formas —primera y segunda persona del singular en género
masculino y tercera persona del plural—, se trata de variaciones dialectales (regionales).

<!-- page 63 (screenshot 0063) -->
Como puede verse en la anterior tabla, la distinción entre las dos clases de
predicación se hace para la tercera persona del singular en relación con las
tres modalidades, y en la modalidad asertiva (mayor grado de conocimien-
to) se hace también en la tercera persona del plural.

Ejemplos de los morfemas predicativos con los diferentes lexemas:
Con lexema verbal

we wek “(él o ella) habla”

[wew-e-ku)

//hablar-IMPF-3psASER.PD//

yuhuga “¿vienes?”

(yuh-u-ga')

//venir-IMPF-2psINTE//

mjiitxna “como que trabajan”

(mji-i-txna)

(/trabajar-IMPF-3ppSUS//

jipha “(él o ella) tiene"

Gi ph-o-a)

(/tener-AOR-3psASER.PE//
Con lexema verbonominal

Ritena ses flor?”

(kite-na”)

//flor-3psINTE.PE//

kiteka “floreció?”

(kite-kaj

//florecer-3psINTE.PD//

memthaw “cantamos (pasado)”

(mem-o-thavvi

//cantar-AOR-1ppASER//
Con lexema cualificativo

wala “es grande”

twala-a')

//grande-3psASER.PE//

<!-- page 64 (screenshot 0064) -->
MORFOSINTAXIS
Ves ss ssssssòesotdSSESis
Número Persona Conca
Masculino Femenino
Primera kwesx
Plural”? Segunda i kwe'sx
| E txàvvesx / Rxàvvesx

Como se puede apreciar en la tabla, en las dos primeras personas del
singular se establece la diferencia de género entre masculino y femenino,
mientras que en la tercera persona no. En la tercera persona del singular
funcionan como personales los demostrativos de lejanía. En las tres perso-
nas del plural no se hace distinción de género.

La modalidad

Las dos dimensiones de la modalidad, la que pone en relación al locutor con
su interlocutor y la que pone en relación al locutor con lo que dice, si bien se
expresan mediante flexión, lo hacen de manera diferente. La primera se mar-
ca por afijos que acompañan a la raíz verbal y no se combina con la persona.
En cuanto a la segunda dimensión mencionada, hay un paradigma de la mo-
dalidad que es opcional —contiene las modalidades volitiva y desiderativa—
y un paradigma que es obligatorio, el de la modalidad de conocimiento.

El modo, correspondiente a la manifestación de la modalidad de cono-
cimiento”, presenta tres grados diferentes de certeza respecto a lo que el
hablante dice: asertivo (ASER), suspensivo (SUS) e interrogativo (INTE). En
el primero, el hablante está seguro del estado de cosas; en el segundo, deduce
o infiere por indicios; el tercero es para interrogar sobre los hechos que no
se conocen. La modalidad de conocimiento se combina con la persona y el
número; las tres categorías están amalgamadas.

Los tres paradigmas de los morfemas de modo.persona.número son:

Tabla 9. Morfemas modopersonales

Persona Asertivo : DOT 3
Suspensivo Interrogativo
l.º singular — -thu -tka -nja
2.º singular — -gu -ga -ga
3.º singular — -ku/-a -ka / -na -ka / -na
1.º plural -tha vv -tkhaw -njaw
2.º plural - kwe -kwe -kwe
3.º plural —txi/ -ta -txna -txna |
* Esta modalidad se conoce también como «evidencialidad».

<!-- page 65 (screenshot 0065) -->
MORFOSINTAXIS
walak “creció”

(vvala-o-Xut

//crecer- AOR-3psASER.PD//

Con lexema nominal

uythu “soy mujer”

fu y-thuj

//mujer-1psASER//

nasaga “seres paez?”

(nasa-ga')

//paez-2psINTE//

misxa “es (un) gato”

Ímisx-a

//gato-3psASER.PE//

Además de los morfemas recogidos en la Tabla 9, hay un morfema mo-
dopersonal con el que el hablante se refiere a acontecimientos futuros que
lo involucren y, en algunos casos, a eventos con los que se compromete; este
morfema no hace parte de un paradigma que contenga morfemas similares
para las otras personas; es el morfema (-n)”, que corresponde a la primera
persona del singular. Ejemplos:

umun tejeré"
fum-u-n)
(/tejer-IMPF-IpsFUT//
mjiin trabajaré"
(mji-i-n)
//trabajar-IMPF-1psFUT//

Siempre es posible dinamizar un lexema de vocación estativa o estatizar
un lexema de vocación dinámica. Existen en la lengua dos morfemas deri-
vativos transpositores o transcategoriales: el morfema nominalizador (-saj,
que sufijado a una raíz verbal o cualificativa forma con ella una palabra apta
para cumplir funciones propias del nombre —predicado estativo o funcio-
7 Este morfema se combina siempre con el aspecto imperfectivo, que se presentará más adelante y

que se expresa mediante una vocal.

<!-- page 66 (screenshot 0066) -->
nes argumentales—, y el morfema dinamizador (-yuuj, que sufijado a una
raíz nominal la vuelve apta para formar una palabra verbal —predicado
dinámico—. Ejemplos:

mjisa “trabajador, el que trabaja”

(mji-saj

/trabajar-NOM/

nasa-yuu- “volverse gente / volverse paez”

(nasa-yuu-)

/gente-DIN-/

Los morfemas modopersonales de predicación se combinan también con
gramemas. Se presentan tres ejemplos, con pronombre personal, con de-
mostrativo y con cuantificador (numeral).

agxthu “soy yo”
(agx-thuj
//yo(masc)-1psASER//
na “es este”
fna-a)
//DEM1-3psASER.PE//
teecxa “es uno”
[teecx-a')
//uno-3psASER.PE//

La modalidad que pone en relación al locutor con su interlocutor, la de
la interacción linguística, se expresa mediante morfemas de predicación que
no flexionan para la categoría de persona gramatical. Estos son:

(m-) “imperativo” (IMP)

[-we) “imperativo plural” (IMP.pl)
(-nu) — “prohibitivo” (PROH)
(-Ral  “exhortativo” (EXH)

(-yal — “incitativo” (INCD

Con el imperativo se dan órdenes directas para que se haga algo; con el
morfema (-wej), que puede ir como el único afijo o simultáneamente con

<!-- page 67 (screenshot 0067) -->
mwecxa “¡bese!”

(m-wecxa]

//IMP-besar//
Con raíces cualificativas

mnxiisx “¡engórdese!”

(m-nxiisxt

//IMP-engordar//

tadxnu “no gire, no dé vueltas”

(tadx-nul

//girar-PROH//

Cuando se quiere hacer una solicitud cortés, se antepone meen “por fa-
vor” al verbo, que va sin marca de imperativo. Ejemplo:

meen puçx “ayúdeme, por favor”

ímeen puçx)

//por favor/ayudar//

CLASES DE PALABRAS

El criterio de predicatividad permite diferenciar en nasa yuwe entre palabras
predicativas y palabras no predicativas. Casi todas las palabras de la lengua
pueden ser centro de predicado, por lo que puede decirse que esta es una
lengua omnipredicativa (Launey, 1994). Hay palabras predicativas verbales
y palabras predicativas nominales; lo que las diferencia fundamentalmente
es la combinación de las palabras verbales con la categoría de aspecto, que
no se da con las palabras nominales. Hay palabras predicativas con aspecto
y palabras predicativas sin aspecto. Las primeras se construyen con lexemas
verbales, verbonominales, cualificativos y nominales dinamizados; las se-
gundas, con lexemas nominales, verbonominales, cualificativos y verbales
nominalizados.
El verbo
El verbo en nasa yuwe, trátese de la construcción sintética —en una sola
palabra— o la construcción analítica —en dos palabras, con estructura de
auxiliaridad—, cumple en la oración la función predicativa.

La palabra predicativa verbal, además de recibir los morfemas flexivos de
modo, persona y número, se caracteriza por la posibilidad de combinarse

<!-- page 68 (screenshot 0068) -->
MORFOSINTAXIS

(m-), se dirige el hablante a un destinatario plural; esta forma se usa también
con las mujeres. En la región de Caldono, la presencia del morfema (-we)
es frecuentemente interpretada como forma cortés de hacer una solicitud,
como un imperativo atenuado. Con el prohibitivo se da también una orden,
pero para que alguien no haga algo. Con el exhortativo el hablante convida
a otros a hacer algo. Con el incitativo se invita a hacer una determinada ac-
ción. Ejemplos:
Con raíces verbales

mtugx “¡tome!”

(m-tugx)

//IMP-tomar//

mkuwjwe “bailen (ustedes)

(m-kuj-wej

//IMP-bailar-pl//

wuwunu “¡no corra!”

fwuwu-nuj

//correr-PROH//

weweka “hablemos”

twew-e-ka)

//hablar-IMPF-EXH*//

ú ya “¡a comer!”

fu ya)

//comer-INCI//
Con raíces verbonominales

pekwenu “¡no golpee!”

(pekwe-nuj

//golpear-PROH//

memya “¡a cantar!”

(mem-ya)

//cantar-INCI//
** El exhortativo va siempre acompañado del imperfectivo.

<!-- page 69 (screenshot 0069) -->
MORFOSINTAXIS
con los morfemas de aspecto. Está formada mínimamente por LEXEMA
+ ASPECTO + MORFEMA MODOPERSONAL. Puede contener igualmente
morfemas pertenecientes a otras categorías gramaticales: otras expresiones
de modalidad, distancia nocional o temporal y la negación. Semánticamente
se refiere a eventos.

La palabra predicativa verbal puede tener como raíz un lexema verbal,
un lexema verbonominal, un lexema cualificativo o un lexema nominal di-
namizado mediante la derivación con el morfema derivativo transpositor
(-yuuj). En todos los casos se entenderá que se refiere siempre a eventos
(acciones o procesos); por lo tanto, cuando se forma con lexemas verbo-
nominales o cualificativos, se trata de la faz dinámica de dichos lexemas.
Ejemplos:

Con lexema verbal

umuth “(yo) tejo”

(um-u-thut

(/tejer-IMPF-1psASER//

umthu “teji”

fum-o-thuj

//tejer-AOR-1psASER//

Con lexema verbonominal

kitek “floreció”

(kite-o-ku)

//florecer- AOR-3psASER.PD//

yatku “hizo casa”

(yat-o-Rul

//casa- AOR-3psASER.PD//

Con lexema cualificativo

walag “creciste”

(vala-g-gul

//crecer- AOR-2psASER//

le'lek “se pudrió”

(le le-g-Rut

(/podrir-AOR-3psASER.PD//

<!-- page 70 (screenshot 0070) -->
MORFOSINTAXIS

La modalidad opcional
En el paradigma de la modalidad opcional están los morfemas [-we-) “mo-
dalidad volitiva” (VOL) y (-weje-) “modalidad desiderativa” (DES). Con la
primera se expresa la intención y con la segunda el deseo de hacer algo; en
este último caso se ve como más lejana la realización del acontecimiento.
Ejemplos:

umweth “quiero tejer”

(um-vé-g-thut

(/tejer- VOL-AOR-IpsASER//

ikhewejeth “quisiera tragar”

(ikhe-weje-9-thuj

//tragar-DES-AOR-1psASER//

thegwejetx “(ellos) quisieran ver”

(theg-véje-o-tx)

//ver-DES-AOR-3ppASER.PD//

Existe otro morfema de modalidad, que se sitúa después del morfema
de flexión modopersonal y que es opcional. Corresponde también a la mo-
dalidad de conocimiento, pero aparece como modalidad suplementaria.
El morfema (-kxij, que advierte de la posibilidad de que lo que se afirma no
sea completamente cierto, es decir, deja un margen de duda, expresa una
incertidumbre (INCER). Ejemplo:

umkukxi “como que ella tejió”

fum-o-ku-kxi)

(/tejer- AOR-3psASER.PD-INCER//
El aspecto
La zona aspectual se divide en dos paradigmas: uno de aparición obligatoria,
en el que se expresa la perfectividad o imperfectividad del acontecimiento, y
otro de aparición opcional, en el que se expresan las diferentes etapas en la
realización del evento.

Los morfemas del paradigma de aparición obligatoria son (-9-) (mor-
fema cero) “aoristo” (AOR, el aspecto no marcado) y (-V-) "imperfecti-
vo” (IMPF). Esta -V- representa una vocal que puede ser cualquiera de las
cuatro vocales básicas de la lengua y que está determinada léxicamente, es
decir, cada raíz verbal se acompaña de una determinada vocal, sin que sea

<!-- page 71 (screenshot 0071) -->
Con lexema nominal dinamizado

nasayuucthu “me estoy volviendo paez”

(nasa-yuu-ç-thu)

//paez-DIN-INT-1psASER//

Los lexemas verbales se clasifican en dos grupos: Lexemas verbales es-
tativos: Us- “estar (eje corporal alargado)”, wp- “estar (eje corporal no alar-
gado)”, ji ph- "tener, jiy- “saber, conocer”, yuh- “venir”. Lexemas verbales
dinámicos: todos los demás.

Los lexemas verbales estativos se combinan en la tercera persona con el
morfema de predicación estativa cuando el aspecto obligatorio es el no mar-
cado, el aoristo”. Ejemplos:

úsa “está”
(ús-o-a't

//estar- AOR-3psASER.PE//
upa “está”
fu'p-g-a')

//estar- AOR-3psASER.PE//
ji pha tiene"
Giph-o-a')

//tener- AOR-3psASER.PE//
jiya “sabe”
Uiy-0-a)

//saber- AOR-3psASER.PE//
yuha “viene”
(yuh-9-a')

//venir- AOR-3psASER.PE//

La palabra verbal está formada por BASE + FLEXIÓN. La base puede es-
tar constituida por el lexema (raíz) más morfemas derivativos. En la flexión
pueden aparecer, además del morfema modopersonal, morfemas de mo-
dalidad no obligatoria, de aspecto —obligatorio y opcional—, de distancia
nocional o temporal, así como el morfema de la negación. Se presentan a
continuación los otros morfemas flexivos del verbo.

* La categoría de aspecto gramatical se presenta más adelante.

<!-- page 72 (screenshot 0072) -->
posible establecer una regla. Hay, sin embargo, una regularidad: cuando la
raíz verbal termina en una consonante palatalizada, el imperfectivo toma la
forma del fonema vocálico /i/. Ejemplos:
Con raíces verbales
umku “tejió”
fum-o-kuj
//tejer-AOR-3psASER.PD//
umuk “teje”
fum-u-kuj
(/tejer-IMPF-3psASER.PD//
ve vgu “hablaste”
(Wwew-o-guj
//hablar- AOR-2psASER//
weweg “hablas”
(Wwew-e-guj
//hablar-IMPF-2psASER//
umutka “yo estoy tejiendo?”
fum-u-tkaj
(/tejer-IMPF-1psINTE//
Con raíces verbonominales
memuth “vo canto"
(mem-u-thul
(/cantar-IMPF-1psASER//
pudgu “(tú) hilaste”
(pud-o-gu)
//hilar-AOR-2psASER//
wakxik  “(éloella) muerde
(wa kx-i-ku)
//morder-IMPF-3psASER.PD//

<!-- page 73 (screenshot 0073) -->
umyáwaya “(ella) ya no más va a tejer”

fum-o-yâwayã-a )

//tejer-AOR-INM-3psASER.PE//

umucyak “(ella) empieza a tejer”

fum-u-cya-kuj

(/tejer-IMPF-INCO-3psASER.PD//

umuça “(ella) está tejiendo”

fum-u-c-a')

(/tejer-IMPF-INT-3psASER.PD//

umyák “(ella) ya tejió”

fum-o-ya-kuj

//tejer-AOR-EXT-3psASER.PD//

Con raíces verbonominales

walayath “va crec?”

(vvala-o-yà-thul

//crecer-AOR-EXT-1psASER//

Con raíces cualificativas

talxyàvvag "te vas a enflaquecer"

(talx-o-yàvva-gu)

//enflaquecer- AOR-PROS-2psASER//

melxyakuk “se envejeció, se gastó (hace ya algún tiempo)”

(melx-9-ya-ku-kuj

//envejecer-AOR-EXT-D2-3psASER.PD//

Como puede verse en los ejemplos de construcción con lexema verbal,
en la tercera persona, cuando el último morfema que aparece antes del mo-
dopersonal es el correspondiente al aspecto exterior o al incoativo, aparece
la predicación dinámica; pero cuando se trata de los aspectos interior, pros-
pectivo e inminente, el morfema modopersonal corresponde a la predica-
ción estativa.

El aspecto iterativo (ITE) se expresa con duplicación de la última sílaba
de la raíz verbal. Ejemplos:

62 En el español regional la construcción ya no más significa “muy pronto”.

<!-- page 74 (screenshot 0074) -->
MORFOSINTAXIS

Con raíces cualificativas

ew-u-ku “se pone bueno”

few-u-kuj

(/(bueno-IMPF-3psASER.PD//

weétku “se volvió sabroso”

(wet-o-ku)

//sabroso- AOR-3psASER.PD//

El paradigma que contiene los morfemas aspectuales que expresan las
distintas fases del desarrollo de un acontecimiento se estructura en la opo-
sición entre el adentro y el afuera del evento”. Para el interior (INT), está el
morfema (-c-) y para el exterior (EXT), el morfema (-ya-). Además de es-
tos morfemas, están el prospectivo (PROS, proyección del acontecimiento)
[-yawa-), que se forma a partir de (-ya-), y el inminente (INM)

(-yawaya-)”, que se forma repitiendo la primera sílaba del morfema pros-
pectivo. El incoativo (INCO), que señala el momento del inicio del evento, se
forma juntando el interior y el exterior: (-gya-). Y el terminativo, la finalización
del acontecimiento, se expresa con el morfema de aspecto exterior (-ya-). Los
aspectos relacionados con el aspecto exterior se combinan con el aoristo y siem-
pre que vaya el aspecto interior aparece el imperfectivo. Las distintas fases del
evento y su marcación aspectual se pueden representar de la siguiente manera:

-yawa- -yawayá- -Cyá- =C- | -yà- >
Figura 3. Estructura del paradigma de aspecto no obligatorio

Ejemplos:

Con raíces verbales

umyáwa “(ella) va a tejer”

fum-0-yawa-a')

(/tejer-AOR-PROS-3psASER.PE//

9. El sistema en la forma como aquí se presenta corresponde a datos de la región de Caldono; en otras
regiones es ligeramente diferente. Puede consultarse Rojas (1998), que lo describe para la región de
Munchique, o Yule (1991b), que lo describe para la región de Toribío.

“ En la región de Munchique aparece un solo morfema, (-yap), que Rojas llama “inminente”; Yule
reporta para Toribío el morfema (-iap), que denomina “incoativo”.

<!-- page 75 (screenshot 0075) -->
MORFOSINTAXIS
yahtath “sacudí (una sola vez)”

(yahta-0-thuj

//sacudir-AOR-1psASER//

yahtatath “sacudí (varias veces)

(yahta-ta-o0-thu)

//sacudir-ITE-AOR-1psASER//

sxúk “chupó (una sola vez)"

(sxú-o-Rut

//chupar-AOR-3psASER.PD//

sxúsxU-9-k “chupó (varias veces)”

(sxú-sxú-g-Rul

//chupar-ITE- AOR-3psASER.PD//

Además de los morfemas gramaticales de aspecto en la palabra predicati-
va, existen los morfemas aspectuales (-naj y (-nxi), que expresan las nocio-
nes de “durativo” (DUR) y “resultativo” (RES), respectivamente. Ejemplos:

umna “tejiendo”

fum-naj

/Itejer-DUR//

umnxi “tejido”

fum-nxi)

/Itejer-RES//

En la zona aspectual, en términos generales, los morfemas del aspecto
externo se combinan con el aoristo y los del aspecto interno, con el imper-
fectivo. Puede darse también la combinación de imperfectivo con aspecto
externo, para referirse a eventos habituales. Ejemplo:

deheyath “ya estoy acostumbrado a dormir”

(deh-e-ya-thu)

//dormir-IMPF-EXT-1psASER//

En la tercera persona se da la distinción entre predicación dinámica
(PD) y predicación estativa (PE). Los verbos dinámicos se combinan con
la PD, tanto si tienen aspecto aoristo como si tienen aspecto imperfectivo.

<!-- page 76 (screenshot 0076) -->
MORFOSINTAXIS

(-ki-) distancia cercana (D1)
(-Tu-) distancia media (D2)
(-ne-t distancia lejana (D3)
Ejemplos:

Con raíces verbales
umkith “tejí (hace poco)”
fum-o-ki-thuj
//tejer-AOR-D1-1psASER//
umkuth “tejí (hace varios días)”
fum-o-ku-thuj
//tejer-AOR-D2-1psASER//
ummekith “no he tejido (pero lo voy a hacer)”
fum-9-me-ki-thuj
//tejer-AOR-NEG-D1-1psASER//
ummekuth “no tejí (y no lo voy a hacer)”
(um-g-me-Ru-thut
(/tejer-AOR-NEG-D2-1psASER//

Con raíces verbonominales
sek-ki-th “yo fui sol (en un juego)”
(sek-ki-thuj)
//sol-D1-1psASER//
putawénetka “debí haber olido”
(puta-we-ne-tkaj
//0ler-VOL-D3-1psSUS//

Con raíces cualificativas
acanekwe “debías de estar enferma”
faca-ne-kwej
//entermo-D3-2ppSUS//

5 El morfema modopersonal de 2.º persona plural se usa también para dirigirse a mujeres con las
que se tiene una relación de familiaridad.

<!-- page 77 (screenshot 0077) -->
Los verbos estativos se combinan con la PE cuando van acompañados del
aoristo y con la PD cuando tienen el morfema de imperfectivo:

Verbo dinámico + AOR + PD um-g-Ru

Verbo dinámico + IMPF + PD um-u-k(u)

Verbo estativo + AOR + PE Ús-g-a

Verbo estativo + IMPF + PD ús-u-k(u)

Si aparece uno de los morfemas aspectuales del paradigma opcional y no
hay morfema de distancia que medie entre el aspectual y el modopersonal,
se da la siguiente combinatoria, independientemente de la clase de verbo de
que se trate:

Base verbal + AOR + EXT +PD um-o-yà-R(u)

Base verbal + IMPF + INCO + PDum-u-çyà-R(u)

Base verbal + IMPF + INT +PE um-u-c-a

Base verbal + AOR + PROS + PE um-o-yàva-a

Base verbal + AOR+INM+PE um-o-yàvayà-a
La distancia nocional o temporal
Otro de los paradigmas flexivos del verbo es el que expresa la distancia exis-
tente con el acontecimiento del cual se habla.

Esta distancia se puede interpretar como una ubicación temporal del
evento en relación con el momento en que se lo enuncia. En este caso, dicha
distancia puede entenderse hacia el pasado o hacia el futuro, dependiendo
de la combinación con los morfemas de modalidad y aspecto.

También puede ser interpretada como una distancia nocional. Por ejem-
plo, al combinarse con la negación las distancias cercana y media: dicha ne-
gación se puede entender como parcial, combinada con la distancia cercana,
o como definitiva, combinada con la distancia media.

El morfema de distancia lejana aparece frecuentemente con la modalidad
suspensiva para expresar suposiciones; este morfema es el que suele apare-
cer en los relatos de la tradición oral, combinado con el modo asertivo, pues
se trata de eventos muy lejanos en el tiempo; por esta razón, no se combina
normalmente con los morfemas de primera o segunda persona. No se ha
encontrado que los morfemas de distancia cercana y media se combinen con
morfemas del modo suspensivo.

Cuando el evento es simultáneo, es decir que no hay distancia entre él y su
enunciación, o cuando se trata de una verdad considerada atemporal, no hay
marca morfológica alguna. Este paradigma está formado por los morfemas:

9%

<!-- page 78 (screenshot 0078) -->
acxakitx “se calentaron (hace poco tiempo)”

facxa-ki-tx)

//calentar-D1-3ppASER.PD//

Cuando aparece un morfema de distancia, independientemente de que
el morfema aspectual sea aoristo o imperfectivo y de que existan en la
palabra verbal otros morfemas —como los del aspecto opcional, por ejem-
plo—, los morfemas de D1 y D2 se combinan con PD y el morfema de D3,
con PE:

Base verbal + aspecto + DI + PD um-u-ki-k(u) um-o-ki-k(u)

Base verbal + aspecto + D2 + PD um-u-ku-k(u) um-9-ku-k(u)

Base verbal + aspecto + D3 + PE um-u-ne-(a) um-9-ne-(a)

La negación

La negación (NEG) se expresa en nasa yuwe con el morfema (-me-), que
se inserta en la palabra predicativa y se ubica entre la zona aspectual y el
paradigma de la distancia modotemporal. En cuanto a su estatuto, no se
puede afirmar categóricamente que se trate de un sufijo flexivo, si bien es
así como funciona en las palabras predicativas, pues dicho morfema puede
actuar también como raíz. Ejemplos:

Como afijo en la palabra predicativa

nasameth “no soy paez”

(nasa-me-thul

//paez-NEG-1psASER//

umucmekik “(él o ella) no estuvo tejiendo”

fum-u-c-me-ki-kuj

(/tejer-IMPF-INT-NEG-DI-3psASER.PD//

weteyawameg “no te vas a caer”

(Wete-9-yawa-me-guj

//caer-AOR-PROS-NEG-2psASER//

Como raíz de palabra predicativa

Kse úsna “está José?”

(Rse-a ús-9-na')

//José-TOP/estar- AOR-3psINTE.PE//

<!-- page 79 (screenshot 0079) -->
Existen, además de la construcción verbal sintética —en una sola pala-
bra—, construcciones llamadas analíticas, que son las que se forman con
estructuras de auxiliaridad. Esta construcción es también predicativa.

La construcción analítica se hace con los verbos (ús-) y (wWp-), que funcio-
nan como auxiliares (posicionales), y las formas resultantes de la afijación de
los morfemas aspectuales (-na) “durativo” y (-nxi) “resultativo”, que funcio-
nan como verbos auxiliados. Estos verbos auxiliados contienen la informa-
ción acerca del evento de que se trate. Los dos verbos que funcionan como
auxiliares están dentro de los clasificados como estativos. Adicionalmente al
significado de “estar”, dan cuenta de la posición corporal de la entidad de la
cual se predica algo”. El verbo (ús-) funciona como genérico, cuando no se
quiere dar la información posicional o esta no es relevante. Ejemplos:

umna upa “está tejiendo (sentada)”

(um-na u'p-g-a)

//tejer-DUR/estar- AOR-3psASER.PE//

umnxi úsa “está tejido”

fum-nxi ús-o-a

//tejer-RES/estar- AOR-3psASER.PE//

La diferencia entre la forma analítica con durativo y la forma sintética
con aspecto interno, que se glosan ambas al español como “estar + gerun-
dio” se explica así: con la forma sintética se refiere a un evento que está
en curso, por ejemplo, cuando una persona está tejiendo una ruana, pues
la tiene montada en el telar y ya ha empezado a tejerla, o se encuentra en
proceso de tejer una mochila. La forma analítica se usa para decir que la
persona está o ha estado efectivamente tejiendo de pie frente al telar o sen-
tada haciendo la mochila; en esta forma intervienen los verbos auxiliares
como posicionales.

El nombre
El nombre puede ser predicativo, cuando tiene el morfema modopersonal, o
no predicativo, cuando cumple en la oración funciones argumentales.

El nombre en función predicativa está formado por LEXEMA + GRAME-
MA MODOPERSONAL. Los lexemas que pueden formar un nombre directa-
mente con el morfema modopersonal son los nominales, los verbonomina-
% Este asunto y todo lo relacionado con la localización se desarrollan detalladamente en Rojas y

Ramos (2004-2005).

<!-- page 80 (screenshot 0080) -->
MORFOSINTAXIS
me-a “no está”

íme-al

//NEG-3psASER.PE//

Cuando aparece el morfema de negación sin que haya un morfema de
distancia, es decir que queda contiguo al morfema modopersonal, e inde-
pendientemente de lo que se tenga en la zona aspectual, se combina siempre
con la predicación estativa.

Base verbal + aspecto + NEG + PE um-9-me-(a) um-u-me-(a)

Cuando el morfema de la negación se combina con el morfema de dis-
tancia cercana (-ki-), se entiende como una negación provisional; cuando
se combina con el morfema de distancia mediana (-ku-), dicha negación se
entiende como definitiva. Ejemplos:

mjiyawamekith “no voy a trabajar (ahora, pero sí más tarde)”

(mji-0-yawa-me-ki-thuj

(/trabajar- AOR-PROS-NEG-D1-1psASER//

mjiyawamekuth “no voy a trabajar (definitivamente)

(mji-0-yawa-me-ku-thuj

(/trabajar- AOR-PROS-NEG-D2-1psASER//

Se recuerda que los lexemas verbales pueden ir acompañados de los mor-
femas derivativos (ya -) “reflexivo, (ka-) “factitivo” y (puutx-) o fpuukx-)
“recíproco”; estos morfemas modifican la valencia del verbo.

La totalidad de los morfemas que pueden ir en la palabra predicativa ver-
bal es:

(REF) + (FACT) + raíz + (modalidad opcional) + aspecto + (aspecto) +
(NEG) + (D) + MPN + (modalidad suplementaria).
Y la fórmula mínima de la palabra verbal en la construcción sintética es:
Base + Aspecto (paradigma obligatorio) + MPN
5 Se escriben entre paréntesis los paradigmas que no son obligatorios.

<!-- page 81 (screenshot 0081) -->
MORFOSINTAXIS
les y los cualificativos; los lexemas verbales pueden hacerlo siempre y cuan-
do vayan acompañados por el morfema derivativo transcategorial (-sa), que
los nominaliza. Ejemplos:

Con lexema nominal
nasath “soy gente / soy paez”
(nasa-thuj
//gente o paez-1psASER//
sxitana “como que es armadillo”
(sxita-nal
//armadillo-3psSUS.PE//
musxkag “eres blanco”
(musxka-gu)
//blanco-2psASER//

Con lexema verbonominal
kwehne “es relámpago”
(kwehne-a')
//relámpago-3psASER.PE//
yúsga “estás triste?”
(yús-ga)
/Itriste-2psINTE//

Con lexema cualificativo
talxthu “estoy flaco”
(talx-thul
//flaco-1psASER//
wala “es/está grande”
(vvala-a'
//grande-3psASER.PE//

Con lexema verbal nominalizado
mjisa "es trabajador"
ímji-sa-a'l
(/trabajar- NOM-3psASER.PE//

<!-- page 82 (screenshot 0082) -->
Es necesario anotar aquí que, si bien no es un hecho muy frecuente, los
morfemas de distancia pueden combinarse también con lexemas nominales.
Esto puede verse en el ejemplo que se da a continuación, tomado de un rela-
to de la tradición oral; en él el morfema de distancia lejana (-ne-) indica una
distancia temporal muy grande, pues se refiere a hechos muy antiguos que
se conocen por tradición oral.

sxitayu nasa knasane “el armadillo fue una jovencita paez”

(sxita-yu” nasa Rna'sa-ne-a'l

//armadillo-ENF/paez/jovencita-D3-3psASER.PE//

En este otro ejemplo, el morfema (-ne-) se combina con el de modo sus-
pensivo para expresar una suposición:

nasanena “como que es gente”

ínasa-ne-nat

//gente-D3-3psSUS.PE//
El caso morfológico
Se ha dicho que el nombre, además de la función predicativa, puede cum-
plir en una oración funciones argumentales; cuando cumple dichas funcio-
nes, estas se indican mediante un morfema flexivo que va como sufijo. Estos
morfemas son:

[-a's) “objeto (acusativo-dativo) singular” (OBJ)*

[-txis) “objeto (acusativo-dativo) plural” (OBJpl)

(ji) “benefactivo”

[-yakh) “sociativo o comitativo” (SOC)

(uh) “instrumental” (INS)

(-tel “inesivo (eje corporal vertical o no marcado)” (INE)

(ka) “inesivo” (eje corporal horizontal) (INEh)

(-sut “inesivo” (eje corporal ligeramente inclinado) (INE1)”

[-khe) — “inesivo (eje corporal pendiente o fuertemente inclinado) (INEp)

(-nal “alativo (a, hacia)” (ALA)

(jul “elativo (de, desde)" (ELA)
% Como este morfema cubre tanto el acusativo como el dativo, que corresponden a los objetos

directo e indirecto, se ha denominado “objeto”.
% Este morfema puede entenderse también como “mediativo”, ejemplo: yu'-su “por el agua”.

<!-- page 83 (screenshot 0083) -->
Mlixayakh wewgu “hablaste con María”
(Mlxia-yakh wew-o-guj
//María-SOC/hablar- AOR-2psASER//
Selsu klatxis yackipuk “Celso arreó las vacas”
fSelsu-a' Rla-txis yackipu-o-kuj
(/Celso- TOP/vaca.OBJpl/arrear- AOR-3psASER.PD//
Con lexemas verbonominales
kwetuh pekwek “golpeó con la piedra”
(kwet-uh pekwe-o-kuj
//piedra-INS/golpear- AOR-3psASER.PD//
kite wetek “la flor se cayó”
(kite-a wete-o-kuj
//flor-TOP/caer-AOR-3psASER.PD//
bekas tugxthu “tomé chicha”
(beka-a's tugx-0-thuj
//chicha-OBJ/tomar-AOR-1psASER//
Con lexemas verbales
mjisa's thegthu “vial trabajador”
(mji-sa-as theg-o-thuj
//trabajar-NOM-OBJ/ver-AOR-1psASER//
umsayakh wewgu “hablaste con la tejedora”
(um-sa-yakh wew-o-gu)
//tejer-NOM-SOC/hablar-AOR-2psASER//
Con lexemas cualificativos
nxiisxsa wetek “el gordo se cayó”
ínxiisx-sa-a vvete-g-Xut
(/gordo-NOM-TO P/caer- AOR-3psASER.PD//
wa lxsas ya ja pesku “(ella) regaló una mochila al perezoso”
(Walx-sa-as yaja pes-0-kuj
//perezoso-NOM-OBJ/mochila/regalar- AOR-3psASER.PD//

<!-- page 84 (screenshot 0084) -->
MORFOSINTAXIS

El nominativo no tiene una marca morfológica propia, se identifica por-
que aparece al inicio de la oración y suele ir acompañado por el morfema
topicalizador (-2'+. El morfema de “objeto” corresponde a acusativo y dativo;
el morfema funciona como indicador de acusativo cuando solo aparece un
objeto y como indicador de dativo cuando aparecen dos, caso en el que el
objeto directo no lleva marca morfológica alguna. Nótese que, si bien en la
lengua no hay una flexión obligatoria de número en el nombre, que distinga
entre singular y plural, en la marca de objeto sí se establece dicha diferencia.
El benefactivo indica que una entidad tiene o le está destinada una posesión.
El sociativo indica que un participante acompaña al agente a realizar la ac-
ción. El instrumental señala el instrumento que usa el agente para llevar a
cabo una determinada acción. Los locativos indican una localización espa-
cial de un hecho o una entidad. Hay cuatro morfemas con valor de inesivo
(“en”), uno con valor de alativo (“a, hacia”) y uno con valor de elativo (“de,
desde”). Los cuatro morfemas con valor de inesivo informan adicionalmen-
te sobre el eje corporal de la entidad situada espacialmente; el morfema Í-te)
funciona también con valor genérico cuando no se quiere dar la informa-
ción específica o si ella es irrelevante.

Los morfemas de caso se combinan directamente con lexemas nominales
y verbonominales; los lexemas verbales y cualificativos necesitan de un pro-
ceso de derivación (transcategorial) para recibirlos. Ejemplos:
Con lexemas nominales

Kse misxas thegku “José vio al gato”

(Rse-a' misx-as theg-o-kuj

//José-TOP/gato-OBJ/ver-AOR-3psASER.PD//

yuzuh umku “tejió con la aguja”

(yuz-uh um-o-Rui

//aguja-INS/tejer- AOR-3psASER.PD//

yatte usta “están en la casa”

(yat-te us-tal

(/casa-INE/estar-3ppASER.PE//

yatju yuha “viene de la casa”

(yat-ju yuh-a')

//casa-ELA/venir-3psASER.PE//

<!-- page 85 (screenshot 0085) -->
MORFOSINTAXIS

Se recuerda que el nombre puede tener también morfemas derivativos,
que fueron presentados en el capítulo de Morfologia.
Sintagma nominal
El nombre puede actuar como núcleo de un sintagma, al ir acompañado por
otras palabras que actúan como determinantes o como modificadores. Se
entiende sintagma como un grupo de palabras que presenta la estructura
NÚCLEO + DETERMINANTES o MODIFICADORES y que puede cumplir, de
manera unitaria, una función sintáctica del nivel oracional".

Determinantes son en este caso las palabras que al acompañar al nom-
bre concretan sus posibilidades referenciales; la determinación se da tanto
por palabras gramaticales como por palabras léxicas. El sintagma nominal
puede ser reemplazado en todos los casos por un nombre o un pronombre.
El sintagma nominal puede cumplir en la oración funciones actanciales o
circunstanciales, para lo que lleva sufijada la correspondiente marca morfo-
lógica de caso. Puede también cumplir la función predicativa y recibir para
ello el morfema modopersonal.
Determinación gramatical
Como determinantes gramaticales aparecen los demostrativos, los cuantifi-
cadores —indefinidos y numerales— y los pronombres personales tomados
como posesivos; los determinantes gramaticales preceden al núcleo, lo que
da como resultado el orden DETERMINANTE - DETERMINADO para este
tipo de construcción. Ejemplos:
Demostrativo + nombre

na tub “esta paloma”

na tuba cxihme “esta paloma es blanca”

(na tub-a cxihme-a')

/DEM1/paloma-TOP/blanco-3psASER.PE//
Cuantificador + nombre

sena nasa “mucha gente”

sena nasa Usa “hay mucha gente”

(sena nasa-a Ús-g-at
$$. Las funciones se tratan en el capítulo 5, Sintaxis.

<!-- page 86 (screenshot 0086) -->
MORFOSINTAXIS
alku juna “perro bravo”

alku junas theguth “veo al perro bravo”

(alku juna-a's theg-u-thuj

//perro/bravo-OB]J/ver-IMPF-1psASER//

La determinación con el nombre expresa una relación de genitivo y sigue
el mismo orden de la determinación gramatical: DETERMINANTE - DETER-
MINADO. Semánticamente se pueden expresar con este mecanismo sin-
táctico diversas relaciones: posesión, parentesco, materia, tema, contenido,
parte de un todo, etc. Ejemplos:

Lamus jiba “caballo de Ramos”

Lamus jiba' habxa “el caballo de Ramos es arisco"

(Lamus jiba-ad' habx-a'l

//Ramos/caballo-TOP/arisco-3psASER.PE//

ape tasx “mata de auyama”

ape tasxa kitek “la mata de auyama floreció”

(ape tasx-a kite-o-kuj

//auyama/mata-TOP/florecer-AOR-3psASER.PD//

Kse ney “padre de José”

Kse neya tuhmetuhme” — “el padre de José está canoso”

(Rse ney-a tuhme-tuhme-a't

(/José/padre- TOP/gris-gris-3psASER.PE//

atx umsa "tejedora de ruanas"

Mixia atx umsa “María es tejedora de ruanas”

(MIxia-a' atx um-sa-a Yº

//María-TOP/ruana/tejer-NOM-3psASER.PE//

sagu jemplu “cuento de la sopa”

79 En este ejemplo, el nombre que actúa como determinante es un verbo nominalizado.

<!-- page 87 (screenshot 0087) -->
//mucho/gente-TOP/estar-AOR-3psASER.PE//

tekh knasa “tres jovencitas”

tekh knasa-a” memtx “cantaron tres jovencitas”

[tekh knasa-a mem-o-txt

//tres/jovencita- TOP/cantar- AOR-3ppASER.PD//

Pronombre personal (posesivo) + nombre

ukwe kahka “mi tío materno”

Peklu ukwe kahka “Pedro es mi tío materno”

(Pellu-a u Rvve kahka-2')

//Pedro-TOP/yo(fem)/tío materno-3psASER.PE//

igx yaja “tu mochila”

igx yaja zxicxkwe “tu mochila es bonita”

figx ya ja-a' zxiexkwe-a')

(tú(masc)/mochila-TOP/bonita-3psASER.PE//

Cuando el poseedor es la tercera persona del singular, el pronombre per-
sonal —que es en realidad el demostrativo distal txà o Rxà “ese/esa” — recibe
el sufijo “benefactivo” -ji”. Ejemplo:

txãji yat “su casa (de él o de ella)”

txaji yatna wjectkhaw “como que vamos a la casa de él”

[txá-ji yat-na Wj-e-c-tkhaw)

/él/ella-BEN/casa-ALA/ir-IMPF-INT-1ppSUS//

Determinación léxica
Las palabras léxicas cualificativo y nombre pueden también funcionar como
determinantes del nombre y formar con él un sintagma nominal.

La determinación con cualificativo se da en el orden DETERMINADO -
DETERMINANTE. Ejemplo:

Una hipótesis sobre esta marca es que se trate de una forma abreviada del verbo ji' ph- “tener”.

<!-- page 88 (screenshot 0088) -->
sagu jemplu's hikutx “dijeron el cuento de la sopa”

(sagu jemplu-'s hi-0-ku-txj

//sopa/cuento-OBJ/decir- AOR-D2-3pp ASER.PD//

beka yat “chichería (casa de la chicha)”

beka yatte upta “están en la chichería”

(beka yat-te u'p-g-ta)

//chicha/casa-INE/estar- AOR-3ppASER.PE//

yu k fxtú ec “hoja de árbol de montaña”

na yu k fxtú eca “esto es (una) hoja de árbol de montaña”

(na-a yu k fxtú eç-a' +

//esto- TOP/montafia/àrbol/hoja-3psASER.PE//

El sintagma puede estar formado por un determinante gramatical, un
nombre y un cualificativo. Ejemplo:

na yaja wala “esta mochila grande”

na yaja wala' zxicxkwe “esta mochila grande es bonita”

(na yaja vvala-a' zxicxkwe-a')

//DEM1/mochila/grande-TOP/bonita-3psASER.PE//

O por un determinante gramatical, un nombre (modificador) y otro
nombre (núcleo). Ejemplo:

na Tmigu nxiisa “esta hija de Domingo”

na Tmigu nxiisa's wedxith “yo quiero a esta hija de Domingo”

(na Tmigu nxiisa-a's wedx-i-thuj

//DEM1/Domingo/hija-OBJ/querer-IMPF-1psASER//

jez beka mitx “dos ollas de chicha”

jez beka mitxa ústa “hay dos ollas de chicha”

(jez beka mitxa s-o-ta)

//dos/chicha/olla-TOP/estar- AOR-3pp ASER.PE//

<!-- page 89 (screenshot 0089) -->
MORFOSINTAXIS

En el sintagma nominal pueden aparecer dos o más determinantes gra-
maticales. Ejemplo:

na u kwe ez luuçx walasa “estos mis dos hijos grandes”

na ukwe ez luuçx vvalasa' nasa yuwes wewetx

(na u'kwe ez luuçx wala-sa-a' nasa yuwe-'s wew-e-txj

//DEM1/yo(fem)/dos/niño/grande-NOM-TOP/paez/lengua-OBJ/

hablar-IMPF-3ppASER.PD//

“estos mis dos hijos grandes hablan lengua páez”
Otras clases de palabras
Además del verbo y el nombre, se encuentran los deícticos, las palabras cua-
lificativas y los conectores.
Deícticos
En correspondencia con las tres categorías deícticas —la persona, el espacio
y el tiempo— existen deícticos personales, espaciales y temporales, que fue-
ron presentados en el capítulo 3 dentro de los morfemas gramaticales. Todos
ellos pueden funcionar como núcleo de una palabra predicativa, tal como se
muestra en los ejemplos que ilustran las palabras predicativas con gramema
como núcleo, en el capítulo de Morfologia.

Los deícticos espaciales y temporales cuando están cumpliendo funcio-
nes circunstanciales no se presentan como palabras predicativas. Ejemplos:

ayte ústa “aquí están”

(ay-te ús-o-ta |

//cerca-INE/estar- AOR-3ppASER.PE//

kuskaya mjiyàvvatha'vv “mañana vamos a trabajar”

(kuskay-a mji-0-yawa-thaw)

//mañana-TOP/trabajar- AOR-PROS-1ppASER//
Palabra cualificativa
Los lexemas cualificativos pueden formar palabras predicativas, tanto nomi-
nales como verbales, como se ha mostrado ampliamente al tratar el nombre
y el verbo. Existe la palabra cualificativa no predicativa. Esto se da cuando
el cualificativo funciona como modificador semántico de un nombre dentro
de un sintagma nominal; en este caso aparece el lexema como forma libre.
Ejemplos:

<!-- page 90 (screenshot 0090) -->
MORFOSINTAXIS
claramente en la tercera persona: la predicación dinámica y la predicación
estativa.

En cuanto a los lexemas de la lengua, los lexemas nominales tienden a ser
núcleo de palabras predicativas nominales, mientras los verbales lo son de
palabras predicativas verbales. Los lexemas de «vocación doble» —verbono-
minales y cualificativos— pueden funcionar indistintamente con una u otra
clase de palabras predicativas. Siempre es posible tomar un lexema nominal
y dinamizarlo —verbalizarlo— para que pueda funcionar como núcleo de
palabra predicativa verbal, así como nominalizar un lexema verbal para que
pueda ser núcleo de palabra predicativa nominal.

Cuando se trata de formar las palabras nominales no predicativas, es decir,
cuando el nombre está en función actancial, los lexemas verbales y los cuali-
ficativos necesitan el sufijo derivativo transpositor que los nominaliza, mien-
tras los lexemas nominales y verbonominales pueden hacerlo directamente.

Como se hace evidente, entonces, este criterio de predicatividad tiene un
papel central en la clasificación de las palabras de la lengua.

El nasa yuwe combina características de lengua flexiva, tanto en el ám-
bito de lo nominal como de lo verbal, y de lengua aglutinante, sobre todo
en la palabra verbal. Presenta declinación del nombre y reúne en el verbo
paradigmas en los que se expresan las categorías de persona, número, mo-
dalidad y aspecto. Entonces, está presente el procedimiento morfológico de
la flexión tanto en el nombre como en el verbo. La tendencia aglutinante en
el verbo se da en tanto la palabra verbal puede estar constituida hasta por
ocho o diez morfemas.

A continuación se presenta un resumen de lo expuesto en relación con
las clases de palabras, su calidad de predicativas o no y la manera como se
construyen en cada caso.

VERBO. Es siempre predicativo. Predica acciones, procesos o estados.

Tabla 10. Formación del verbo
V + aspecto + MPN
VN + aspecto + MPN
Q + aspecto + MPN
N + yuu + aspecto + MPN

NOMBRE. Puede ser predicativo o no. Predica identidad o propiedad.

Como no predicativo cumple funciones actanciales.

<!-- page 91 (screenshot 0091) -->
lku khuçx “perro negro”

a

/perro/negro/

atx duh “ruana pesada”

/ruana/pesada/

Pero si el sintagma nominal que contiene una palabra cualificativa cum-

ple la función predicativa, entonces será la palabra cualificativa la que lleve
el morfema de la predicación, morfema que incide en este caso en el sintag-
ma completo. Ejemplo:

na atx duha “esto es (una) ruana pesada”

ína-a atx dubh-a

//DEM1-TOP/ruana/pesada-3psASER.PE//

La palabra cualificativa también puede actuar como modificador semánti-
co de una palabra predicativa; en este caso precede a dicha palabra. Ejemplo:

ew wewku “habló bien”

few wew-o-kuj

//bien/hablar- AOR-3psASER.PD//

Las palabras cualificativas tienen el mecanismo de la duplicación, que
da como resultado semántico una atenuación. Ejemplos: beh “rojo” beh-
beh “rosado”; lem “amarillo” lemlem “amarillo pálido”; u'se "nuevo, u"seu'se
“casi nuevo”.

Conectores
Los conectores son las únicas palabras que no pueden ser centro de pre-
dicado y por lo tanto aparecen siempre como palabras no predicativas.
Son, entre otros, Riçxa “entonces”, txaju “entonces, así que”, sa” “y”, napa
“pero” meeçxa “tal vez, txa wi "así, entonces", aga” o agyu “entonces,
así que”.
A manera de recapitulación
Como ha podido verse, el nasa yuwe es una lengua omnipredicativa: casi
todas sus palabras pueden asumir la función predicativa en una oración.
Tiene, adicionalmente, dos clases de predicación que se diferencian

<!-- page 92 (screenshot 0092) -->
Tabla 11. Formación del nombre
Predicativo No predicativo
N + MPN N+CM
VN + MPN VN +CM
Q + MPN Q + sa + CM
V+sa+MPN = V +sa+ CM
CUALIFICATIVO. Cuando no es predicativo, actúa como modificador
semántico de nombres o verbos. Se construye con el solo lexema: Q.
DEÍCTICO. Puede ser predicativo o no predicativo. Como no predicativo
cumple funciones actanciales o circunstanciales.
Tabla 12. Formación de los deícticos
Predicativo No predicativo
D + MPN D+ CM
CONECTORES. No predicativos. Se construyen con el morfema: C.

# Capítulo 5 — Sintaxis
<!-- ocr -->

<!-- page 93 (screenshot 0093) -->
CAPÍTULO 5
SINTAXIS

El presente capítulo trata de la oración. Se considera que la oración es tanto
la unidad básica como el ámbito máximo del nivel sintáctico; la oración es
igualmente la sede de la predicación —abordada en el capítulo 4—. Sus di-
ferentes funciones —sintácticas, semánticas e informativas— se presentarán
en el presente apartado, avanzando hacia la descripción de las diferentes
clases de oraciones de la lengua, partiendo de la clasificación sintáctica e
intercalando las clasificaciones que se hacen con criterio semántico.

Como se ha visto en el capítulo precedente, en nasa yuwe una sola pala-
bra predicativa reúne los dos elementos de la relación predicativa: el lexema,
núcleo de la palabra, es el elemento determinativo principal, lo que se pre-
dica; el morfema modopersonal es el índice actancial, elemento referencial
que representa la base de predicación. Así, existe en la lengua la palabra-ora-
ción: una palabra predicativa puede constituir por sí sola una oración. Pero
la oración puede contener además otros elementos.

Se entiende oración como una estructura proposicional acompañada de
la formulación del hablante. La estructura proposicional contiene los ele-
mentos de la relación predicativa —predicado y base de predicación—; la
formulación del hablante se expresa por medio de la modalidad.

Según la formulación del hablante y su manifestación formal, las oracio-
nes del nasa yuwe se dividen en declarativas y no declarativas. En atención
al nivel de complejidad de su estructura, las oraciones se dividen en simples,
compuestas y complejas. Se presentan las clases sintácticas de oración en
ese orden.

<!-- page 94 (screenshot 0094) -->
SINTAXIS
excepto los conectores, con los deícticos espaciales —que se forman con dos
o tres morfemas— y con el morfema de la negación.

En nasa yuwe hay predicados estativos y dinámicos. Hay predicación con
aspecto y predicación sin aspecto. Cuando está ausente la categoría grama-
tical de aspecto, el predicado es siempre estativo. Cuando está presente la
categoría de aspecto, puede ser estativo o dinámico, dependiendo de la com-
binatoria de morfemas que contenga la palabra predicativa.

Los predicados sin aspecto pueden tener como núcleo un lexema nomi-
nal, un lexema verbonominal, un lexema cualificativo o un lexema verbal
nominalizado. Ejemplos:

Con lexema nominal

nasa “es paez”

ínasa-a't

//paez-3psASER.PE//

Con lexema verbonominal

kwehnena “como que es (un) relámpago”

(kwehne-naj

//relámpago-3psSUS.PE//

Con lexema cualificativo

talxna “es flaco?”

(talx-na't

(/flaco-3psINTE.PE//

Con lexema verbal nominalizado

kapiyasa “es profesor”

(ka-piya-sa-a”)

//FACT-aprender-NOM-3psASER.PE//

Estos predicados se pueden construir igualmente con gramemas libres:
demostrativos, deícticos espaciales, deícticos temporales, interrogativos y
cuantificadores. Ejemplos:

Con demostrativo

na “es este”

ína-al

//DEM1-3psASER.PE//

<!-- page 95 (screenshot 0095) -->
FUNCIONES

Se entiende por función sintáctica el papel que cumplen los constituyen-
tes de la oración dentro de su marco estructural. Se trata de relaciones que
contraen entre ellos los elementos presentes en una estructura oracional
en tanto son componentes de una unidad, que es la oración. Como fun-
ciones sintácticas del nivel oracional se identifican la función predicativa,
el sujeto, el complemento u objeto directo, el complemento u objeto indi-
recto y los complementos circunstanciales —locativo, temporal, sociativo,
instrumental, etcétera—.

La función semántica, también llamada papel semántico o rol actan-
cial, se refiere al papel que cumplen las entidades involucradas en un even-
to. Hasta ahora no ha sido posible establecer una lista única y definitiva
de las funciones semánticas, esto se encuentra en elaboración actualmente
en la teoría lingúística. Sin embargo, se han identificado algunas como las
más frecuentes: agente —el que hace la acción—, paciente o tema —el que
recibe los efectos de una acción o es afectado en un determinado evento—,
destinatario —la tercera entidad involucrada en la matriz actancial básica
de un evento, entidad a la cual está destinada la acción—, beneficiario
—entidad en cuyo beneficio se hace una acción—, sociativo o comitati-
vo —la entidad que acompaña a otra en un evento—, instrumental —el
objeto o instrumento del cual se vale el agente para hacer una acción—.
Se consideran también funciones semánticas la localización espacial y
temporal de un evento.

En las funciones sintácticas es conveniente distinguir entre argumentos
y adjuntos. Los primeros son los que el verbo selecciona según su valen-
cia: el sujeto, el objeto directo y el objeto indirecto. Un verbo de valencia
1 selecciona un sujeto, sea este agente o paciente; un verbo de valencia 2
normalmente selecciona un sujeto y un objeto directo; un verbo de valencia
3 selecciona además un destinatario. Los verbos que se refieren a ubicación
espacial requieren de una indicación de lugar entre sus argumentos. Las
otras informaciones que pueden aparecer, pero que no son requeridas por el
verbo, son los adjuntos: complementos circunstanciales de tiempo, de lugar,
de compañía, de instrumento, etcétera.

El constituyente que cumple la función predicativa es el elemento nu-
clear de la oración y, como se ha planteado, su sola presencia es suficien-
te para que exista la oración. En adelante se le denominará predicado.
Tal como se mostró en el capítulo 4, todos los lexemas pueden recibir el
morfema de la predicación y constituir una palabra predicativa que cumpla
esta función. Esto sucede igualmente con los morfemas gramaticales libres,

<!-- page 96 (screenshot 0096) -->
Con deíctico espacial

ayte “es aquí”

fay-te-d'l

//cerca-INE-3psASER.PE//

Con deíctico temporal

acxha “es hoy”

(açxh-a'

//hoy-3psASER.PE//

Con interrogativo

kimna “¿quién es?

(kim-na)

//quién-3psINTE.PE//

Con cuantificador indefinido

jxuka “es todo”

(jxuka-a')

//todo-3psASER.PE//

Con cuantificador numeral

tekhta “son tres”

Ttekh-taj

//tres-3ppASER.PE//

Es también esta la clase de predicado que se construye con el morfema de
negación como núcleo y que se da como respuesta a alguna pregunta (total
o absoluta). Ejemplo:

mea “(es) no”
(me-a')
//NEG-3psASER.PE//

Los predicados con aspecto pueden tener como núcleo un lexema ver-
bal, un lexema verbonominal, un lexema cualificativo o un lexema nominal
dinamizado. Ejemplos:

Con lexema verbal
umuk “teje”

<!-- page 97 (screenshot 0097) -->
SINTAXIS
fum-u-kuj
(/tejer-IMPF-3psASER.PD//
Con lexema verbonominal

sekuk “hace sol”

(sek-u-ku)

(/sol-IMPF-3psASER.PD//

Con lexema cualificativo

lemku “amarilleó”

(lem-o-Ru y

//amarillo- AOR-3psASER.PD//

Con lexema nominal dinamizado

knasayuuyák “ya se hizo señorita”

(knasa-yuu-ya-kuj

//jovencita-DIN-EXT-3psASER.PD//

En los ejemplos anteriores se trata de predicados dinámicos. Los predi-
cados estativos con aspecto se presentan cuando el morfema que precede al
gramema modopersonal es el de la negación (NEG), el morfema de distan-
cia lejana (D3) o los aspectos interior (INT), prospectivo (PROS) e inminen-
te (INM). Ejemplos:

Con la negación

wa kxmea “no muerde”

(wa kx-o-me-a

//morder-AOR-NEG-3psASER.PE//

Con la distancia lejana

puucnena “como que le dio de comer”

(puuç-g-ne-na)

//dar de comer-AOR-D3-3psSUS.PE//

Con el aspecto interior

lemuca “se está amarilleando”

(lem-u-c-a')

//amarillo-IMPF-INT-3psASER.PE//

<!-- page 98 (screenshot 0098) -->
Con el aspecto prospectivo

weteyawa “se va a caer”

(vete-o-yàva-a'l

//caer-AOR-PROS-3psASER.PE//

Con el aspecto inminente

mjiyáwaya “ya no más va a trabajar”

(mji-o-yàvayà-a')

(/trabajar- AOR-INM-3psASER.PE//

Los verbos estativos se combinan con la predicación estativa cuando van
con el aoristo, lo que da un valor temporal de presente, y con la predicación
dinàmica cuando van con el imperfectivo, lo que da un valor temporal de
pasado. Ejemplos:

jipha tiene"

Gi ph-o-a)

(/tener-AOR-3psASER.PE//

jiphuk “tuvo”

ti ph-u-kuj

//tener-IMPF-3psASER.PD//

Existen también predicados que consisten en un sintagma verbal forma-
do por un verbo auxiliar (posicional) y un verbo auxiliado. Ejemplos:

fxinxi úsa “está escrito”

(fxi-nxi ús-o-a |

//escribir-RES/estar-AOR-3psASER.PE//

pudna u'pa “está hilando (sentada)”

(pud-na up-9-a')

//hilar-DUR/estar- AOR-3psASER.PE//

Para las funciones argumentales se tendrá en cuenta la relación que
las funciones sintácticas tienen con las funciones semánticas o roles ac-
tanciales.

La función de sujeto gramatical corresponde al participante al que se le
da realce mediante su representación en la persona —correspondiente a la
base de predicación— expresada en el morfema de la predicación. Además

<!-- page 99 (screenshot 0099) -->
Paciente de proceso

ape tasxa kitek “la mata de auyama floreció”

(ape tasx-a kite-o-ku)

//auyama/mata-TOP/florecer- AOR-3psASER.PD//

Agente de acción-proceso

alku cxidas tecxik “el perro lame el pie”

falku-a' cxida-a's tecx-i-kuj

//perro-TOP/pie-OBJ/lamer-IMPF-3psASER.PD//

También, mediante la prefijación del morfema reflexivo, se puede hacer
una correferencia entre los roles del participante activo y el participante pa-
sivo de un evento, es decir, una misma entidad cumple las dos funciones
semánticas. Con este mecanismo, igualmente, puede funcionar como sujeto
el participante pasivo —paciente semántico— sin que se nombre al partici-
pante activo —agente semántico—. Ejemplos:

Correferencia de agente y paciente

agxa ya wa kxkuth “yo me mord?”

fagx-a ya -wakx-o-ku-thuj

(/yo(masc)-TOP/REF-morder-AOR-D2-1psASER//

alku yatecxik “el perro se lame (a sí mismo)”

(alku-a' ya -tecx-i-ku)

//perro-TOP/REF-lamer-IMPF-3psASER.PD//

Paciente como sujeto sin mención del agente

yata ya paduk “la casa se barre (alguien la barre)”

(yat-a' ya -pad-u-kuj

(/casa-TOP/REF-barrer-IMPF-3psASER.PD//

agxa yuyith “me dejo pegar (alguien me pega)”

(agx-a ya -uyi-i-thuj

//yo(masc)-TOP/REF-pegar-IMPE-1psASER//

Las funciones de objeto directo y de objeto indirecto aparecen también
expresadas por palabras nominales, que se refieren a entidades involucra-
das en los eventos. El directo corresponde al participante pasivo —paciente
7 Esto puede traducirse también por: “se deja barrer”.

<!-- page 100 (screenshot 0100) -->
SINTAXIS
de su expresión en la palabra predicativa, se puede explicitar léxicamente
mediante un nombre, un pronombre o un sintagma nominal; esta explicita-
ción léxica del sujeto va normalmente acompañada del morfema topicaliza-
dor (-a'+. Ejemplos:

Peklu” kásekik “Pedro descanso”

(Peklu-a' kase-0-ki-kuj

//Pedro-TOP/descansar- AOR-D1-3psASER.PD//

wkwe mjikith “yo trabajé”

fu kwe-a mji-o-ki-thu)

//yo(tem)-TOP/trabajar- AOR-D1-1psASER//

txá misxa pebek “ese gato chilla”

(txá misx-a peb-e-kuj

//ese/gato-TOP/chillar-IMPF-3psASER.PD//

atx txitxa duha “la ruana mojada está pesada”

fatx txitx-a duh-a)

//ruana/mojada-TOP/pesado-3psASER.PE//

El sujeto corresponde al participante único de una predicación atributiva,
al participante único de un evento monoactancial —acción o proceso” — y
al participante activo de un evento diactancial —acción-proceso—, es decir,
el agente semántico. Ejemplos:
Predicación atributiva

Mlxia zxicxkwe “María es bonita”

(Mlxia-a' zxicxkwe-a')

//María-TOP/bonita-3psASER.PE//
Agente de acción

txá alku vxihkna úsa “ese perro está ladrando”

(txà alku-a' vxihk-na ús-g-a'

//DEM2/perro-TOP/ladrar-DUR/estar- AOR-3psASER.PE//
7 En la acción participa un agente —activo— y en el proceso participa un paciente —pasivo—.

En el evento diactancial participan tanto un agente como un paciente.

<!-- page 101 (screenshot 0101) -->
SINTAXIS
semántico— en un evento que involucre también a un participante activo,
siempre y cuando la función de sujeto corresponda a dicho participante
activo; el objeto directo corresponde al caso acusativo. El indirecto corres-
ponde al tercer participante involucrado en un evento como destinatario;
corresponde al caso dativo. La marca morfológica del objeto (acusativo-da-
tivo) se hace con los sufijos (-a's), para el singular, y (-txi's), para el plural.
Ejemplos:

alku” luucgxas wa kxku “el perro mordió al niño”

falku-a' luuçx-as wa k-0-kuj

//perro-TOP/niño-OBJ/morder- AOR-3psASER.PD//

klatxis yackiputhaw “arreamos las vacas”

(kla-txis yackipu-o-thawj

//vaca-OB]pl/arrear- AOR-1ppASER//

Cuando en una oración coexisten objeto directo y objeto indirecto, se
marca el indirecto con el sufijo y el directo queda como no marcado. Ejemplo:

Tmigu yaja ukwes pesku “Domingo me regaló una mochila”

(Tmigu-a yaja ukwe-as pes-g-Ru)

//Domingo-TOP/mochila/yo(fem)-OBJ/regalar- AOR-3psASER.PD//

Silvxina kukx tubtxis pucuk — “Silvina les da maíz a las palomas”

fSilvxina-a' kukx tub-txis puc-u-kuj

//Silvina-TOP/maiz/paloma-OBJpl/dar de comer-IMPF-3psASER.PD//

Sucede también con frecuencia que si en la situación comunicativa no
se hace necesario identificar al objeto directo, este aparece exento de marca
morfológica. Ejemplo:

luuça cxaju U'wek “el niño come piña”

(luuçx-a' cxaju 4 -e-kuj

//niño- TOP/piña/comer-IMPF-3psASER.PD//

Rosa us kukupxik “Rosa desgrana los frijoles”

fRosa-a' us kukupx-i-kuj

//Rosa-TOP/frijol/desgranar-IMPF-3psASER.PD//

<!-- page 102 (screenshot 0102) -->
Además de las funciones sintácticas que expresan los diferentes roles que
los eventos involucran en su módulo semántico básico, existen también las
funciones circunstanciales. Se han identificado: locativo espacial, temporal,
beneficiario, sociativo e instrumental.

El locativo temporal suele ir al principio de la oración, acompañado del
morfema topicalizador (-a”). Para el locativo espacial hay un paradigma de
morfemas de caso: inesivos (-te), [-ka), (-sul y (-khej; alativo (-na); elativo
(-ju). Ejemplos:

kuskaya” cxhabju u'jeçtha'vv “mañana nos vamos del pueblo”

(kuskay-a' exhab-ju Wj-e-c-thawj

//mañana-TOP/pueblo-ELA/ir-IMPE-INT-1ppASER//

kusia” kabildote úsuth “esta mañana estuve en el Cabildo”

[kusi-a' kabildo-te ús-u-thut

//esta mafiana-TOP/cabildo-INE/estar-IMPF- 1psASER//

Para las funciones de beneficiario, sociativo e instrumental existen los
morfemas (-j1), (-yalchi y (-uh), respectivamente. Ejemplos:

Beneficiario

Lilia ya ja agxji vxitku “Lilia hizo una mochila para mí”

(Lilia-a' yaja agx-ji vxit-o-kuj

(/Lilia-TOP/mochila/yo(masc)- BEN/hacer-AOR-3psASER.PD//

Mixia atx Selsuji umuca “María está tejiendo una ruana para Celso”

(Mixia-d'atx Selsu-ji um-u-ç-a'l

(/María- TOP/ruana/Celso-BEN/tejer-IMPF-INT-3psASER.PE//
Sociativo

Selsu' Silvxinayakh kujuk “Celso baila con Silvina”

(Selsu-a' Silvxina-yakh kuj-u-kuj

//Celso- TOP/Silvina-SOC/bailar-IM PF-3psASER.PD//

Rixiana khasx pladyakh UR. “Julián comió sopa con plátano”

(Rixian-a' khasx plad-yakh -90-kuj

//Julián-TOP/sopa/plátano-SOC/comer- AOR-3psASER.PD//

3. Lasílaba /si/ es acentuada, por esto aparece la forma larga del morfema TOP.

<!-- page 103 (screenshot 0103) -->
SINTAXIS
Instrumental

çxiçxas cxilxuh wakath “corté la carne con el cuchillo”

[exiex-a's cxilx-uh waka-0-thuj

//carne-OBJ/cuchillo-INS/cortar-AOR-1psASER//

Entre las funciones sintácticas y las funciones semánticas no hay una re-
lación biunivoca, de tal modo que un elemento que cumpla una determina-
da función semántica puede tener asignadas funciones sintácticas diferen-
tes, según la manera como se construya la oración. A la inversa, una misma
función sintáctica puede estar asociada a diferentes funciones semánticas.
Esta relación que se establece entre los argumentos del verbo y las funciones
sintácticas que los expresan en la oración, es decir, a cuál de los participantes
se le da el realce morfosintáctico en tanto se toma como sujeto, es lo que se
conoce como la voz.

De la relación que se establece entre la función sintáctica de sujeto y las
funciones semánticas de agente y paciente, se desprende que en nasa yuwe
hay voz activa y voz media. La voz activa se da cuando el sujeto coincide
con el agente; en voz activa se construye la gran mayoría de las oraciones
de la lengua. La voz media aparece cuando el reflexivo se usa para hacer
funcionar al paciente semántico como sujeto y prescindir de la información
relacionada con el agente; aquí se le da realce como sujeto a la entidad que es
afectada por el evento sin que ejerza control sobre él. Ejemplos:

Voz activa

igxa klatxis yackipug “tú arreaste las vacas”

figx-a kla-txi's yackipu-0-gu)

(/tú(masc)-TOP/vaca- OBJpl/arrear- AOR-2psASER//

uRvve misxas ukawakxith “empujo a la gata”

fu kwe-a' misx-as ukawakx-i-thuj

//yo(tem)-TOP/gata-OBJ/empujar-IMPF-1psASER//

Voz media

kla ya yackiputx “las vacas se dejaron arrear”

(kla-a' ya -yackipu-o-tx)

(/vaca- TOP/REF-arrear- AOR-3ppASER.PD//

misxa yaukawakxik “la gata se deja empujar”

ímisx-a' ya -ukawakx-i-kuj

//gata-TOP/REF-empujar-IMPF-3psASER.PD//

<!-- page 104 (screenshot 0104) -->
En las oraciones de voz activa aparece en el morfema modopersonal la
persona que corresponde al agente semántico: segunda singular y primera
singular. En las oraciones de voz media aparecen en el morfema modoper-
sonal la tercera persona plural y la tercera persona del singular, respectiva-
mente, que corresponden al paciente semántico en cada caso.

Existen también otras funciones que, si bien se expresan a través de me-
dios y estrategias formales —morfológicas y sintácticas—, corresponden al
nivel pragmático, en tanto cumplen un papel en relación con la información
que el hablante transmite al oyente; son las funciones informativas. En nasa
yuwe se encuentran la topicalización y la focalización.

Mediante la topicalización se toma un constituyente y se lo presenta
como el tema de lo que se va a hablar. Normalmente está situado al inicio de
la oración y lleva sufijado el morfema (-a”). Frecuentemente coincide con el
sujeto, que no tiene una marca morfológica propia. Los circunstantes tem-
porales son topicalizados también con frecuencia. Ejemplos:

Topicalización de sujeto

txá jiba sena wuwuk “ese caballo corre mucho”

[txá jiba-a sena wuwu-u-kuj

//DEM2/caballo- TOP/mucho/correr-IM PF-3psASER.PD//

tuba cxihme “la paloma es blanca”

[tub-a cxihme-a')

(/paloma-TOP/blanca-3psASER.PE//

Topicalización de circunstante temporal

unaha cxhabte úsuth “ayer estuve en el pueblo”

funah-a' cxhab-te ús-u-thuj

//ayer- TOP/pueblo-INE/estar-IMPF- 1psASER//

igxa kuskaya mjimenega “¿no trabajaràs mañana?”

figx-a' kuskay-a” mji-i-me-ne-ga')

(/tú(masc)-TOP/mafiana- TOP/trabajar-IMP-NEG-D3-2psINTE//

Con la focalización se le otorga un mayor relieve informativo a algún
constituyente de la oración, que se destaca para informar que se trata de
ese constituyente y no de otro diferente. El procedimiento formal consiste
en mover hacia dicho constituyente los morfemas modopersonal y de dis-
tancia, que quedan así sufijados en el constituyente y no en el predicado.
Ejemplos:

<!-- page 105 (screenshot 0105) -->
SINTAXIS
Sin focalización
misxa Karlusas wa kxkuk “el gato mordió a Carlos”
ímisx-a' Rarlus-as wa Rx-o-Ru-Rut
(/gato- TOP/Carlos- OBJ/morder- AOR-D2-3psASER.PD//
Focalización del sujeto
misxkuk Rarlusas vva EX "fue el gato el que mordió a Carlos"
(misx-ku-ku Karlus-as wa kx-o)
(/gato-D2-3psASER.PD/Carlos- OBJ/morder- AOR//
Focalización del objeto
misxa Karlusaskuk wa kx “fue a Carlos a quien mordió el gato”
ímisx-a' Karlus-a's-ku-ku wa kx-oj
//gato-TOP/Carlos-OBJ-D2-3psASER.PD/morder-AOR//
Focalización del circunstante espacial
yattekuk misxa Karlusas wa RX
(yat-te-ku-ku misx-a' Karlus-a's wa kx-o)
//casa-INE-D2-3psASER.PD/gato-TOP/Carlos-OBJ/morder- AOR//
“fue en la casa donde el gato mordió a Carlos”
Focalización del circunstante temporal
saptukuk misxa' Karlusas wa kx
(saptu-ku-ku misx-a' Karlus-a's wa kx-o)
//sábado-D2-3psASER.PD/gato-TOP/Carlos-OBJ/morder-AOR//
“fue el sábado cuando el gato mordió a Carlos”
Otros ejemplos:
isath we'we “es la verdad lo que yo hablo”
fisa-thu wew-e)
//verdad-1psASER/hablar-IMPE//
nak uyi “fue este el que me pegó”
(na-ku uyi-9)
//DEM1-3psASER.PD/pegar-AOR//
Selsuyakhthu kuj “fue con Celso con quien baile”
(Selsu-yakh-thu kuj-9)
//Celso-SOC-1psASER/bailar- AOR//

<!-- page 106 (screenshot 0106) -->
SINTAXIS

Las oraciones declarativas asertivas se construyen con los morfemas
modopersonales correspondientes a los modos asertivo (ASER) —aserción
fuerte— y suspensivo (SUS) —aserción débil—, que expresan dos grados
distintos de certeza o de conocimiento sobre lo que se dice.

Con las oraciones asertivas se predica la existencia, la ubicación espa-
cial, las propiedades o la pertenencia a un determinado conjunto, las carac-
terísticas, las acciones, los procesos, los estados, los fenómenos naturales.
Ejemplos:

Predicación de existencia

bahç úsa “hay fique”

(bahç ús-9-a')

//fique/estar- AOR-3psASER.PE//

Predicación de ubicación espacial

Peklu yatte úsa “Pedro está en la casa”

(Peklu-a' yat-te ús-o-a

//Pedro-TOP/casa-INE/estar- AOR-3psASER.PE//

Predicación de propiedad

uythu “soy mujer”

(u'y-thu)

//mujer-1psASER//

Predicación de identificación

na kweta “esto es (una) piedra”

ína-a kwet-a)

//DEM1-TOP/piedra-3psASER.PE//

Predicación de una característica

wala “es grande”

(vvala-a'

//grande-3psASER.PE//

Predicación de una acción

wewgu “hablaste”

(Wwew-o-guj

//hablar- AOR-2psASER//

<!-- page 107 (screenshot 0107) -->
ye : « . . »”»
yuzuhg yaja vxitu es con aguja con lo que haces mochilas

(yuz-uh-gu yaja vxitu-ul

//aguja-INS-2ps/mochila/hacer-IMPE//

Los dos procedimientos son excluyentes entre sí, no coinciden sobre un
mismo constituyente: cuando se focaliza el sujeto o el circunstante temporal,
dichos constituyentes no tienen el morfema topicalizador. Los marcadores
de caso morfológico sí se conservan aunque el constituyente que los tiene
esté focalizado.

LA ORACIÓN
Formalmente la lengua distingue entre oraciones declarativas y oraciones
no declarativas, según las categorías gramaticales presentes en el morfema
predicativo. Esta es la primera clasificación que puede hacerse de las oracio-
nes del nasa yuwe. Para la presentación de las oraciones se tiene en cuenta
también el grado de complejidad de la estructura oracional: se empieza por
presentar la oración simple y con ella las otras clasificaciones; posteriormen-
te se presentan la oración compuesta y la oración compleja.
La oración simple
Esta contiene una sola relación predicativa, una proposición con sus ele-
mentos: el predicado y la base de predicación. En nasa yuwe hay oraciones
simples declarativas y no declarativas.

Las oraciones declarativas llevan el morfema modopersonal, es decir
que contienen la flexión de tres categorías: la persona, el número y el modo.
Con las oraciones declarativas se habla de un estado de cosas. La diferencia
que se establece en la tercera persona entre la predicación dinámica (PD) y
la predicación estativa (PE), que puede verse claramente en los morfemas
modopersonales recogidos en la tabla de abajo (a la izquierda, los morfemas
de la PD y a la derecha, los morfemas de la PE), se da en el marco de las
oraciones declarativas. Las oraciones declarativas, a su vez, se dividen en
asertivas y no asertivas.

Tabla 13. Morfemas modopersonales de tercera persona
Tercera persona Asertivo Suspensivo Interrogativo
Singular -ku / -a -ka / -na -Ra' / -na
Plural -txi / -ta -txina -txna

<!-- page 108 (screenshot 0108) -->
Predicación de un proceso

nxiisxku “se engordó"

(nxiisx-o-Rut

//gordo- AOR-3psASER.PD//

Predicación de un estado

duha “está pesado”

(duh-a)

//pesado-3psASER.PE//

Predicación de un fenómeno natural

sekuk “hace sol”

[sek-u-ku)

(/sol-IMPF-3psASER.PD//

Como puede verse en los ejemplos, las propiedades y las características se
predican sin necesidad de un verbo que actúe como cópula, en tanto las pa-
labras nominales reciben directamente el morfema de la predicación. Pero
sí es necesaria una cópula para la predicación de la existencia y la ubicación
espacial. En estos casos actúan como cópula los mismos verbos que funcio-
nan como auxiliares y que contienen información acerca del eje corporal de
la entidad a la cual se refieren: (ús-) y fu p-) “estar”.

Para la predicación de la posesión, es decir, la pertenencia de una entidad
a otra, se sufija el morfema (-ji) “benefactivo” al nombre del poseedor, y la
palabra así construida constituye el núcleo del predicado. Ejemplos:

jiba Lamusji "el caballo es de Ramos"

(jiba-a” Lamus-ji-a'l

//caballo-TOP/Ramos-BEN-3psASER.PE//

na ya ja u kweji “esta mochila es mía”

(na yaja-a Wkwe-ji-a')

//DEM1/mochila-TOP/yo(fem)-BEN-3psASER.PE//

Las oraciones asertivas pueden tener explicitación léxica del sujeto, ex-
cepto aquellas cuyo predicado se refiere a fenómenos naturales expresados
por lexemas verbonominales. Se trata de eventos que no son atribuibles a
una entidad y por lo tanto no es posible explicitar un sujeto. Ejemplo:

<!-- page 109 (screenshot 0109) -->
SINTAXIS
Con explicitación de sujeto

misxa alku's wa kxku “el gato mordió al perro”

ímisx-a alku-as wa kx-0-kuj)

//gato-TOP/perro-OBJ/morder- AOR-2psASER.PD//

seka sena acxa “el sol está muy caliente”

[sek-a' sena açxa-a't

(/sol-TOP/mucho/caliente-3psASER.PE//

Mixia dehek “María duerme”

(MIxia-a' deh-e-kuj

//María-TOP/dormir-IMPF-3psASER.PD//

Sin explicitación de sujeto (fenómenos naturales)

kwehnek “relampagueó”

(kwehne-o-kuj)

//relámpago- AOR-3psASER.PD//

wejxan úsa “está venteando”

(Wejxa-na ús-g-a'l

//viento-DUR/estar-AOR-3psASER.PE//

kusuca “está anocheciendo”

(kus-u-c-a')

//noche-IMPF-INT-3psASER.PE//

Si bien existe el lexema verbonominal (nus), que significa “lluvia/hacer
invierno” para hablar del hecho de llover se usa en su faz nominal, referido a
una “entidad que llega”; como verbo, en su faz dinámica, se refiere a la época
de invierno. Ejemplos:

nus pa'jn úsa “está lloviendo”

(nus paj-na ús-0-4)

(Muvia/llegar- DUR/estar-AOR-3psASER.PE//

sena nusuk “hace mucho invierno”

(sena nus-u-kuj

//mucho/hacer invierno-IMPF-3psASER.PD//

<!-- page 110 (screenshot 0110) -->
SINTAXIS

Wjecyaga “ya te vas?”

fuj-e-çyà-ga'l

//ir-IMPF-INCO-2psINTE//

Kse kihka “¿bajó José?”

(Rse-a kih-0-ka)

//José-TOP/bajar- AOR-3psINTE.PD//

Es frecuente en nasa yuwe que esta clase de oración interrogativa se for-
mule acompañada de la negación, como una forma cortés de preguntar.
Ejemplos:

mjimenetxna “ellos no trabajaron?”

(mji-0-me-ne-txna')

(/trabajar- AOR-NEG-D3-3ppINTE.PD//

umucmega “¿usted no está tejiendo?”

fum-u-e-me-ga')

(/tejer-IMPF-INT-NEG-2psINTE//

útumekwe “¿no se mojaron (ustedes)?”

(útu-9-me-kwe)

//mojar-AOR-NEG-2ppINTE//

Las oraciones interrogativas parciales o relativas se construyen con las
palabras interrogativas y con los morfemas modopersonales interrogativos;
con estas oraciones se pregunta sobre un dato específico: qué sucede, quién
lo hace, cómo, cuándo, dónde, etc. Ejemplos:

na Rihna “¿qué es esto?

(na kih-na'J

//esto/;¿qué?-3psINTE.PE//

mtena “¿dónde es?”

imte-na)

//¿dónde?-3psINTE.PE//

kimga “quién es usted?”

(kim-ga”)

//¿quién?-2psINTE//

<!-- page 111 (screenshot 0111) -->
Semánticamente, todas las oraciones declarativas pueden ser negativas.
La negación se hace con un sufijo en el verbo, que se sitúa entre la zona as-
pectual y el morfema de distancia —o el morfema modopersonal, cuando
no se expresa la distancia—. Ejemplos:

unaha mjimekith “ayer no trabajé”

funah-a' mji-9-me-ki-thuj

//ayer/trabajar-AOR-NEG-D1-1psASER//

ukawakxwemekutx “ellos no quisieron empujar”

fukawakx-we-o0-me-ku-txij

//empujar-VOL-AOR-NEG-D2-3ppASER.PD//

vxicna ujemetkha'w “como que no vamos al cerro”

(vxic-na u'j-e-me-tkhaw)

//cerro- ALA/ir-IMPF-NEG-1ppSUS//

umyáwameg “no vas a tejer”

(um-0-yawa-me-guj

//tejer-AOR-PROS-NEG-2psASER//

Oraciones declarativas no asertivas son las interrogativas, que se cons-
truyen con el morfema modopersonal correspondiente al modo interrogati-
vo (INTE); con estas oraciones se pregunta sobre un estado de cosas.

Las oraciones interrogativas totales o absolutas se diferencian de las
asertivas solamente por la presencia del modo interrogativo en el morfema
predicativo. Con estas oraciones se pregunta por un estado de cosas en ge-
neral, sobre si el hecho enunciado es falso o verdadero; normalmente se
espera una respuesta afirmativa o negativa. Ejemplos:

na luugxa hibana'w pebeka “ese niño chilló como caballo?

(na luuçx-a' hiba-na'w pebe-o-ka')

//DEM1/niño-TOP/caballo-SIMI/chillar- AOR-3psINTE.PD//

wewna Úsga “estás hablando?”

(Wwew-na ús-9-ga')

//hablar-DUR/estar-AOR-2psINTE//

<!-- page 112 (screenshot 0112) -->
baçxga wejas theg “¿cuándo viste la escalera?

(baçx-ga' wej-a's theg-o)

(/,cuàndo2-2psINTE/escalera- OBJ/ver- AOR//

kimka uphas péecx “¿quién tumbó la cerca?”

(kim-ka” uph-as péeçx-o)

//¿quién?-3psINTE.PD/cerca-OBJ/tumbar- AOR//

Dentro de este tipo de oraciones entran algunas fórmulas de saludo, tales
como:

mawga pete “¿cómo amaneció (usted)?, ¿cómo amaneciste?”

(maw-ga pete-o)

//¿cómo?-2psINTE/amanecer-AOR//

mawkwe pete “¿cómo amanecieron (ustedes)?”*

(maw-kwe pete-o)

//¿cómo?-2ppINTE/amanecer-AOR//

Dentro de las oraciones declarativas hay oraciones intransitivas, transi-
tivas y ditransitivas, según las funciones sintácticas que aparezcan en ellas.
Las intransitivas involucran un solo participante, que normalmente cumple
la función de sujeto. Las transitivas expresan eventos en los que se involu-
cran dos participantes, uno activo y otro pasivo. Las ditransitivas se refieren
a eventos que involucran tres participantes en su módulo semántico básico,
uno activo, uno pasivo y un destinatario. Ejemplos:

Oraciones intransitivas

agx ew weweth “yo hablo bien”

(agx ew wew-e-thuj

//yo(masc)/bien/hablar-IMPF-1psASER//

iRvve wala zxicxkwe “tú eres muy bonita”

tikwe-a wala zxicxkwe-a')

//tú(fem)-TOP/grande/bonita-3psASER.PE//

Oraciones transitivas

misxa çxiçxas Uk “el gato comió carne”

7 Esta fórmula se usa también para dirigirse a una mujer con la que se tiene familiaridad.

<!-- page 113 (screenshot 0113) -->
imperativas, prohibitivas, incitativas, exhortativas. En el caso de las oraciones

imperativas, se distingue si se dirige a una o a varias personas. Ejemplos:
mthame “tenga verguenza, avergiéncese

(m-thamel

//IMP-avergonzarse//

neganu “no lo sale”

(nega-nu)

//salar-PROH//

Ru'jya “¡a bailar!”

(kuj-ya)

//bailar-INCI//

kiduka “peinémonos”

(kid-u-kaj

(/peinar-IMPF-EXH//

vvaças à ya “a comer arepa”

(vaç-as Ú'-ya'l

//arepa-OB]/comer-INCI//

La oración compuesta

Bajo la denominación oración compuesta se agrupan las oraciones que tie-
nen más de una relación predicativa y están formadas por oraciones simples
que pueden tener independencia sintáctica; los predicados involucrados co-
rresponden a formas finitas. Esto comprende dos mecanismos sintácticos: la
yuxtaposición y la coordinación.

La yuxtaposición se entiende como la relación que se da entre dos uni-
dades sintácticas que aparecen seguidas en secuencia sin que se establezca
mediante un elemento explícito algún tipo de nexo entre ellas. Puede darse
entre oraciones simples, puestas una al lado de la otra sin una palabra o un
morfema que las conecte de manera específica, aunque estén relacionadas
semánticamente. En nasa yuwe se encuentra este mecanismo en los casos
que se presentan a continuación.

En el caso de las oraciones completivas que funcionan como objeto direc-
to de verbos como pensar, saber y decir, cada una de las oraciones tiene su
correspondiente morfema modopersonal. Ejemplos:

<!-- page 114 (screenshot 0114) -->
SINTAXIS
ímisx-a' cxiex-as Ú -g-RI

//gato-TOP/carne-OBJ/comer- AOR-3psASER.PD//

Salvxiku bekas tugxik + “Salvador toma chicha”

(Salvxiku-a beka-as tugx-i-ku)

(/Salvador- TOP/chicha-OBJ/tomar-IMPF-3psASER.PD//

Oraciones ditransitivas

Mixia cxiex misxa's pucuk "María le da carne al gato”

(Mixia-a' cxiex misx-as puc-u-kuj

//María-TOP/carne/gato-OBJ/dar de comer-IMPF-3psASER.PD//

Rapiyasd mem luuçxtxis kapiyak — “el profesor enseñó un canto a los niños”

(ka-piya-sa-a” mem luuçx-txis ka-piya-0-kuj

//FACT-aprender-NOM-TOP/canto/niño-OBJplI/FACT-aprender-AOR-

3psASER.PD//

En las oraciones transitivas se da el orden sintáctico sujeto-objeto-verbo
(SOV), que por su gran frecuencia de aparición puede considerarse el orden
canónico de esta clase de oraciones. Cuando aparecen los dos objetos, se si-
túan primero el directo y después el indirecto. En general, la tendencia es a
que el verbo o la palabra predicativa vaya al final de la oración, si bien no se
trata de un orden rígido; este es, por lo tanto, el orden canónico”.

Las oraciones no declarativas se construyen con los morfemas de la
modalidad que expresa la interacción directa con un interlocutor. Con las
oraciones no declarativas el hablante no da cuenta de un estado de cosas ni
interroga sobre ellas, sino que se dirige a un interlocutor esperando de él un
determinado comportamiento. El morfema predicativo en este caso expresa
solamente la modalidad, pero no flexiona para la persona; se entiende que si
lo que se expresa es la apelación directa a un interlocutor, no es posible hacer
una variación en cuanto a la categoría gramatical de la persona, y se asume
que si hay una persona expresada, esta será siempre la segunda.

La estructura de una oración no declarativa consiste en una sola palabra
—predicativa— que contiene un lexema verbal —también verbonominal o
cualificativo— más el morfema de modalidad correspondiente; en esta clase
de oraciones no se explicita el sujeto gramatical. Según el morfema modal que
interviene, hay semánticamente cuatro tipos de oraciones no declarativas:
7. Se le llama orden canónico al orden no marcado, el que tiene mayor frecuencia de uso, el que

aparece “por defecto”.

<!-- page 115 (screenshot 0115) -->
SINTAXIS

Kse yuhmena ji XP “(ella) dijo que José no viene”

(Kse-a yuh-me-na ji -9-ku)

(/José- TOP/venir- NEG-3psSUS.PE/decir- AOR-3psASER.PD//

eva súhu'th “pienso que está bien"

few-a súh-u -thuj

//bien-3psASER.PE/pensar-IMP-1psASER//

Ukwes wedxmeg jiyith — “sé que no me quieres”

fu kwe-as wedx-9-me-gu jiy-i-thu)

//yo(fem)-OBJ/querer- AOR-NEG-2psASER/saber-IMP-1psASER//

Es este, a la vez, un mecanismo para hacer citaciones en estilo directo.
Las oraciones de los ejemplos podrían traducirse también, respectivamente:
“«José no viene», dijo”; “«está bien», pienso” y “«no me quieres», (lo) sé”.

Las oraciones completivas de verbos de desplazamiento y verbos «psico-
lógicos» —de voluntad y de actitud frente a algo— se construyen sufijando
el morfema (-ya) “incitativo” al verbo que funciona como complemento.
Ejemplos:

bahç kudya wjyáwath “voya desfibrar cabuya”

(bahç Rud-ya' wj-0-yawa-thuj)

//cabuya/desfibrar-INCI/ir- AOR-PROS-1psASER//

ezya wijwejeth “quisiera ir a pescar”

(ez-ya Uj-weje-o-thuj

(/pescar-INCI/ir- DES-AOR-1psASER//

pweesahya wedxiga “ste gusta jugar?

(pweesah-ya wedx-i-ga')

//jugar-INCI/querer-IMPF-2psINTE//

dehya kuhunega “vendrás a dormir”

(deh-ya kuh-u-ne-gaj

//dormir-INCI/venir-IMPF-D3-2psSUS//

7 Es este un mecanismo para hacer citaciones en estilo directo. La oración podría traducirse también
como “«José no viene», dijo”

<!-- page 116 (screenshot 0116) -->
SINTAXIS
ikheci kwe napa kuskaya' vxite uy pajexayu kutxhas itxhvxih túscxa
pajahana
(ikh-e-c-i kwe napa kuskay-a' vxite uy paj-çxa-yu' kutxh-a's i-t hvxih
tús-cxa pa'j-a-ha-naj
//matar-IMP-INT-2ppASER/pero/mañana-TOP/otra/mujer/llegar-REST-
TOP/maíz-OBJ/con tusa/cargar-REST/llegar-IMP-ITE-3psSUS. PE//

“me matas, pero mañana ha de llegar otra mujer cargando no más la tusa”*”

Las disyuntivas tienen como nexo el conector 'meegxa”, que une oracio-
nes que se presentan como opciones de una alternativa; puede ir solamente
entre las dos oraciones o, como se ha encontrado con mayor frecuencia, al
principio de cada una de las dos oraciones. Ejemplos:

meecxa acxh ujun meeçxa ayte dehen

ímeeçxa acxh uj-u'-n meeçxa ay-te deh-e-nj

//tal vez/hoy/ir-IMP-1psFUT/tal vez/aquí-INE/dormir-IMPF-1ps

FUT//

“tal vez me vaya hoy o tal vez duerma aquí”

Las consecutivas son oraciones de las cuales la primera expresa la cau-
sa y la segunda la consecuencia; están unidas por los conectores txaju y
aç- —este último suele ir topicalizado por el morfema -a' o acompañado del
enfático -yu —. Ejemplo:

adxa pejxmekuth aça idxa majimekung

(adx-a' pejx-o-me-Ru-thu aç-a idx-a maji-o-me-Ru-gu)"

//yo(masc)/preguntar- AOR-NEG-D2-1psASER/entonces-TOP/tú

(masc)-TOP/decir-AOR-NEG-D2-2psASER//

“yo no pregunté, entonces tú no me dijiste (no me diste la información)”

fxtúu pesatu úskik txaju wetekith

(fxtúu pesatu ús-0-ki-ku txaju wete-o-ki-thu)

//palo/atravesado/estar- AOR-D1-3psASER.PD/así que/caer-AOR-

D1-1psASER//

“había un palo atravesado, así que me caí”
7 Tomado del cuento de la Siska, una mujer que se convierte en el gusanito de la mazorca. Tusa es el

corazón de la mazorca al que se adhieren los granos de maiz.
7 Parece que en la base "ma'ji" hubiera una composición entre el interrogativo ma'w = “cómo” (que

pierde su último fonema) y la raíz del verbo ji = “decir”.

<!-- page 117 (screenshot 0117) -->
Se usa también el mecanismo de la yuxtaposición para «adicionar» ora-
ciones que se refieren a eventos sucesivos o concatenados. Ejemplos:

yuhyaja ujweçyaja “vino y ya se va”

(yuh-o-yaj-a' uji-(w)e-çya-(j)a')

//venir-AOR-EXT-3psASER.PE/ir-IMP-INC-3psASER.PE//

Khwena kutxhas uja'k Tmigu pkhakhek

(khwen-a' kutxh-a's uj-a-k tmigu pkhakh-e-kuj

//Juan-TOP/maiz-OBJ/sembrar-IMP-3psASER.PD/Domingo/cosechar-

IMP-3psASER.PD//

Juan siembra el maíz y Domingo lo cosecha"

acyu mji-ya tudumeça mawthejwa Rabane 7

(ac-yu” mji-ya tudu-me-ç-a' mawthejwa Raba-ne-a't

//entonces-ENF/trabajar-INCI/elaborar-NEG-INT-3psASER.PE/de

cualquier

manera/terminar-D3-3psASER.PE//

“Entonces no pudo elaborar y terminó de cualquier manera”

La coordinación se entiende como la unión de elementos sintácticamente
equivalentes. Para el caso de las oraciones, se da cuando se unen oraciones
simples cuyo nexo explícito está expresado por un elemento que funciona
como conector de dichas oraciones en igualdad de condiciones, es decir, al
mismo nivel sintáctico. Se puede hablar de coordinación de oraciones en
nasa yuwe, teniendo en cuenta que cada una de las oraciones simples tiene
un verbo flexionado —forma finita— que funciona como núcleo predicativo,
lo que indica que no hay una diferencia jerárquica entre ellas. Esto es lo que
caracteriza formalmente las oraciones coordinadas en esta lengua. Semánti-
camente, hay oraciones coordinadas adversativas, disyuntivas y consecutivas.

Las adversativas están unidas por el conector “napa”, que contrapone una
idea a otra expresada primero. Ejemplos:

vxu himeth napa ya jas wayu'n

(vxu hi -me-thu napa yaja-as way-u'-nj

//dinero/tener-NEG-1psASER/pero/mochila-OBJ/comprar-IMP-1psFUT//

“no tengo plata, pero compraré la mochila”

7 Tomado del Cuento del armadillo, recogido en Caldono.

<!-- page 118 (screenshot 0118) -->
Estos dos conectores pueden tener también la función pragmática de in-
troducir enunciados, de modo que puede considerarse que, en términos ge-
nerales, son conectores ilativos y en esa medida pueden conectar oraciones
que establecen una relación de causa y consecuencia. Ejemplo:

Aça naa yuweteyu kwesx yuwe fxizenxi jinxisateyu) txaju” lecx naa

eensu jez een yuçte wala sena théysa yuwe Úsnaçe "

faç-a naa yuve-te-yu kwesx yuwe fxize-nxi ji-nxi-sa-te-yu  txaju leçx

naa een-su jez een yucte wala sena-a' théy-sa yuwe ús-na-ce')

//entonces- TOP/este/idioma-INE-ENF/nuestro/idioma/vivir-RES/

decir-RES-NOM-INE-ENF/entonces/pequeño/este/día-INE/dos/día/al

cabo/grande/mucho-TOP/dificil-NOM/idioma/estar- DUR-CONFE//

“Entonces en esta noticia, en nuestro idioma nos referimos al contexto,

entonces brevemente en estos dos días tenemos que analizar la difícil si-

tuación que tiene nuestra lengua”

La oración compleja

Se entiende por oración compleja una estructura oracional que contiene dos
predicados y en la que uno de ellos cumple la función de núcleo de toda la ora-
ción y el otro predicado cumple una función de argumento o de adjunto en re-
lación con el predicado nuclear, de tal manera que uno de los predicados está
subordinado al otro; la relación jerárquica entre ellos establece la existencia
de un predicado principal —o subordinante— y un predicado subordinado.

En nasa yuwe este tipo de estructura se caracteriza formalmente por el
hecho de que el predicado subordinado carece de flexión modo-personal, es
una forma no finita, y lleva un morfema que indica su estatus de “subordi-
nado”, mientras que el predicado subordinante tiene el morfema modoper-
sonal y todas sus otras marcas flexivas. Esto constituye una marca formal de
la diferencia jerárquica entre las dos oraciones. Por otra parte, los morfemas
que indican la subordinación de los predicados son en su mayoría morfemas
usados como flexivos o como derivativos en el ámbito nominal, lo que lleva
a plantear que, en términos generales, la lengua le da tratamiento nominal a
los predicados subordinados”.

En cuanto a la presencia del morfema que indica la subordinación, se
ha encontrado que algunas oraciones llevan un solo morfema que informa,
* Tomado del discurso pronunciado por el líder Silverio Yuju en el evento Minga de las lenguas

originarias, realizado en Totoró (Cauca) en el año 2008.
*! La nominalización es una estrategia muy usada por las lenguas del mundo para la subordinación

de oraciones, según algunos teóricos (véase, por ejemplo, Givón 1990: 190).

<!-- page 119 (screenshot 0119) -->
Condicionales

mji hyàçxa yuhen “si termino de trabajar, vendré"

(mji hyà-çxa yuh-e-n)

//trabajar/terminar-REST/venir-IMPE-1psFUT//

Kse pajte puukx wewenhaw — “si llega José, hablamos con él”

(kse-a paj-te puukx wew-e-nhaw)

//José-TOP/llegar-INE/RECI/hablar-IMPF-1ppSUS//

Entre las temporales, además de las ya presentadas, que expresan si-
multaneidad de los acontecimientos, están las que indican que lo expresa-
do en el predicado subordinado es anterior a lo expresado por el principal.
Los morfemas que indican dicha anterioridad son (-mey-) (ANT.IS), cuando
el sujeto de los dos predicados es el mismo, y (-meyna-) (ANT.DS), cuando
los sujetos son diferentes. Ejemplos:

ujmey acayakug upyu “antes de irte, ya estabas enfermo”

fu'j-mey àça-yà-Ru-gu up-yu' +

(/ir-ANT.IS/enfermo-INT-D2-2psASER/estar-ENF//

adxa idx pajmeyna kucxna wputh “yo estaba aburrido antes de que llegaras”

(adx-a' idx paj-meyna Ruçxna u'p-u-thul

//yo(masc)-TOP/tú(masc)/llegar-ANT.DS/aburrido-estar-IMPF-1psASER//

En las oraciones semánticamente concesivas el morfema de igual suje-
to es f-exapa) (CONC.IS) y el de distinto sujeto es (-tepa)* (CONC.DS).
Se recuerda aquí que las concesivas expresan lo que podría ser un obstáculo
para que se cumpla un determinado evento pero no lo es, o lo que podría
constituir razón suficiente para un acontecimiento pero no lo es.

nasacxapa nasa yuwes wewecme

ínasa-çxapa nasa yuwe-as wew-e-c-me-a')

//paez-CONC-.IS/paez/idioma-OBJ/hablar-IMPE-INT-NEG-3psASER-PE//

“aunque es paez, no habla la lengua paez”

misxas puuckuth weepeyicmetepa

ímisx-as puuc-9-ku-thu weepey-i-c-me-tepaj
* Una hipótesis es que la forma (-pa) o (-wa) —según la región— que se les agrega a los morfemas

(-çxal y (-te) corresponda al sufijo “aditivo”.

<!-- page 120 (screenshot 0120) -->
SINTAXIS
además, acerca de si el sujeto correspondiente a los dos predicados es igual
(IS) o es diferente (DS), esto es lo que en la teoría linguística se conoce como
referencia alternante”. Otras oraciones no tienen estos marcadores. Se pre-
sentan, entonces, las oraciones que tienen estructura de subordinación par-
tiendo de esta distinción formal.

Las oraciones con distinción entre igual sujeto (IS) y distinto sujeto (DS)
tienen en el predicado subordinado bien el sufijo (-exa) restrictivo” o bien
el sufijo (-te) “inesivo (locativo)”. El primero indica que el sujeto de las dos
oraciones es el mismo; se entiende de esta manera la restricción expresada
por él. El segundo morfema indica que los sujetos son diferentes; presenta el
evento correspondiente al predicado subordinado como un marco en el que
se da el otro evento.

Entre las oraciones que establecen esta diferencia se han encontrado las
que tienen valor semántico de temporales, de condicionales y de concesivas.

En cuanto a las condicionales y temporales, son oraciones en las que
solo aparece el morfema que indica IS o DS y en ellas el valor semántico de
temporal o condicional de la subordinada depende del morfema modoper-
sonal que aparezca en la flexión del verbo —de la oración subordinante—.
Si el morfema modopersonal corresponde al modo asertivo, el evento ex-
presado por el predicado subordinado es presentado como marco temporal
de realización del acontecimiento expresado por el predicado subordinante
(principal). Si el morfema modopersonal no corresponde al modo asertivo,
el evento correspondiente al predicado subordinado se presenta como una
condición para que se dé el otro evento. Puede pensarse que el morfema de
IS o DS indicará una cierta simultaneidad entre los acontecimientos expre-
sados por las dos oraciones; si el evento se da por cierto, esa simultaneidad
se entiende como temporal, y si el evento se plantea como supuesto, la si-
multaneidad se entiende como una condición. Ejemplos:

Temporales

txàvesxa' pajexa Ú'tx "cuando ellos llegaron, comieron"

(txà-vesx-a paj-çxa Ú -o-txi)

((DEM2-COL-TOP/llegar-REST/comer-AOR-3ppASER.PD//

nus pajn úste yatte uka'k "cuando està lloviendo, entra a la casa"

(nus pa'j-na ús-te yat-te uk-a-kuy

(Muvia/llegar- DUR/estar-INE/casa-INE/entrar-IMP-3psASER.PD//

* Originalmente swicth-reference en inglés. Traducida como “referencia alternante” en la edición

española del Diccionario de lingúística y fonética de David Crystal (2000: 480).

<!-- page 121 (screenshot 0121) -->
Las oraciones subordinadas causales se marcan con el sufijo (-pa Ral.
Con estas oraciones, el evento expresado por el predicado subordinado se
presenta como la causa del otro evento. Ejemplos:

wejxa atxtxi's kazx vxitpa ka Mlxia thetku

(Wejxa atx-txis kazx vxit-pa ka Mlia-a' thet-o-Ru)

//viento/ropa-OBJ/feo/hacer-CAUS/María/lavar- AOR-3psASER.PD//

“María lavó la ropa porque el viento la ensució”

unah yuweemekuth nus kihn úspa'Ra

fu'nah yuw-e-c-me-ku-thu nus kih-na ús-pa'kaj

//ayer/venir-IMP-INT-NEG-D2-1 ps ASER/lluvia/caer-DUR/estar-CAUS//

“ayer no vine porque estaba lloviendo”

yat zxiexkwepa Ra wedxith “me gusta la casa porque es bonita”

(yat zxiexkwe-pa ka wedx-i-thuj

//casa/bonita-CAUS/gustar-IMPF-1psASER//

Las subordinadas finales llevan sufijado al predicado subordinado o
bien el morfema Í-vvalY (FIN.G), que indica una finalidad general, o bien
el morfema (-kanj (FIN.E), que expresa una finalidad específica. El evento
presentado en el predicado subordinado constituye la finalidad del evento
presentado por el predicado subordinante. Ejemplos:

Kse kutxhas jxaawku txajx luuextxi's sájiwa

(kse-a kutx-as jaaw-o-ku txajx luuçx-txis sáji-waj

//José- TOP/maíz-OBJ/cosechar- AOR-3psASER.PD/sus/hijos-OBJ/co-

mer-FIN.G//

José cosechó el maíz para dar de comer a sus hijos”

MIixia'ustxis ahku adx kan

(Mixia-a us-txis ah-o-Xu ú -Rant

//María-TOP/frijol-OBJpl/cocinar-AOR-3psASER.PD/yo(masc)/comer-

FIN.E//

“María cocinó los fríjoles para que yo comiera”

Las subordinadas hipotéticas se refieren a eventos o estados que serían
ciertos si otros eventos o estados lo fueran. Se marcan con el sufijo (-paca) en
*% Puede ser también (-pa), según la variante regional.

<!-- page 122 (screenshot 0122) -->
SINTAXIS

//gato-OBJ/dar de comer-AOR-D2-1psASER/pedir-IMP-INT-NEG-CONC.

“le di de comer al gato aunque no me estaba pidiendo”

Existen, como se ha dicho, oraciones subordinadas en las que no se ex-
plicita una relación de igualdad o diferencia entre los sujetos de los dos
predicados involucrados. En esta clase de oraciones hay un morfema que
indica que el predicado es subordinado e informa también de lo expresado
por el predicado subordinado en relación con el predicado principal.

Existen también oraciones con estructura de subordinación en las que no
aparece el morfema que indica IS o DS, sino otro sufijo que indica igualmen-
te el estatus de subordinado al predicado que lo tiene, que aparece desprovis-
to del morfema flexivo modopersonal, y que agrega información semántica.

Entre las oraciones con estructura de subordinación que no indican la
relación entre los sujetos de las dos oraciones contenidas en dicha estruc-
tura se encuentran también algunas subordinadas con valor temporal. Los
morfemas aspectuales (-na) “durativo” y (-nxi) resultativo” se usan también
para acompañar predicados subordinados —formas no finitas— que están
en relación temporal con los predicados subordinantes, en estructuras de
subordinación en las que no se indica la relación entre los sujetos. El dura-
tivo expresa un acontecimiento simultáneo; el resultativo, un evento inme-
diatamente anterior. Ejemplos:

memna umuk * teje cantando”

fmem-na um-u-kuj

//cantar-DUR/tejer-IMPF-3psASER.PD//

pajna weweth “llego y hablo”

(paj-na wew-e-thuj

(Megar-DUR/hablar-IMPF-1psASER//

Rse pahnxi esuhçxa adxa' wijkuth “apenas llegó José, yo me fui "

(Rse pah-nxi esuhçxa adx-a' wj-o-ku-thuj

//José/llegar-RES/enseguida/yo(masc)-TOP/ir-AOR-D2-1psASER//

* Nótese que en este ejemplo el predicado subordinado tiene el morfema de la negación y dos
morfemas flexivos de aspecto, de manera que los morfemas de la subordinación no solo se sufijan

a los lexemas desnudos.

% Es la traducción dada por un hablante; tal vez sería más literal “hablo al llegar" o, en una forma un
poco antigua, "en llegando, hablo'.
* Una traducción más literal podría ser “una vez llegado José, yo me fui”.

<!-- page 123 (screenshot 0123) -->
SINTAXIS
el verbo subordinado, y el verbo de la oración subordinante se flexiona con
las modalidades que corresponden a la inferencia o a la futuridad. Ejemplos:

Liliakwe àçxh pajpaga ukwe wajxkwe weexwecxa nenyun

(lilia-kwe áçxh paj-paga ukwe weexwecxa neny-u-n)

(/Lilia-DIM/hoy/llegar-HIP/yo(fem)/contenta/quedar-IMPF-1psFUT//

“si Liliecita llegara hoy, yo me pondría muy contenta”

mji jiphmepaca çxhabna ujwen

(mji ji ph-me-paça çxhab-na wj-(w)e-n)

(/trabajar/tener-NEG-HIP/pueblo-ALA/ir-IMPF-FUT//

“si no tuviera trabajo me iría al pueblo”

tadxpaça pweesate ewuna “si fuera redonda, sería buena para jugar”

(tadx-paça pweesa-te evv-u-nal

(/redondo-HIP /jugar-INE/bueno-IMPF-3psSUS.PE//

Hay que anotar que la diferencia entre predicación dinàmica y predica-
ción estativa no incide en el funcionamiento de estos morfemas de IS o DS.
Ejemplos:

Tmigu nejwesxcxa seena mhikuk

(Tmigu ne jwesx-exa seena mhi-o-ku-kuj

//Domingo/gobernador-REST/mucho/trabajar- AOR-D2-3psASER.PD//

“cuando Domingo era gobernador, trabajaba mucho”

wecxan úste txihxpa ewku kasehe

(vveça-na Ús-te txihxpa ew-ku kaseh-e')

//contento-DUR/estar-INE/todo/bien-3psASER.PD/salir-IMPE//

“cuando estoy contento, todo sale bien”

atx zxicxkwete adx wayu'n “si la ruana es bonita, la compro”

(atx zxiexkwe-te adx vvay-u-n)

//ruana /bonita-DS/yo(masc)/comprar-IMP-1psFUT//

watxkwecxa mjiimena “si es perezoso, no trabaja”

(Watxkwe-cxa mji-i-me-nal

//perezoso-REST/trabajar-IMP-NEG-3psSUS//

* En esta oración el predicado subordinado tiene lexema cualificativo.

<!-- page 124 (screenshot 0124) -->
SINTAXIS
uyisas wa kxthu “mordí al que me pegó”

fuyi-sa-as wa Ex-o-thu)

//pegar-NOM-OBJ/morder- AOR-1psASER//

En función de complemento indirecto

teeçx ya'ja peeskith mitx ahn ússa's

íteeçx yaja pees-o-Ri-thu mitx ah-na ús-sa-a's)

//uno/jigra”/regalar- AOR/D1-1psASER/olla/cocinar-DUR/estar-NOM-

OBJ//

“le regalé una jigra a la que está cocinando”

kujn ússatxis atx duukhwe

(kuj-na ús-sa-txi's atx duukh-we)

//bailar-DUR/estar-NOM-OBJpl/ropa/entregar-IMP.pl//

“entregue la ropa a los que están bailando”

Como predicado de una relación atributiva

txà mhisa "él es (un) trabajador"

(txà-a mhi-sa-at

(/€1-TOP/trabajar- NOM -3psASER.PE//

Mixia mitx ahsa “María es la que cocina”

(MIxia-a mitx ah-sa-a'j

//María-TOP/olla/cocinar-NOM-3psASER.PE//

Las relativas adnominales pueden agregar diversas indicaciones semánticas
al nombre que complementan en tanto actúan como modificadores. Ejemplos:
Con lexema verbal

fxtúu ukanxisa seena wala” — "el árbol que tumbamos era muy grande”

[fxtúu uka-nxi-sa seena vala-a't

//árbol/tumbar-RES-NOM/muy/grande-3psASER.PE//

picthe mjin ússa yuhta “vienen los hombres que estaban trabajando”

(pic-the mji-na ús-sa yuh-o-ta)

//varón-adulto/trabajar-DUR/estar-NOM/venir- AOR-3ppASER.PE//

* Jigra: palabra para “mochila” en el español regional.
* En esta oración aparecen sobre el lexema verbal dos morfemas que surten el efecto de nominalizar:
el resultativo (-nxi) y el nominalizador (por excelencia) (-saj.

<!-- page 125 (screenshot 0125) -->
Mixia nxusna upa thakwe nus kihte

(Mixia-d' nxus-na up-a thakwe nus kih-te)

//María-TOP/triste-DUR/estar-3psASER.PE/demasiado/lluvia/llegar-INE//

“María está triste cuando llueve mucho”

Por último, entre las oraciones subordinadas, se presentan las relati-
vas. La estrategia formal de la lengua para formar relativas es la nomi-
nalización. Se incluyen como relativas en nasa yuwe tanto las oraciones
que ocupan ellas solas una posición nominal, que cumplen una función
argumental en la oración principal, como las que se encuentran incluidas
dentro de un constituyente nominal, que funcionan como modificadores.
Las primeras se llaman relativas nominales o libres; las que están incluidas
en un sintagma nominal constituyente de la oración principal se llaman
relativas adnominales.*

Las dos clases de oraciones relativas se forman sufijándole al predicado
subordinado el morfema (-saj, que funciona como nominalizador de las ba-
ses verbales y cualificativas, a las que vuelve aptas para cumplir funciones
argumentales.

Estas construcciones de lexemas verbales nominalizados, que constituyen
las relativas nominales, pueden ocupar distintas posiciones argumentales,
tales como sujeto gramatical (explícito), complemento directo, complemento
indirecto y atributo. Ejemplos:

En función de sujeto

mjisawe'sx à ipa katx “los que trabajaron recibieron comida”

(mhi-sa-wesx Ú' ipaka-o-txi)

//trabajar-NOM-COL/comida/recibir- AOR-3pp ASER.PD//

nasa yuwes wewesa' nasa” “el que habla lengua paez es paez”

(nasa yuwe-as wew-e-sa-d' nasa-a')

//paez-idioma-OB]J/hablar-NOM-TOP/paez-3psASER.PE//

En función de complemento directo

bahç wakasatxis uyuga “¿ves a los que cortan cabuya?”

(bahç wakasa-txi's uy-u-ga”)

//cabuya/cortar-NOM-OBJ(pl)/ver-IMPEF-2psINTE//

* Véase, por ejemplo, Crystal (2000: 487) o Creissels (1997).

# Capítulo 6 — Expresión de la deíxis
<!-- ocr -->

<!-- page 126 (screenshot 0126) -->
CAPÍTULO 6
EXPRESIÓN DE LA DEÍXIS

Merece en esta lengua un espacio particular la expresión de las categorías
deícticas, en especial las de espacio y tiempo. Se entiende por expresión de
la deíxis los mecanismos mediante los cuales ciertos elementos lingúísti-
cos remiten a las circunstancias espacial, temporal y de los participantes
en un acto comunicativo —en el que se produce un enunciado—. Es una
especie de “anclaje” de la lengua en la realidad. Los elementos que expre-
san esta relación se llaman deícticos. Enunciación y deíxis se implican
mutuamente: no hay enunciación que no tenga su marco referencial, es
decir, su deíxis, y no existe deíxis que no esté relacionada directamen-
te con determinado acto enunciativo. Por esto, el significado de los ele-
mentos deícticos es siempre relativo al acto enunciativo particular en el
que se usa.

Las categorías deícticas se estructuran a partir de la tríada yo-aquí-
ahora del acto comunicativo. Son tres las categorías deícticas: la persona
gramatical, que se refiere a los participantes en el acto comunicativo y se
estructura a partir del yo enunciador; el espacio, que se estructura a partir
del aquí, lugar de la enunciación, que se toma como punto de referencia o
centro de la deíxis espacial; el tiempo, que se estructura a partir del aho-
ra, momento de la enunciación, que es punto de referencia y centro de la
deíxis temporal.

<!-- page 127 (screenshot 0127) -->
Con lexema cualificativo

uy zxiczkwesa ahkuk “la mujer que es bonita cocinó”

[uy zxiczkwe-sa ah-o-ku-kuj

//mujer/bonita-NOM/cocinar-AOR-D2-3psASER.PD//

Poseedor

mjisawe'sx Ú'a eva “la comida de los que trabajan es buena"

Imhi-sa-wesx Ú -a ew-a)

//trabajar-NOM-COL/comida-TOP/bueno-3psASER.PE//

A manera de recapitulación
En nasa yuwe las funciones sintácticas se expresan generalmente mediante
el mecanismo morfológico de la flexión.

Formalmente esta lengua distingue entre oraciones declarativas y oracio-
nes no declarativas. Las no declarativas no flexionan para la persona, sino
solamente para el modo. En las declarativas aparece en el núcleo predicativo
la flexión de modo y persona-número,

Las oraciones declarativas se clasifican en asertivas y no asertivas, según
el modo expresado en ellas. Las asertivas comprenden asertivas propiamen-
te y suspensivas. En las no asertivas se incluyen las interrogativas totales o
absolutas y las interrogativas parciales o relativas. Todas las oraciones decla-
rativas pueden ser también negativas.

Desde el punto de vista sintáctico, en atención a la cantidad de núcleos
predicativos que tengan las oraciones, estas se dividen en simples, compues-
tas y complejas. En las compuestas existen las que reúnen oraciones simples
por yuxtaposición y por coordinación. Entre las coordinadas, se encuentran
las que son semanticamente adversativas, disyuntivas y consecutivas.

Entre las oraciones complejas —unidas por subordinación— existen
unas oraciones que establecen la relación de igualdad o diferencia entre los
sujetos de la oración subordinada y la oración subordinante, y unas oracio-
nes que no expresan tal relación. Semánticamente se encuentran subordina-
das temporales, condicionales, hipotéticas, concesivas, causales; estas dife-
rencias semanticas se marcan con diferentes morfemas. Existen igualmente
oraciones relativas, entre las que hay nominales —que pueden cumplir las
funciones de sujeto, complemento directo, complemento indirecto o atri-
buto— y adnominales —que funcionan como modificadores del nombre—.

<!-- page 128 (screenshot 0128) -->
LA PERSONA

La persona se expresa normalmente por medio de los pronombres persona-
les, los determinantes posesivos y la flexión personal en el verbo. Esta cate-
goría ya fue presentada en detalle en el capítulo de Mortosintaxis: el sistema
de pronombres personales y la flexión personal, al presentar el morfema de
la predicación. Los posesivos se presentan al hablar de la determinación gra-
matical en el sintagma nominal.

En nasa yuwe la categoría de persona se combina con la de número y
parcialmente con la de género. Tiene un sistema de tres personas singu-
lares y tres plurales, con lo que está dentro de la tendencia mayoritaria de
las lenguas. Pero en cuanto a la combinación con la categoría de género, es
totalmente contraria a la tendencia mayoritaria, cual es la de que la tercera
persona es la que con más frecuencia establece diferenciación de género.
En nasa yuwe esta diferenciación se hace para las personas primera y segun-
da de número singular y no se hace para la tercera persona, para la cual se
usa como pronombre el demostrativo de la mayor distancia. En la siguiente
tabla pueden verse tanto los pronombres personales como los determinan-
tes posesivos, que son los mismos pronombres en las dos primeras personas
y sufren una modificación en la tercera”.

Tabla 14. Pronombres personales y determinantes posesivos
Pronombres personales Determinantes posesivos
Género Género
Número Persona Número Persona
Masculino Femenino Masculino Femenino
1º adx/agx ukwe 1º adx/agx  ukwe
Singular 2º idx/igx ikwe 2: idx/i i kwe
$ ig Singular ligx
3a txà / Rxà 3a txaji / kxãji
la kwe'sx 1: kwesx
Plural 2a i kwesx Da i kwesx
Plural
3º txàvvesx / kxáwesx 3º txàmesx / kxáwesx
” Como en realidad el pronombre personal de tercera persona del singular es el demostrativo distal,
que también puede funcionar como determinante del nombre, se hace necesario diferenciarlos e
interviene para ello el morfema benefactivo (-ji).

<!-- page 129 (screenshot 0129) -->
es
ae — | thakweh
pesat e pe j
- uh ao. | tasuh
|
Figura 4. Líneas y sus nombres

Se puede decir, entonces, que (úy-) sigue la línea pesath, (kutee-) sigue
la línea kath, (khe-) sigue la línea Riith, (kaa-) sigue la línea kuuth y (súu-)
sigue la línea suth.

En cuanto al segundo paradigma, hay en él dos morfemas que indican la
distancia cercana f-ay-) o lejana (-nu-). El primero se usa cuando la entidad
o situación se ubica en un área que se considera cercana y que puede ser, por
ejemplo, el resguardo. El segundo, para referirse a lo lejano, por ejemplo, lo
que está por fuera del resguardo o del territorio propio. La determinación
de los límites entre lo cercano y lo lejano es variable y subjetiva. Se observa
que se estructura en dos grados, de la misma manera que los demostrativos.
Hay un tercer morfema, (-kx-), que indica un lugar preciso.

Figura 5. Grados de distancia espacial

En el tercer paradigma de los que forman los deícticos espaciales, se da
información sobre el eje corporal de la entidad que se sitúa espacialmente.
Se trata de los cuatro morfemas locativos con valor de inesivo: Í-tel, que es el
genérico, no marcado, y que con valor específico se refiere a eje corporal pre-
ferentemente vertical, (-kaj, para ejes corporales horizontales; (-suj, para
entidades ligeramente inclinadas; (-khej, para una verdadera inclinación o
fuerte pendiente; este último morfema es el que se usa cuando la entidad se
encuentra colgada. Como -te es el genérico, es el que se usa cuando lo que se
ubica espacialmente es una situación, un estado de cosas, y no una entidad;
se usa igualmente cuando no se quiere o no es necesario dar la información
del eje corporal.

<!-- page 130 (screenshot 0130) -->
EXPRESIÓN DE LA DEÍXIS

Los pronombres personales se acompañan del morfema benefactivo Í-ji),
al igual que los nombres, cuando se predica la posesión; también cuando
reemplazan el sintagma nominal formado por determinante posesivo más
nombre. Ejemplo:

atx cxihme ukweji “la ruana blanca es mía”

fatx cxihme-a wkwe-ji-a')

//ruana/blanca-TOP/yo(fem)-BEN-3psASER.PE//

na kla' agxji “esta vaca es mía”

(na Rla-a' agx-ji-a')

//esta-vaca- TOP/yo(masc)-BEN-3psASER.PE//

pisxa Tmiguji “la oveja es de Domingo”

(pisxa-a Tmigu-ji-a')

//oveja-TOP/Domingo-BEN-3psASER.PE//

igx atalxa uuk, agxhiwa “tu gallina se murió, la mía también”

figx atalx-a uu-0-ku agx-ji-waj

//túlmasc)/gallina-TOP/morir- AOR-3psASER.PD/yo(masc)-BEN-ADI//

EL ESPACIO

En relación con la categoría deíctica del espacio, ya se han presentado los
demostrativos, que la expresan en tanto indican la ubicación de cercanía
o lejanía que una entidad o una situación tengan en relación con el punto
de referencia o centro de la deíxis. En nasa yuwe el sistema es de dos gra-
dos, cercano y lejano, como en muchas otras lenguas: na “cercano”, txà o
kxa “lejano”.

Dentro de la expresión de esta categoría están también, por supuesto, los
deícticos espaciales, cuyos morfemas constitutivos se han presentado en el
capítulo de Morfología, dentro de los morfemas gramaticales.

El primero de los tres paradigmas que forman los deícticos espaciales
contiene cinco morfemas que expresan información sobre la relación exis-
tente entre la entidad o la situación que se ubica espacialmente y el punto
de referencia o centro de la deíxis. Estas relaciones pueden ser: horizontal
(Uy-), vertical hacia arriba (kutee-), vertical hacia abajo (khe-), diagonal
hacia arriba (kaa-) y diagonal hacia abajo (súu-). Estas direcciones co-
rresponden a ejes o líneas llamadas respectivamente: pesath, kath, kiith,
kuuth y suth.

<!-- page 131 (screenshot 0131) -->
EXPRESIÓN DE LA DEÍXIS
7 N — , - . o ts ã ”
a A AA | pisthéha yatte úsa > <A CA fxtúu mesaka úsa
N | | | | “el hombre está en la casa” | > - “el palo está en la mesa”
If ==
<N ==" klaweçxa' dxi'su úsa 1 à O À j túpa fxtáutasxkhe wpa
a “el lagarto está en el camino” <<» 7 “la araña está en el árbol”
a sn V +
VA XX SIA
Figura 6. Locativos según el eje corporal de la entidad
Se pueden combinar los tres paradigmas, o el primero con el tercero, o el
segundo con el tercero. En el primer caso, el deíctico da tres informaciones:
1) relación de direccionalidad entre lo situado y el punto de referencia, 2) cer-
canía o lejanía y 3) eje corporal de la entidad situada. En el segundo caso, el
deíctico da las informaciones (1) y (3). En el tercer caso, da las informaciones
(2) y (3). Ejemplo:
Uy-ay-khe “situado en relación horizontal, cerca, eje corporal fuertemen-
te inclinado”
kutee-kx-ka “arriba con ascenso fuerte, punto preciso, eje corporal horizontal”
súu-te “abajo con descenso no fuerte, eje corporal vertical o no espe-
cificado”
kaa-su “arriba con ascenso no fuerte, cuerpo ligeramente inclinado”
ay-ka “cerca, eje corporal horizontal”
nu-khe “lejos, eje corporal fuertemente inclinado”
En oraciones:
khenute kwesx yata” “allá abajo —vertical— es nuestra casa”
(khe-nu-te-a kwesx yat-a')
//abajo vertical-lejos-INE-TOP/nosotros”/casa-epsASER.PE//
súusayka” adx kiwe — “allá abajo —dirección oblicua, descenso no fuerte—
(súu(s)-nu-Xa-a adx kiwe-a') es mi parcela”
//abajo descenso suave-cerca-INEh-TOP/yo(masc)/tierra//
* El pronombre personal funciona también como posesivo.
% Por razones morfofonológicas —cuando hay juntura de dos vocales en límites de morfema— se
duplica la consonante inicial.

<!-- page 132 (screenshot 0132) -->
EXPRESIÓN DE LA DEÍXIS

Se puede decir que (kúh-) y (séh-) siguen la dirección úy con una ligera
aproximación de subida o de bajada, mientras que (káh-) sigue la dirección
teekhe y (kih-), la dirección khetee (ver Figura 6).

La acción de mirar se expresa con cinco verbos diferentes, dependiendo
de la dirección de la mirada según los ejes y direcciones: (pesay-) “mirar ho-
rizontalmente”, (paakay-) “mirar hacia arriba verticalmente”, (skiy-) “mirar
hacia abajo verticalmente”, (kuuy-) “mirar hacia arriba de manera oblicua”
y (spay-) “mirar hacia abajo de manera oblicua”. Existe también el verbo
(theg-) “ver”, que funciona como verbo genérico, para cuando no se da esa
información específica.

=

Qu

Ruy
— pesay /

|
|
> spay
Figura 9. Verbos para “mirar”

Se puede decir que pesay- es un mirar que sigue la dirección Uy; paakay-,
la dirección kheetee; skiy-, la dirección teekhe; kuuy-, la dirección súuka;
spay-, la dirección tesúu.

2 7
o -
z e
sikaa — kuy — —
dy O er úy Oe" pesay
tesiu spay —
z >
2 Z
Figura 10. Relación entre las miradas y las direcciones

<!-- page 133 (screenshot 0133) -->
Con el mismo esquema de las cinco líneas, se nombran las direcciones:
la dirección horizontal, úy; la vertical hacia arriba, kheetee; la vertical hacia
abajo, teekhee; la diagonal hacia arriba, sãka; la diagonal hacia abajo, tesãu.

vi
o
v
sikaa —
tes
Figura 7. Direcciones y sus nombres

Hay dos acciones cuya expresión se puede detallar también siguiendo
estas direcciones. La acción de llegar, para la que existen cuatro verbos dife-
rentes según la dirección que tenga el recorrido: (kúh-) “llegar con recorrido
horizontal o subiendo con ligera inclinación”

[séh-) “llegar bajando, casi horizontalmente”, (kah-) “llegar subiendo” y
(kih-) “llegar bajando”. De los cuatro verbos, es kúh- el que funciona como
genérico o no marcado; se usa cuando no se requiere la información precisa
y normalmente se refiere a llegar de cerca. Para expresar que se llega de lejos
existe el verbo (pa -.

EEN Rbkhe kabk CCAA haria kábk
Á Ç o
a E “la hormiga llegó A “la hormiga llegó
y (fuerte subida)” V | (fuerte bajada)”
khãkha kúhk khãkha kúhk khãkha' séhk
a hormigallegó —— — HP hormiga llegó a _ Ta hormiga llegó
(horizontalmente)” (ligera subida)” (ligera bajada)”
Figura 8. Verbos que significan “llegar”

<!-- page 134 (screenshot 0134) -->
EXPRESIÓN DE LA DEÍXIS

El palo es alargado y por lo tanto aparece el verbo ús-; por otra parte,
aparece el inesivo -ka porque el palo se encuentra puesto horizontalmente
sobre la mesa. El sombrero no tiene cuerpo alargado, por lo tanto aparece el
verbo u'p-.

Para decir que una persona está durmiendo, por ejemplo, aunque está
horizontalmente sobre la cama, se usará (Ús-) si está estirada y (uwp-) si su
cuerpo está recogido. Ejemplo:

Kse dehna úsa José está durmiendo (acostado y estirado)”
(Rse-a deh-na ús-o-a?

//José-TOP/dormir-DUR/estar- AOR-3psASER.PE//

Kse dehna upa José está durmiendo (acostado y recogido)
(Rse-a' deh-na up-9-a”)

//José-TOP/dormir-DUR/estar- AOR/3psASER.PE//

Si se quiere especificar que está acostado en una cama, será entonces el
inesivo de horizontalidad el que aparecerá. Ejemplo:

Kse atúka dehna úsa “José está durmiendo en la cama”
(Rse-a atú-ka deh-na ús-g-a't
//José-TOP/cama-INEh/dormir-DUR/estar- AOR-3psASER.PE//

Para la localización de una situación o un estado de cosas, también van el

locativo genérico y el verbo (ús-). Ejemplo:
ayte wala bahça úsa “aquí hay mucho fique”
(ay-te wala bahç-a' ús-0-a')
//cerca-INE/mucho/fique- TOP/estar- AOR-3psASER.PE//

En el trabajo de Rojas y Ramos (2004-2005: 213), se muestra que estos
verbos también pueden indicar, en oraciones en las que se sitúan entidades
en un determinado lugar, si esas entidades están en actividad, caso en el que
aparece fús-), o en reposo, usando el verbo fu"p-I.

Tanto en el uso de los locativos como en el de los verbos posicionales,
se observa que lo relacionado con lo vertical funciona como no marcado,
mientras la horizontalidad se asocia con elementos marcados.

<!-- page 135 (screenshot 0135) -->
El espacio se manifiesta también en dos verbos con los que se predica
la ubicación espacial de algo y que funcionan también como auxiliares po-
sicionales en la construcción de sintagmas verbales: (ús-) y fu p-) “estar”.
El primero se usa cuando se quiere expresar que el eje corporal de la entidad
sobre la cual se predica algo es alargado; es el no marcado y por ello funcio-
na como genérico cuando no se conoce el detalle o esa información es irrele-
vante”. El segundo se usa para expresar que el eje corporal está flexionado o
recogido; se aplica igualmente a entidades cuya forma no sea alargada, sino,
por ejemplo, esférica. Ejemplo:
Según la disposición corporal de la entidad.
Mixia' umna úsa “María está tejiendo (de pie)”
(Mlxia-a2 um-na ús-g-a't
//María-TOP/tejer-DUR/estar- AOR-3psASER.PE//
Mixia umna wpa “María está tejiendo (sentada)”
(Mixia-d um-na up-9-a')
//María-TOP/tejer-DUR/estar- AOR-3psASER.PE//
Cuando se desconoce el detalle o no es posible determinarlo, tanto el
morfema locativo como el verbo son los genéricos.
Tmigu çxhabte úsa "Domingo està en el pueblo"
(Tmigu-a cxhab-te ús-9-4')
((Domingo- TOP/pueblo-INE/estar- AOR-3psASER.PE//
En función de la configuración corporal de la entidad.
cxwa ayte upa "el sombrero està aquí"
(exvva-a' ay-te Up-9-a')
(/sombrero- TOP/cerca-INE/estar- AOR-3psASER.PE//
fxtú” mesaka úsa “el palo está en la mesa”
(fxtú-a mesa-ka ús-9-a')
(/palo-TOP/mesa-INEh/estar-AOR-3psASER.PE//
% El verbo ús- funciona como cópula para predicar la existencia de algo.

<!-- page 136 (screenshot 0136) -->
EXPRESIÓN DE LA DEÍXIS

Cuando se trata de un verbo estativo, estos valores temporales se invier-
ten y se observa que al combinarse con el aspecto aoristo aparece el morfe-
ma modopersonal de la predicación estativa. Ejemplo:

ji pha “(él o ella) tiene”

Giph-o-a')

(/tener-AOR-3psASER.PE//

ji phux “(él o ella) tuvo”

Giph-u-Rut

(/tener-IMPF-3psASER.PD//

La combinación con el aspecto obligatorio y el modo suspensivo arroja
los siguientes valores temporales:

Verbo dinámico + IMPF + SUS presente o futuro (no pasado)

Verbo dinámico + AOR + SUS pasado reciente

Verbo estativo + IMPF + SUS futuro

Verbo estativo + AOR + SUS pasado

La combinación de lexemas verbales dinámicos con imperfectivo y mor-
femas del modo suspensivo tiene valor temporal de presente o futuro, es
decir, no-pasado. Ejemplo:

ew umuga “usted teje muy bien”

fevv um-u-gal

//bueno!tejer-IMPF-2psSUS.PD//

memunha “cantare”

(mem-u-nhat

//cantar-IMPF-1psSUS//

Si se combina un lexema verbal dinámico con el aoristo y el modo sus-
pensivo, se obtiene un valor temporal de pasado reciente.

umga “has tejido”

(um-g-ga)

/Itejer-AOR-2psSUS//

<!-- page 137 (screenshot 0137) -->
EL TIEMPO
La categoría deíctica de tiempo se expresa en los deícticos temporales y en
la morfología verbal. Los deícticos se presentaron en el capítulo de Morfolo-
gía, dentro de los morfemas gramaticales libres. Son palabras que se refieren
al tiempo relativo al acto de enunciación. Algunas de ellas son: àçxh “hoy/
ahora, wnah “ayer”, kuskay “mañana”, kusi “esta mañana”.

En cuanto a la morfología verbal, no existe en nasa yuwe un paradig-
ma que se especialice en la expresión de la categoría gramatical de tiempo.
Los morfemas de distancia contienen alguna indicación temporal, pero ex-
presan también nociones modales. El tiempo se expresa mediante la combi-
nación de morfemas, lo que puede incluir la clase de lexema verbal —diná-
mico o estativo—, los morfemas aspectuales, los morfemas de distancia, los
morfemas modopersonales y el tipo de predicación. *

En la combinación de las clases de lexemas verbales con el paradigma
de aspecto obligatorio (imperfectivo/aoristo) y el morfema modopersonal
correspondiente al modo asertivo —con los dos tipos de predicación—, apa-
recen los siguientes valores temporales:

Verbo dinámico + AOR+PD pasado

Verbo dinámico + IMPF + PD presente

Verbo estativo + AOR + PE presente

Verbo estativo + IMPF + PD pasado

Los verbos dinámicos se combinan en ambos casos con el morfema
modopersonal de la predicación activa. Combinado con el imperfectivo
arroja un valor temporal de presente y con el aoristo, un valor de pasado.
Ejemplo:

umku “El o ella tejió"

fum-o-kuj

//tejer-AOR-3psASER.PD//

umuk “El o ella teje”

fum-u-kuj

(/tejer-IMPF-3psASER.PD//

** Esto se presenta también en el trabajo de Rojas (1994).

<!-- page 138 (screenshot 0138) -->
La combinación de lexemas verbales estativos con imperfectivo y morfe-
mas del modo suspensivo tiene valor temporal de futuro; en la tercera per-
sona aparece la predicación estativa. Ejemplo:

fxina upuna “estará escribiendo”

(fxi-na wp-u-naj

//escribir-DUR/estar-IMPF-3psSUS.PE//

yuhena “(él o ella) vendrá”

(yuh-e-na)

//venir-IMPF-3psSUS.PE//

Si se combina un lexema verbal estativo con el aoristo y con el modo
suspensivo, se interpreta como pasado; en este caso aparece la predicación
dinámica en la tercera persona. Ejemplo:

upka “(él o ella) estaba””

fu'p-o-Ra)

//estar- AOR-3psSUS.PD//

Para examinar la combinación de los lexemas verbales con el aspecto
obligatorio, los morfemas de distancia y los modos, hay que tener en cuenta
que los morfemas de distancia cercana (-ki-) (D1) y media (-ku-) (D2) están
asociados la mayoría de las veces con valores temporales; cuando se combi-
nan con la negación, tienen un valor fundamentalmente modal. El morfema
de distancia lejana í-ne-t (D3) tiene valor temporal cuando se combina con
el modo asertivo y valor modal de inferencia o suposición cuando se com-
bina con el modo suspensivo. Cuando está presente el morfema (-ne-), en la
tercera persona aparece la predicación estativa. Se presentan a continuación
los valores temporales de estas combinaciones.

LV +IMPF+DIloD2+ASER — pasado imperfecto o habitual

LV + IMPF + D3 + ASER pasado imperfecto lejano

LV+AOR+DloD2+ASER pasado

LV + AOR + D3 + ASER pasado lejano
” Aquí se afirma que la persona estaba en un determinado sitio y el uso del verbo u"p- sugiere que se

encontraba quieta o en reposo.

<!-- page 139 (screenshot 0139) -->
Cuando se combina uno de estos morfemas con el de distancia lejana
(-ne-i en un relato de la tradición oral, se entiende necesariamente hacia el
pasado. Ejemplo:

peeteyawaneju “iba a suceder (hace muchísimo tiempo)”

(peete-yàvva-ne-ju-a'l

//suceder-PROS-D3-ENF-3psASER.PE//

La combinación de aspecto externo con los morfemas de distancia cerca-
na y media produce un valor temporal de pasado. Ejemplo:

umyákith “ya tejí (hace poco)”

fum-o-ya-ki-thuj)

//tejer-AOR-EXT-D1-1psASER//

memyákuk “ya cantó (hace algún tiempo)”

(mem-o0-ya-ku-kuj)

//cantar-AOR-EXT-D2-3psASER.PD//

La presencia de los morfemas interno e incoativo da normalmente un
valor temporal de presente: el acontecimiento en curso y el inicio del acon-
tecimiento, respectivamente.

umucthu “estoy tejiendo”

fum-u-c-thuj

//tejer-IMPF-INT-1psASER//

fxi jacyak “(él o ella) está empezando a escribir”

(Mxij-a-eya-ku)

//escribir-IMPF-INCO-3psASER.PD//

Si se combinan con los morfemas (-ki-) y (-ku-), se entiende el inicio
del acontecimiento o el acontecimiento en curso desarrollándose en tiempo
pasado.

memucyákig “ya estabas cantando”

(mem-u-cya-ki-gu)

//cantar-IMPF-INCO-D2-2psASER//

<!-- page 140 (screenshot 0140) -->
EXPRESIÓN DE LA DEÍXIS

Ejemplo:

umukik “(él o ella) tejía”

fum-u-ki-kuj

/Itejer-IMPF-D1-3psASER.PD//

upune “estaba (en un tiempo muy lejano)”

f(up-u-ne-a)

//estar-IMPF-D3-3psASER.PE//

memkuth “canté (hace varios días)"

(mem-o-Ru-thut

//cantar-AOR-D2-1psASER//

umne “tejió (pasado muy lejano)”

fum-o0-ne-a')

(/tejer-AOR-D3-3psASER.PE//

Para la combinación de los lexemas verbales con los morfemas del para-
digma no obligatorio de aspecto, hay que tener en cuenta que los morfemas
de aspecto externo (-yaá-), prospectivo [-yawa-) e inminente (-yawaya-) se
combinan siempre con el aoristo, mientras que los morfemas de aspecto in-
terno (-6-) e incoativo (-eya-) lo hacen con el imperfectivo.

Cuando los lexemas verbales se combinan con los morfemas aspectuales
prospectivo e inminente, resultan valores temporales de futuro, dado que la
indicación aspectual corresponde a acontecimientos que no han sucedido.
Si adicionalmente aparece un morfema de distancia cercana o media, esta
distancia temporal se interpreta también hacia el futuro. Ejemplo:

umyáwath “voy a tejer”

fum-o0-yawa-thuj

//tejer-AOR-PROS-1psASER//

umyáwayath “ya no más voy a tejer”

(um-o-yàvayà-thul

(/tejer-AOR-INM-1psASER//

memyâwakig “vas a cantar (pronto)”

(mem-0-yawa-ki-gu)

//cantar-AOR-PROS-D1-2psASER//

<!-- page 141 (screenshot 0141) -->
En relación con el tiempo, no existe en la palabra verbal un paradigma
especializado en su expresión. Los morfemas de distancia hacen algunas in-
dicaciones temporales, pero los valores temporales que arrojan las palabras
verbales resultan de la combinatoria de los tipos de lexemas verbales con los
morfemas de aspecto, distancia y modo.

<!-- page 142 (screenshot 0142) -->
EXPRESIÓN DE LA DEÍXIS
jiyucyákuth “(yo) ya estaba entendiendo”
Giy-u-çyà-Ru-thul
//entender-IMPF-INCO-D2-1psASER//

Mlxia ya'jas umuckik “María estaba tejiendo una mochila”

(Mixia-a' yaja-as um-u-c-ki-kuj

//María-TOP/mochila-OBJ/tejer-IMPE-INT-D1-3psASER.PD//

Por último, el morfema modopersonal de primera persona del singular
[-n), que se combina siempre con el aspecto imperfectivo, expresa un valor
temporal de futuro. Algunas veces expresa también un compromiso del ha-
blante con alguna acción que hará en el futuro. Ejemplo:

uhan “sembraré”

(uh-a- ni

//sembrar-IMPF-1psFUT//

yatas padu'n “barreré la casa”

(yat-as pad-u-nj

//casa-OB]J/barrer-IMPF-1psFUT//

ya ja zxicxkwete ukwe wayun “si la mochila es bonita, la compraré”

(yaja zxiexkwe-te ukwe way-u-'nj

//mochila/bonita-INE/yo(fem)/comprar-IMPF-1psFUT//

A MANERA DE RECAPITULACIÓN
En nasa yuwe la deíxis se expresa fundamentalmente por medios grama-
ticales, aunque en relación con la categoría de tiempo pueden intervenir
también algunos elementos léxicos.

En cuanto a la categoría de la persona, esta lengua sigue la tendencia ge-
neral al tener un sistema formado por tres personas y dos números, pero se
aleja fuertemente de la tendencia general al hacer distinción de género en las
dos primeras personas del singular y no en la tercera persona.

La expresión del espacio es sumamente detallada, sobre todo en lo que
concierne a la localización espacial de las entidades. En cuanto a la distancia
espacial, tiene un sistema de dos grados —cerca/lejos—, en lo que sigue la
tendencia general de las lenguas”.

% La mayoría de las lenguas tienen sistemas de dos y de tres grados.

<!-- page 143 (screenshot 0143) -->
BIBLIOGRAFÍA

Alcaraz Varó, Enrique y Martínez Linares, Ma. Antonia (2004). Diccionario de Lin-
giística Moderna. Barcelona, España: Ariel.

Benveniste, Émile (1966). Problèmes de linguistique générale. Paris, France: Galli-
mard.

Brown, Keith y Miller, Jim (eds.) (1999). Concise Encyclopedia of Grammatical Ca-
tegories. Oxford, United Kingdom: Elsevier.

Burquest, Donald (2009). Análisis fonológico: Un enfoque funcional. (Giuliana
López, Trad.). Dallas, United States: SIL International.

Cauty, André (1990). Vigilancia etnocultural: el caso de la numeración tradicional
nasa-yuwe. Boletín de Lingúística Aborigen, 2, 3-15.

Cervoni, Jean (1987). Lénonciation. Paris, France: Presses Universitaires de France.

Creissels, Denis (1997). Las estructuras de relativización en las lenguas del mundo
(documento de trabajo). Seminario realizado en el Magíster en Etnolingúística.
Bogotá, Colombia: Universidad de los Andes.

Creissels, Denis (2006). Syntaxe générale: Une introduction typologique. Paris, Fran-
ce: Hermes-Lavoisier. 2 vols.

Comrie, Bernard (1976). Aspect: An introduction to the study of verbal aspect and
related problems. Cambridge, England: Cambridge University Press.

Consejo Regional Indígena del Cauca (2007). Estudio sociolingilístico preliminar:
Lenguas nasa yuwe y namtrik, fase exploratoria: Informe final. Popayán, Colom-
bia: CRIC.

Consejo Regional Indígena del Cauca (2008). Base censal de los cabildos indígenas.
Popayán, Colombia: CRIC.

Constenla, Adolfo (1993). La familia chibcha. En María L. Rodríguez de Montes
(comp.; ed.), Estado actual de la clasificación de las lenguas indígenas de Colom-
bia (pp. 75-125). Bogotá, Colombia: Instituto Caro y Cuervo.