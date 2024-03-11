(defun swap-third-and-last (lst)
  (if (null lst)
      lst
      (let ((third (car (cdr (cdr lst))))
            (last (car (last lst))))
        (if (null (cdr (cdr lst))) ; Проверяем, есть ли третий элемент
            lst
            (if (null (cdr (cdr (cdr lst)))) ; Проверяем, есть ли еще как минимум один элемент после третьего
                (cons (car lst)
                      (cons last
                            (cons (car (cdr lst))
                                  (cdr (cdr lst)))))
                (let ((rest (butlast lst)))
                  (append rest (list third last))))))))