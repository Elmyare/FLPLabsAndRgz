(defun rotate-left (lst n)
  (cond
    ((= n 0) lst)
    ((null lst) nil)
    (t (rotate-left (append (cdr lst) (list (car lst))) (- n 1)))))