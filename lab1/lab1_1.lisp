(defun find-atom-star (lst)
  (cond ((atom lst) (if (eql lst '*)
                        '*
                        nil))
        ((listp lst) (or (find-atom-star (car lst))
                         (find-atom-star (cdr lst))))))