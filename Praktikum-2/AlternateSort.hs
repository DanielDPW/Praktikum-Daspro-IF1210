module AlternateSort where
import Control.Applicative (liftA)
insertionSort :: [Int] -> [Int]
insert :: Int -> [Int] -> [Int]

insertionSort li
    | null li = []
    | otherwise = insert (head li) (insertionSort (tail li))

insert x li
    | null li = [x]
    | x <= head li = [x] ++ li
    | otherwise = [head li] ++ insert x (tail li)

alternateSort :: [Int] -> [Int]
alternateSort li
    | null li = []
    | length li == 1 = [head li]
    | otherwise = [head (insertionSort li)] ++ [last (insertionSort li)] ++ alternateSort (init (tail (insertionSort li)))