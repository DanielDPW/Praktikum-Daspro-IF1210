module ListOfInteger where
-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Int: [ ] atau [e o List] atau [List o e]  
   Definisi type List of Int
   Basis: List of Int kosong adalah list of Int 
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
   (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
-- REALISASI
konso e li = [e] ++ li

konsDot :: [Int] -> Int -> [Int]
{- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
   e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
-- REALISASI
konsDot li e = li ++ [e]

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Int] -> Int
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Int] -> [Int]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Int] -> Int
-- last l menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Int] -> [Int]
-- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of integer l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1 

isEqual :: [Int] -> [Int] -> Bool
isEqual l1 l2
    | null l1 && null l2 = True
    | null l2 = False
    | null l1 = False
    | otherwise = head l1 == head l2 && isEqual (tail l1) (tail l2)

maxList :: [Int] -> Int
maxList li
    | length li <= 1 = head li
    | head li > maxList (tail li) = head li
    | otherwise = maxList (tail li)

minList :: [Int] -> Int
minList li
    | length li <= 1 = head li
    | head li < minList (tail li) = head li
    | otherwise = minList (tail li)

nbX :: Int -> [Int] -> Int
nbX x li
    | null li = 0
    | x == head li = 1 + nbX x (tail li)
    | otherwise = nbX x (tail li)

jmlMin :: [Int] -> (Int,Int)
jmlMin li = (minList li, nbX (minList li) li)

maxNb :: [Int] -> (Int,Int)
maxNb li = (maxList li, nbX (maxList li) li)

positiveList :: [Int] -> [Int]
positiveList li
    | null li = []
    | head li >= 0 = [head li] ++ positiveList (tail li)
    | otherwise = positiveList (tail li)

negativeList :: [Int] -> [Int]
negativeList li
    | null li = []
    | head li < 0 = [head li] ++ negativeList (tail li)
    | otherwise = negativeList (tail li)

pecahListPosNeg :: [Int] -> ([Int],[Int])
pecahListPosNeg li = (positiveList li, negativeList li)

isMember :: [Int] -> Int -> Bool
isMember li x
    | null li = False
    | x == (head li) = True
    | otherwise = isMember (tail li) x