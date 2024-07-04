module LamaTidur where
lamaTidur :: Int -> Int -> Int -> (Bool, Int, Int, Int)
konversi :: Int -> Int -> Int -> Int
konversi a b c
    | time >= 18000 = (86400 - time) + 18000
    | otherwise = 18000 - time
    where
        time = a * 3600 + b * 60 + c
lamaTidur a b c = (konversi a b c >= 21600, div (konversi a b c) 3600, div (mod (konversi a b c) 3600) 60, mod (konversi a b c) 60)

    
        