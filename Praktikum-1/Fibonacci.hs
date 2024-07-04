module Fibonacci where
fibonacci :: Int -> Int
fibonacci n
    | n < 1 = 0
    | n == 1 = 1
    | n == 2 = 1
    | otherwise = fibonacci(n-1) + fibonacci (n-2)