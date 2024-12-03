module Main where

import qualified Day3

main :: IO ()
main = do
  putStrLn "day:"
  inp <- getLine
  case inp of
    "3" -> Day3.run
    _ -> putStrLn "invalid day"
