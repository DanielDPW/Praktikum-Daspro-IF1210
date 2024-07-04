module NbKelipatanX where
nbKelipatanX :: Int -> Int -> Int -> Int
nbKelipatanX m n x 
    | n < m = 0
    | n >= m && (mod n x == 0) = 1 + nbKelipatanX m (n - 1) x
    | otherwise = nbKelipatanX m (n - 1) x