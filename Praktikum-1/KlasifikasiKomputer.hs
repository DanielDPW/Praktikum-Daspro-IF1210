module KlasifikasiKomputer where
klasifikasi :: Int -> Int -> Int -> Int
klasifikasi cpu gpu hd
    | cpu < 2 || gpu < 2 || hd < 2 = 1
    | cpu < 5 || gpu < 5 = 2
    | cpu <= 7 && gpu <= 7 && hd <= 7 = 3
    | cpu <= 7 || gpu <= 7 || hd <= 7 = 4
    | otherwise = 5