module HitungBensin where
hitungBensin :: Int -> Int -> Int
collatz :: Int -> Int
collatz a
    | a == 1 = 0
    | mod a 2 == 1 && a /= 1 = 1 + collatz (3 * a + 1)
    | mod a 2 == 0 = 1 + collatz (div a 2)

hitungBensin a b
    | b < a = 0
    | otherwise = collatz b + hitungBensin a (b - 1)
