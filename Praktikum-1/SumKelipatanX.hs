module SumKelipatanX where
sumKelipatanX :: Int -> Int -> Int -> Int
sumKelipatanX m n x 
    | n < m = 0
    | n >= m && (mod n x == 0) = n + sumKelipatanX m (n - 1) x
    | otherwise = sumKelipatanX m (n - 1) x