cube :: Int -> Int
cube x = x * x * x

double ::  Int -> Int
double x = x * 2

modulus :: Int -> Int -> Int 
modulus x m 
    | x < m       = x
    | x - m >= m  = modulus(x - m) m
    | otherwise   = x - m

factorial :: Int -> Int
factorial x 
    | x == 0  = 1
    | x < 0   = x * factorial(x + 1) --for negative
    | x > 0   = x * factorial(x - 1)

summation :: Int -> Int
summation x 
    | x <= 0     = 0
    | otherwise  = x + summation(x - 1)

compose :: (Int -> Int) -> (Int -> Int) -> (Int -> Int)
compose f g = \x -> f(g x)

subtractMaker :: Int -> (Int -> Int)
subtractMaker x y = y - x

applyNTimes :: (Int -> Int) -> Int -> Int -> Int
applyNTimes f x n 
    | n <= 0    = x
    | otherwise = f(applyNTimes f x (n - 1))