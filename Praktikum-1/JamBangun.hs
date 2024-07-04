module JamBangun where
jamBangun :: Int -> Int -> Int -> (Bool, Int, Int, Int)
jamBangun j m d = (konversi < 27900, div selisih 3600, div (mod selisih 3600) 60, mod selisih 60)
    where
        konversi = 3600 * j + 60 * m + d
        selisih
            | konversi <= 27900 = 27900 - konversi
            | otherwise = konversi - 27900
        
        