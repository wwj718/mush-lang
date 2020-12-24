(define (factorial n acc) (if (= n 0) acc (factorial (- n 1) (* n acc))))
(define (fact n) (factorial n 1))
(display (fact 10))