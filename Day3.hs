module Day3 (run) where

import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Void
import Data.List
import Data.Either
import Data.Time.Clock.POSIX

type Parser = Parsec Void String

data Expr
  = Mul Int Int
  | Do
  | Dont

number :: Parser Int
number = read <$> some digitChar

mul :: Parser Expr
mul = liftA2 Mul (string "mul(" *> number) (char ',' *> number <* char ')')

do_ :: Parser Expr
do_ = Do <$ string "do()"

dont :: Parser Expr
dont = Dont <$ string "don't()"

exprs :: Parser [Expr]
exprs = concat <$> some ((singleton <$> try mul) <|> (singleton <$> try do_) <|> (singleton <$> try dont) <|> ([] <$ noneOf []))

prs :: String -> [Expr]
prs = fromRight [] . parse exprs ""

part1 :: String -> Int
part1 = foldl (\cases
  acc (Mul a b) -> acc + a * b
  acc _ -> acc) 0 . prs

part2 :: String -> Int
part2 = fst . foldl (\cases
  (acc, whether) (Mul a b)
    | whether -> (acc + a * b, whether)
    | otherwise -> (acc, whether)
  (acc, _) Do -> (acc, True)
  (acc, _) Dont -> (acc, False)) (0, True) . prs

run :: IO ()
run = do
  input <- readFile "input/3.txt"
  as <- getPOSIXTime
  print $ part1 input
  ae <- getPOSIXTime
  print $ ae - as
  bs <- getPOSIXTime
  print $ part2 input
  be <- getPOSIXTime
  print $ be - bs
