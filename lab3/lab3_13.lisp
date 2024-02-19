(defun check-property (predicate lst)
  (labels ((check (lst)
             (cond
               ((null lst) nil)
               ((funcall predicate (car lst)) t)
               (t (check (cdr lst))))))
    (check lst)))

;; Проверка для неположительного числа
(format t "Check for non-positive number property~%")
(format t "List 1 result: ~a~%" (check-property (lambda (x) (<= x 0)) '(1 2 3 4 5)))
(format t "List 2 result: ~a~%" (check-property (lambda (x) (<= x 0)) '(-1 -2 -3 -4 -5)))

;; Проверка для символа
(format t "~&Check for symbol property~%")
(format t "List 1 result: ~a~%" (check-property #'symbolp '(1 a 3 4 b)))
(format t "List 2 result: ~a~%" (check-property #'symbolp '(1 2 3 4 5)))