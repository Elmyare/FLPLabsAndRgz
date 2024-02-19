(defun count-occurrences (element lst)
  (if (null lst)
      0
      (if (equal element (car lst))
          (+ 1 (count-occurrences element (cdr lst)))
          (count-occurrences element (cdr lst)))))

(defun transform-list (lst)
  (cond
    ((null lst) nil)
    (t (cons (list (car lst) (count-occurrences (car lst) lst))
             (transform-list (remove (car lst) lst))))))