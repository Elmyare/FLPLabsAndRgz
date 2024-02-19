(defun transpose-matrix (matrix)
  (if (null (car matrix))
      nil
      (cons
        (mapcar #'car matrix)
        (transpose-matrix (mapcar #'cdr matrix)))))