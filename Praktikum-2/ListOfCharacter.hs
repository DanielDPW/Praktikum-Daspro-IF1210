module ListOfCharacter where
-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Char: [ ] atau [e o List] atau [List o e]
   Definisi type List of Char
   Basis: List of Char kosong adalah list of Char
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Char di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Char di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Char -> [Char] -> [Char]
{- konso e lc menghasilkan sebuah list of character dari e (sebuah character)  
   dan lc (list of integer), dengan cc sebagai elemen pertama: e o lc -> lc' -}
-- REALISASI
konso e lc = [e] ++ lc

konsDot :: [Char] -> Char -> [Char]
{- konsDot(lc,cc) menghasilkan sebuah list of character dari lc (list of 
   character) dan e (sebuah character), dengan e sebagai elemen terakhir: 
   lc o e -> lc' -}
-- REALISASI
konsDot lc e = lc ++ [e]

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Char] -> Char
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Char] -> [Char]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Char] -> Char
-- last l  menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Char] -> [Char]
-- init(l) menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Char] -> Bool
-- isEmpty l true jika list of character l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Char] -> Bool
-- isOneElmt l true jika list of character l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1

isPalindrom :: [Char] -> Bool
isPalindrom lc 
    | null lc = True
    | length lc == 1 = True
    | otherwise = head lc == last lc && isPalindrom (init (tail lc))

oddList :: [Char] -> [Char]
oddList lc
    | null lc = []
    | mod (length lc) 2 == 1 = oddList (init lc) ++ [last lc]
    | otherwise = oddList (init lc)

evenList :: [Char] -> [Char]
evenList lc
    | null lc = []
    | mod (length lc) 2 == 0 = evenList (init lc) ++ [last lc]
    | otherwise = evenList (init lc)

splitAlternate :: [Char] -> ([Char],[Char])
splitAlternate lc = (oddList lc, evenList lc)

konkat :: [Char] -> [Char] -> [Char]
konkat lc1 lc2
    | null lc1 && null lc2 = []
    | null lc1 = lc2
    | null lc2 = lc1
    | otherwise = lc1 ++ lc2

pajakMakan :: [Char] -> [Int] -> [Char]
pajakMakan lc li
    | null lc && null li = []
    | fromIntegral(head li) * 1.1 <= 200 = [head lc] ++ pajakMakan (tail lc) (tail li)
    | otherwise = pajakMakan (tail lc) (tail li)