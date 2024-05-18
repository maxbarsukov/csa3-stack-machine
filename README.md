# CSA Lab 3

## Вариант

`alg -> asm | stack | harv | hw | tick -> instr | struct | stream | port | pstr | prob2 | cache`

Я делаю:

`alg | stack | harv | hw | tick | struct | stream | port | pstr | prob2`

| Задание | Вариант | Описание |
| --- | --- | --- |
| Язык программирования. Синтаксис | `alg` | **Синтаксис языка должен напоминать java/javascript/lua**. Должен поддерживать математические выражения. В тестах необходимо осуществить проверку AST (абстрактного синтаксического дерева, полученного в процессе трансляции). |
| Архитектура | `stack` | Система команд должна быть **стековой**: вместо регистров используется стек; это не исключает и не заменяет наличие памяти команд и памяти данных. |
| Архитектура организации памяти | `harv` | **Гарвардская архитектура**: в тестах необходимо привести/проверить как память команд, так и память данных. |
| Control Unit | `hw` | **Hardwired**. Реализуется как часть модели. |
| Точность модели | `tick` | Процессор необходимо моделировать **с точностью до такта**, процесс моделирования может быть приостановлен на любом такте. |
| Представление машинного кода | `struct` | В виде **высокоуровневой структуры данных**. Считается, что одна инструкция укладывается в одно машинное слово, за исключением CISC архитектур. |
| Ввод-вывод | `stream` | Ввод-вывод осуществляется как **поток токенов**. |
| Ввод-вывод ISA | `port` | **Port-mapped** (специальные инструкции для ввода-вывода): адресация портов ввода-вывода должна присутствовать. |
| Поддержка строк | `pstr` | **Length-prefixed** (Pascal string) |
| Алгоритм | `prob2` | **Even Fibonacci numbers**. [Project Euler. Problem 2](https://projecteuler.net/problem=2) |
