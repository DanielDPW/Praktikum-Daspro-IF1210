module DeretSegitiga where
-- DERETSEGITIGA
-- DEFINISI DAN SPESIFIKASI
deretSegitiga :: Int -> Int
    -- deretSegitiga mencari bilangan ke- n pada deretSegitiga
    -- n adalah integer

-- REALISASI
deretSegitiga n
    | n == 1 = 1
    | otherwise = n + deretSegitiga (n - 1)

-- APLIKASI
-- deretSegitiga 2
-- deretSegitiga 5