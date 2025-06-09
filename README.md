# Zadania Python - Generatory i Iteratory

## 1. Generator niestandardowego zakresu (custom_range)

**Opis dla studentów:**

Zaimplementuj funkcję generatora `custom_range(start, end, step)`, która działa podobnie do wbudowanej funkcji `range()`. Ma ona generować liczby zaczynając od `start`, zwiększając (lub zmniejszając) je o `step`, aż do momentu osiągnięcia wartości granicznej `end` (nie włącznie).

**Wskazówka:** Użyj pętli `while` oraz słowa kluczowego `yield`.

## 2. Nieskończony generator Fibonacciego

**Opis dla studentów:**

Stwórz funkcję generatora `infinite_fibonacci()`, która generuje nieskończony ciąg liczb Fibonacciego. Każde wywołanie `next()` powinno zwracać kolejną liczbę ciągu: 0, 1, 1, 2, 3, 5, ...

**Wskazówka:** Użyj dwóch zmiennych do śledzenia aktualnej i następnej liczby oraz nieskończonej pętli `while`.

## 3. Generator liczb pierwszych do n

**Opis dla studentów:**

Napisz funkcję generatora `prime_generator(n)`, która zwraca kolejne liczby pierwsze mniejsze lub równe `n`.

**Wskazówka:** Użyj prostego algorytmu sprawdzania pierwszości (np. dzielenie przez wcześniejsze liczby). Generator powinien zatrzymać się po przekroczeniu `n`.

## 4. Slajdujące okno na iteratorze (Sliding Window)

**Opis dla studentów:**

Zaimplementuj funkcję `sliding_window(iterable, size)`, która zwraca generator produkujący okna (krotki) o długości `size`, przesuwane o jeden element po iterable.

Dla wejścia `[1, 2, 3, 4, 5]` i `size=3`, generator powinien zwrócić: `(1,2,3)`, `(2,3,4)`, `(3,4,5)`.

**Wskazówka:** Użyj bufora (np. listy lub deque) do śledzenia ostatnich `size` elementów.

## 5. Iterowalny obiekt z funkcją podglądu (trudniejsze)

**Opis dla studentów:**

Stwórz klasę `PeekableIterator`, która owija dowolny iterator i umożliwia podejrzenie następnej wartości bez jej pobierania. Metoda `peek()` powinna zwracać następny element bez przesuwania iteratora, natomiast `__next__()` ma ten element zwracać i przesuwać iterator dalej.

Klasa powinna implementować także metodę `__iter__()`.

**Wskazówka:** Wykorzystaj wewnętrzne zmienne do buforowania wartości zwróconej przez `peek()`.