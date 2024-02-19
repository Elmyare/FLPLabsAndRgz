(defun swap-third-and-last (lst)
  (if (or (null (car (cdr (cdr lst))))
          (null (cdr (cdr (cdr lst)))))
      lst
      (let* ((result (list (car lst) (car (cdr lst))))
             (lastt (last lst))
             (thirdd (car (cdr (cdr lst)))))
        (append result lastt (butlast (cdr (cdr (cdr lst)))) (list thirdd)))))