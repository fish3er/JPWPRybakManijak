# Zadania: Generatory i Iteratory w Pythonie

## 1. Generator niestandardowego zakresu (`custom_range`)

**Opis:**

Zaimplementuj funkcję generatora `custom_range(start, end, step)`, która działa podobnie do wbudowanej funkcji `range()`. Generator powinien zwracać kolejne liczby, zaczynając od `start`, zwiększając (lub zmniejszając) je o `step`, aż do osiągnięcia wartości granicznej `end` (nie włącznie).

**Wskazówka:**  
Użyj pętli `while` oraz słowa kluczowego `yield`.

---

## 2. Nieskończony generator Fibonacciego (`infinite_fibonacci`)

**Opis:**

Stwórz funkcję generatora `infinite_fibonacci()`, która generuje nieskończony ciąg liczb Fibonacciego. Każde wywołanie `next()` powinno zwracać kolejną liczbę ciągu:

